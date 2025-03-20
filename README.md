# To-Do List App with Color Coding
Overview
This Python script implements a basic to-do list app, where you can add, delete, list, and edit tasks. The app is enhanced with cross-platform color coding for user-friendly, visually appealing output. It uses the sty library to apply colors and styles to the printed text.

Features
Add a Task: Allows the user to input a new task.
List Tasks: Displays all current tasks.
Delete a Task: Allows the user to remove a task by specifying its number.
Edit a Task: Allows the user to modify an existing task.
Color Coding: The app uses different colors to highlight different sections, making it visually engaging and easier to navigate.
Colors Used
The app uses the following colors for different parts of the user interface:

Blue for prompts (e.g., entering a task or choosing a menu option).
Green for successful actions (e.g., adding or editing a task).
Red for errors or invalid actions.
Yellow for the delete task option.
Bold for important messages like task lists and option prompts.
Requirements
To run this script and utilize the color coding feature, you need to install the sty library.

Installation Steps
Install the sty library via pip:

bash
Copy code
pip install sty
Once the library is installed, you can run the script using Python 3.

To execute the script:

bash
Copy code
python todo_app.py
How to Use
Add a Task: When prompted, type in a task description and press Enter.
List Tasks: View all tasks currently on the list.
Delete a Task: Choose a task number to remove it from the list.
Edit a Task: Choose a task number and provide a new description to update it.
Quit: Exit the app.
Example Output
When you run the script, you might see output like this:

markdown
Copy code
Welcome to the to-do list app:

Please select one of the following options:
-------------------------------------------
1. Add a new task
2. Delete a task
3. List tasks
4. Edit task
5. Quit

Enter your choice: 1
Please enter a task: Finish the report
Task 'Finish the report' added to the list.

Please select one of the following options:
-------------------------------------------
1. Add a new task
2. Delete a task
3. List tasks
4. Edit task
5. Quit

Enter your choice: 3
Current Tasks:
Task # 1. Finish the report
Contributing


License
This project is licensed under the MIT License - see the LICENSE file for details.

