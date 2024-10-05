import React, { useState } from 'react';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

export default function AddTaskBar({ onAddTask }) {
    const [task, setTask] = useState('');
    const handleInputChange = (e) => {
        setTask(e.target.value);
    };
    const handleAddTask = () => {
        if (task.trim()) {
            onAddTask(task);
            setTask('');
        }
    };

    return (
        <>
            <Container fluid className="AddTaskBar">
                <Row>
                    <Col xs={12} md={10}>
                        <input 
                            type="text" 
                            className="AddTaskField" 
                            value={task}
                            onChange={handleInputChange}
                            />
                    </Col>
                    <Col xs={12} md={2}>
                        <button 
                            type="submit" 
                            className="AddTaskButton btn btn-primary btn-lg"
                            onClick={handleAddTask}>+ Add Task</button>
                    </Col>
                </Row>
            </Container>
        </>
    );
}