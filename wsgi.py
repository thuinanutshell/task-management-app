import os
import sys

# Add the project root directory to Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(project_dir, 'backend')
sys.path.insert(0, backend_dir)

from app import app

if __name__ == "__main__":
    app.run()
