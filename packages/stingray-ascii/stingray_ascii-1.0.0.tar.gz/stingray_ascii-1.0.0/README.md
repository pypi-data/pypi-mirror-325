# Stingray ASCII

A **useless** Python library that helps you print stingray ASCII art.

## Installation

You can install this package using pip:

```bash
pip install stingray-ascii
```

## Usage

Import the package and use the functions to print stingray ASCII art facing left or right.

```python
from stingray_ascii.core import print_mini_stingray_ascii, print_stingray_ascii

# Print a mini stingray facing left (default)
print_mini_stingray_ascii()

# Print a mini stingray facing right
print_mini_stingray_ascii('right')

# Print a large stingray facing left (default)
print_stingray_ascii()

# Print a large stingray facing right
print_stingray_ascii('right')
```

## Examples

### Mini Stingray ASCII
```bash
◀--
```
```bash
--▶
```

### Large Stingray ASCII
#### Facing Left
```bash
    /\  
  |  \.  
 /     \  
|:      >------  
 \     /  
  |  /'  
    \/  
```

#### Facing Right
```bash
           /\
         ./  |
        /     \
------<      :|
        \     /
         '\  |
           \/
```

## Error Handling

If an incorrect direction is provided, an `IncorrectDirection` exception is raised:

```python
from stingray_ascii.core import print_mini_stingray_ascii

print_mini_stingray_ascii('up')  # Raises IncorrectDirection error
```

## License

This project is licensed under the MIT License.

## Author

Developed by **Stingray Park**.

For more details, visit the [GitHub Repository](https://github.com/stingraypark/stingray-ascii).

