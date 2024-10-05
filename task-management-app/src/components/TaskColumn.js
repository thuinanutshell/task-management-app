import React, { useState } from 'react';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import AddTaskBar from './AddTaskBar';

export default function TaskColumn() {
    const [tasks, setTasks] = useState([]);
    const handleAddTask = (task) => {
        setTasks([...tasks, task]);
    };
    return (
        <>
            <Container fluid className="TaskColumn">
                <AddTaskBar onAddTask={handleAddTask} />
                <Row className="grid gap-3">
                    <Col className="Col to-do">
                        <h3>To Do</h3>
                        {tasks.map((task, index) => (
                            <div className='task-card' key={index}>{task}</div>
                        ))}
                    </Col>
                    <Col className="Col in-progress">
                        <h3>In Progress</h3>
                    </Col>
                    <Col className="Col done">
                        <h3>Done</h3>
                    </Col>
                    <Col className="Col pending">
                        <h3>Pending</h3>
                    </Col>
                </Row>
            </Container>
        </>
    );
}