# app/project/utils/verify.py
import json
from pathlib import Path
import subprocess
import re

BASE_DIR = Path(__file__).resolve().parent.parent   # app/project
WHITELIST = BASE_DIR / "whitelist" / "banks.json"   # adjust if your file name/path different

# --- load whitelist (cached) ---
_whitelist_cache = None
def load_whitelist():
    global _whitelist_cache
    if _whitelist_cache is None:
        if not WHITELIST.exists():
            _whitelist_cache = {"apps": {}, "banks": []}
        else:
            with WHITELIST.open("r", encoding="utf-8") as f:
                _whitelist_cache = json.load(f)
    return _whitelist_cache

def reload_whitelist():
    global _whitelist_cache
    _whitelist_cache = None
    return load_whitelist()

# --- verify a signer hex against an app entry in whitelist ---
def normalize_hex(s: str) -> str:
    return s.lower().replace(":", "").strip()

def verify_signer(app_id: str, signer_hex: str) -> bool:
    wl = load_whitelist()
    apps = wl.get("apps", {})
    app_info = apps.get(app_id)
    if not app_info:
        return False
    signer_hex = normalize_hex(signer_hex)
    allowed = [normalize_hex(s) for s in app_info.get("signers_sha256", [])]
    return signer_hex in allowed

# --- call apksigner and parse SHA-256 digest (requires apksigner on PATH) ---
def extract_signer_sha256_apksigner(apk_path: str) -> str:
    """
    Runs: apksigner verify --print-certs <apk>
    returns: hex string (lowercase, no colons) of first signer SHA-256
    Raises RuntimeError if not found or apksigner missing.
    """
    try:
        proc = subprocess.run(
            ["apksigner", "verify", "--print-certs", apk_path],
            capture_output=True, text=True, check=False
        )
    except FileNotFoundError:
        raise RuntimeError("apksigner not found. Install Android build-tools and ensure apksigner is on PATH.")

    output = (proc.stdout or "") + (proc.stderr or "")
    # Try common patterns
    m = re.search(r"(?i)sha-256(?: digest)?:\s*([0-9A-Fa-f:]+)", output)
    if not m:
        m = re.search(r"(?i)certificate SHA-256 digest:\s*([0-9A-Fa-f:]+)", output)
    if not m:
        m = re.search(r"Signer #\d+ certificate SHA-256 digest:\s*([0-9A-Fa-f:]+)", output)
    if not m:
        raise RuntimeError("Could not find SHA-256 digest in apksigner output. Output:\n" + output[:2000])

    sha = normalize_hex(m.group(1))
    return sha
