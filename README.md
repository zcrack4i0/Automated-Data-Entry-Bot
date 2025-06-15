# 📝 Automated Data Entry Bot for Notepad

This Python project automates data entry into the Notepad desktop application by fetching blog posts from the JSONPlaceholder API and saving them as .txt files.

## 🔧 Features

✅ Automatically launches Notepad

✅ Fetches the first 10 posts from the JSONPlaceholder API
https://jsonplaceholder.typicode.com/posts

✅ Types (or pastes) each post into Notepad with:

Title as a heading

Body as the content

✅ Saves each post as post 1.txt, post 2.txt, ... in a fresh tjm-project folder on your Desktop

✅ Recreates the target folder every time (deletes old content)

✅ Handles timing and clipboard to prevent mistyped text

## 💻 Technologies Used

Python

requests for fetching post data

pyautogui for simulating keyboard and UI automation

subprocess for launching Notepad

## 🚀 How to Run

1- Clone the repo

2- Create a virtual environment

python -m venv venv
source venv/bin/activate

3- Install dependencies:

pip install pyautogui botcity-core requests

4- Run the script:

python automate_notepad.py

### Note: If your Desktop is synced via OneDrive just uncomment this part ⬇️

desktop = os.path.join(desktop, "OneDrive")
