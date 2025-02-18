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


```
sudo docker run -d \
-p 7989:7989 \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_api" \
--env MOC_PRICES_SOURCE_ARGS="--port 7989" \
moc_prices_source
```

Or locally and interactively

```
sudo docker run --rm \
-p 7989:7989 \
--name some_moc_prices_source \
--env COMMAND="moc_prices_source_api" \
--env MOC_PRICES_SOURCE_ARGS="--port 7989" \
-it moc_prices_source
```


Options to be passed by the `MOC_PRICES_SOURCE_ARGS` environment variable:

```
-a, --addr TEXT     Server host addr.
-p, --port INTEGER  Server port.
```

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
