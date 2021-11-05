import React, { useState } from "react";
import ClassCounter from "./components/ClassCounter";
import Counter from "./components/Counter";
import PostItem from "./components/PostItem";
import PostList from "./components/PostList";
import "./styles/App.css";

function App() {
  const [posts, setPosts] = useState([
    { id: 1, title: "Javascriopt", body: "Description" },
    { id: 2, title: "Javascriopt", body: "Description" },
    { id: 3, title: "Javascriopt", body: "Description" },
  ]);
  const [posts2, setPosts2] = useState([
    { id: 1, title: "Python", body: "Description" },
    { id: 2, title: "Python", body: "Description" },
    { id: 3, title: "Python", body: "Description" },
  ]);
  return (
    <div className="App">
      <PostList posts={posts} title="Список постов" />
      <PostList posts={posts2} title="Список постов" />
    </div>
  );
}

export default App;
