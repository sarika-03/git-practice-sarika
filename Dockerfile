FROM python
WORKDIR /appy
COPY requirements.txt  .
RUN pip install --root-user-action=ignore -r requirements.txt
COPY app.py .
RUN chmod 755 /appy/app.py
EXPOSE 8000 
CMD ["python" "./app.py"]