

# Adding and veiwing tasks
# Need a way of adding tasks
# Need a way to get a list of incomplete tasks

# Marking tasks as complete 
# Need a way to mark a task as done
# Completed tasks should not show up in the list of active tasks

class toDo:
     
# As a user So that I can keep track of my tasks I want a program that I can add todo tasks to and see a list of them.
     def __init__(self):
          self.tasks = [] # Initialize a list to keep track of tasks

     def add_task(self, task):
         self.tasks.append(task) # Add the given task to the list
     
     def get_tasks(self):
          return self.tasks # Return the current list of tasks
      
# As a user So that I can focus on tasks to complete I want to mark tasks as complete and have them disappear from the list.
# 1. Change the task representation from a string to a dict or a small object with:
#    - task description
#    - completed status (True/False)

# 2. Modify add_task to store this richer task object

# 3. Create a method, e.g., mark_complete(task_description)
#    - It should find the task and mark it completed

# 4. Update get_tasks to return only tasks that are NOT completed
