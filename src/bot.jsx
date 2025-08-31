//import Spline from '@splinetool/react-spline/next';
import Spline from '@splinetool/react-spline';
import Loading from './assets/Loading';
import { useState } from 'react';

export default function Home() {
   const[loading,setLoading] =useState(true);


  return (
    <>
   
    <main  className=" max-w-md fade-in  h-11/12">
   
    
    { <Spline 
        scene="https://prod.spline.design/pOWgeYZEBOhqustO/scene.splinecode" 
        onLoad={() => { 
          console.log("state chnged")
          setLoading(false)}}
     />} 

     
        
     
    </main>
  
    </>
  );
}

