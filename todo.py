import streamlit as st

# To-Do App Class
class TodoApp:
    def __init__(self):
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []

    def add_task(self, task):
        st.session_state.tasks.append(task)
        st.success(f'Task "{task}" added.')

    def view_tasks(self):
        if not st.session_state.tasks:
            st.write("No tasks available.")
        else:
            st.write("Tasks:")
            for idx, task in enumerate(st.session_state.tasks, start=1):
                st.write(f"{idx}. {task}")

    def delete_task(self, task_number):
        if 0 < task_number <= len(st.session_state.tasks):
            removed_task = st.session_state.tasks.pop(task_number - 1)
            st.success(f'Task "{removed_task}" deleted.')
        else:
            st.warning("Invalid task number.")

# Streamlit layout
st.title("To-Do App")

todo_app = TodoApp()

# Add Task
task_input = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if task_input:
        todo_app.add_task(task_input)
    else:
        st.warning("Please enter a task.")

# View Tasks
st.subheader("Current Tasks")
todo_app.view_tasks()

# Delete Task
task_to_delete = st.number_input("Enter the task number to delete:", min_value=1, step=1)
if st.button("Delete Task"):
    todo_app.delete_task(task_to_delete)
