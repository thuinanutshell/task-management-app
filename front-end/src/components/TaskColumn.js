import React, { useState } from 'react';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import AddTaskBar from './AddTaskBar';

export default function TaskColumn() {
    const [toDoTasks, setToDoTasks] = useState([]);
    const [inProgressTasks, setInProgressTasks] = useState([]);
    const [doneTasks, setDoneTasks] = useState([]);
    const [pendingTasks, setPendingTasks] = useState([]);

    const handleAddTask = (task) => {
        setToDoTasks([...toDoTasks, task]);
    };

    const onDragStart = (event, task, column) => {
        event.dataTransfer.setData('task', task);
        event.dataTransfer.setData('column', column);
    };

    const onDrop = (event, setTasks, tasks) => {
        const task = event.dataTransfer.getData('task');
        const column = event.dataTransfer.getData('column');

        if (column === 'to-do') {
            setToDoTasks(toDoTasks.filter(t => t !== task));
        } else if (column === 'in-progress') {
            setInProgressTasks(inProgressTasks.filter(t => t !== task));
        } else if (column === 'done') {
            setDoneTasks(doneTasks.filter(t => t !== task));
        } else if (column === 'pending') {
            setPendingTasks(pendingTasks.filter(t => t !== task));
        }

        setTasks([...tasks, task]);
    };

    const allowDrop = (event) => {
        event.preventDefault();
    };

    return (
        <>
            <Container fluid className="TaskColumn">
                <AddTaskBar onAddTask={handleAddTask} />
                <Row className="grid gap-3">
                    <Col className="Col to-do" onDragOver={allowDrop} onDrop={(event) => onDrop(event, setToDoTasks, toDoTasks)}>
                        <h3>To Do</h3>
                        {toDoTasks.map((task, index) => (
                            <div className='task-card' key={index} draggable="true" onDragStart={(event) => onDragStart(event, task, 'to-do')}>
                                <input type="checkbox" /> {task}
                            </div>
                        ))}
                    </Col>
                    <Col className="Col in-progress" onDragOver={allowDrop} onDrop={(event) => onDrop(event, setInProgressTasks, inProgressTasks)}>
                        <h3>In Progress</h3>
                        {inProgressTasks.map((task, index) => (
                            <div className='task-card' key={index} draggable="true" onDragStart={(event) => onDragStart(event, task, 'in-progress')}>{task}</div>
                        ))}
                    </Col>
                    <Col className="Col done" onDragOver={allowDrop} onDrop={(event) => onDrop(event, setDoneTasks, doneTasks)}>
                        <h3>Done</h3>
                        {doneTasks.map((task, index) => (
                            <div className='task-card' key={index} draggable="true" onDragStart={(event) => onDragStart(event, task, 'done')}>{task}</div>
                        ))}
                    </Col>
                    <Col className="Col pending" onDragOver={allowDrop} onDrop={(event) => onDrop(event, setPendingTasks, pendingTasks)}>
                        <h3>Pending</h3>
                        {pendingTasks.map((task, index) => (
                            <div className='task-card' key={index} draggable="true" onDragStart={(event) => onDragStart(event, task, 'pending')}>{task}</div>
                        ))}
                    </Col>
                </Row>
            </Container>
        </>
    );
}