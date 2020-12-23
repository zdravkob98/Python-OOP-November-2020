


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        current_task = [t for t in self.tasks if t.name == task_name]
        if current_task:
            current_task[0].completed = True
            return f"Completed task {current_task[0].name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        current_tasks = [t for t in self.tasks if t.completed]
        for t in current_tasks:
            self.tasks.remove(t)
        return f"Cleared {len(current_tasks)} tasks."

    def view_section(self):
        data = f'Section {self.name}:\n'

        for t in self.tasks:
            data += f'{t.details()}\n'
        return ''.join(data)
