import os
import sys
from pathlib import Path

# Get the absolute path of the current file
current_dir = Path(__file__).resolve().parent

# Add the backend directory to Python path
backend_dir = current_dir / 'backend'
sys.path.append(str(backend_dir))

# Change the import statement to use the correct path
from backend.app import app

if __name__ == "__main__":
    app.run()
