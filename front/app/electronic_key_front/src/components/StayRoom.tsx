import React from 'react'
import Product from '../models/Product'
import { useState, useEffect } from 'react';

import '../css/StayRoom.css';

function StayRoom() {
  const [bool,setBool]=React.useState<boolean>(false);
  const [time, setTime] = useState('');
  const [topics,setTopics]=useState<Product[]>([]);
  const [date, setDate] = useState("")
  const now_date=()=>{
    let tmp="";
    let date=new Date()
    tmp+=String(date.getFullYear())+"-";
    tmp+=String("0"+(date.getMonth() + 1)).slice(-2)+"-";
    tmp+=String("0"+(date.getDate())).slice(-2);
    setDate(tmp); 
  }
    useEffect(() => {
      now_date()
      const fetchData = async () => {
        try {
        const response = await fetch("http://localhost:5001/return_data");
        const data = await response.json();
        setBool(true);
        console.log(...data)
        setTopics([...data])
        setTime(data[0].date)
        
        }catch (err) {
          setBool(false);
        }
      
      };
      fetchData();
    }, []);
    
  
  return (
    <>
    <li>
    <div>
      {date}の入室状況
    </div>
    </li>
   
    {bool ? 
      topics.map((topic,i) => {
          return  (<div className="border" key={i}>{i+1}番目の入室者:<b>{ topic.name }</b>入室時間:{topic.time}</div>);
      })
      :<div className="noEnter">入室記録なし</div>
   }
    </>
  )
}

export default StayRoom