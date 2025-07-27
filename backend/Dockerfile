FROM python:slim

WORKDIR /app

COPY . .

RUN pip install flask

Expose 5000

CMD ["python", "app.py"]