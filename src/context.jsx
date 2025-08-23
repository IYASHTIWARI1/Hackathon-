import { createContext } from "react";


export default TransferContext = createContext();

   
export function ContextComponent({children}){
   return {children};
}