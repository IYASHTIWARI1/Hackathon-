from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Fake Bank APK Detector Backend is running 🚀"

if __name__== "__main__":
    app.run(debug=True)
    from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Fake Bank APK Detector Backend is running 🚀"


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    
    return jsonify({"message": "File uploaded successfully!", "filename": file.filename})


    app.run(debug=True)
    from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Fake Bank APK Detector is running 🚀"

# ---- Upload route ----
@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return jsonify({"message": f"File {file.filename} uploaded successfully!"})
    

if __name__ == "__main__":
    app.run(debug=True)
    import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# agar banks.json white_list ke andar hai
BANKS_FILE = os.path.join(BASE_DIR, "white_list", "banks.json")

with open(BANKS_FILE, "r", encoding="utf-8") as f:
    data = f.read()