import os
import re
import hashlib
from typing import List, Dict, Any, Tuple
from androguard.core.apk import APK
from .heuristics import score_result   # <-- तुम्हारा scoring function import

# ----------------- Helpers -----------------
def _extract_urls_from_text(txt: str):
    """Text से crude URLs निकालता है"""
    if not txt:
        return []
    return re.findall(r"https?://[^\s\"\'<>]+", txt)

def _gather_cert_ders(a: APK) -> List[bytes]:
    """APK Signing v3/v2/v1 - जो भी मिले collect कर लो"""
    for getter in (a.get_certificates_der_v3, a.get_certificates_der_v2, a.get_certificates):
        try:
            certs = getter() or []
            if certs:
                return certs
        except Exception:
            pass
    return []

def signer_sha256_list(apk_path: str) -> List[str]:
    """Har signing certificate ka SHA-256 fingerprint return karta hai"""
    a = APK(apk_path)
    ders = _gather_cert_ders(a)
    return [hashlib.sha256(der).hexdigest() for der in ders]

# ----------------- Main Analysis -----------------
def analyze_apk(path: str, sha256: str = None) -> Dict[str, Any]:
    """
    APK Analyze karke final result return karega
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"APK not found: {path}")

    # --- APK load ---
    a = APK(path)   # Invalid APK hua to exception throw karega

    # --- Basic metadata ---
    label = a.get_app_name()
    pkg = a.package
    version = a.get_androidversion_name()
    perms = sorted(set(a.get_permissions()) or [])

    # --- Signer fingerprint(s) ---
    signer = None
    try:
        certs = _gather_cert_ders(a)
        if certs:
            signer = hashlib.sha256(certs[0]).hexdigest()
    except Exception:
        pass

    # --- URLs extraction ---
    urls = set()
    try:
        axml = a.get_android_manifest_axml()
        urls |= set(_extract_urls_from_text(axml.get_xml().decode()))
    except Exception:
        pass

    try:
        for s in (a.get_strings_resources() or []):
            urls |= set(_extract_urls_from_text(s))
    except Exception:
        pass

    # --- Final metadata object ---
    meta = {
        "package": pkg,
        "label": label,
        "version": version,
        "size_mb": round(os.path.getsize(path) / 1024 / 1024, 2),
        "signer_sha256": signer,
        "permissions": perms,
        "urls": sorted(urls),
    }

    # --- Heuristic scoring ( तुम्हारे module se ) ---
    try:
        verdict, score, reasons = score_result(meta, sha256 or "")
    except Exception as e:
        verdict, score, reasons = "ERROR", 0.0, [f"Heuristics failed: {e}"]

    return {
        "package": pkg,
        "verdict": verdict,   # SAFE / SUSPICIOUS / FAKE
        "score": round(score, 2),
        "reasons": reasons,
        "meta": meta
    }