import React, { useRef, useState } from "react";
import { Link2 } from "./Button";
import BackendComponent from "./Backend"; // Fix import path if needed

function FormComponent({ setHide ,getCollectedData}) {
  const [isDisable, setDisable] = useState(true);
  const [haveClicked, setHaveClicked] = useState(false);
  const [method, setMethod] = useState("GET");
  const [authType, setAuthType] = useState("none");
  const [headers, setHeaders] = useState([{ key: "", value: "" }]);
  const [bodyType, setBodyType] = useState("raw");
  const [collectedData, setCollectedData] = useState(""); // NEW STATE

  const inputRef = useRef(null);
  const bearerRef = useRef(null);
  const basicUserRef = useRef(null);
  const basicPassRef = useRef(null);
  const rawBodyRef = useRef(null);
  const fileRef = useRef(null);

  const isValidURL = (str) => {
    try {
      new URL(str);
      return true;
    } catch (e) {
      return false;
    }
  };

  const inputValue = () => {
    const value = inputRef.current?.value.trim();
    const valid = value !== "" && isValidURL(value);
    setDisable(!valid);
  };

  const handleHeaderChange = (index, field, value) => {
    const updated = [...headers];
    updated[index][field] = value;
    setHeaders(updated);
  };

  const addNewHeader = () => {
    setHeaders([...headers, { key: "", value: "" }]);
  };

  const removeHeader = (index) => {
    const updated = headers.filter((_, i) => i !== index);
    setHeaders(updated);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const dataObject = {
      method,
      url: inputRef.current?.value || "",
      authType,
      headers: headers.filter(h => h.key || h.value), // remove empty headers
      bodyType,
    };

    if (authType === "bearer") {
      dataObject.bearerToken = bearerRef.current?.value || "";
    } else if (authType === "basic") {
      dataObject.basicUser = basicUserRef.current?.value || "";
      dataObject.basicPass = basicPassRef.current?.value || "";
    }

    if ((method === "POST" || method === "PUT")) {
      if (bodyType === "raw") {
        dataObject.rawBody = rawBodyRef.current?.value || "";
      } else if (bodyType === "form") {
        const file = fileRef.current?.files?.[0];
        dataObject.uploadFile = file ? file.name : ""; // just the name for now
      }
    }

    // Pass JSON to the mock backend component
    setCollectedData(dataObject);
    console.log("📦 Collected Form Data:", dataObject);
  };

  return (
    <div className="flex relative items-center">
      <div className="relative mb-4 sm:ml-10 sm:w-md max-w-lg items-end flex flex-col">

        <form onSubmit={handleSubmit} className="w-full">
          {/* Method + URL */}
          <div className="flex mb-2">
            <select
              className="m-1 border border-gray-500 text-white bg-[#08111b] p-3 py-1 rounded-sm"
              onChange={(e) => setMethod(e.target.value)}
              name="method"
              value={method}
            >
              <option value="GET">GET</option>
              <option value="POST">POST</option>
              <option value="PUT">PUT</option>
              <option value="DELETE">DELETE</option>
            </select>

            <input
              onFocus={() => setHaveClicked(true)}
              ref={inputRef}
              onChange={inputValue}
              name="url"
              className="p-3 block mb-1 bg-[#08111b] rounded-sm text-white w-70 border border-gray-500"
              type="url"
              required
              placeholder="http://example.com/api"
            />
          </div>

          {haveClicked && isDisable && (
            <p className="text-red-500 font-bold size-md ml-23">
              Please enter a valid URL
            </p>
          )}

          {/* Auth Section */}
          <div className="mb-2">
            <label className="text-white font-bold">Authentication:</label>
            <select
              value={authType}
              onChange={(e) => setAuthType(e.target.value)}
              name="authType"
              className="ml-2 p-1 border border-gray-500 text-white bg-gray-600 rounded-sm"
            >
              <option value="none">No Auth</option>
              <option value="basic">Basic Auth</option>
              <option value="bearer">Bearer Token</option>
            </select>

            {authType === "bearer" && (
              <input
                type="text"
                ref={bearerRef}
                name="bearerToken"
                placeholder="Bearer Token"
                className="block mt-1 p-2 border text-white border-gray-500 w-full rounded-sm"
              />
            )}

            {authType === "basic" && (
              <>
                <input
                  type="text"
                  ref={basicUserRef}
                  name="basicUser"
                  placeholder="Username"
                  className="block mt-1 p-2 text-white border border-gray-500 w-full rounded-sm"
                />
                <input
                  type="password"
                  ref={basicPassRef}
                  name="basicPass"
                  placeholder="Password"
                  className="block mt-1 p-2 border text-white border-gray-500 w-full rounded-sm"
                />
              </>
            )}
          </div>

          {/* Headers Section */}
          <div className="mb-2">
            <label className="text-white font-bold">Custom Headers:</label>
            {headers.map((h, index) => (
              <div className="flex mt-1" key={index}>
                <input
                  name={`headerKey_${index}`}
                  value={h.key}
                  placeholder="Key"
                  onChange={(e) => handleHeaderChange(index, "key", e.target.value)}
                  className="p-1 border text-white border-gray-500 mr-2 rounded-sm w-1/2"
                />
                <input
                  name={`headerValue_${index}`}
                  value={h.value}
                  placeholder="Value"
                  onChange={(e) => handleHeaderChange(index, "value", e.target.value)}
                  className="p-1 border text-white border-gray-500 mr-2 rounded-sm w-1/2"
                />
                <button
                  type="button"
                  onClick={() => removeHeader(index)}
                  className="text-red-500"
                >
                  X
                </button>
              </div>
            ))}
            <button
              type="button"
              onClick={addNewHeader}
              className="mt-1 text-blue-500"
            >
              + Add Header
            </button>
          </div>

          {/* Body Section */}
          {(method === "POST" || method === "PUT") && (
            <div className="mb-2">
              <label className="text-white font-bold">Body:</label>
              <select
                value={bodyType}
                onChange={(e) => setBodyType(e.target.value)}
                name="bodyType"
                className="ml-2 p-1 bg-gray-600 text-white rounded-sm"
              >
                <option value="raw">Raw (JSON)</option>
                <option value="form">Form-Data</option>
              </select>

              {bodyType === "raw" && (
                <textarea
                  ref={rawBodyRef}
                  name="rawBody"
                  className="w-full h-32 p-2 mt-1 border text-white border-gray-500 rounded-sm"
                  placeholder='{"key": "value"}'
                ></textarea>
              )}

              {bodyType === "form" && (
                <>
                  <label className="mt-2 text-gray-600 block">Upload File:</label>
                  <input
                    ref={fileRef}
                    type="file"
                    name="uploadFile"
                    className="block w-full text-white mt-1"
                  />
                </>
              )}
            </div>
          )}

          {/* Submit */}
          <div className="space-x-2.5 mt-2.5">
            <button
              disabled={isDisable}
              className="bg-gray-950 hover:bg-white border border-white sm:border-0 hover:text-black inline-block shadow-md text-white py-1 px-1.5 rounded-sm font-medium cursor-pointer"
              type="submit"
            >
              Analyse URL
            </button>

            <Link2 To={"/"}>Return Home</Link2>
          </div>

          {/* Pass collected JSON data to the mock backend component */}
          {collectedData &&  getCollectedData(collectedData) }
        </form>
      </div>
    </div>
  );
}

export default FormComponent;

