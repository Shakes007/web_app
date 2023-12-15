# From a lighter version of python
FROM python:3.10-slim-buster

#
WORKDIR /app

# Copy requirements.txt from the local repo to the image and call it:
# requirements.txt
COPY requirements.txt requirements.txt

# Install the prerequisites from requirements.txt
RUN pip install -r requirements.txt

# Copy all files from the directory.
COPY . .

# Run the command line to start server at port 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]