

# Adding and veiwing tasks
# Need a way of adding tasks
# Need a way to get a list of incomplete tasks

# Marking tasks as complete 
# Need a way to mark a task as done
# Completed tasks should not show up in the list of active tasks

class toDo:
     
# As a user So that I can keep track of my tasks I want a program that I can add todo tasks to and see a list of them.
     def __init__(self):
        #   self.tasks = [] # Initialize a list to keep track of tasks
        self.tasks = [] # Now storing tasks as dicts with 'description' and 'completed' keys

     def add_task(self, task):
         self.tasks.append({"Description": task, "Completed": False}) # Add a task as a dict with completed False initially --> Key: "Description" / Value: Task | Key: "Completed" / Value: False

     
     def get_tasks(self):
        #   return self.tasks # Return the current list of tasks
        return [task["Description"] for task in self.tasks if not task["Completed"]] # Return a list of descriptions for all tasks that are not completed


     
     def mark_complete(self, task):
        for task_item in self.tasks:
            if task_item["Description"] == task:
                task_item["Completed"] = True
                break