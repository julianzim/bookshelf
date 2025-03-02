FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod -R 777 /app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
