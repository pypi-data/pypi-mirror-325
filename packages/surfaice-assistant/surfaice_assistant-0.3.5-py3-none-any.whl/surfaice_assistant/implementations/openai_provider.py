import asyncio
import json
import logging
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum
from typing import Any, Literal, Optional

from openai import AsyncOpenAI
from openai.types.beta import Assistant, Thread
from openai.types.shared_params import ResponseFormatText, ResponseFormatJSONObject, ResponseFormatJSONSchema
from openai.types.beta.threads import Message, Run
from pydantic import BaseModel

from ..abstract_provider.assistant import AssistantInterface

logger = logging.getLogger(__name__)


# Добавить универсальный респонсе для всех функций пидантик возможно саксесс тру или фолсе  и месседж


class AssistantCreateResponse(BaseModel):
    """Response model for assistant creation."""

    success: bool
    assistant: Optional[Assistant] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class AssistantGetResponse(BaseModel):
    """Response model for getting an assistant."""

    success: bool
    assistant: Optional[Assistant] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class AssistantUpdateResponse(BaseModel):
    """Response model for updating an assistant."""

    success: bool
    assistant: Optional[Assistant] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class ThreadGetResponse(BaseModel):
    """Response model for getting a thread."""

    success: bool
    thread: Optional[Thread] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class ThreadMessagesGetResponse(BaseModel):
    """Response model for getting thread messages."""

    success: bool
    messages: list[Message]
    error: Optional[str] = None
    status_code: Optional[int] = None


class MessageCreateResponse(BaseModel):
    """Response model for message creation."""

    success: bool
    message: Optional[Message] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class AssistantMessageGetResponse(BaseModel):
    """Response model for getting assistant message."""

    success: bool
    message: Optional[Message] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class ThreadClearResponse(BaseModel):
    """Response model for clearing thread messages."""

    success: bool
    error: Optional[str] = None
    status_code: Optional[int] = None


class ThreadSetupResponse(BaseModel):
    """Response model for setting up thread with messages."""

    success: bool
    error: Optional[str] = None
    status_code: Optional[int] = None


class ToolOutputsSubmitResponse(BaseModel):
    """Response model for submitting tool outputs."""

    success: bool
    run: Optional[Run] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class RunCreateResponse(BaseModel):
    """Response model for creating a run."""

    success: bool
    run: Optional[Run] = None
    error: Optional[str] = None
    status_code: Optional[int] = None


class InferResponse(BaseModel):
    """Response model for inference."""

    success: bool
    message: Optional[str] = None
    error: Optional[str] = None
    status_code: Optional[int] = None

class RunListResponse(BaseModel):
    """Response model for listing runs."""

    success: bool
    runs: list[Run] = []
    error: Optional[str] = None
    status_code: Optional[int] = None


class RunCancelResponse(BaseModel):
    """Response model for canceling a run."""

    success: bool
    run: Optional[Run] = None
    error: Optional[str] = None
    status_code: Optional[int] = None

@dataclass
class Function:
    """Represents a function with its OpenAI schema and Python implementation.

    Attributes:
        name: Name of the function
        schema: OpenAI function schema definition
        func: Python callable implementation
    """

    name: str
    assistant_schema: dict[str, Any]
    runnable_func: Callable


class FuncTools:
    """Singleton class for managing function tools."""

    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not FuncTools._initialized:
            self._functions: dict[str, Function] = {}
            FuncTools._initialized = True

    def register(
        self,
        name: str,
        schema: dict[str, Any],
        func: Callable,
    ) -> None:
        self._functions[name] = Function(name, schema, func)

    def register_all(
        self,
        functions: list[Any] | None = None,
    ) -> None:
        """Register multiple functions at once.

        Args:
            functions: Dictionary mapping function names to tuples of (schema, function).
                    Each tuple contains the OpenAI schema and the Python implementation.
                    If None, no functions will be registered.
        """
        if functions is None:
            functions = []

        for function_name, function_schema, function_callable  in functions:
            self.register(function_name, function_schema, function_callable)

    def get_tool(self, name: str) -> Function:
        return self._functions[name]


