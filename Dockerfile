# Dupa cum a fost specificat in enuntul temei
FROM python:3.9-alpine

WORKDIR /app

# Copiez tot
COPY . .

COPY requirements.txt .

# instalez ce e in requirements
RUN pip install --no-cache-dir -r requirements.txt

# deschid portul
EXPOSE 5000

# comanda de rulare
CMD ["python", "server.py"]
