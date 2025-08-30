import re, json, os

# Dangerous permissions list (agar APK inka use kare to suspicious maana jaayega)
DANGEROUS = {
    "android.permission.READ_SMS",
    "android.permission.READ_CALL_LOG",
    "android.permission.REQUEST_INSTALL_PACKAGES",
}

# Check karna ki URL me koi IP address to nahi hai
def has_ip(urls): 
    return any(re.search(r'\d+\.\d+\.\d+\.\d+', u) for u in urls)

# Check karna ki koi URL "http://" se start to nahi ho raha
def is_http(urls): 
    return any(str(u).startswith("http://") for u in urls)


# WHITELIST load karo (banks.json se signers)
WHITELIST = set()
fp = os.path.join(os.path.dirname(__file__), "../whitelist/banks.json")
if os.path.exists(fp):
    try:
        WHITELIST = set([x.lower() for x in json.load(open(fp)).get("signers", [])])
    except Exception:
        WHITELIST = set()


# Main function: score_result()
def score_result(meta: dict):
    score, reasons = 0, []

    # Metadata extract
    label   = (meta.get("label") or "").lower()
    pkg     = (meta.get("package") or "").lower()
    perms   = set(meta.get("permissions") or [])
    urls    = meta.get("urls") or []
    signer  = (meta.get("signer_sha256") or "").lower()

    # Check if label/package me bank related keyword hai
    bank_hint = any(k in label or k in pkg for k in ["bank", "upi", "pay"])

    # Rule 1: Agar bank app lag rahi hai but signer whitelist me nahi hai → suspicious
    if bank_hint and signer and signer not in WHITELIST:
        score += 30
        reasons.append("Unknown signer for banking app")

    # Rule 2: Agar dangerous permissions me se kuch use ho rahe hain
    if {"android.permission.READ_SMS", "android.permission.INTERNET"} & perms:
        score += 20
        reasons.append("SMS + Internet permission")

    # Rule 3: Agar APK install karne ki permission le raha hai
    if "android.permission.REQUEST_INSTALL_PACKAGES" in perms:
        score += 15
        reasons.append("Installer permission")

    # Rule 4: Privacy-related permissions (contacts, location, etc.)
    if any(p in perms for p in ["android.permission.READ_CONTACTS", "android.permission.ACCESS_FINE_LOCATION"]):
        score += 10
        reasons.append("Privacy-sensitive permissions")

    # Rule 5: Agar http:// ya IP based URL mile to suspicious
    if is_http(urls):
        score += 15
        reasons.append("Insecure HTTP URLs")
    if has_ip(urls):
        score += 15
        reasons.append("IP-based URLs found")

    # Verdict decide karo
    verdict = "suspicious" if score >= 30 else "likely_genuine"

    return {
        "verdict": verdict,
        "risk_score": score,
        "reasons": reasons
    }
import json
import os

# banks.json ka sahi path (1 folder upar jaake)
BANKS_FILE = os.path.join(os.path.dirname(__file__), "..", "banks.json")
BANKS_FILE = os.path.abspath(BANKS_FILE)

with open(BANKS_FILE, "r", encoding="utf-8") as f:
    BANKS = json.load(f)["trusted_banks"]

# --- yahan signer compare function banao ---
def check_signer(meta: dict):
    signer = meta.get("signer_sha256")
    if not signer:
        return False, None

    for bank in BANKS:
        if signer == bank["signer_sha256"]:
            return True, bank["name"]   # genuine
    return False, None                  # suspicious


# --- main scoring function ---
# def score_result(meta, sha256):
#     reasons = []
#     score = 0

#     # Call signer compare
#     is_genuine, bank_name = check_signer(meta)
#     if is_genuine:
#         return "genuine", 100, [f"Signed by trusted bank: {bank_name}"]

#     # Agar nahi mila to suspicious
#     score += 50
#     reasons.append("Signer not in trusted bank list")

#     return "suspicious", score, reasons
# from .heuristics_signer import check_signer   # agar alag file banayi hai
# ya same file me banaya hai to direct call kar sakte ho

# def score_result(meta, sha256):
#     reasons = []
#     score = 0

#     # Signer check
#     is_genuine, bank_name = check_signer(meta)
#     if is_genuine:
#         return "genuine", 100, [f"Signed by trusted bank: {bank_name}"]

#     # Agar match nahi hua to suspicious count karo
#     score += 50
#     reasons.append("Signer not in trusted bank list")

#     return "suspicious", score, reasons