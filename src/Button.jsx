 
import { Link } from "react-router-dom";

 function Button({children,className}){
    return(
        <>
        <Link to="/CheckMate/InputPage" className={"transform transition-transform duration-300 hover:scale-110 bg-purple-700  inline-block w-40 shadow-md shadow-purple-700/50 text-white p-2 rounded-md font-medium cursor-pointer"+"  " + className}>{children}</Link>
        </>
    )
 }
 export default Button;

 export function Button2({children,type,className,state}){

     
   
     return (
        <>
           <button onClick={() => {state(false)} }  className={" bg-gray-950 hover:bg-white hover:text-black inline-block shadow-md  text-white py-1 px-1.5 rounded-sm font-medium cursor-pointer"+"  " + className} type={type} >{children} </button>
           </>
      )}

 export function Link2({children,className,To}){
     return (
        <>
           <Link to={To} className={" hover:bg-white hover:text-black bg-gray-950  inline-block shadow-md  text-white py-1 px-1.5 rounded-sm font-medium cursor-pointer"+"  " + className}  >{children} </Link>
           </>
      )}



//  export function Button2({children,type,className,To}){
//      return (
//         <>
//            <button  className={" bg-gray-950  inline-block shadow-md  text-white py-1 px-1.5 rounded-sm font-medium cursor-pointer"+"  " + className} type={type} >{children} </button>
//            </>
//       )}
