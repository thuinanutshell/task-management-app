import os
import sys
from pathlib import Path

# Add the project root to Python path
current_dir = Path(__file__).resolve().parent
sys.path.append(str(current_dir))

from backend.app import app

if __name__ == "__main__":
    app.run()
