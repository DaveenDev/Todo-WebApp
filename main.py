import streamlit as st
import os
import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt","w") as file:
        pass
todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]  + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

def complete_todo():
    for index, todo in enumerate(todos):
        if st.session_state[index] == "true":
            todos.remove(todo)

st.title("My Todo App")
st.subheader("My first web app using python")


st.write("List of todos:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="New todo",
              placeholder="Input new todo here ",
              on_change=add_todo, key="new_todo",
              label_visibility="visible")

#st.session_state