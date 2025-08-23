
import { useState } from 'react';
import TransferContext from '/context';
import { ContextComponent } from '/context';

function DataComponent({children}){
    const [progress,setProgress] = useState(0);
return(
      <TransferContext.Provider value = {{progress,setProgress}}>
   
  <ContextComponent>{children}</ContextComponent>


  </TransferContext.Provider>
)
}
export default DataComponent;