#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -e .

# Convert static asset files
python src/manage.py collectstatic --no-input

# Apply any outstanding database migrations
python src/manage.py migrate