import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./Pages/layout"
import Home from "./Pages/Home"
import Profile from "./Pages/Profile"
import Sessions from "./Pages/Sessions"
import Trends from "./Pages/Trends"
import About from "./Pages/About"
import SignIn from "./Pages/SignIn"
import NoPage from "./Pages/NoPage"

//This needs to be passed in by the backend
import currentUser from "./UserData/brandonData";


export default function App() {
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