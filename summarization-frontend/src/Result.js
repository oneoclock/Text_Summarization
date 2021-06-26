import { Container } from 'semantic-ui-react';

function Result(props)
{
  return (
    <Container style={{ marginTop: 40 }}>
    <p><b>Summary:</b></p>
      {props.summary}

    </Container>
  );
}

export default Result;
