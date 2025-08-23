
function Loading(){
    
     



   console.log("loading called");
    return(
     <div className="bg-[#08111b] border-[#334155]  h-fit gap-1 flex items-center justify-center ">
          <div  className="pulse-height brightness-200" style={{width:"20px", height:"80px", background:"green", animationDuration: "0.5s"}}></div>
          <div  className="pulse-height brightness-200" style={{width:"20px", height:"80px", background:"green",  animationDuration: "0.8s"}}></div>
  <div  className="pulse-height brightness-200" style={{width:"20px", height:"80px", background:"green",  animationDuration: "1.1s" }}></div>
  <div  className="pulse-height brightness-200" style={{width:"20px", height:"80px", background:"green",       animationDuration: "1.4s"}}></div>
  <div  className="pulse-height brightness-200" style={{width:"20px", height:"80px", background:"green",  animationDuration: "1.7s"}}></div>
 
 </div>)
}
export default Loading;


