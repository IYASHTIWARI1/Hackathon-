// scoringUtils.js
export async function evaluateWithBackend(collectData, fetchBackendResult) {
  let score = 0;
  let reason = null;

  const {
    url,
    method,
    authType,
    bearerToken,
    basicUser,
    basicPass,
    headers,
    bodyType,
    rawBody,
    uploadFile,
  } = collectData;

 


 

  const backendResult = await fetchBackendResult(collectData); // must return { verdict: string }

  let backendScore = 0;
  if (backendResult.verdict === "good") backendScore = 100;
  else if (backendResult.verdict === "suspicious") backendScore = 60;
  else if (backendResult.verdict === "bad") backendScore = 9;


  // Final score
  const totalScore = backendScore;
  console.log("total score",totalScore)
  return {
    score: totalScore,
   
    backendScore,
    verdict: backendResult.verdict,
    reason: backendResult?.reason, 
  };
}
