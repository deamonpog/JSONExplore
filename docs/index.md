# JSON Scout

**Scout JSON structure and navigate data safely with intuitive exploration tools.**

JSON Scout provides a robust suite of tools designed for developers and data professionals who need to introspect, analyze, and safely navigate complex JSON data structures. Whether you're working with APIs, configuration files, or large datasets, JSON Scout offers both low-level utilities and high-level abstractions to make JSON exploration intuitive and error-free.

## Key Features

### 🔍 **Structural Analysis**
- **Schema Discovery**: Automatically analyze and understand JSON structure patterns
- **Hierarchy Inspection**: Navigate nested objects and arrays with ease
- **Statistical Analysis**: Generate frequency reports for keys and data patterns

### 🛡️ **Safe Navigation**
- **Exception-Free Access**: Monadic-style `Maybe` wrapper prevents runtime errors
- **Chainable Operations**: Fluent interface for complex data traversal
- **Null-Safe Operations**: Gracefully handle missing keys and malformed data

### 🔧 **Comprehensive Utilities**
- **File Operations**: Robust JSON file discovery and loading with encoding support
- **XML Integration**: Seamless XML-to-JSON conversion capabilities
- **Unified Interface**: Single entry point combining all functionality

### 📊 **Enterprise Ready**
- **Type Safety**: Full type annotations and comprehensive error handling
- **Performance Optimized**: Efficient algorithms for large data structures
- **Well Documented**: Complete API documentation with examples

## Installation

Install JSON Scout using pip:

```bash
pip install json-scout
```

## Quick Start

### Basic Exploration

```python
import jsonscout as js

# Load and explore JSON data
data = {
    "users": [
        {"name": "Alice", "age": 30, "email": "alice@example.com"},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35, "email": "charlie@example.com"}
    ],
    "metadata":     "metadata": {"version": "1.0", "created": "2024-01-01"}
}

# Use the unified Xplore interface
explorer = js.Xplore(data)

# Safe navigation with automatic error handling
user_name = explorer['users'][0]['name'].value()  # Returns: "Alice"
missing_field = explorer['users'][1]['email'].value()  # Returns: None (no exception)

# Discover available keys
print(explorer.keys())  # ['users', 'metadata']
```

### Structural Analysis

```python
# Analyze data structure patterns
explore = js.Explore(data['users'])
field_frequency = explore.field_counts()
print(field_frequency)  # {'name': 3, 'age': 3, 'email': 2}

# Safe array operations with transformations
maybe_users = js.Maybe(data['users'])
adult_names = maybe_users.array(
    func=lambda i, user: user.get('name'),
    filter=lambda i, user: user.get('age', 0) >= 30
)
print(adult_names)  # ['Alice', 'Charlie']
```

### File Operations

```python
# Discover and load JSON files
json_files = js.get_json_file_paths('/path/to/data', '*.json')
for file_path in json_files:
    try:
        data = js.read_json_file(file_path)
        explorer = js.Xplore(data)
        # Process each file safely
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
```

### XML Integration

```python
# Convert XML to JSON-like structures
xml_data = """
}

# Use the unified Xplore interface
explorer = je.Xplore(data)

# Safe navigation with automatic error handling
user_name = explorer['users'][0]['name'].value()  # Returns: "Alice"
missing_field = explorer['users'][1]['email'].value()  # Returns: None (no exception)

# Discover available keys
print(explorer.keys())  # ['users', 'metadata']
```

### Structural Analysis

```python
# Analyze data structure patterns
explore = je.Explore(data['users'])
field_frequency = explore.field_counts()
print(field_frequency)  # {'name': 3, 'age': 3, 'email': 2}

# Safe array operations with transformations
maybe_users = je.Maybe(data['users'])
adult_names = maybe_users.array(
    func=lambda i, user: user.get('name'),
    filter=lambda i, user: user.get('age', 0) >= 30
)
print(adult_names)  # ['Alice', 'Charlie']
```

### File Operations

```python
# Discover and load JSON files
json_files = je.get_json_file_paths('/path/to/data', '*.json')
for file_path in json_files:
    try:
        data = je.read_json_file(file_path)
        explorer = je.Xplore(data)
        # Process each file safely
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
```

### XML Integration

```python
# Convert XML to JSON-like structures
xml_data = """
<users>
    <user>
        <name>Alice</name>
        <age>30</age>
    </user>
</users>
"""

explorer = js.Xplore(xml_data)
if explorer.xml:
    json_structure = explorer.xml.to_dict()
    print(json_structure)  # {'user': {'name': 'Alice', 'age': '30'}}
```

## Use Cases

### API Response Analysis
- **Schema Evolution**: Track changes in API response structures over time
- **Data Validation**: Verify expected fields and data types in responses
- **Error Handling**: Safely extract data from potentially malformed API responses

### Configuration Management
- **Dynamic Configuration**: Navigate complex configuration hierarchies safely
- **Environment Validation**: Ensure required configuration keys are present
- **Default Value Handling**: Provide fallbacks for missing configuration values

### Data Pipeline Processing
- **ETL Operations**: Transform and validate JSON data in processing pipelines
- **Data Quality Assessment**: Analyze data completeness and structure consistency
- **Batch Processing**: Process large numbers of JSON files with robust error handling

### Research and Analysis
- **Dataset Exploration**: Quickly understand the structure of unfamiliar JSON datasets
- **Statistical Analysis**: Generate reports on data distribution and patterns
- **Data Profiling**: Create comprehensive profiles of JSON data sources

## Architecture

JSON Scout is built around four core components:

- **`Explore`**: Lightweight structural analysis and schema discovery
- **`Maybe`**: Monadic wrapper for safe, chainable data access
- **`SimpleXML`**: Efficient XML-to-dictionary conversion utilities
- **`Xplore`**: Unified facade combining all functionality into a single interface

This modular design allows you to use individual components for specific tasks or leverage the unified interface for comprehensive JSON exploration workflows.

## Documentation

- **[API Reference](api.md)**: Complete documentation of all classes and methods
- **Examples**: Comprehensive usage examples and patterns
- **Best Practices**: Guidelines for effective JSON exploration

## Contributing

We welcome contributions! Please see our contributing guidelines for details on how to submit bug reports, feature requests, and code contributions.

## License

JSON Scout is released under the Apache License 2.0. See the LICENSE file for details.
