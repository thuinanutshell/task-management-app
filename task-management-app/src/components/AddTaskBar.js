import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

export default function AddTaskField() {
    return (
        <>
            <Container fluid className="AddTaskBar">
                <Row>
                    <Col xs={12} md={10}>
                        <input type="text" className="AddTaskField" />
                    </Col>
                    <Col xs={12} md={2}>
                        <button type="button" className="AddTaskButton btn btn-primary btn-lg">+ Add Task</button>
                    </Col>
                </Row>
            </Container>
        </>
    );
}