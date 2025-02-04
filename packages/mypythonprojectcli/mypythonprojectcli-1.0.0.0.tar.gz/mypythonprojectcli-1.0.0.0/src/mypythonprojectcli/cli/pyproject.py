#!/usr/bin/env python3

import os

# pyproject.toml preparation

# Locate the root directory (one level above 'src')
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Locate the package directory
package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Path to pyproject.toml
toml_path = os.path.join(root_dir, "pyproject.toml")

# Get the project name (folder where 'src' is located)
project_name = os.path.basename(package_dir)

# Read the TOML file
with open(toml_path, "r", encoding="utf-8") as f:
    toml_data = f.read()

# Replace occurrences of 'PROJECT_NAME'
toml_data = toml_data.replace("PROJECT_NAME", project_name)

# Save the updated file
with open(toml_path, "w", encoding="utf-8") as f:
    f.write(toml_data)

print(f"Updated pyproject.toml with project name: {project_name}")
