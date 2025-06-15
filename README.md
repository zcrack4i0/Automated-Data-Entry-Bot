📝 Automated Data Entry Bot for Notepad using PyAutoGUI
This Python project automates data entry into the Notepad desktop application by fetching blog posts from the JSONPlaceholder API and saving them as .txt files.

🔧 Features
✅ Automatically launches Notepad

✅ Fetches the first 10 posts from the JSONPlaceholder API

✅ Types (or pastes) each post into Notepad with:

Title as a heading

Body as the content

✅ Saves each post as post 1.txt, post 2.txt, ... in a fresh tjm-project folder on your Desktop

✅ Recreates the target folder every time (deletes old content)

✅ Handles timing and clipboard to prevent mistyped text

💻 Technologies Used
Python

requests for fetching post data

pyautogui for simulating keyboard and UI automation

pyperclip for reliable text pasting

subprocess for launching Notepad

📁 Folder Output Example
markdown
Copy
Edit
Desktop/
└── tjm-project/
├── post 1.txt
├── post 2.txt
├── ...
└── post 10.txt
