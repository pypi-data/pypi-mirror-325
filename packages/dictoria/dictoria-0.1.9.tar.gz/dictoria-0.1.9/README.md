# Dictoria: Regex-based Dictionary Extension

**Dictoria** is an extension of Python's built-in `dict` type that allows searching for values using regular expressions. The library supports recursive searching in nested dictionaries and provides convenient methods for filtering results.

Keys in the dictionary are represented as paths in the format `/root/key/subkey`, making it intuitive and powerful to work with complex data structures.

---

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Key Features](#key-features)
  - [Initialization](#initialization)
  - [Method `__getitem__`](#__getitem__)
  - [Method `get`](#method-get)
- [Examples](#examples)
- [Documentation](#documentation)
- [Requirements](#requirements)
- [License](#license)
- [Authors](#authors)
- [Contributing](#contributing)
- [Contact](#contact)

---

## Description

Dictoria extends Python's standard dictionary to enable regex-based key searches. It is particularly useful for scenarios where dynamic access to nested data structures is required. With Dictoria, you can:
- Search for values using regular expressions.
- Filter results by type or content.
- Handle non-existent keys gracefully with a `default` parameter.

This library simplifies working with deeply nested dictionaries and provides a flexible way to retrieve data.

---

## Installation

You can install Dictoria using `pip`:

```bash
pip install dictoria
```

If you're using `poetry`, add the library to your project:

```bash
poetry add dictoria
```

## Quick Start

```python
from dictoria import Dictoria

# Create a Dictoria instance
data = Dictoria({
    "users": {
        "user1": {"name": "Alice", "age": 25},
        "user2": {"name": "Bob", "age": 30}
    },
    "settings": {
        "timeout": 60,
        "debug": False
    }
})

# Search for all user ages
ages: list[int] = list(data[r"/users/.+/age"])
print(ages)  # Output: [25, 30]

# Search for a specific user name
name: str = data.get(r"/users/.+/name", target=r"Alice")
print(name)  # Output: Alice

# Handle non-existent keys
result: str = data.get(r"/nonexistent", default="Not found")
print(result)  # Output: Not found
```

## Key Features

### Initialization
Dictoria accepts a dictionary as input when creating an instance:

```python
data = Dictoria({
    "key1": "value1",
    "key2": {
        "subkey1": "subvalue1",
        "subkey2": "subvalue2"
    }
})
```

### Method `__getitem__`

The `__getitem__` method allows retrieving values from the dictionary using regular expressions. Keys are represented as paths in the format `/root/key/subkey`.

```python
# Retrieve all values matching the pattern
ages: list[int] = list(data[r"/users/.+/age"])
print(ages)  # Output: [25, 30]
```

### Method `get`

The `get` method extends the standard `dict.get` functionality and supports additional parameters for filtering results:

- `typeof`: Filters results by the specified type.
- `target`: Matches values against a regular expression.
- `default`: Specifies a default value if no matches are found.

```python
# Filter by type
age: int = data.get(r"/users/.+/age", typeof=int)
print(age)  # Output: 25

# Match value content
name: str = data.get(r"/users/.+/name", target=r"Alice")
print(name)  # Output: Alice

# Handle missing keys
result: str = data.get(r"/nonexistent", default="Not found")
print(result)  # Output: Not found
```

## Examples

### Example 1: Recursive Age Search

```python
from dictoria import Dictoria

data = Dictoria({
    "users": {
        "user1": {"name": "Alice", "age": 25},
        "user2": {"name": "Bob", "age": 30}
    }
})

# Search for all user ages
ages: list[int] = list(data[r"/users/.+/age"])
print(ages)  # Output: [25, 30]
```

### Example 2: Combined Filtering

```python
# Filter by type
age: int = data.get(r"/users/.+/age", typeof=int)
print(age)  # Output: 25

# Match value content
name: str = data.get(r"/users/.+/name", target=r"Alice")
print(name)  # Output: Alice
```

### Example 3: Error Handling

```python
# If no matches are found, return a default value
result: str = data.get(r"/nonexistent", default="Not found")
print(result)  # Output: Not found
```

## Documentation

You can also generate the documentation locally using `Sphinx` :

1. Install Sphinx:

```bash
poetry add sphinx
```

2. Build the documentation:

```bash
sphinx-build -b html docs/ docs/_build
```

3. Open the generated documentation:

```bash
open docs/_build/index.html
```

## Requirements

- Python 3.8+
- Built-in libraries:
    - `re` (for regular expressions)

## License

This project is licensed under the MIT License.

## Authors

- Tamerlan Larsanov `@tamerlanlarsanov`

## Contributing

Contributions are welcome! To contribute to Dictoria:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes and submit a pull request.
Please ensure your code adheres to the existing style and includes appropriate tests.

## Contact

@tamerlanlarsanov
