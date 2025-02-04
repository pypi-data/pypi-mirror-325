# pylint: skip-file
import pytest
from unittest.mock import AsyncMock, patch
from llmworkbook import LLMRunner, LLMConfig


@pytest.fixture
def mock_config():
    """Fixture for creating an LLMConfig object."""
    return LLMConfig(
        provider="openai",
        api_key="test-api-key",
        system_prompt="Process these Data rows as per the provided prompt",
        options={
            "model_name": "gpt-4o-mini",
            "temperature": 1,
            "max_tokens": 1024,
        },
    )


@pytest.mark.asyncio
async def test_llmrunner_initialization(mock_config):
    """Test that LLMRunner initializes correctly."""
    runner = LLMRunner(config=mock_config)
    assert runner.config == mock_config


@pytest.mark.asyncio
async def test_run(mock_config):
    """Test the run method with the OpenAI provider."""
    # Initialize the runner
    runner = LLMRunner(config=mock_config)

    # Mock _call_llm_openai
    runner._call_llm_openai = AsyncMock(return_value="LLM response for prompt")

    # Call run
    result = await runner.run("Explain Newton's first law in simple terms.")

    # Assert the result
    assert result == "LLM response for prompt"

    # Verify the internal method call
    runner._call_llm_openai.assert_called_once_with(
        "Explain Newton's first law in simple terms."
    )


def test_run_sync(mock_config):
    """Test the synchronous wrapper for the run method."""
    # Initialize the runner
    runner = LLMRunner(config=mock_config)

    # Mock the async run method
    runner.run = AsyncMock(return_value="LLM response for prompt")

    # Call run_sync
    result = runner.run_sync("Explain Newton's first law in simple terms.")

    # Assert the result
    assert result == "LLM response for prompt"

    # Verify the run method call
    runner.run.assert_called_once_with("Explain Newton's first law in simple terms.")


@pytest.mark.asyncio
async def test_provider():
    """Test handling of an unimplemented provider."""
    with pytest.raises(NotImplementedError):
        await LLMRunner(config=LLMConfig(provider="llmprovider")).run("prompt")


@pytest.mark.asyncio
async def test_call_llm_openai(mock_config):
    """Test the _call_llm_openai method with mocked OpenAI response."""
    # Create an instance of LLMRunner with the mock configuration
    runner = LLMRunner(config=mock_config)

    # Mock response data format from OpenAI API
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock()]
    mock_response.choices[0].message = AsyncMock()
    mock_response.choices[0].message.content = "Mocked response text"

    # Patch the specific OpenAI method instead of the entire class
    with patch(
        "openai.resources.chat.completions.Completions.create",
        return_value=mock_response,
    ) as mock_create:
        # Call the async function
        response = await runner._call_llm_openai("Test prompt")

        # Assertions to check the behavior
        assert response == "Mocked response text"
        mock_create.assert_called_once_with(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": mock_config.system_prompt},
                {"role": "user", "content": "Test prompt"},
            ],
            temperature=mock_config.options["temperature"],
        )
