import streamlit as st
import functions
todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todo(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
     checkbox = st.checkbox(todo, key=todo)
     if checkbox:
         todos.pop(index)
         print(todos)
         functions.write_todo(todos)
         del st.session_state[todo]
         st.rerun()

st.text_input(label='todo input', label_visibility='hidden', placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')
