
import Button, { Button2 } from "./Button";
import Bot from "./bot";




function HomePage(){
 

        
  
 return (<>
  <div className="bg-[rgb(8,17,27)] border-[#334155]  h-screen w-full text-center pt-10 flex flex-col  ">
    <div className="mb-5  p-0.5 bg-gradient-to-r from-yellow-400 via-pink-500 to-red-600 rounded-lg shadow-md" >
       <div className="text-reveal-container pt-1.5 sm:pt-4  bg-[rgb(8,17,27)] h-full w-full ">
        <h1 className="text-3xl sm:text-7xl reveal-text  text-blue-600  rounded  pb-1.5 sm:pb-5  font-serif bg-[#08111b] 
        
        " >Check-Mate</h1>
        </div>
         </div>
          <p className=" text-[#94a3b8] fade-in mb-5">A web Based Detection System  to check harmful phished APK files with using FastAPI</p>
    
    <div className="flex gap-x-8 justify-center fade-in " >
         <Button >Check APK !</Button>
         <Button2>Feature</Button2>
    </div>
    <div className="flex grow items-end  justify-center">
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