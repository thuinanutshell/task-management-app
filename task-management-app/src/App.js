import Container from 'react-bootstrap/Container';
import Header from './components/Header';
import TaskColumn from './components/TaskColumn';
import './index.css';

function App() {
  return (
    <Container fluid className="App">
      <Header />
      <TaskColumn />
    </Container>
  );
}

export default App;
