
import React, { useEffect, useState } from "react";
import { evaluateWithBackend } from "./scoringUtils";
import CircularProgress from "./ResultPage";

function BackendComponent({ collectData, setHide, onScoreCalculated }) {
  const [finalResult, setFinalResult] = useState(null);

  async function fetchBackendResult(collectData) {
  try {
    const formData = new FormData();
    formData.append("file", collectData); // "file" same hona chahiye backend ke param ke saath

    const response = await fetch("https://hackathon-16.onrender.com/upload", {
      method: "POST",
      body: formData, // Content-Type auto set hoga multipart/form-data
    });

    const data = await response.json();
    console.log("Backend response:", data);

    return { verdict: data.verdict }; 
  } catch (error) {
    console.error("Error calling backend:", error);
    return { verdict: "error" };
  }
}
   console.log(collectData);
  useEffect(() => {
    
    if (!collectData) return;
 
    async function runChecks() {
      const result = await evaluateWithBackend(collectData, fetchBackendResult);
      setFinalResult(result);
          
      // Pass score to circular bar
      if (typeof onScoreCalculated === "function") {
        onScoreCalculated(result.score);
      }
    }

    runChecks();

  }, [collectData]);

 
console.log(finalResult);
{ if(!finalResult){
      return ;
    }
  }
   setHide(false);
  return (
   

      <CircularProgress progress={finalResult.score} />
  );
}

export default BackendComponent;
