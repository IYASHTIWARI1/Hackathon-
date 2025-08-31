
import {useState} from "react";
import Loading from './assets/Loading';
import CircularProgress  from './ResultPage';
import FormComponent from "./form";
import { useEffect } from "react";
import BackendComponent from "./Backend";


function InputPage(){
  const[hide,setHide] = useState(false);
  
  const[Collected,setCollect] = useState("");


    
 function getCollectedData(collectData){
  setCollect(collectData);
 }
    return(
<>
<div className="bg-[#08111b] border-[#334155] scroll-auto h-screen flex items-center sm:justify-center p-1 md:p-10">
    <div className="flex flex-col  w-full h-[80%] scroll-auto sm:flex-row justify-around ">


       <div className=" flex items-center  sm:w-1/2 max-w-120 h-full justify-center ">
        {hide && <Loading/>}
         {!Collected ? (<div className="  max-w-lg ">
             <h1 className="text-5xl  mb-3 text-blue-600 sm:mb-1 font-serif  " >CHECK URL</h1>
            <p className="hidden sm:block text-[#94a3b8]">Please add the URL of a apk to verify wheather the url if the 
                <span className="text-blue-500 text-2xl"> legitimate </span>
                or
                <span  className=" text-2xl text-amber-300"> phishing</span>
                </p>
    
        </div>)  : (<BackendComponent setHide={setHide} collectData={Collected} />)
       }
        
         </div>
         
        <FormComponent setHide={setHide} getCollectedData={getCollectedData}></FormComponent>
        
    </div>
</div>
</>
    )
}
export default InputPage;