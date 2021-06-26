import { useEffect } from 'react';
import InputText from './InputText';
import { Container } from 'semantic-ui-react';

function App() {
//const [state1, setState1] = useState([]);

  useEffect(() => {
    fetch("/home").then((response) =>
      response.json()).then((data) => {
        console.log(data);
      });

  }, []);

  return (
    <div className="App">
          <Container style={{ marginTop: 40 }}>
            <InputText />

          </Container>

    </div>
  );
}

export default App;
