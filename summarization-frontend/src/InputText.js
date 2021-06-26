import { Form, Input, Button } from 'semantic-ui-react';
import { useState } from 'react';
import Result from './Result'

function InputText()
{
  const [title, setTitle] = useState("");
  const [display, setDisplay] = useState("");
  const [submitted, setSubmit] = useState(false);

  function displaySummary(summary) {
    setDisplay(summary);
    setSubmit(true);
  }

  return (
    <div>
      <Form>
        <Form.Field>
        <Input
        placeholder="Input Text"
        value={title}
        onChange={e => setTitle(e.target.value)}
        />
        </Form.Field>
        <Form.Field>
          <Button onClick={async () => {
            const text = {"text": title}
            const response = await fetch("/summarize", {
              method: "POST",
              headers: {
                "Content-Type": "application/json"
              },
              body: JSON.stringify(text)
            });

            if (response.ok) {
              //console.log(response.json().then(data=>{data.summary}))
              response.json().then(data=>{displaySummary(data.summary)});
            }
          }}
          >
          Submit
          </Button>
        </Form.Field>
      </Form>
      <div>
        {submitted && <Result summary={display} />}
      </div>
    </div>
  );
}

export default InputText;
