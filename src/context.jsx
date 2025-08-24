import { createContext } from "react";



import { useState } from 'react';


const TransferContext = createContext();
export default TransferContext;


export function DataComponent({children}){
    const [progress,setProgress] = useState(0);
return(
      <TransferContext.Provider value = {{progress,setProgress}}>
   
  <>{children}</>


  </TransferContext.Provider>
)
}
