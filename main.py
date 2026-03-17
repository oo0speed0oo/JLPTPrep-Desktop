import csv
from datetime import datetime
import os

DATA_FOLDER = "data/test_scores"
SCORE_FILENAME = os.path.join(DATA_FOLDER, "quiz_scores.csv")

current_quiz_file = None


def ensure_file_exists():
    """Create the scores folder and CSV file with headers if they don't exist."""
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)
    if not os.path.exists(SCORE_FILENAME):
        with open(SCORE_FILENAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Quiz Name", "Score", "Total"])


def start_quiz(file):
    """Sets the active quiz file for the session."""
    global current_quiz_file
    current_quiz_file = file
    ensure_file_exists()
    print(f"Starting quiz: {current_quiz_file}")


def end_quiz(score, total):
    """Saves the final score to the CSV file."""
    global current_quiz_file
    ensure_file_exists()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(SCORE_FILENAME, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, current_quiz_file, score, total])
        print(f"Score saved: {score}/{total}")
    except Exception as e:
        print(f"Error saving score: {e}")