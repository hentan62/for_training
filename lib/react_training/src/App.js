import React, { useState } from "react";
import ClassCounter from "./components/ClassCounter";
import Counter from "./components/Counter";
import PostItem from "./components/PostItem";
import PostList from "./components/PostList";
import "./styles/App.css";
import MyButton from "./components/UI/button/MyButton";
import MyInput from "./components/UI/input/MyInput.jsx";

function App() {
  const [posts, setPosts] = useState([
    { id: 1, title: "Javascriopt", body: "Description" },
    { id: 2, title: "Javascriopt", body: "Description" },
    { id: 3, title: "Javascriopt", body: "Description" },
  ]);

  const [title, setTitle] = useState("as");
  const addNewPost = () => {};
  return (
    <div className="App">
      <form>
        <MyInput
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          type="text"
          placeholder="Название поста"
        />
        <MyInput type="text" placeholder="Описание поста" />
        <MyButton onClick={addNewPost}>Создать пост</MyButton>
      </form>
      <PostList posts={posts} title="Посты про JS" />
    </div>
  );
}

export default App;
