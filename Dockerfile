# Pull in official Node.js v14.x base image.
FROM node:14-buster-slim AS client_builder

# Set working directory and copy client/ directory into build environment.
WORKDIR /client_build
COPY ./client /client_build/client

# Build client.
RUN cd client && npm install . && npm run build

# Pull in official Python3.10.2 base image.
FROM python:3.10.2-slim-buster

# Set working directory and copy client and server into container.
WORKDIR /usr/src/app
COPY --from=client_builder /client_build/client/www client/www
COPY ./server server
RUN ls -al client

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for server.
RUN pip install --upgrade pip && pip install -r server/requirements.txt
