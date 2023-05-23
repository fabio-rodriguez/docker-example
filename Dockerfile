FROM python:3.10.7

# Set the working directory
WORKDIR /app 

COPY main.py .

CMD ["python", "./main.py"]