# API Connection Handling

## Current Issues

### 1. Inconsistent API Key Validation
- Different validation approaches across the codebase
- Validation happening at different stages (init vs runtime)
- Inconsistent error messages
- No standardized retry mechanism

### 2. Security Concerns
- API keys exposed in test outputs
- Hardcoded mock keys in test files
- `.env` file with real keys in repository
- No key rotation or expiration handling

### 3. Error Handling Variations
- Mix of exceptions and error strings
- Inconsistent error message formats
- Missing detailed error information
- No standardized logging

## Standardization Guidelines

### 1. API Key Management

```python
from typing import Optional
from pydantic import BaseModel, SecretStr
import os
from enum import Enum

class Provider(str, Enum):
    CLAUDE = "claude"
    GEMINI = "gemini"

class APIKeyManager:
    """Centralized API key management."""
    
    ENV_KEYS = {
        Provider.CLAUDE: "ANTHROPIC_API_KEY",
        Provider.GEMINI: "GOOGLE_API_KEY"
    }
    
    @classmethod
    def get_key(cls, provider: Provider) -> SecretStr:
        """Get API key for provider with validation."""
        env_key = cls.ENV_KEYS[provider]
        key = os.getenv(env_key)
        if not key:
            raise ValueError(f"{env_key} not found in environment variables")
        return SecretStr(key)
    
    @classmethod
    def validate_all(cls) -> dict[Provider, bool]:
        """Validate all configured API keys."""
        return {
            provider: bool(os.getenv(env_key))
            for provider, env_key in cls.ENV_KEYS.items()
        }
```

### 2. Provider Connection Management

```python
from abc import ABC, abstractmethod
from typing import Optional
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

class ProviderConnection(ABC):
    """Base class for provider connections."""
    
    def __init__(self, provider: Provider):
        self.provider = provider
        self.api_key = APIKeyManager.get_key(provider)
        self.client = self._init_client()
    
    @abstractmethod
    def _init_client(self):
        """Initialize provider client."""
        pass
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    def validate_connection(self) -> bool:
        """Validate connection with retry."""
        try:
            self._test_connection()
            return True
        except Exception as e:
            logger.error(f"Connection failed for {self.provider}: {str(e)}")
            raise
    
    @abstractmethod
    def _test_connection(self):
        """Test the connection with a simple API call."""
        pass
```

### 3. Provider-Specific Implementations

```python
class ClaudeConnection(ProviderConnection):
    """Claude-specific connection handling."""
    
    def _init_client(self):
        return anthropic.Anthropic(api_key=self.api_key.get_secret_value())
    
    def process_message(self, message: str, system: str = None) -> str:
        """Process a message with proper Claude formatting."""
        try:
            messages = [{"role": "user", "content": message}]
            if system:
                # Claude supports system messages directly
                response = self.client.messages.create(
                    model=self.config["model"],
                    max_tokens=self.config.get("max_tokens", 4096),
                    messages=messages,
                    system=system
                )
            else:
                response = self.client.messages.create(
                    model=self.config["model"],
                    max_tokens=self.config.get("max_tokens", 4096),
                    messages=messages
                )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude API error: {str(e)}")
            raise ProviderError(f"Claude API error: {str(e)}")

class GeminiConnection(ProviderConnection):
    """Gemini-specific connection handling."""
    
    def _init_client(self):
        return OpenAI(
            api_key=self.api_key.get_secret_value(),
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
    
    def process_message(self, message: str, system: str = None) -> str:
        """Process a message with proper Gemini formatting."""
        try:
            # Gemini doesn't support system messages directly, so include in user message
            content = message
            if system:
                content = f"Instructions: {system}\n\nUser message: {message}"
            
            response = self.client.chat.completions.create(
                model=self.config["model"],
                messages=[{"role": "user", "content": content}]
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Gemini API error: {str(e)}")
            raise ProviderError(f"Gemini API error: {str(e)}")
```

### 4. Error Handling

```python
class ProviderError(Exception):
    """Base class for provider-specific errors."""
    pass

class AuthenticationError(ProviderError):
    """Raised when authentication fails."""
    pass

class ConnectionError(ProviderError):
    """Raised when connection fails."""
    pass

class RateLimitError(ProviderError):
    """Raised when rate limit is exceeded."""
    pass

def handle_provider_error(e: Exception) -> ProviderError:
    """Map provider-specific errors to our error types."""
    error_msg = str(e).lower()
    
    if "authentication" in error_msg or "api key" in error_msg:
        return AuthenticationError(str(e))
    elif "rate limit" in error_msg or "quota" in error_msg:
        return RateLimitError(str(e))
    elif "connection" in error_msg or "timeout" in error_msg:
        return ConnectionError(str(e))
    return ProviderError(str(e))
```

### 5. Development Guidelines

