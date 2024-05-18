# Automatic Exam Answers Generator

This project is a simple Python program for getting answers to questions for exams. I created this to get answers to the important questions list form teachers as the exam style is based on memorization. This program will take a file containing a list of questions, with any aditional information and get answers throught the Gemini API and then output them to a file (.txt).

## Files

* `API testing.ipynb` - Test if your API is working as it should and check for any error so that environment is also set up correctly.
* `main.py` - Program that gives the answers to questions in text files and write to another text file.
* `schedule.json` - JSON file storing the anime schedule data.

## Features

* **Add Anime** - Allows users to add new anime entries to the schedule.
* **Edit Schedule** - Enables users to edit existing anime entries in the schedule.
* **Delete Anime** - Allows users to delete anime entries from the schedule.
* **Clear Schedule** - Allows users to remove all anime entries from the schedule.
* **Notifications** - Sends notifications for upcoming anime airing times.

## Usage

1. Run `jsonCode.py` to manage the anime schedule.
2. The program will prompt you to choose from the following options:
   * Add Anime
   * Edit Schedule
   * Delete Anime
   * Clear Schedule
3. Follow the prompts to perform the desired action.
