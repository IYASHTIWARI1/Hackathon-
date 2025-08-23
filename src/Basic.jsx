import { useEffect } from "react";
import Button from "./Button";
import Bot from "./bot";
import { useState } from "react";
import Loading from "./assets/Loading";



function HomePage(){
 

        
  
 return (<>
  <div className="bg-[#08111b] border-[#334155]  h-screen text-center pt-10 flex flex-col  ">
    <div className="mb-5 " >
        <h1 className="text-7xl text-blue-600  mb-4 pb-5 shadow-xl shadow-blue-500/50  font-serif bg-[#08111b] " >CheckMate</h1>
         </div>
          <p className=" text-[#94a3b8] mb-5">A web Based Detection System  to check harmful phished website with using FastAPI</p>
    
    <div className="flex gap-x-8 justify-center" >
         <Button >Check URL !</Button>
         <Button>Feature</Button>
    </div>
    <div className="flex grow items-end justify-center">
       <Bot/>
      
    </div>
  </div>
    </>)
}
export default HomePage;

//bg-[#1e293b]
//bg-[#0f172a]
//text-[#94a3b8]
// style={{ textShadow: '2px 2px 4px rgba(0,0,0,0.3)' }}
//drop-shadow-xl drop-shadow-blue-500