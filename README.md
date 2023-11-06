Step 1: Install Python

Go to the official Python website: https://www.python.org/downloads/windows/
Download the latest version of Python for Windows (typically Python 3.x).
Run the downloaded installation file (usually with a .msi extension).
Make sure to check the "Add Python X.X to PATH" option during the installation. This allows you to run Python from the command line.
Follow the on-screen instructions to complete the installation.

Step 2: Install Libraries

Open the Command Prompt on your computer. You can do this by pressing Win + R, typing "cmd," and hitting Enter.

Install the required libraries using the pip command. In your case, run the following command to install the aiogram and sqlite3 libraries:

pip install aiogram sqlite3

Step 3: Install project from github

Step 4: Create a Database
Open the Command Prompt on your computer. You can do this by pressing Win + R, typing "cmd," and hitting Enter.

go to database folder and enter:python create_db.py

Step 5: Edit Your Bot's Code

Open your bot's create_bot.py file using a text editor

Find the line that contains TOKEN = "", and replace the empty quotes with your token obtained from BotFather:

TOKEN = ""

add admin(the user id) in root_admins = []

example:
TOKEN = "ASDASJDSAD1273HSAS:ASDJB12HAVSD"

root_admins = [
    1245678,
]

Step 6: Run Your Bot
Go to the folder where the main.py file is located
Open the Command Prompt and navigate to the directory where your code file is located.

Run your bot by executing the following command:
python main.py


