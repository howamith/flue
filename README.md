# Flue #

Flue is a simple example web application that uses
[Flask](https://flask.palletsprojects.com/en/2.0.x/) on the server and
[Vue.js](https://vuejs.org/) on the client (specifically
[`@vue-cli`](https://cli.vuejs.org/)), put together purely for learning and
experimentation.

### Why 'Flue'? ###

Flue = Flask + Vue.js

## TODO ##

- [ ] Server tests
- [ ] Client tests
- [ ] Aesthetics
- [ ] Add controls/ components to add new tasks


## Running ##

Flue can either be run by starting the required services manually or via Docker.
Using Docker is easier, however it is more convenient during development to
start the services manually, as this saves having to keep rebuilding the
containers.

### Running via Docker ###

Build and spin up the containers:

```bash
docker-compose up -d --build
```

Once you've built the containers once, you can spin them up without having to
build them every time:

```bash
docker-compose up -d
```

Note that if you make changes to any of the source then you need to rebuild the
containers for those changes to take effect.

### Running Manually ###

Start `redis` in a Docker container:

```bash
docker run -d -p 6379:6379 redis
```

Start the `celery` worker server:

```bash
. venv/bin/activate
celery -A server.tasks worker --loglevel=INFO
```

Build the Vue.js application

```bash
cd client/
npm run build # or build-dev if you want to be able to use Vue.js DevTools
```

Run the Flask server

```bash
. venv/bin/activate
export FLASK_APP=server
flask run
```
