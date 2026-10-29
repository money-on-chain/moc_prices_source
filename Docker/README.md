# Run `moc_prices_source` inside a container (Docker)



This can be very useful to run on AWS as a task



## 1. Build docker image

```
$ sudo ./build.sh
```



## 2. Test docker image

```
$ sudo docker run --rm --name some_moc_prices_source -it moc_prices_source /check.sh
```




## 3. Run

### 3.1 Run `moc_prices_source_api`

Useful if you want to run it as part of end-to-end testing.

```
sudo docker run -d \
-p 7989:7989 \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_api" \
--env MOC_PRICES_SOURCE_ARGS="--addr 0.0.0.0 --port 7989" \
moc_prices_source
```

Or locally and interactively

```
sudo docker run --rm \
-p 7989:7989 \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_api" \
--env MOC_PRICES_SOURCE_ARGS="--addr 0.0.0.0 --port 7989" \
-it moc_prices_source
```

Options to be passed by the `MOC_PRICES_SOURCE_ARGS` environment variable:

```
-a, --addr TEXT     Server host addr.
-p, --port INTEGER  Server port.
```

API environment variables can be passed with `--env` (or `-e`) to `docker run`:

| Variable | Default in the image | Purpose |
| --- | --- | --- |
| `COMMAND` | `moc_prices_source_api` | Selects the program started by the container. |
| `MOC_PRICES_SOURCE_ARGS` | Empty | Command-line options passed to the selected program, such as `--addr` and `--port`. |
| `GUNICORN_WORKERS` | `2` | Number of API worker processes. Override this according to container resources and request load. |
| `GUNICORN_TIMEOUT` | `60` seconds | Time allowed for a worker to handle a request before Gunicorn restarts it. |
| `MAX_COINPAIR_LIMIT` | `12` | Maximum number of coinpairs accepted in a single API request. |
| `HEALTH_CHECK_USER_AGENT` | Built-in probe prefix | Only successful `GET /health_check` requests whose User-Agent starts with this value are omitted from the access log. Set it to an empty string to omit all successful requests to that endpoint. Failed checks and other endpoints remain logged. |
| `HEALTH_CHECK_LOG_INTERVAL` | `100` | Number of omitted successful health checks per API worker before a summary is written to the access log. Must be a positive integer. |
| `FLASK_DEBUG` | `false` | Runs the Flask development server when enabled. This mode requires `--addr` to be a loopback address and is not used for the published Docker port. |

For example, `--env GUNICORN_WORKERS=3` changes the worker count. To suppress
access logs for every successful health check, use
`--env HEALTH_CHECK_USER_AGENT=`. The bundled Redis configuration is stored in
`/home/app/.moc_prices_source/redis.json`; it is not selected by these
environment variables.

#### Health check

The API exposes `GET /health_check` for a load balancer or monitoring probe.
Use the address of the host running the container and the host port published
by `docker run -p`. For a request from that host with the `-p 7989:7989`
example above:

```sh
API_HOST=localhost
HOST_PORT=7989
curl "http://${API_HOST}:${HOST_PORT}/health_check"
```

The endpoint returns HTTP `200` with the JSON body `{"status":"ok"}`. Configure
the load balancer's health-check path as `/health_check`. This confirms that the
API can respond to HTTP requests; it does not check Redis or external price
sources.

Successful probes are omitted from individual access log entries according to
`HEALTH_CHECK_USER_AGENT` as described above. Each API worker logs a summary
after `HEALTH_CHECK_LOG_INTERVAL` omitted probes. Failed probes remain logged individually.

### Run 3.2 `moc_prices_source_to_db`


```
sudo docker run -d \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_to_db" \
--env MOC_PRICES_SOURCE_DB_CONF_NAME="MoC" \
--env MOC_PRICES_SOURCE_DB_CONF_HOST="xxxxxxx" \
--env MOC_PRICES_SOURCE_DB_CONF_PORT="8086" \
--env MOC_PRICES_SOURCE_ARGS="--frequency 10 --interval 0" \
moc_prices_source
```

Or locally and interactively

```
sudo docker run --rm \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_to_db" \
--env MOC_PRICES_SOURCE_DB_CONF_NAME="MoC" \
--env MOC_PRICES_SOURCE_DB_CONF_HOST="host.docker.internal" \
--env MOC_PRICES_SOURCE_DB_CONF_PORT="8086" \
--env MOC_PRICES_SOURCE_ARGS="--frequency 10 --interval 0" \
--add-host=host.docker.internal:host-gateway \
-it moc_prices_source
```


Options to be passed by the `MOC_PRICES_SOURCE_ARGS` environment variable:

```
-v, --verbose            Verbose mode.
-f, --frequency INTEGER  Loop delay in seconds.
-i, --interval INTEGER   How long the program runs (in minutes, 0 =
                         infinity)
```
