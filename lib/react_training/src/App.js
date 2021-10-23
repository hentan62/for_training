import React, { useState } from "react";
import ClassCounter from "./components/ClassCounter";
import Counter from "./components/Counter";

function App() {
  const [likes, setLikes] = useState(5);
  const [value, setValue] = useState("Какой-то текст");

  return (
    <div className="App">
      <Counter />
      <ClassCounter />
    </div>
  );
}

export default App;
