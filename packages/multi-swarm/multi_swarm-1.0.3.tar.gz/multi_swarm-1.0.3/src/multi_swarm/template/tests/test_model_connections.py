import pytest
import os
from dotenv import load_dotenv
import anthropic
from openai import OpenAI

# Force reload of environment variables
load_dotenv(override=True)

def test_claude_connection():
    """Test connection to Claude API and verify model name."""
    try:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            pytest.fail("ANTHROPIC_API_KEY not found in environment variables")
            
        print(f"\nUsing Claude API Key (first 10 chars): {api_key[:10]}...")
        
        client = anthropic.Anthropic(api_key=api_key)
        
        # Test a simple completion to verify connection and model
        response = client.messages.create(
            model="claude-3-5-sonnet-latest",  # Using the latest Claude 3.5 Sonnet model
            max_tokens=1000,
            messages=[{"role": "user", "content": "Say hello!"}]
        )
        print("Claude connection successful")
        print(f"Response: {response.content[0].text}")
    except Exception as e:
        pytest.fail(f"Claude API connection failed: {str(e)}")

def test_gemini_connection():
    """Test connection to Gemini API using OpenAI compatibility layer."""
    try:
        # Debug: Print all environment variables
        print("Environment variables:")
        for key, value in os.environ.items():
            if 'KEY' in key:
                print(f"{key}: {value[:10]}...")  # Only show first 10 chars for security
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            pytest.fail("GOOGLE_API_KEY not found in environment variables")
        
        print(f"\nUsing API Key (first 10 chars): {api_key[:10]}...")
        
        # Initialize OpenAI client with Gemini configuration
        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )

        # Test chat completion
        response = client.chat.completions.create(
            model="gemini-pro",  # Using the standard production model
            messages=[
                {"role": "user", "content": "Say hello!"}
            ]
        )
        
        print("Gemini connection successful")
        print(f"Response: {response.choices[0].message}")

    except Exception as e:
        pytest.fail(f"Gemini API connection failed: {str(e)}")

if __name__ == "__main__":
    print("Testing API connections...")
    test_claude_connection()
    test_gemini_connection()
    print("All API connections successful!") 