1. **Connection Testing**:
```python
def test_provider_connection():
    """Test all provider connections before starting."""
    results = {}
    for provider in Provider:
        try:
            connection = get_provider_connection(provider)
            connection.validate_connection()
            results[provider] = "OK"
        except Exception as e:
            results[provider] = str(e)
    return results
```

2. **Debugging Support**:
```python
def debug_provider_call(provider: str, message: str, system: str = None):
    """Debug a provider API call."""
    try:
        connection = get_provider_connection(provider)
        logger.debug(f"Provider: {provider}")
        logger.debug(f"Message: {message}")
        logger.debug(f"System: {system}")
        
        response = connection.process_message(message, system)
        logger.debug(f"Response: {response}")
        return response
    except Exception as e:
        logger.error(f"Error in provider call: {str(e)}")
        raise
```

3. **Environment Validation**:
```python
def validate_environment():
    """Validate the development environment."""
    issues = []
    
    # Check API keys
    for provider in Provider:
        if not os.getenv(APIKeyManager.ENV_KEYS[provider]):
            issues.append(f"Missing {APIKeyManager.ENV_KEYS[provider]}")
    
    # Check provider configurations
    for provider in Provider:
        try:
            _ = get_provider_config(provider)
        except Exception as e:
            issues.append(f"Invalid config for {provider}: {str(e)}")
    
    return issues
```

## Common Issues and Solutions

### 1. Authentication Errors
- **Issue**: "API key not valid" or "invalid x-api-key"
- **Solution**: 
  1. Verify key exists in environment
  2. Check key format and validity
  3. Ensure no whitespace in key
  4. Verify API is enabled in provider console

### 2. System Message Handling
- **Issue**: Different providers handle system messages differently
- **Solution**:
  1. Use provider-specific message formatters
  2. For Gemini, include system message in user content
  3. For Claude, use dedicated system parameter

### 3. Connection Issues
- **Issue**: Connection timeouts or failures
- **Solution**:
  1. Implement retry mechanism
  2. Use exponential backoff
  3. Add proper error handling
  4. Log detailed error information

### 4. Development Setup
- **Issue**: Inconsistent environment setup
- **Solution**:
  1. Use `.env.example` template
  2. Document required environment variables
  3. Add environment validation
  4. Provide setup scripts

## Testing Best Practices

1. **Separation of Tests**:
   ```python
   @pytest.mark.unit
   def test_api_key_validation():
       """Unit test for API key validation."""
       pass

   @pytest.mark.integration
   def test_provider_integration():
       """Integration test for provider API."""
       pass
   ```

2. **Mock Responses**:
   ```python
   @pytest.fixture
   def mock_provider_response():
       """Mock provider API responses."""
       def _mock_response(provider: str, content: str):
           if provider == "claude":
               return {"content": [{"text": content}]}
           return {"choices": [{"message": {"content": content}}]}
       return _mock_response
   ```

3. **Error Testing**:
   ```python
   @pytest.mark.parametrize("error_type", [
       "authentication",
       "rate_limit",
       "connection",
       "unknown"
   ])
   def test_error_handling(error_type):
       """Test different error scenarios."""
       pass
   ```

## Monitoring and Logging

1. **Request Logging**:
   ```python
   def log_provider_request(provider: str, request: dict):
       """Log provider API request (excluding sensitive data)."""
       safe_request = request.copy()
       safe_request.pop("api_key", None)
       logger.info(f"Provider request: {safe_request}")
   ```

2. **Error Tracking**:
   ```python
   def track_provider_error(provider: str, error: Exception):
       """Track provider-specific errors."""
       error_type = type(error).__name__
       metrics.increment(f"provider.{provider}.error.{error_type}")
       logger.error(f"Provider error: {error}", extra={
           "provider": provider,
           "error_type": error_type
       })
   ```

3. **Performance Monitoring**:
   ```python
   def monitor_provider_latency(provider: str, start_time: float):
       """Monitor provider API latency."""
       latency = time.time() - start_time
       metrics.timing(f"provider.{provider}.latency", latency)
       logger.info(f"Provider latency: {latency}s", extra={
           "provider": provider,
           "latency": latency
       })
   ```

## Implementation Steps

1. **Create New Classes**:
   - Implement `APIKeyManager`
   - Implement `ProviderConnection` base class
   - Implement provider-specific connection classes

2. **Update Existing Code**:
   - Replace direct `os.getenv()` calls with `APIKeyManager`
   - Update provider initialization to use new connection classes
   - Standardize error handling

3. **Security Updates**:
   - Remove API key printing from tests
   - Update mock key handling
   - Add `.env` to `.gitignore`
   - Add key rotation documentation

4. **Documentation**:
   - Update provider setup guides
   - Add security best practices
   - Document error handling
   - Add troubleshooting guides

## Best Practices

1. **API Key Handling**:
   - Never log or print API keys
   - Use `SecretStr` for key storage
   - Validate keys at initialization
   - Support key rotation

2. **Error Handling**:
   - Use specific exception types
   - Include detailed error messages
   - Implement retry mechanisms
   - Log errors appropriately

