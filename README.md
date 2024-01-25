# Kivy ToDo App

## Description

This is a simple ToDo application built using the Kivy framework. The app allows users to create, mark as complete or incomplete, and delete tasks. It utilizes the KivyMD library for Material Design components.

## Dependencies
KivyMD - Material Design components for Kivy
datetime - Basic date and time types

## Usage
Run the MainApp class to start the ToDo application.
The main screen displays a list of tasks. Completed tasks are marked with strikethrough text.
Click the "Create Task" button to open a dialog for adding new tasks.
In the task creation dialog, enter the task details and choose a due date using the date picker.
Click the "Save" button to add the task to the list.
Tasks can be marked as complete or incomplete by checking/unchecking the checkbox next to each task.
To delete a task, click the delete button next to the task.

## Features
Create new tasks with due dates.
Mark tasks as complete or incomplete.
Delete tasks.

## Database
The app uses a simple database module (database.py) for storing task information. Ensure that the database module is created before running the app.

`python
from d import d
`
