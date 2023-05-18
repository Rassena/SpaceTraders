FROM python:3.10
WORKDIR /app
COPY . /app
ENV PYTHONPATH=/app/
RUN pip install -r requirements.txt
ENTRYPOINT  ["python", "src/main.py"]