# Creating Tools

Tools are the specific actions that agents can perform. Each tool is defined using Pydantic for input validation and clear interfaces.

## Important Requirements

1. **Tool Structure**
   - Must inherit from `BaseTool`
   - Must implement `run` method
   - Must use Pydantic fields
   - Must handle errors properly

2. **Environment Variables**
   - Load at tool initialization
   - Use secure storage
   - Handle missing variables
   - Provide clear error messages

## Basic Tool Structure

```python
from multi_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class APITool(BaseTool):
    """
    Make API calls to external services.
    
    This tool handles authentication, request formatting,
    and response processing for API interactions.
    """
    endpoint: str = Field(
        ..., description="API endpoint to call"
    )
    method: str = Field(
        default="GET",
        description="HTTP method to use"
    )
    data: Optional[Dict] = Field(
        default=None,
        description="Data to send with request"
    )

    def __init__(self, **data):
        super().__init__(**data)
        self.api_key = os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API_KEY environment variable not set")

    def run(self) -> Dict:
        """Execute the API call with proper error handling."""
        try:
            # Make API call
            response = requests.request(
                method=self.method,
                url=self.endpoint,
                json=self.data,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()
            return response.json()
            
        except requests.RequestException as e:
            raise ToolError(f"API call failed: {str(e)}")
```

## Tool Components

### 1. Class Definition
```python
class CustomTool(BaseTool):
    """
    Clear docstring explaining:
    - Tool's purpose
    - Required inputs
    - Expected outputs
    - Usage examples
    """
```

### 2. Fields
```python
class CustomTool(BaseTool):
    required_field: str = Field(
        ...,  # ... means required
        description="Clear description of the field"
    )
    optional_field: Optional[str] = Field(
        default=None,
        description="Description of optional field"
    )
```

### 3. Run Method
```python
def run(self) -> Union[str, Dict]:
    """
    Main execution logic with:
    - Input validation
    - Error handling
    - Resource management
    - Proper return types
    """
```

## Error Handling

### 1. Tool-Specific Errors
```python
from multi_swarm.exceptions import ToolError

class DatabaseTool(BaseTool):
    query: str = Field(..., description="SQL query to execute")
    
    def run(self):
        try:
            # Execute query
            with self.get_connection() as conn:
                result = conn.execute(self.query)
                return result.fetchall()
                
        except Exception as e:
            raise ToolError(
                error_type="database_error",
                message=f"Query execution failed: {str(e)}",
                context={
                    "query": self.query,
                    "error": str(e)
                }
            )
```

### 2. Resource Cleanup
```python
class FileProcessingTool(BaseTool):
    file_path: str = Field(..., description="Path to file")
    
    def run(self):
        temp_files = []
        try:
            # Process file
            temp_file = self.create_temp_file()
            temp_files.append(temp_file)
            return self.process_file(temp_file)
            
        finally:
            # Clean up resources
            for file in temp_files:
                try:
                    os.remove(file)
                except Exception as e:
                    self.logger.error(f"Cleanup failed: {str(e)}")
```

### 3. Input Validation
```python
from pydantic import validator

class DataProcessingTool(BaseTool):
    data_path: str = Field(..., description="Path to data file")
    
    @validator("data_path")
    def validate_path(cls, v):
        if not os.path.exists(v):
            raise ValueError(f"File not found: {v}")
        if not v.endswith((".csv", ".json")):
            raise ValueError("Only CSV and JSON files are supported")
        return v
```

## Testing Tools

### 1. Unit Tests
```python
def test_api_tool():
    # Test successful case
    tool = APITool(endpoint="https://api.example.com/data")
    response = tool.run()
    assert response is not None
    
    # Test error handling
    with pytest.raises(ToolError) as exc:
        tool = APITool(endpoint="invalid-url")
        tool.run()
    assert "API call failed" in str(exc.value)
```

### 2. Integration Tests
```python
def test_tool_in_agent():
    # Create agent with tool
    agent = TestAgent("TestAgent")
    tool = APITool(endpoint="https://api.example.com/data")
    agent.add_tool(tool)
    
    # Test tool usage in agent
    thread = agent.thread_manager.create_thread()
    thread.add_message(
        content="Use API tool",
        role="user",
        agent_name="user"
    )
    
    response = agent._process_with_llm(thread)
    assert response is not None
```

