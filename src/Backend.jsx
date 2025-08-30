
import React, { useEffect, useState } from "react";
import { evaluateWithBackend } from "./scoringUtils";
import CircularProgress from "./ResultPage";

function BackendComponent({ collectData, setHide, onScoreCalculated }) {
  const [finalResult, setFinalResult] = useState(null);

  async function fetchBackendResult(collectData) {
    try {
      const response = await fetch("https://hackathon-16.onrender.com/docs", {
        method: "POST",
          headers: {
        "Content-Type": "application/json",  // ✅ Tells backend to parse body as JSON
      },
        body: JSON.stringify(collectData),
      });

      const data = await response.json();  // ✅ properly await the JSON
      console.log("Backend response:", data); // ✅ see what backend returns
      
      // Assuming backend returns: { verdict: "fraud" } or { verdict: "safe" }
      return {
        verdict: data
      };
    } catch (error) {
      setHide(false);
      console.error("Error calling backend:", error);
      return { verdict: "error" };
    }
  }

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

  if (!finalResult) return( () => setHide(true));

  if (finalResult.reason) {
    return (
       <>
       <CircularProgress Reason={finalResult.reason} progress={finalResult.score}/>
       </>
    );
  }

  return (
      <CircularProgress progress={finalResult.score} Reason={finalResult.reason}/>
  );
}

export default BackendComponent;
