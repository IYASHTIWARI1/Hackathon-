# Python 3.13 official slim image use करें
FROM python:3.13-slim

# Working directory set करें container के अंदर
WORKDIR /app

# Dependencies install करने के लिए पहले requirements.txt copy करें
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# अब पूरा project container में copy करें
COPY . .

EXPOSE 8000

# FastAPI के लिए uvicorn run command
CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]