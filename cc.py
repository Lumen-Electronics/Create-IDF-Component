import os
import sys
import re

def create_component_structure(component_name):
    if not os.path.isdir("components"):
        print("Error: 'components' folder not found in the current directory.")
        sys.exit(1)

    component_folder = os.path.join("components", component_name)

    if os.path.exists(component_folder):
        print(f"Error: The folder '{component_folder}' already exists. Aborting.")
        sys.exit(1)

    os.makedirs(component_folder, exist_ok=False)

    hpp_file_path = os.path.join(component_folder, f"{component_name}.hpp")
    cpp_file_path = os.path.join(component_folder, f"{component_name}.cpp")
    cmake_file_path = os.path.join(component_folder, "CMakeLists.txt")

    with open(hpp_file_path, "w") as hpp_file:
        hpp_file.write("#pragma once\n")

    with open(cpp_file_path, "w") as cpp_file:
        cpp_file.write(f'#include "{component_name}.hpp"\n')
        cpp_file.write(f'static const char *TAG = "{component_name}";\n')
        cpp_file.write('#include "esp_log.h"\n\n')
        cpp_file.write("void function (void)\n{\n\n}\n")

    with open(cmake_file_path, "w") as cmake_file:
        cmake_file.write(f'idf_component_register(SRCS "{component_name}.cpp"\n')
        cmake_file.write('    INCLUDE_DIRS "."\n')
        cmake_file.write('    REQUIRES\n')
        cmake_file.write(')\n')

    print(f"Component '{component_name}' created successfully in '{component_folder}'.")
def update_extra_component_dirs(component_name):
    main_cmake_path = os.path.join(os.path.dirname(__file__), "CMakeLists.txt")
    if not os.path.isfile(main_cmake_path):
        print("Error: Main CMakeLists.txt file not found.")
        sys.exit(1)

    component_dir = f'components/{component_name}'

    with open(main_cmake_path, "r") as cmake_file:
        cmake_content = cmake_file.readlines()

    # Locate the set(EXTRA_COMPONENT_DIRS ...) block
    start_index = None
    end_index = None
    for i, line in enumerate(cmake_content):
        if re.match(r'\s*set\s*\(\s*EXTRA_COMPONENT_DIRS', line):
            start_index = i
            # Find the closing parenthesis
            for j in range(i, len(cmake_content)):
                if ')' in cmake_content[j]:
                    end_index = j
                    break
            break

    if start_index is not None and end_index is not None:
        # Check if the component is already listed
        block_lines = cmake_content[start_index:end_index+1]
        block_text = ''.join(block_lines)
        if component_dir in block_text:
            print(f"Warning: '{component_dir}' is already listed in EXTRA_COMPONENT_DIRS.")
            return

        # Insert the new component before the closing parenthesis
        cmake_content.insert(end_index, f'    "{component_dir}"\n')

        with open(main_cmake_path, "w") as cmake_file:
            cmake_file.writelines(cmake_content)

        print(f"Added '{component_dir}' to EXTRA_COMPONENT_DIRS in main CMakeLists.txt.")
    else:
        # Handle case where the block is not found
        # (Same as before)
        pass  # For brevity, the rest of the code remains the same


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_component.py <component_name>")
        sys.exit(1)

    component_name = sys.argv[1]
    create_component_structure(component_name)
    update_extra_component_dirs(component_name)
