"""Run some tests using a real LLaMAv2 model."""

import logging

import pytest

from kani import ChatMessage, Kani
from kani.engines.llamacpp import LlamaCppEngine

pytestmark = pytest.mark.llama


@pytest.fixture(scope="module")
def llama():
    return LlamaCppEngine(repo_id="TheBloke/Llama-2-7B-Chat-GGUF", filename="*.Q4_K_M.gguf")


@pytest.fixture()
def create_kani(llama):
    default_system_prompt = (
        "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while"
        " being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic,"
        " dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive"
        " in nature.\n\nIf a question does not make any sense, or is not factually coherent, explain why"
        " instead of answering something not correct. If you don't know the answer to a question, please don't"
        " share false information."
    )

    def _inner(system_prompt=default_system_prompt, **kwargs):
        return Kani(llama, system_prompt=system_prompt, **kwargs)

    return _inner


@pytest.fixture(autouse=True, scope="module")
def debug_logging():
    log = logging.getLogger()
    old_level = log.level
    log.setLevel(logging.DEBUG)
    yield
    log.setLevel(old_level)


async def test_llama(create_kani, gh_log):
    """Do one round of conversation with LLaMA."""
    ai = create_kani()
    print("Q: What are some cool things to do in Tokyo?\n")
    stream = ai.chat_round_stream("What are some cool things to do in Tokyo?")
    async for token in stream:
        print(token, end="", flush=True)
    resp = await stream.message()

    gh_log.write(
        "# LLaMA Basic\n"
        "*This is a real output from kani running LLaMA v2 on GitHub Actions.*\n\n"
        "---\n\n"
        "> What are some cool things to do in Tokyo?\n\n"
    )
    gh_log.write(resp.text)
    gh_log.write("\n\n---\n\n")


async def test_chatting_llamas(create_kani, gh_log):
    """Two kanis chatting with each other for 5 rounds."""
    tourist = create_kani(
        "You are a tourist with plans to visit Tokyo.",
        chat_history=[ChatMessage.assistant("What are some cool things to do in Tokyo?")],
    )
    guide = create_kani()

    tourist_response = tourist.chat_history[-1].text
    gh_log.write(
        "# LLaMAs Visit Tokyo\n"
        "*These are real outputs from two kani running LLaMA v2 on GitHub Actions.*\n\n"
        "---\n\n"
        f"### Tourist\n{tourist_response}\n"
    )
    for _ in range(5):
        print("\n========== GUIDE ==========\n")
        guide_stream = guide.chat_round_stream(tourist_response)
        async for token in guide_stream:
            print(token, end="", flush=True)
        guide_msg = await guide_stream.message()
        guide_response = guide_msg.text

        print("\n========== TOURIST ==========\n")
        tourist_stream = tourist.chat_round_stream(guide_response)
        async for token in tourist_stream:
            print(token, end="", flush=True)
        tourist_msg = await tourist_stream.message()
        tourist_response = tourist_msg.text

        gh_log.write(f"### Guide\n{guide_response}\n\n### Tourist\n{tourist_response}\n\n")
