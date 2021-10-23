import React, { useState } from "react";
import ClassCounter from "./components/ClassCounter";
import Counter from "./components/Counter";

function App() {
  const [likes, setLikes] = useState(5);
  const [value, setValue] = useState("Какой-то текст");

  return (
    <div className="App">
      <div className="post">
        <div className="post__content">
          <strong>1. Javascript</strong>
          <div>Javascript - язык программирования</div>
        </div>
      </div>
      <div className="post__btns">
        <button>Удалить</button>
      </div>

      <p>Счетчики</p>
      <Counter />
      <ClassCounter />
    </div>
  );
}

export default App;
