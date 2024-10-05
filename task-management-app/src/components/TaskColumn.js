import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';

export default function TaskColumn() {
    return (
        <>
            <Container fluid className="TaskColumn">
                <Row className="grid gap-3">
                    <Col className="Col to-do">To Do</Col>
                    <Col className="Col in-progress">In Progress</Col>
                    <Col className="Col done">Done</Col>
                    <Col className="Col pending">Pending</Col>
                </Row>
            </Container>
        </>
    );
}