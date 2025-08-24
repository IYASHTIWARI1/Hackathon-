import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Routes ,Route} from 'react-router-dom';
import Basic from './Basic';
import NavBar from './navBar';
import InputPage from './InputPage';

import Loading from './assets/Loading';
import { DataComponent } from './context';




function App() {

 

  return (
    <>

    <NavBar/>
      <div className="">
        <DataComponent>
        <Routes>
                            
        <Route index element={<Basic/>}></Route>
        <Route path="/CheckMate/InputPage" element={<InputPage/>}></Route>
     
        <Route path = "*" element={<Basic/>}/>
        <Route path = "/loading" element={<Loading/>}/>
       </Routes>
      </DataComponent>
       </div>
    </>
  )
}

export default App

  // <input
  //       type="range"
  //       min="1"
  //       max="100"
  //       value={progress}
  //       onChange={(e) => setProgress(Number(e.target.value))}
  //       className="mt-6 w-64"
  //     />}