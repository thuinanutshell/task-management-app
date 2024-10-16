import React, { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Container from 'react-bootstrap/Container';
import './index.css';

function AddSubtaskButton({ onAddSubTask }) {
  const [isAdding, setIsAdding] = useState(false);
  const [subtaskName, setSubtaskName] = useState('');

  const handleAddSubtask = () => {
    if (subtaskName.trim()) {
      onAddSubTask(subtaskName);
      setIsAdding(false);
      setSubtaskName('');
    }
  };

  return (
    <div>
      {isAdding ? (
        <div>
          <input 
            type="text"
            value={subtaskName}
            onChange={(e) => setSubtaskName(e.target.value)}
            placeholder="Enter Subtask Name"
          />
          <Button onClick={handleAddSubtask}>Add</Button>
        </div>
      ) : (
        <Button onClick={() => setIsAdding(true)}>+ Add Subtask</Button>
      )}
    </div>
  );
};

function DeleteTaskButton({ onRemoveTask }) { // <-- this is the state
  // When this button is clicked, it should delete the task
  return (
    <Button 
      variant='danger'
      onClick={onRemoveTask}
    >x</Button>
  );
}

function TaskNameInput({ task }) { // <-- this is the state
  // When user write a task name and press Enter, the task name is updated to the new value
  return (
    <input
      type="text"
      value={task.name}
      onChange={() => {}}
    />
  );
}

function TaskCard({ task, taskIndex, itemIndex, setTasks }) {
  const deleteTask = () => {
    setTasks((prevTasks) => {
      const newTasks = [...prevTasks];
      newTasks[taskIndex].items.splice(itemIndex, 1);
      return newTasks;
    });
  };

  const addSubTask = (subtaskName) => {
    setTasks((prevTasks) => {
      const newTasks = [...prevTasks];
      newTasks[taskIndex].items[itemIndex].subtasks.push(subtaskName);
      return newTasks;
    });
  };

  return (
    <li className="task-card">
      <TaskNameInput task={task} />
      <AddSubtaskButton onAddSubTask={addSubTask} />
      <DeleteTaskButton onDeleteTask={deleteTask} />
    </li>
  );
};
 
function TaskList({ tasks, taskIndex, setTasks }) {
  return (
    <ul>
      {tasks.map((task, index) => (
        <TaskCard
          key={index}
          task={task}
          taskIndex={taskIndex}
          itemIndex={index}
          setTasks={setTasks}
        />
      ))}
    </ul>
  );
}

function ListHeaderInput({ task }) { // <-- this is the state
  // When user write a list name and press Enter, the list name is updated to the new value
  return (
    <input
      type="text"
      value={task.name}
      onChange={() => {}}
      // <-- event handler
    />
  );
}

function ListHeader({ task }) { // <-- this isn't a state
  return (
    <Container>
      <h2>{task.name}</h2>
      <ListHeaderInput task={task} />
    </Container>
  );
}

function NestedTaskList({ tasks, taskIndex, setTasks }) {
  return (
    <Container className="nested-task-list">
      <TaskList tasks={tasks} taskIndex={taskIndex} setTasks={setTasks} />
    </Container>
  );
}

function AddNewTaskButton({ onAddTask }) {
  const [isAdding, setIsAdding] = useState(false);
  const [taskName, setTaskName] = useState('');

  const handleAddTask = () => {
    if (taskName.trim()) {
      onAddTask(taskName);
      setIsAdding(false);
      setTaskName('');
    }
  };

  return (
    <Container>
      {isAdding ? (
        <div>
          <input 
            type="text"
            value={taskName}
            onChange={(e) => setTaskName(e.target.value)}
            placeholder="Enter Task Name"
          />
          <Button onClick={handleAddTask}>Add</Button>
        </div>
      ) : (
        <Button onClick={() => setIsAdding(true)}>+ Add Task</Button>
      )}
    </Container>
  )
}

function TaskColumn({ task, taskIndex, setTasks }) { // <-- this isn't a state
  const addNewTask = (taskName) => {
    setTasks((prevTasks) => {
      const newTasks = [...prevTasks];
      if (!newTasks[taskIndex].items) {
        newTasks[taskIndex].items = [];
      }
      newTasks[taskIndex].items.push({ name: taskName, subtasks: [] });
      return newTasks;
    });
  };

  if (!task) {
    return null; // or return a placeholder component
  }

  return (
    <div className="task-column">
      <ListHeader task={task} />
      <NestedTaskList tasks={task.items || []} taskIndex={taskIndex} setTasks={setTasks} />
      <AddNewTaskButton onAddTask={addNewTask} />
    </div>
  );
};

function BoardView({ tasks, setTasks }) { // <-- this isn't a state
  return (
    <Container className="board-view">
      {tasks.map((task, index) => (
        task && <TaskColumn key={index} task={task} taskIndex={index} setTasks={setTasks} />
      ))}
    </Container>
  );
};

function CreateListButton({ onCreateList }) { // <-- this is the state
  const [isCreating, setIsCreating] = useState(false);
  const [newListName, setNewListName] = useState('');

  const handleCreateList = () => {
    if (newListName.trim()) {
      onCreateList(newListName);
      setIsCreating(false);
      setNewListName('');
    }
  };

  return (
    <Container>
      {isCreating ? (
        <div>
          <input 
            type="text"
            value={newListName}
            onChange={(e) => setNewListName(e.target.value)}
            placeholder="Enter List Name"
          />
          <Button onClick={handleCreateList}>Create</Button>
        </div>
      ) : (
        <Button onClick={() => setIsCreating(true)}>Create New List</Button>
      )}
    </Container>
  );
};

function Header({ onCreateList }) { // <-- this is a state
  return (
    <Container>
      <h1>Task Manager</h1>
      <CreateListButton onCreateList={onCreateList}/>
    </Container>
  );
}

function App() {
  const [tasks, setTasks] = useState([]);

  const addNewList = (listName) => {
    setTasks([...tasks, { name: listName, items: [] }]);
  };

  return (
    <>
      <Header onCreateList={addNewList} />
      <BoardView tasks={tasks} setTasks={setTasks}/>
    </>
  );
}

export default App;
