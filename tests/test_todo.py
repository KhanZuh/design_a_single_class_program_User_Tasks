from lib.todo import *

def test_add_and_list_tasks():
    todo = toDo() # Create instance
    todo.add_task("Fix brakes") # Add a task
    tasks = todo.get_tasks() # Retrive task list
    assert tasks == ["Fix brakes"]

def test_mark_task_complete():
    todo = toDo()
    todo.add_task("Fix brakes")
    todo.add_task("Change oil")

    todo.mark_complete("Fix brakes") # Make one task complete
    tasks = todo.get_tasks() # Get remaining tasks
    assert tasks == ["Change oil"] # We expect only "Change oil" to remain
