#!/usr/bin/python
import os
import sys

VERSION_FILE = "version.txt"

# Check if version file exists; if not, create it with default version
if not os.path.isfile(VERSION_FILE):
    with open(VERSION_FILE, 'w') as f:
        f.write("1.0.0\n")

# Read the current version
with open(VERSION_FILE, 'r') as f:
    CURRENT_VERSION = f.read().strip()

# Split the version into major, minor, and patch
major, minor, patch = map(int, CURRENT_VERSION.split('.'))

# Increment the version based on the level specified as the first argument
LEVEL = sys.argv[1] if len(sys.argv) > 1 else 'patch'

if LEVEL == 'major':
    major += 1
    minor = 0
    patch = 0
elif LEVEL == 'minor':
    minor += 1
    patch = 0
elif LEVEL == 'patch':
    patch += 1
else:
    print(f"Invalid increment level: {LEVEL}")
    sys.exit(1)

# Construct the new version
NEW_VERSION = f"{major}.{minor}.{patch}"

# Write the new version back to the version file
with open(VERSION_FILE, 'w') as f:
    f.write(NEW_VERSION + '\n')

# Output the new version
print(f"New Version: {NEW_VERSION}")