3. **Testing**:
   - Use mock keys in tests
   - Mock API responses
   - Test error cases
   - Validate connection handling

4. **Security**:
   - Keep keys in environment variables
   - Use key rotation
   - Implement access logging
   - Monitor usage patterns

## API Version Control

```python
class ProviderVersion(BaseModel):
    """Provider version configuration."""
    api_version: str
    model_version: str
    compatibility_mode: Optional[str] = None

class ProviderVersions:
    """Current supported versions for each provider."""
    CLAUDE = ProviderVersion(
        api_version="2024-03",
        model_version="claude-3-5-sonnet-latest"
    )
    GEMINI = ProviderVersion(
        api_version="2024-01",
        model_version="gemini-pro",
        compatibility_mode="openai"
    )

    @classmethod
    def get_version(cls, provider: Provider) -> ProviderVersion:
        """Get version configuration for provider."""
        return getattr(cls, provider.upper())
```

## Response Format Standardization

```python
class StandardResponse(BaseModel):
    """Standardized response format across providers."""
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    usage: Dict[str, int] = Field(default_factory=dict)
    provider: str
    model: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResponseFormatter:
    """Format provider responses into standard format."""
    
    @classmethod
    def format_claude_response(cls, response: Any) -> StandardResponse:
        return StandardResponse(
            content=response.content[0].text,
            metadata={
                "id": response.id,
                "role": response.role
            },
            usage={
                "prompt_tokens": response.usage.input_tokens,
                "completion_tokens": response.usage.output_tokens
            },
            provider="claude",
            model=response.model
        )
    
    @classmethod
    def format_gemini_response(cls, response: Any) -> StandardResponse:
        return StandardResponse(
            content=response.choices[0].message.content,
            metadata={
                "id": response.id,
                "role": response.choices[0].message.role
            },
            usage={
                "total_tokens": response.usage.total_tokens
            },
            provider="gemini",
            model=response.model
        )
```

## Environment Setup

### Required Environment Variables

```bash
# .env.example

# Claude API Configuration
ANTHROPIC_API_KEY=sk-ant-api03-************************  # 32-char key
ANTHROPIC_API_VERSION=2024-03

# Gemini API Configuration
GOOGLE_API_KEY=AIza********************************     # 39-char key
GOOGLE_API_VERSION=2024-01

# Optional Configuration
DEFAULT_TEMPERATURE=0.7
DEFAULT_MAX_TOKENS=4096
ENABLE_STREAMING=false
```

### API Key Validation

```python
import re

class APIKeyValidator:
    """Validate API key formats."""
    
    PATTERNS = {
        Provider.CLAUDE: r'^sk-ant-api03-[A-Za-z0-9]{32}$',
        Provider.GEMINI: r'^AIza[A-Za-z0-9_-]{35}$'
    }
    
    @classmethod
    def validate_key(cls, provider: Provider, key: str) -> bool:
        """Validate API key format."""
        pattern = cls.PATTERNS.get(provider)
        if not pattern:
            raise ValueError(f"No validation pattern for provider: {provider}")
        return bool(re.match(pattern, key))
    
    @classmethod
    def validate_key_with_feedback(cls, provider: Provider, key: str) -> tuple[bool, str]:
        """Validate API key format with feedback."""
        try:
            if not key:
                return False, "API key is empty"
            
            if not cls.validate_key(provider, key):
                if provider == Provider.CLAUDE:
                    return False, "Invalid Claude API key format. Should start with 'sk-ant-api03-' followed by 32 characters."
                elif provider == Provider.GEMINI:
                    return False, "Invalid Gemini API key format. Should start with 'AIza' followed by 35 characters."
            
            return True, "API key format is valid"
        except Exception as e:
            return False, f"Validation error: {str(e)}"
```

### Environment Validation Script

```python
def validate_environment_setup():
    """Validate complete environment setup."""
    results = {
        "api_keys": {},
        "versions": {},
        "configuration": {}
    }
    
    # Validate API keys
    for provider in Provider:
        key = os.getenv(APIKeyManager.ENV_KEYS[provider])
        is_valid, message = APIKeyValidator.validate_key_with_feedback(provider, key)
        results["api_keys"][provider] = {
            "present": bool(key),
            "valid": is_valid,
            "message": message
        }
    
    # Validate API versions
    for provider in Provider:
        version_key = f"{provider.upper()}_API_VERSION"
        version = os.getenv(version_key)
        expected = ProviderVersions.get_version(provider).api_version
        results["versions"][provider] = {
            "present": bool(version),
            "valid": version == expected,
            "current": version,
            "expected": expected
        }
    
    # Validate configuration
    results["configuration"] = {
        "temperature": os.getenv("DEFAULT_TEMPERATURE", "0.7"),
        "max_tokens": os.getenv("DEFAULT_MAX_TOKENS", "4096"),
        "streaming": os.getenv("ENABLE_STREAMING", "false").lower() == "true"
    }
    
    return results 