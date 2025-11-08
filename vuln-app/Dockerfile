FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# initialize DB on container start (creates sample data)
RUN python init_db.py

EXPOSE 5000
CMD ["python", "app.py"]
