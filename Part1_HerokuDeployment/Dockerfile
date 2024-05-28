# Using an official Python runtime as a parent image
FROM python:3.10-slim

# Setting the working directory to /app
WORKDIR /app

# Copyping the current directory contents into the container at /app
COPY . /app

# Installing any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Making port 5000 available to the world outside this container
EXPOSE 5000

# Defining environment variable
ENV NAME World

# Running app.py when the container launches
CMD ["gunicorn", "app:app", "--config", "gunicorn_config.py"]
