FROM python:3.10-slim

# Setare zonă de lucru în container
WORKDIR /app

# Copiem dependencies
COPY requirements.txt .

# Instalăm libs
RUN pip install --no-cache-dir -r requirements.txt

# Copiem tot proiectul
COPY . .

# Port pentru FastAPI
EXPOSE 8000

# Rulează serverul
CMD ["uvicorn", "backend.web.server:app", "--host", "0.0.0.0", "--port", "8000"]


