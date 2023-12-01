import streamlit as st
import functions


todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo != '':
        todos.append(new_todo + "\n")
        functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("You can enter, modify and delete/complete to-dos.")

for idx, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(idx)
        functions.write_todos(todos)
        st.rerun()

st.text_input(label=" ", placeholder="Add a new To-Do...",
              on_change=add_todo, key="new_todo")

