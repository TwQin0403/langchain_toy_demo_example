# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# 更新apt的套件庫並安裝 pdflatex
RUN apt-get update && apt-get install -y texlive-latex-base

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 開放應用程式所需的網路端口
EXPOSE 4321

# Run app.py when the container launches
CMD ["python", "app.py"]
