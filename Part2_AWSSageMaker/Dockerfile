# Using an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Jupyter Lab explicitly
RUN pip install jupyterlab

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to configure Jupyter to listen on all interfaces
ENV JUPYTER_ENABLE_LAB=yes

# Run Jupyter Lab when the container launches
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=5000", "--no-browser", "--allow-root"]
