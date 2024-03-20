import React from 'react'
import { useState, useEffect } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';

function Login() {
    const [name, setName] = useState('');
    const [time, setTime] = useState("");
    const [date, setDate] = useState("")
    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };
    const now_date=()=>{
        let tmp="";
        let date=new Date()
        tmp+=String(date.getFullYear())+"-";
        tmp+=String("0"+(date.getMonth() + 1)).slice(-2)+"-";
        tmp+=String("0"+(date.getDate())).slice(-2);
        setDate(tmp);
        
    }
    const now_time=()=>{
        let tmp="";
        let date=new Date()
        date.getHours();
        
        tmp+=String("0"+(date.getHours())).slice(-2)+":";
        date.getMinutes(); 
        tmp+=String("0"+(date.getMinutes())).slice(-2)+":";
        date.getSeconds();
        tmp+=String("0"+(date.getSeconds())).slice(-2);
        setTime(tmp)
    }
    const handleSubmit = async () => {

        const response = await fetch("http://localhost:5001/add_data", {
            method: "POST",
            headers: {'Content-Type' : 'application/json'},
            body: JSON.stringify({name: name, date: date, time: time})
            
        })
        const data = await response.json();
        console.log(data);
    }
    useEffect(()=>{
        now_time(); 
        now_date();
      },[])
  return (
    <Container maxWidth="sm">
            <Typography variant="h4" component="h1" gutterBottom>
                入室登録
            </Typography>
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    gap: 2, // スペース
                    alignItems: 'center',
                    justifyContent: 'center',
                }}
            >
                <TextField 
                    label="名前を入力" 
                    variant="outlined" 
                    value={name} 
                    onChange={handleChange} 
                    fullWidth
                />
                <Button variant="contained" color="primary" onClick={handleSubmit}>
                    登録
                </Button>
            </Box>
        </Container>
  )
}

export default Login