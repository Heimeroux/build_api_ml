FROM python:3.9-slim

WORKDIR /app

COPY . /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter l'application
CMD ["uvicorn", "service_user.user:app", "--host", "0.0.0.0", "--port", "8001"]