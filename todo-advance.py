import streamlit as st

# To-Do App Class
class TodoApp:
    def __init__(self):
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []

    def add_task(self, task):
        st.session_state.tasks.append({"task": task, "completed": False})
        st.success(f'Task "{task}" added.')

    def view_tasks(self, filter_status):
        if not st.session_state.tasks:
            st.write("No tasks available.")
        else:
            filtered_tasks = [task for task in st.session_state.tasks if 
                              (filter_status == "All" or 
                               (filter_status == "Completed" and task["completed"]) or 
                               (filter_status == "Pending" and not task["completed"]))]
            if not filtered_tasks:
                st.write("No matching tasks.")
            else:
                for idx, task in enumerate(filtered_tasks, start=1):
                    status = "✅" if task["completed"] else "❌"
                    st.write(f"{idx}. {task['task']} {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(st.session_state.tasks):
            st.session_state.tasks[task_number - 1]["completed"] = True
            st.success(f'Task "{st.session_state.tasks[task_number - 1]["task"]}" marked as completed.')

    def delete_task(self, task_number):
        if 0 < task_number <= len(st.session_state.tasks):
            removed_task = st.session_state.tasks.pop(task_number - 1)
            st.success(f'Task "{removed_task["task"]}" deleted.')
        else:
            st.warning("Invalid task number.")

# Streamlit layout
st.title("Advanced To-Do App")

todo_app = TodoApp()

# Add Task
task_input = st.text_input("Enter a new task:")
if st.button("Add Task"):
    if task_input:
        todo_app.add_task(task_input)
    else:
        st.warning("Please enter a task.")

# Filter Tasks
filter_option = st.selectbox("Filter tasks:", ["All", "Completed", "Pending"])

# View Tasks
st.subheader("Current Tasks")
todo_app.view_tasks(filter_option)

# Mark Task as Complete
task_to_complete = st.number_input("Enter the task number to mark as completed:", min_value=1, step=1)
if st.button("Complete Task"):
    todo_app.complete_task(task_to_complete)

# Delete Task
task_to_delete = st.number_input("Enter the task number to delete:", min_value=1, step=1)
if st.button("Delete Task"):
    todo_app.delete_task(task_to_delete)
