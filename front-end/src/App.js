import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Checkbox from 'react-bootstrap/Checkbox';
import Container from 'react-bootstrap/Container';
import Input from 'react-bootstrap/Input';
import './index.css';

function AddNewTaskButton() { // <-- this is the state
  // The one that goes into the parenthesis is the props
  // When this button is clicked, it should add a new task card to the list
  // The UI of task card is defined in the function below
  return (
    <Button variant='primary'>+ Add New Task</Button>
  );
}

function AddSubtaskButton() { // <-- this is the state
  return (
    <Button variant='primary'>+</Button>
  );
}

function DeleteTaskButton() { // <-- this is the state
  return (
    <Button variant='danger'>x</Button>
  );
}

function TaskNameInput({ onTaskNameChange }) { // <-- this is the state
  // When user write a task name and press Enter, the task name is updated to the new value
  return (
    <Input 
      type="text"
      placeholder='Enter Task Name'
      onChange={(e) => onTaskNameChange(e.target.value)} // <-- event handler
    />
  );
}

function TaskCard() { // <-- this isn't a state, it needs to use the state
  // This is a task card that contains a checkbox, a task name input, and two buttons
  // The checkbox is used to mark the task as completed
  // The task name input is used to edit the task name
  // The first button is used to add a new task card
  // The second button is used to delete the current task card
  const [taskName, setTaskName] = useState('');
  return (
    <Container>
      <Checkbox></Checkbox>
      <TaskNameInput />
      <AddSubtaskButton /> {/* When this button is clicked on the task card, a new task will be nested under the card */}
      <DeleteTaskButton />
    </Container>
  )
}

function TaskNode() { // recursive component <-- this isn't a state
  return (
    <TaskCard />
  );
}
 
function TaskList() { // <-- this isn't a state
  // This is a list of task cards, which will be updated dynamically
  const [tasks, setTasks] = useState([]);
  return (
    <Container>
      <TaskNode/>
    </Container>
  );
}

function ListHeaderInput({ onListHeaderInputChange }) { // <-- this is the state
  // When user write a list name and press Enter, the list name is updated to the new value
  return (
    <Input
      type="text"
      placeholder='Enter List Name'
      onChange={(e) => onListHeaderInputChange(e.target.value)} // <-- event handler
    />
  );
}

function ListHeader() { // <-- this isn't a state
  // This is a list header that contains a list name input and a delete button
  const [listName, setListName] = useState('');
  return (
    <Container>
      <ListHeaderInput />
      <Button>Delete</Button>
    </Container>
  );
}

function TaskColumn() { // <-- this isn't a state
  const [taskLists, setTaskLists] = useState([]);
  return (
    <Container>
      <ListHeader />
      <TaskList />
      <AddNewTaskButton />
    </Container>
  );
}

function BoardView() { // <-- this isn't a state
  const [taskColumns, setTaskColumns] = useState([]);
  return (
    <Container>
      <TaskColumn />
    </Container>
  );
}

function CreateListButton() { // <-- this is the state
  return (
    <Button variant='primary'>+ Create List</Button>
  );
}

function Header() { // <-- this is a state
  return (
    <Container>
      <h1>Task Manager</h1>
      <CreateListButton />
    </Container>
  );
}

const TASKS = [
  {"task name": "task 1"},
  {"task name": "task 2"},
  {"task name": "task 3"},
  {"task name": "task 4"},
  {"task name": "task 5"},
];

function App() { // This isn't a state
  return (
    <>
      <Header />
      <BoardView tasks={TASKS}/>
    </>
  );
}

export default App;
