import { Button2 } from "./Button";
import { Link2 } from "./Button";
import {useState} from "react";
import Loading from './assets/Loading';
import CircularProgress  from './ResultPage';


function InputPage(){
  const[hide,setHide] = useState(true);
  const[graph,setGraph] = useState(true);

  if(!hide){
    setInterval(() => {
        setGraph(false);
    }, 3000);
   
  }

    return(
<>
<div className="bg-[#08111b] border-[#334155]  h-screen flex items-center sm:justify-center p-5 md:p-10">
    <div className="flex flex-col h-[80%] sm:flex-row ">


       <div className=" flex items-center  w-80 h-full justify-center ">
        
        {graph ? (hide ? (<div className="  max-w-lg ">
             <h1 className="text-5xl  mb-3 text-blue-600 sm:mb-1 font-serif  " >CHECK URL</h1>
            <p className="hidden sm:block text-[#94a3b8]">Please add the URL of a apk to verify wheather the url if the 
                <span className="text-blue-500 text-2xl"> legitimate </span>
                or
                <span  className=" text-2xl"> phishing</span>
                </p>
        </div>) : <Loading />) : <CircularProgress progress={90} />
       }

         </div>
        <div className="flex  items-center ">
           <div className=" sm:ml-10  sm:w-md max-w-lg items-end flex flex-col">
            <form >
            <label htmlFor="urlInput" className="sr-only">Enter APK URL</label>
            <input  className=" p-3 block mb-4 text-gray-500 w-70 border border-gray-500" type="url" required  placeholder="http//checkUrl.com"/>
           </form>
          <div className="space-x-2.5">
            
                
            <Button2  type="submit" state={setHide} >Analyzie url</Button2>
            
           <Link2 >Return Home</Link2>
           </div>
        </div>
        </div>
    </div>
</div>
</>
    )
}
export default InputPage;