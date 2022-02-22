# Pull official base image.
FROM python:3.10.2-slim-buster

# Install Node.js and NPM via NVM (required in order to build client).
RUN apt-get update && apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Set working directory and copy project.
WORKDIR /usr/src/app
COPY . .

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for server.
RUN pip install --upgrade pip && pip install -r server/requirements.txt

# Build client.
RUN cd client && npm install . && npm run build-dev
