import { useState } from "react";
import styled from "styled-components";

const Container = styled.div`
  padding: 10px;
  background-color: lightgray;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Buttons = styled.button`
  margin-top: 20px;
`;

const Count = styled.div`
  width: 100px;
  height: 50px;
  line-height: 50px;
  font-size: 2rem;
  border: 1px solid black;
  border-radius: 8px;
  text-align: center;
`;

const Button = styled.button`
  color: white;
  width: 80px;
  height: 50px;
  text-align: center;
  border-radius: 10px;

  background-color: ${(props) => (props.inc ? "blue" : "red")};

  + button {
    margin-left: 10px;
  }

  &:hover {
    box-shadow: 10px 5px 5px gray;
  }
`;

// styled component를 이용해 카운터를 만들어보세요.

export default function App() {
  const [count, setCount] = useState(0);

  return (
    <Container>
      <Count>{count}</Count>
      <Buttons>
        <Button onClick={() => setCount(count + 1)} inc>
          증가
        </Button>
        <Button onClick={() => setCount(count - 1)}>감소</Button>
      </Buttons>
    </Container>
  );
}
