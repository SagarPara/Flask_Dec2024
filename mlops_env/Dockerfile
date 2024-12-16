#getting OS and Python Image from DockerHub
from python:3.13.1-slim-bullseye

WORKDIR /docker

# Install the application dependencies
COPY requirements.txt ./ 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Copy in the source code
COPY . .

CMD ["python", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]


