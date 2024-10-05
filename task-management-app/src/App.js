import Container from 'react-bootstrap/Container';
import AddTaskBar from './components/AddTaskBar';
import Header from './components/Header';
import TaskColumn from './components/TaskColumn';
import './index.css';

function App() {
  return (
    <Container fluid className="App">
      <Header />
      <AddTaskBar />
      <TaskColumn />
    </Container>
  );
}

export default App;
