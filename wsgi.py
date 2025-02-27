import os
import sys

# Add the project root directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)

from backend.app import app

if __name__ == "__main__":
    app.run()
