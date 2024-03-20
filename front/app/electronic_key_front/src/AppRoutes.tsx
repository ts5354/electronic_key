import { Routes, Route } from "react-router-dom";

import StayRoom from "./components/StayRoom"
import Login from "./components/Login"
import App from "./App"
export const AppRoutes = () => {
    return (
        <Routes>
            <Route path="/" element={<App />} />
            <Route path="/StayRoom" element={<StayRoom />} />
            <Route path="/Login" element={<Login />} />
        </Routes>
    )
}