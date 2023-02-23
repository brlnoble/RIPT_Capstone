import ReactDOM from "react-dom";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./Pages/layout";
import Home from "./Pages/Home";
import Profile from "./Pages/Profile";
import NoPage from "./Pages/NoPage"


export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="/profile" element={<Profile />} />

          <Route path="*" element={<NoPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));