import { LiaAdobe } from "react-icons/lia";
import { FaBiohazard } from "react-icons/fa";
import { FaAccusoft } from "react-icons/fa";

function NavBar(){
    return(
        <>
        <header className="h-15 bg-[#1e293b] flex items-center ">
            <FaAccusoft style= {{ color: "blue" }} className="text-4xl m-1" />
            <div className=" p-1 m-1 bg-blue-600 text-md font-stretch-expanded font-serif rounded-md">CheckMate</div>
        </header>
        </>
    )

}
export default NavBar;
// <LiaAdobe className="size-md" />
// <FaBiohazard className="size-md"/>