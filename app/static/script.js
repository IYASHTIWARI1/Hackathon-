console.log("Page loaded successfully!");
const form = document.getElementById('uploadForm');
const statusBox = document.getElementById('status');
const resultCard = document.getElementById('result');
const labelEl = document.getElementById('label');
const scoreEl = document.getElementById('score');
const pkgEl = document.getElementById('pkg');
const reasonsEl = document.getElementById('reasons');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  resultCard.style.display = 'none';
  reasonsEl.innerHTML = '';
  statusBox.textContent = 'Uploading & analyzing...';

  const file = document.getElementById('apkFile').files[0];
  if (!file) {
    statusBox.textContent = 'Please choose an .apk file.';
    return;
  }

  const fd = new FormData();
  fd.append('file', file);

  try {
    const res = await fetch('/api/upload', { method: 'POST', body: fd });
    const data = await res.json();

    if (!data.ok) {
      statusBox.textContent = "Error: " + (data.error || "Unknown error");
      return;
    }

    statusBox.textContent = 'Done.';
    labelEl.textContent = data.result.label;
    scoreEl.textContent = data.result.score;
    pkgEl.textContent = data.result.package || 'N/A';

    (data.result.reasons || []).forEach(r => {
      const li = document.createElement('li');
      li.textContent = r;
      reasonsEl.appendChild(li);
    });

    resultCard.style.display = 'block';
  } catch (err) {
    statusBox.textContent = 'Network error or server down.';
  }
});