# project/banks.py

# Example bank data (dummy IFSC + country info)
banks_data = {
    "SBI": {
        "name": "State Bank of India",
        "ifsc": "SBIN0000001",
        "country": "IN"
    },
    "HDFC": {
        "name": "HDFC Bank",
        "ifsc": "HDFC0000001",
        "country": "IN"
    },
    "ICICI": {
        "name": "ICICI Bank",
        "ifsc": "ICIC0000001",
        "country": "IN"
    },
    "PNB": {
        "name": "Punjab National Bank",
        "ifsc": "PUNB0000001",
        "country": "IN"
    }
}

# Utility function (optional)
def get_bank_info(code: str):
    """Return bank info by short code like 'SBI' or 'HDFC'"""
    return banks_data.get(code.upper(), {"error": "Bank not found"})