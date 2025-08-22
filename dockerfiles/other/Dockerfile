FROM python:3.1.2-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirementes.txt
EXPOSE 8080
CMD ["python", "sec.py"]