# ESP-IDF Component Creator Script (`cc.py`)

`cc.py` is a Python script designed to automate the creation and integration of new components in ESP-IDF projects. It generates a new component folder with boilerplate files and updates the main `CMakeLists.txt` to include the component in `EXTRA_COMPONENT_DIRS`.

## Setup

Place `cc.py` in the root directory of your ESP-IDF project, ensuring it has access to `CMakeLists.txt` and the `components` directory.

## Usage

Run the script from the root project directory as follows:

```bash
python cc.py <component_name>
```

Replace `<component_name>` with your desired component name. This command will:

1. Create a folder named `<component_name>` in the `components` directory.
2. Populate it with:
   - `<component_name>.hpp` (header file with `#pragma once`).
   - `<component_name>.cpp` (source file with a template function).
   - `CMakeLists.txt` for the component.
3. Append the new component path to `EXTRA_COMPONENT_DIRS` in the main `CMakeLists.txt`, maintaining formatting.

## Example

```bash
python cc.py MyComponent
```

### Output Files

- `components/MyComponent/MyComponent.hpp`
- `components/MyComponent/MyComponent.cpp`
- `components/MyComponent/CMakeLists.txt`
- Updated `CMakeLists.txt` with `"components/MyComponent"` added to `EXTRA_COMPONENT_DIRS`.

## Error Handling

- Warns if the component already exists.
- Exits if `components` or `CMakeLists.txt` is not found.
- Prevents duplicate entries in `EXTRA_COMPONENT_DIRS`.

## License

This script is released under the [Unlicense](https://unlicense.org/), making it public domain. You are free to use, modify, and distribute it as you wish.
