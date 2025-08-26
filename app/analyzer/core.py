from androguard.core.apk import APK
import hashlib, os, re
from .heuristics import score_result


# Helper function: text me se URLs nikalna
def _extract_urls_from_text(txt: str):
    if not txt:
        return []
    return re.findall(r"https?://[^\s\"\'<>]+", txt)


# Main function: APK analyze karna
def analyze_apk(path: str, sha256: str):
    # APK file load karo
    a = APK(path)   # Agar invalid APK hai to error throw karega

    # Basic metadata
    label = a.get_app_name()
    pkg = a.package
    version = a.get_androidversion_name()
    perms = sorted(set(a.get_permissions()) or [])

    # Signer fingerprint (best effort)
    signer = None
    try:
        certs = a.get_certificates_der_v2() or a.get_certificates_der_v3() or a.get_certificates()
        if certs:
            signer = hashlib.sha256(certs[0]).hexdigest()
    except Exception:
        pass

    # Crude URL extraction
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

    # Final collected metadata
    meta = {
        "package": pkg,
        "label": label,
        "version": version,
        "size_mb": round(os.path.getsize(path) / 1024 / 1024, 2),
        "signer_sha256": signer,
        "permissions": perms,
        "urls": sorted(urls),
    }

    # Heuristic score nikalna (alag module me define hai)
    verdict, score, reasons = score_result(meta, sha256)

    return verdict, score, reasons, meta
import hashlib
from typing import List
from androguard.core.apk import APK

def _gather_cert_ders(a: APK) -> List[bytes]:
    """
    APK Signing v3/v2/v1 sab cover: jo mil jaye use kar lo.
    """
    for getter in (a.get_certificates_der_v3, a.get_certificates_der_v2, a.get_certificates):
        try:
            certs = getter() or []
            if certs:
                return certs
        except Exception:
            pass
    return []

def signer_sha256_list(apk_path: str) -> List[str]:
    """
    Har signing certificate ka SHA-256 fingerprint (lowercase hex) return karta hai.
    """
    a = APK(apk_path)
    ders = _gather_cert_ders(a)
    return [hashlib.sha256(der).hexdigest() for der in ders]
# app/core.py
import os

def analyze_apk(apk_path: str) -> dict:
    """
    Return a dict like:
    {
      "package": "com.bank.app",
      "label": "FAKE" / "SUSPICIOUS" / "SAFE",
      "score": 0.92,
      "reasons": ["Unknown signer", "Mismatched package name"],
      "meta": {"size_bytes": 1234}
    }
    """
    if not os.path.exists(apk_path):
        raise FileNotFoundError("APK not found")

    # --- Hook #1: call your heuristics ---
    reasons = []
    score = 0.0
    label = "UNKNOWN"
    package_name = None

    # Example wiring (rename according to your code):
    try:
        # from app.heuristics import run_all_checks
        # hr = run_all_checks(apk_path)     # expect dict with 'score','reasons','package'
        # score = hr.get('score', 0.0)
        # reasons.extend(hr.get('reasons', []))
        pass
    except Exception as e:
        reasons.append(f"Heuristics error: {e}")

    # --- Hook #2: signer verification ---
    try:
        # from app.heuristics_signer import check_signer
        # signer_ok, signer_reason = check_signer(apk_path)
        # if not signer_ok:
        #     score = max(score, 0.8)
        #     reasons.append(signer_reason or "Signer not trusted")
        pass
    except Exception as e:
        reasons.append(f"Signer check error: {e}")

    # --- Example simple labeling (tune as per your calc) ---
    if score >= 0.85:
        label = "FAKE"
    elif score >= 0.5:
        label = "SUSPICIOUS"
    else:
        label = "SAFE"

    return {
        "package": package_name,
        "label": label,
        "score": round(score, 2),
        "reasons": reasons,
        "meta": {"size_bytes": os.path.getsize(apk_path)}
    }
def analyze_apk(filepath):
    # Dummy analysis
    return {"label": "Safe", "score": 95}