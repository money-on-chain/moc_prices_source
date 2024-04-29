# Run `moc_prices_source_to_db` inside a container (Docker)



This can be very useful to run on AWS as a task



### 1. Build docker image

```
$ ./build.sh
```



### 2. Test docker image

```
$ sudo docker run --rm --name some_moc_prices_source -it moc_prices_source /check.sh
```




### 3. Run

```
sudo docker run -d \
--name some_moc_prices_source \
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
--env MOC_PRICES_SOURCE_DB_CONF_NAME="MoC" \
--env MOC_PRICES_SOURCE_DB_CONF_HOST="host.docker.internal" \
--env MOC_PRICES_SOURCE_DB_CONF_PORT="8086" \
--env MOC_PRICES_SOURCE_ARGS="--frequency 10 --interval 0" \
--add-host=host.docker.internal:host-gateway \
-it moc_prices_source bash
```


Options to be passed by the `MOC_PRICES_SOURCE_ARGS` environment variable:

```
-v, --verbose            Verbose mode.
-f, --frequency INTEGER  Loop delay in seconds.
-i, --interval INTEGER   How long the program runs (in minutes, 0 =
                         infinity)
```
