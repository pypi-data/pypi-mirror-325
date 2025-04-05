import backoff
import openai

from textwrap import dedent
from openai import AsyncOpenAI

from .base import ModelAPIInterface
from tiny_eval.core._types import Message, Choice

def on_backoff(details):
    """We don't print connection error because there's sometimes a lot of them and they're not interesting."""
    exception_details = details["exception"]
    if not str(exception_details).startswith("Connection error."):
        print(exception_details)

@backoff.on_exception(
    wait_gen=backoff.expo,
    exception=(
        openai.RateLimitError,
        openai.APIConnectionError,
        openai.APITimeoutError,
        openai.InternalServerError,
    ),
    max_value=60,
    factor=1.5,
    on_backoff=on_backoff,
)
async def _openai_chat_completion(*, client: AsyncOpenAI, **kwargs):
    return await client.chat.completions.create(**kwargs)

class OpenAIModelAPI(ModelAPIInterface):
    """
    Model API for OpenRouter.
    """
    model: str
    client: AsyncOpenAI

    def __init__(
        self,
        model: str,
        client: AsyncOpenAI | None = None,
    ):
        self.client = client or AsyncOpenAI()
        self.model = model
    
    async def _get_response(
        self, 
        messages: list[Message],
        # extra options 
        n: int = 1,
        temperature: float = 1.0,
        logprobs: bool = False
    ) -> str:
        choices = await self._get_response_many(
            messages,
            n=n,
            temperature=temperature, 
            logprobs=logprobs
        )
        return choices[0].message.content
    
    async def _get_logprobs(self, messages: list[Message]) -> dict[str, float]:
        """ Get logprobs for the next token. Always samples 1 token."""
        completion = await _openai_chat_completion(
            client=self.client,
            model=self.model,
            messages=[message.to_dict() for message in messages], # type: ignore
            max_tokens=1,
            temperature=0,
            logprobs=True,
            top_logprobs=20,
        )
        try:
            logprobs = completion.choices[0].logprobs.content[0].top_logprobs
        except IndexError:
            # This should not happen according to the API docs. But it sometimes does.
            warning = dedent(f"""\
                Failed to get logprobs because {self.model} didn't send them.
                Returning empty dict, I hope you can handle it.
                Last completion has empty logprobs.content: {completion}.
            """)
            print(warning)
            return {}

        result = {}
        for el in logprobs:
            result[el.token] = float(el.logprob)
        return result

    async def _get_response_many(
        self, 
        messages: list[Message],
        *,
        # extra options 
        n: int = 1,
        temperature: float = 1.0,
        logprobs: bool = False
    ) -> list[Choice]:
        
        try: 
            completion = await _openai_chat_completion(
                client=self.client,
                model=self.model,
                messages=[message.to_dict() for message in messages], # type: ignore
                n=n,
                temperature=temperature,
                logprobs=logprobs,
            )
            return [
                Choice(
                    message=Message(
                        role=choice.message.role,
                        content=choice.message.content or "",
                    ),
                    # TODO: add logprobs
                ) for choice in completion.choices
            ]
        
        except Exception as e:
            raise e