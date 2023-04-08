import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React, { useState, useEffect } from "react";
import axios from "axios";

import Layout from "./Pages/layout"
import Home from "./Pages/Home"
import Profile from "./Pages/Profile"
import Sessions from "./Pages/Sessions"
import Trends from "./Pages/Trends"
import About from "./Pages/About"
import SignIn from "./Pages/SignIn"
import NoPage from "./Pages/NoPage"

//This needs to be passed in by the backend
import defaultUser from "./UserData/userData";



export default function App() {
  const [currentUser, setUser] = useState(defaultUser);
  const getData = async () => {
    await axios.get("http://localhost:8080/frontend/GingaNinja").then((response) => {
        //console.log(response.data);
        setUser(response.data);
    });
  }

  useEffect(() => {getData()}, [])
  console.log(currentUser);

  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/profile" element={<Profile user={currentUser}/>} />
          <Route path="/sessions" element={<Sessions user={currentUser}/>} />
          <Route path="/trends" element={<Trends user={currentUser}/>} />
          <Route path="/about" element={<About />} />
          <Route path="/sign-in" element={<SignIn/>} />

          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));