### 3. Resource Tests
```python
def test_resource_management():
    tool = FileProcessingTool(file_path="test.txt")
    
    # Check resource cleanup
    temp_files_before = set(os.listdir(temp_dir))
    tool.run()
    temp_files_after = set(os.listdir(temp_dir))
    
    assert temp_files_before == temp_files_after
```

## Best Practices

### 1. Tool Design
- Single responsibility principle
- Clear input/output interfaces
- Comprehensive error handling
- Proper resource management

### 2. Security
- Validate all inputs
- Sanitize file paths
- Handle sensitive data
- Use environment variables

### 3. Performance
- Optimize resource usage
- Implement timeouts
- Cache when appropriate
- Monitor execution time

### 4. Testing
- Write comprehensive tests
- Test error cases
- Check resource cleanup
- Verify in agent context

## Common Issues and Solutions

### 1. Resource Leaks
**Problem**: Resources not properly cleaned up
**Solution**:
- Use context managers
- Implement cleanup in finally blocks
- Monitor resource usage
- Log cleanup failures

### 2. Error Handling
**Problem**: Unclear error messages
**Solution**:
- Use custom ToolError
- Include context in errors
- Log detailed information
- Implement proper recovery

### 3. Performance
**Problem**: Slow tool execution
**Solution**:
- Optimize operations
- Implement caching
- Use async where appropriate
- Monitor execution time

## Example Tools

### 1. File Processing
```python
class FileProcessor(BaseTool):
    """Process files with proper resource management."""
    input_path: str = Field(..., description="Input file path")
    output_path: str = Field(..., description="Output file path")
    
    @validator("input_path", "output_path")
    def validate_paths(cls, v):
        if not os.path.exists(os.path.dirname(v)):
            raise ValueError(f"Directory not found: {os.path.dirname(v)}")
        return v
    
    def run(self):
        try:
            with open(self.input_path, 'r') as f_in:
                data = f_in.read()
                
            processed = self.process_data(data)
            
            with open(self.output_path, 'w') as f_out:
                f_out.write(processed)
                
            return {"status": "success", "output_path": self.output_path}
            
        except Exception as e:
            raise ToolError(f"File processing failed: {str(e)}")
```

### 2. API Integration
```python
class SecureAPITool(BaseTool):
    """Make secure API calls with proper error handling."""
    endpoint: str = Field(..., description="API endpoint")
    method: str = Field(default="GET")
    timeout: int = Field(default=30)
    
    def __init__(self, **data):
        super().__init__(**data)
        self.session = self.create_secure_session()
    
    def run(self):
        try:
            response = self.session.request(
                method=self.method,
                url=self.endpoint,
                timeout=self.timeout
            )
            return self.process_response(response)
            
        except Exception as e:
            self.handle_error(e)
```

## Learn More

- [Creating Agents](creating-agents.md)
- [Testing Guide](testing.md)
# Creating Tools

Tools are the specific actions that agents can perform. Each tool is defined using Pydantic for input validation and clear interfaces.

## Basic Tool Structure

```python
from multi_swarm.tools import BaseTool
from pydantic import Field
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

class DataVisualizationTool(BaseTool):
    """
    Create data visualizations using various plotting libraries.
    Supports multiple chart types and customization options.
    """
    data_path: str = Field(
        ..., description="Path to the data file to visualize"
    )
    chart_type: str = Field(
        ..., description="Type of chart to create (line, bar, scatter, etc.)"
    )
    title: str = Field(
        default="", description="Title for the visualization"
    )

    def run(self):
        """Execute the visualization logic."""
        # Implementation using plotting libraries
        return f"Created {self.chart_type} chart from {self.data_path}"
```

## Tool Components

1. **Class Definition**
   - Inherit from `BaseTool`
   - Clear docstring explaining purpose
   - Input validation with Pydantic

