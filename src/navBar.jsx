import { LiaAdobe } from "react-icons/lia";
import { FaBiohazard } from "react-icons/fa";
import { FaAccusoft } from "react-icons/fa";

function NavBar(){
    return(
        <>
        <header className="h-15 bg-[#1e293b] flex items-center ">
            <FaAccusoft style= {{ color: "blue" }} className="text-4xl m-1" />
            <div className=" p-1 m-1  text-md font-stretch-expanded font-serif 
            bg-gradient-to-r from-teal-400 via-cyan-400 to-blue-500 rounded-lg shadow-md
            animate-pulse text-white
            ">Check-Mate</div>
        </header>
        </>
    )

}
export default NavBar;
// <LiaAdobe className="size-md" />
// <FaBiohazard className="size-md"/>