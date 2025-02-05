# Opus

Opus is a Python package for efficient task execution, designed to handle parallel and distributed workloads seamlessly. Whether you need to execute tasks asynchronously, schedule workflows, or manage dependencies, Opus provides a simple yet powerful interface.

## Features

- **Asynchronous Task Execution**: Run tasks concurrently using Python's async capabilities.
- **Parallel Processing**: Utilize multi-threading and multi-processing for performance.
- **Simple API**: Easy-to-use interface for defining and executing tasks.

## Installation

You can install Opus using pip:

```sh
pip install opus
```

## Quick Start

### Define and Execute a Task

```python
from opus import Task

# Define a simple task
def my_task(name):
    print(f"Hello, {name}!")

# Create and execute the task
task = Task(my_task, args=("World",))
task.run()
```

### Using Async Tasks

```python
import asyncio
from opus import AsyncTask

async def async_task(name):
    await asyncio.sleep(1)
    print(f"Async Hello, {name}!")

# Run an async task
task = AsyncTask(async_task, args=("Async World",))
asyncio.run(task.run())
```

## Contributing

Contributions is welcomed! Please open an issue or submit a pull request on GitHub.

## License

Opus is licensed under the MIT License.

---

For more details, visit our [GitHub repository](https://github.com/kolodkin/opus).