2. **Fields**
   - Use Pydantic's `Field` for validation
   - Clear descriptions for each field
   - Appropriate default values

3. **Run Method**
   - Main execution logic
   - Return results as string
   - Handle errors appropriately

## Best Practices

### 1. Environment Variables

```python
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

class APITool(BaseTool):
    endpoint: str = Field(..., description="API endpoint to call")
    
    def run(self):
        """Make API call using environment variables."""
        # Use API_KEY and BASE_URL from environment
        return "API response"
```

### 2. Error Handling

```python
from multi_swarm.exceptions import ToolError

class RiskySQLTool(BaseTool):
    query: str = Field(..., description="SQL query to execute")
    
    def run(self):
        """Execute SQL query with error handling."""
        try:
            # Execute query
            return "Query results"
        except Exception as e:
            raise ToolError(f"SQL execution failed: {str(e)}")
```

### 3. Resource Management

```python
class FileProcessingTool(BaseTool):
    file_path: str = Field(..., description="Path to file to process")
    
    def run(self):
        """Process file with proper resource management."""
        try:
            with open(self.file_path, 'r') as f:
                # Process file
                return "Processing results"
        finally:
            # Cleanup if needed
            pass
```

## Advanced Features

### 1. Async Support

```python
class AsyncAPITool(BaseTool):
    endpoint: str = Field(..., description="API endpoint")
    
    async def run(self):
        """Asynchronous API call."""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.endpoint) as response:
                return await response.text()
```

### 2. Progress Tracking

```python
class LongRunningTool(BaseTool):
    steps: int = Field(..., description="Number of steps")
    
    def run(self):
        """Execute with progress updates."""
        for i in range(self.steps):
            self.update_progress(i / self.steps)
            # Do work
        return "Task completed"
```

### 3. File Storage Integration

```python
class DataStorageTool(BaseTool):
    data: str = Field(..., description="Data to store")
    
    def run(self):
        """Store data with file system integration."""
        storage = self.get_file_storage()
        path = storage.save_file("data.txt", self.data)
        return f"Data stored at {path}"
```

## Example Tools

### 1. API Integration

```python
class OpenAITool(BaseTool):
    """
    Interact with OpenAI's API for specific tasks.
    """
    prompt: str = Field(..., description="Prompt for the API")
    model: str = Field(default="gpt-4", description="Model to use")
    
    def run(self):
        """Execute OpenAI API call."""
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": self.prompt}]
        )
        return response.choices[0].message.content
```

### 2. Data Processing

```python
class DataFrameTool(BaseTool):
    """
    Process data using pandas DataFrame operations.
    """
    csv_path: str = Field(..., description="Path to CSV file")
    operation: str = Field(..., description="Operation to perform")
    
    def run(self):
        """Execute DataFrame operation."""
        import pandas as pd
        df = pd.read_csv(self.csv_path)
        
        if self.operation == "summary":
            return df.describe().to_string()
        elif self.operation == "head":
            return df.head().to_string()
        else:
            raise ToolError(f"Unknown operation: {self.operation}")
```

### 3. File Operations

```python
class FileAnalyzerTool(BaseTool):
    """
    Analyze file contents and structure.
    """
    file_path: str = Field(..., description="Path to file")
    analysis_type: str = Field(..., description="Type of analysis")
    
    def run(self):
        """Perform file analysis."""
        if not os.path.exists(self.file_path):
            raise ToolError(f"File not found: {self.file_path}")
            
        stats = os.stat(self.file_path)
        return {
            "size": stats.st_size,
            "created": stats.st_ctime,
            "modified": stats.st_mtime
        }
```

## Testing Tools

```python
if __name__ == "__main__":
    # Test visualization tool
    viz_tool = DataVisualizationTool(
        data_path="data.csv",
        chart_type="line",
        title="Test Chart"
    )
    print(viz_tool.run())
    
    # Test API tool
    api_tool = OpenAITool(
        prompt="Hello, world!",
        model="gpt-4"
    )
    print(api_tool.run())
```

## Learn More

- [Creating Agents](creating-agents.md)
- [Communication Flows](communication-flows.md)
- [API Reference](../api/tools.md) 