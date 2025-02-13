import shutil
import os
from setuptools import setup

# Copy README from parent directory if it doesn't exist in current directory
if not os.path.exists('README.md') and os.path.exists('../README.md'):
    shutil.copy('../README.md', 'README.md')

setup() 