async def retry_async(
    operation,
    max_retries: int = 5,
    delay: float = 0.5,
    error_handler=None,
) -> tuple[bool, Any, str | None]:
    """Retry an async operation with exponential backoff.

    Args:
        operation: Async function to retry
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        error_handler: Optional function to handle errors between retries

    Returns:
        Tuple of (success: bool, result: Any, error: str | None)
    """
    attempt = 0
    last_error = None

    while attempt < max_retries:
        try:
            result = await operation()
            status_code = getattr(result, "status_code", None)
            return True, result, None, status_code
        except Exception as e:
            last_error = getattr(e, "message", str(e))
            attempt += 1
            if attempt < max_retries:
                if error_handler:
                    error_handler(attempt, max_retries, e)
                logger.warning(f"Retry attempt {attempt}/{max_retries}: {e}")
                await asyncio.sleep(delay * (2 ** (attempt - 1)))
            else:
                logger.error(f"Operation failed after {max_retries} retries: {e}")

            status_code = getattr(e, "status_code", None)

    return False, None, last_error, status_code


class AIProvider(Enum):
    """
    Enum representing supported AI providers.
    """

    OPENAI = "openai"


class OpenAIAssistantImpl(AssistantInterface):
    """OpenAI implementation of the AssistantInterface."""

    func_tools: FuncTools = FuncTools()

    def __init__(self, api_key: str) -> None:
        self.client = AsyncOpenAI(api_key=api_key)

    async def create_assistant(
        self,
        name: str,
        description: str,
        instructions: str,
        model: str,
        tools: list[dict],
        response_format: str | None = None,
        max_retries: int = 5,
    ) -> AssistantCreateResponse:
        """Creates an external assistant with the specified parameters."""

        async def _create_assistant():
            return await self.client.beta.assistants.create(
                name=name,
                instructions=instructions,
                description=description,
                model=model,
                tools=tools,  # type: ignore
                response_format=response_format,
            )

        try:
            if response_format:
                response_format_map = {
                    "text": ResponseFormatText(type="text"),
                    "json_object": ResponseFormatJSONObject(type="json_object"),
                    "json_schema": ResponseFormatJSONSchema(type="json_schema")
                }
                if response_format in response_format_map:
                    response_format = response_format_map[response_format]
            success, assistant, error, status_code = await retry_async(
                _create_assistant,
                max_retries=max_retries,
            )
            return AssistantCreateResponse(
                success=success, assistant=assistant, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error creating openai assistant: {e}")
            return AssistantCreateResponse(
                success=False, assistant=None, error=str(e), status_code=None
            )

    async def get_assistant(
        self,
        assistant_id: str,
        max_retries: int = 5,
    ) -> AssistantGetResponse:
        """Get an assistant by ID."""
        try:
            success, assistant, error, status_code = await retry_async(
                lambda: self.client.beta.assistants.retrieve(assistant_id=assistant_id),
                max_retries=max_retries,
            )
            return AssistantGetResponse(
                success=success, assistant=assistant, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error getting openai assistant: {e}")
            return AssistantGetResponse(
                success=False, assistant=None, error=str(e), status_code=None
            )

    async def update_assistant(
        self,
        assistant_id: str,
        max_retries: int = 5,
        **update_params,
    ) -> AssistantUpdateResponse:
        """Updates an existing assistant with the specified parameters."""
        try:
            if update_params.get("response_format"):
                response_format = update_params.get("response_format")
                response_format_map = {
                    "text": ResponseFormatText(type="text"),
                    "json_object": ResponseFormatJSONObject(type="json_object"),
                    "json_schema": ResponseFormatJSONSchema(type="json_schema")
                }
                if response_format in response_format_map:
                    update_params["response_format"] = response_format_map[response_format]
            success, assistant, error, status_code = await retry_async(
                lambda: self.client.beta.assistants.update(
                    assistant_id=assistant_id,
                    **update_params,
                )
            )
            return AssistantUpdateResponse(
                success=success, assistant=assistant, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error updating openai assistant: {e}")
            return AssistantUpdateResponse(
                success=False, assistant=None, error=str(e), status_code=None
            )

    async def create_thread(self, max_retries: int = 5, **kwargs) -> ThreadGetResponse:
        """Create a new thread."""
        try:
            success, thread, error, status_code = await retry_async(
                lambda: self.client.beta.threads.create(**kwargs)
            )
            return ThreadGetResponse(
                success=success, thread=thread, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error creating thread: {e}")
            return ThreadGetResponse(
                success=False, thread=None, error=str(e), status_code=None
            )

    async def get_thread(
        self,
        thread_id: str,
        max_retries: int = 5,
    ) -> ThreadGetResponse:
        """Get a thread by ID."""
        try:
            success, thread, error, status_code = await retry_async(
                lambda: self.client.beta.threads.retrieve(thread_id=thread_id)
            )
            return ThreadGetResponse(
                success=success, thread=thread, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error getting thread: {e}")
            return ThreadGetResponse(
                success=False, thread=None, error=str(e), status_code=None
            )

    async def create_message(
        self,
        thread_id: str,
        content: str,
        role: Literal["user", "assistant"] = "user",
    ) -> MessageCreateResponse:
        """Create a message in a thread."""
        try:
            success, message, error, status_code = await retry_async(
                lambda: self.client.beta.threads.messages.create(
                    thread_id=thread_id, role=role, content=content
                )
            )
            return MessageCreateResponse(
                success=success, message=message, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error creating message: {e}")
            return MessageCreateResponse(
                success=False, message=None, error=str(e), status_code=None
            )

    async def get_thread_messages(
        self,
        thread_id: str,
        max_retries: int = 5,
    ) -> ThreadMessagesGetResponse:
        """Get all messages from a thread."""
        try:
            success, messages, error, status_code = await retry_async(
                lambda: self.client.beta.threads.messages.list(thread_id=thread_id)
            )
            if success:
                return ThreadMessagesGetResponse(
                    success=True, 
                    messages=list(messages.data) if messages else [], 
                    error=None,
                    status_code=status_code
                )
            return ThreadMessagesGetResponse(
                success=False, 
                messages=[], # Возвращаем пустой список вместо None
                error=error,
                status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error getting thread messages: {e}")
            return ThreadMessagesGetResponse(
                success=False, 
                messages=[], # Возвращаем пустой список вместо None
                error=str(e),
                status_code=None
            )

    async def _try_get_latest_assistant_message(self, thread_id: str) -> Message | None:
        """Get the latest message from the assistant in the messages list.

        Args:
            thread_id: The ID of the thread to get messages from.

        Returns:
            Message | None: The latest assistant message if found, None otherwise.
        """
        response = await self.get_thread_messages(thread_id=thread_id)

        if response.success and response.messages:
            for msg in response.messages:
                if msg.role == "assistant":
                    return msg

        raise Exception("Assistant message not found, retrying...")

    async def get_assistant_response(
        self,
        thread_id: str,
        max_retries: int = 5,
    ) -> AssistantMessageGetResponse:
        """Get the assistant's response from a thread."""

        async def _get_assistant_message():
            messages = await self.client.beta.threads.messages.list(thread_id=thread_id)
            if not messages.data:
                raise Exception("No messages found in thread")

            assistant_message = next(
                (msg for msg in messages.data if msg.role == "assistant"),
                None,
            )
            if not assistant_message:
                raise Exception("Assistant message not found")

            return assistant_message

        success, message, error, status_code = await retry_async(
            _get_assistant_message, max_retries=max_retries
        )
        return AssistantMessageGetResponse(
            success=success,
            message=message,
            error=error,
            status_code=status_code
        )

    async def clear_thread_messages(
        self,
        thread_id: str,
        max_retries: int = 5,
    ) -> ThreadClearResponse:
        """Delete all messages from a thread."""
        try:
            # Get all messages
            success, messages, error, status_code = await retry_async(
                lambda: self.client.beta.threads.messages.list(thread_id=thread_id),
                max_retries=max_retries,
            )

            if not success or not messages:
                return ThreadClearResponse(
                    success=False, error=error or "Failed to get messages", status_code=status_code
                )

            # Delete each message
            for message in messages.data:
                success, _, error, status_code = await retry_async(
                    lambda: self.client.beta.threads.messages.delete(
                        thread_id=thread_id, message_id=message.id
                    )
                )
                if not success:
                    return ThreadClearResponse(
                        success=False,
                        error=f"Failed to delete message {message.id}: {error}",
                        status_code=status_code
                    )

            return ThreadClearResponse(success=True, status_code=status_code)
        except Exception as e:
            logger.warning(f"Error clearing thread messages: {e}")
            return ThreadClearResponse(success=False, error=str(e), status_code=None)

    async def setup_new_thread(
        self,
        thread_id: str,
        messages: list[Message],
        max_retries: int = 5,
    ) -> ThreadSetupResponse:
        """Put messages in the new thread.

        Args:
            thread_id: The ID of the thread to setup
            messages: List of messages to add to the thread
            max_retries: Maximum number of retry attempts
        """
        try:
            for message in messages:
                # Safely extract content from message
                content = ""  # todo : fix it - bad code
                if message.content and len(message.content) > 0:
                    content_block = message.content[0]  # todo : fix it - magic index
                    if hasattr(content_block, "text"):
                        content = content_block.text.value  # type: ignore

                success, _, error, status_code = await retry_async(
                    lambda: self.client.beta.threads.messages.create(
                        thread_id=thread_id, role=message.role, content=content
                    )
                )
                if not success:
                    return ThreadSetupResponse(
                        success=False, error=f"Failed to create message: {error}", status_code=status_code
                    )

            return ThreadSetupResponse(success=True, status_code=status_code)
        except Exception as e:
            logger.warning(f"Error setting up thread: {e}")
            return ThreadSetupResponse(success=False, error=str(e), status_code=None)

    async def submit_tool_outputs(
        self,
        run: Run,
        thread: Thread,
        tool_calls: list,
        max_retries: int = 5,
    ) -> ToolOutputsSubmitResponse:
        """Submit tool outputs for a run."""
        try:
            tool_outputs = []
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                function_id = tool_call.id

                function_response = await self.func_tools.get_tool(
                    function_name
                ).runnable_func(**arguments)
                tool_outputs.append(
                    {"tool_call_id": function_id, "output": str(function_response)}
                )

            success, run_result, error, status_code = await retry_async(
                lambda: self.client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread.id,
                    run_id=run.id,
                    tool_outputs=tool_outputs,
                ),
                max_retries=max_retries,
            )
            return ToolOutputsSubmitResponse(
                success=success, run=run_result, error=error, status_code=status_code
            )

        except Exception as e:
            logger.warning(f"Error submitting tool outputs: {e}")
            return ToolOutputsSubmitResponse(success=False, run=None, error=str(e), status_code=None)

    async def create_run(
        self,
        thread_id: str,
        assistant_id: str,
        max_retries: int = 5,
        additional_instructions: str | None = None
    ) -> RunCreateResponse:
        """Create a new run for a thread."""
        try:
            success, run, error, status_code = await retry_async(
                lambda: self.client.beta.threads.runs.create(
                    thread_id=thread_id,
                    assistant_id=assistant_id,
                    additional_instructions=additional_instructions
                ),
                max_retries=max_retries,
            )
            return RunCreateResponse(
                success=success, run=run, error=error, status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error creating run: {e}")
            return RunCreateResponse(
                success=False, run=None, error=str(e), status_code=None
            )
        
    async def list_runs(
        self,
        thread_id: str,
        max_retries: int = 5,
    ) -> RunListResponse:
        """List all runs for a thread.

        Args:
            thread_id: The ID of the thread to list runs for.
            max_retries: Maximum number of retry attempts.

        Returns:
            RunListResponse containing success status, list of runs if successful,
            and error message if failed.
        """
        try:
            success, runs, error, status_code = await retry_async(
                lambda: self.client.beta.threads.runs.list(thread_id=thread_id)
            )
            if success:
                return RunListResponse(
                    success=True,
                    runs=list(runs.data) if runs else [],
                    error=None,
                    status_code=status_code
                )
            return RunListResponse(
                success=False,
                runs=[],
                error=error,
                status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error listing runs: {e}")
            return RunListResponse(success=False, runs=[], error=str(e), status_code=None)

    async def cancel_run(
        self,
        thread_id: str,
        run_id: str,
        max_retries: int = 5,
    ) -> RunCancelResponse:
        """Cancel a run.

        Args:
            thread_id: The ID of the thread containing the run.
            run_id: The ID of the run to cancel.
            max_retries: Maximum number of retry attempts.

        Returns:
            RunCancelResponse containing success status, cancelled run object if successful,
            and error message if failed.
        """
        try:
            success, run, error, status_code = await retry_async(
                lambda: self.client.beta.threads.runs.cancel(
                    thread_id=thread_id,
                    run_id=run_id
                )
            )
            return RunCancelResponse(
                success=success,
                run=run,
                error=error,
                status_code=status_code
            )
        except Exception as e:
            logger.warning(f"Error canceling run: {e}")
            return RunCancelResponse(
                success=False, run=None, error=str(e), status_code=None
            )
        
    async def infer(
        self,
        assistant_id: str,
        thread_id: str,
        message: str,
        additional_instructions: str | None = None,
    ) -> InferResponse:
        """Complete cycle of interaction with assistant.

        1. Create message
        2. Create and run assistant
        3. Handle tool calls if needed
        4. Get assistant response
        """
        try:
            # Create message
            message_response = await self.create_message(
                thread_id=thread_id, content=message
            )
            if not message_response.success:
                return InferResponse(
                    success=False,
                    error=f"Failed to create message: {message_response.error}",
                    status_code=message_response.status_code
                )

            # Create run
            run_response = await self.create_run(
                thread_id=thread_id, 
                assistant_id=assistant_id, 
                additional_instructions=additional_instructions,
            )
            if not run_response.success or not run_response.run:
                return InferResponse(
                    success=False, error=f"Failed to create run: {run_response.error}", status_code=run_response.status_code
                )

            run: Run = run_response.run

            # Wait for run completion or handle tool calls
            while run.status not in ["completed", "failed", "expired"]:
                # Get updated run status
                success, run, error, status_code = await retry_async(
                    lambda: self.client.beta.threads.runs.retrieve(
                        thread_id=thread_id,
                        run_id=run.id,
                    )
                )
                if not success or not run:
                    return InferResponse(
                        success=False,
                        error=f"Failed to get run status: {error}",
                        status_code=status_code
                    )

                # Handle tool calls if needed
                if run.status == "requires_action":
                    thread = await self.client.beta.threads.retrieve(
                        thread_id=thread_id
                    )
                    tool_response = await self.submit_tool_outputs(
                        run=run,
                        thread=thread,
                        tool_calls=run.required_action.submit_tool_outputs.tool_calls,  # type: ignore
                    )
                    if not tool_response.success:
                        return InferResponse(
                            success=False,
                            error=f"Failed to submit tool outputs: {tool_response.error}",
                            status_code=tool_response.status_code
                        )
                    run = tool_response.run  # type: ignore

                await asyncio.sleep(1)

            if run.status != "completed":
                return InferResponse(
                    success=False,
                    error=f"Run failed with status: {run.status}",
                    status_code=status_code
                )

            # Get assistant response
            response = await self.get_assistant_response(thread_id=thread_id)
            if not response.success or not response.message:
                return InferResponse(
                    success=False,
                    error=f"Failed to get assistant response: {response.error}",
                    status_code=response.status_code
                )

            # Extract message content
            content = ""
            if response.message.content and len(response.message.content) > 0:
                content_block = response.message.content[0]
                if hasattr(content_block, "text"):
                    content = content_block.text.value  # type: ignore

            return InferResponse(success=True, message=content, status_code=status_code)

        except Exception as e:
            logger.warning(f"Error in infer: {e}")
            return InferResponse(success=False, error=str(e), status_code=None)
