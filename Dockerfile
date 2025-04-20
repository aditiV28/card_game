# Dockerfile 

#Python image
FROM python:3.13.3

#Set working directory inside the container
WORKDIR /app

#Copy everything from current directory to container
COPY . .

#Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Set default command to run the app
CMD ["python", "main.py"]