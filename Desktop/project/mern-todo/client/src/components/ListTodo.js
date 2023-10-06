import React from 'react';


const ListTodo = ({ todos, deleteTodo }) => {
    console.log('todos:', todos);
  
    // Ensure that todos is always an array, even if it's undefined or null
    const todoList = todos || [];
    console.log('todos:', todos);
    console.log('todoList:', todoList);
  
    return (
      <ul>
        {todoList.length > 0 ? (
          todoList.map((todo) => {
            return (
              <li key={todo._id} onClick={() => deleteTodo(todo._id)}>
                {todo.action}
              </li>
            );
          })
        ) : (
          <li>No todo(s) left</li>
        )}
      </ul>
    );
  };
  
  export default ListTodo;