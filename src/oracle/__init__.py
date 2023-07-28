import os
from pathlib import Path

# file path
file_path = Path(os.path.realpath(__file__))

# kingh0730 path
kingh0730 = file_path.parent.parent / "kingh0730"

# Markdown files
INDEX_PATH = kingh0730 / "index.md"
EXPERIENCE_PATH = kingh0730 / "experience.md"
COURSEWORK_PATH = kingh0730 / "coursework.md"


def main():
    """Secret message from the oracle"""

    # Read markdown files
    with open(INDEX_PATH, "r", encoding="utf-8") as f:
        index = f.read()
    with open(EXPERIENCE_PATH, "r", encoding="utf-8") as f:
        experience = f.read()
    with open(COURSEWORK_PATH, "r", encoding="utf-8") as f:
        coursework = f.read()

    # Print the message
    message = {
        "index": index,
        "experience": experience,
        "coursework": coursework,
    }

    print(message)
