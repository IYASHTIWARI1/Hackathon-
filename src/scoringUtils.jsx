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

  // -------------------------------
  // 🚫 Hard Fail Checks
  // -------------------------------
  try {
    new URL(url);
  } catch (err) {
    return { score: 0, reason: "Invalid or missing URL" };
  }

  const bannedDomains = ["000webhostapp.com", "freehosting.com", "infinitefree.net"];
  if (bannedDomains.some(domain => url.includes(domain))) {
    return { score: 0, reason: "Suspicious domain detected" };
  }

  if (authType === "bearer" && (!bearerToken || bearerToken.length < 5)) {
    return { score: 0, reason: "Bearer token missing or too short" };
  }

  if (authType === "basic" && (!basicUser || !basicPass)) {
    return { score: 0, reason: "Basic auth username or password missing" };
  }

  if ((method === "POST" || method === "PUT")) {
    if (bodyType === "raw" && (!rawBody || rawBody.trim().length < 5)) {
      return { score: 0, reason: "POST/PUT requires valid body but it's empty" };
    }
    if (bodyType === "form" && !uploadFile) {
      return { score: 0, reason: "File missing in form-data body" };
    }
  }

  // -------------------------------
  // ✅ Soft Scoring (Max 30)
  // -------------------------------
  if (url.startsWith("https://")) score += 5;

  if (authType !== "none") score += 5;

  const filledHeaders = headers.filter(h => h.key && h.value);
  if (filledHeaders.length >= 1) score += 5;
  if (filledHeaders.length >= 3) score += 3;

  if (bodyType === "raw" && rawBody?.trim().startsWith("{")) score += 5;

  if (bodyType === "form" && uploadFile) score += 7;

  if (score > 30) score = 30;
  const primaryScore = score;

  // -------------------------------
  // 🧠 Fetch Backend Result
  // -------------------------------



  const backendResult = await fetchBackendResult(collectData); // must return { verdict: string }

  let backendScore = 0;
  if (backendResult.verdict === "good") backendScore = 70;
  else if (backendResult.verdict === "suspicious") backendScore = 50;
  else if (backendResult.verdict === "fraud") backendScore = 0;

  // Apply fraud penalty
  if (primaryScore > 10 && backendResult.verdict === "fraud") {
    backendScore -= 10;
  }

  // Final score
  const totalScore = primaryScore + backendScore;
  return {
    score: totalScore < 0 ? 0 : totalScore,
    primaryScore,
    backendScore,
    verdict: backendResult.verdict,
    reason: null
  };
}
