import React from 'react'
import ReactDOM from 'react-dom';
import Button from '@mui/material/Button';
import InforCss from "../css/Information.css" 
import { useNavigate } from "react-router-dom";
function Information() {
  const navigate = useNavigate()
  const StayRoom = () => {
    navigate('/StayRoom')
}
const Login = () => {
  navigate('/Login')
}
  return (
    <div>
      <div className="wrapper">
        <div><Button variant="contained" onClick={StayRoom}>在室状況</Button></div>
        <div><Button variant="contained" onClick={Login}>入室登録</Button></div>
      </div>
    </div>
  )
}

export default Information