import pyautogui
import time
import os
import subprocess
import requests
from botcity.core import DesktopBot
import shutil

# Create project directory
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
project_dir = os.path.join(desktop, "tjm-project")
# Delete the folder if it already exists
if os.path.exists(project_dir):
    shutil.rmtree(project_dir)
os.makedirs(project_dir, exist_ok=True)


# Initialize BotCity bot for screenshots or fallback
bot = DesktopBot()


def launch_notepad():
    try:
        subprocess.Popen(['notepad.exe'])
        time.sleep(1.5)  # Wait for Notepad to open
    except Exception as e:
        print("Error launching Notepad:", e)
        raise

def save_file(filename):
    try:
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.write(filename)
        pyautogui.press('enter')
        time.sleep(1)
    except Exception as e:
        print("Saving error:", e)
        raise

def close_notepad():
    pyautogui.hotkey('ctrl', 'w')  # Close Notepad tab
    time.sleep(0.5)

def get_post(post_id):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Failed to get post {post_id}")
            return None
    except Exception as e:
        print("API Error:", e)
        return None

def type_text(text):
    try:
        pyautogui.write(text, interval=0.11)
    except Exception as e:
        print("Typing error:", e)
        raise

# Main loop for first 10 posts
for i in range(1, 11):
    print(f"Processing post {i}")
    post = get_post(i)
    if post:
        try:
            # Launch Notepad
            launch_notepad()

            # Type the post title and body
            title = post['title']
            body = post['body']            
            type_text(f"{title}\n")
            pyautogui.press('enter')
            pyautogui.press('enter')  # Add an extra line break
            type_text(f"{body}\n")
            
            # Save the file
            filename = os.path.join(project_dir, f"post {i}.txt")
            save_file(filename)
            print(f"Post {i} saved successfully as {filename}")

            # Close Notepad
            close_notepad()

        except Exception as e:
            print(f"Error with post {i}: {e}")
            # Take a screenshot on error
            bot.screenshot(f"error_post_{i}.png")
    else:
        print(f"Skipping post {i} due to retrieval failure.")
