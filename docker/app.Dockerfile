FROM python:3.10
WORKDIR /app

COPY requirements-prod.txt requirements-prod.txt
RUN pip install -r requirements-prod.txt

COPY . .
RUN rm -rf /tests

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]


