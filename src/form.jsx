import React, { useRef, useState } from "react";
import { Link2 } from "./Button";

function FormComponent({ setHide, getCollectedData }) {
  const [isDisable, setDisable] = useState(true);
  const [collectedData, setCollectedData] = useState(null);
  const inputRef = useRef(null);

  const inputValue = () => {
    const file = inputRef.current?.files?.[0];
    if (file) {
      setCollectedData(file);
      setDisable(false);
    } else {
      setDisable(true);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // prevent page reload

    if (collectedData) {
      getCollectedData(collectedData);
      setHide(true); // hide the form after submission
    }
  };

  return (
    <div className="flex relative items-center">
      <div className="relative mb-4 sm:ml-10 sm:w-md max-w-lg items-end flex flex-col">
        <form onSubmit={handleSubmit} className="w-full">
          <label className="mt-2 text-gray-400 block">Upload File:</label>
          <input
            onChange={inputValue}
            ref={inputRef}
            type="file"
            name="uploadFile"
            className="block w-full text-white mt-1"
          />

          <div className="space-x-2.5 mt-2.5">
            <button
              disabled={isDisable}
              className="bg-gray-950 hover:bg-white border cursor-pointer disabled:cursor-not-allowed border-white sm:border-0 hover:text-black inline-block shadow-md text-white py-1 px-1.5 rounded-sm font-medium cursor-pointer"
              type="submit"
            >
              Analyse APK
            </button>

            <Link2 To={"/"}>Return Home</Link2>
          </div>
        </form>
      </div>
    </div>
  );
}

export default FormComponent;
