FROM python:3.8

RUN apt-get update && \
    apt-get install -y \
        locales redis supervisor

RUN echo $TZ > /etc/timezone && \
    apt-get update && apt-get install -y tzdata && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip3 install rusty-rlp

COPY ./files/moneyonchain_prices_source.tar.gz /
RUN pip3 install /moneyonchain_prices_source.tar.gz
RUN rm /moneyonchain_prices_source.tar.gz

RUN mkdir /root/.moc_prices_source
COPY ./files/conf/redis.json /root/.moc_prices_source/
COPY ./files/run.sh /
COPY ./files/check.sh /

RUN mkdir -p /etc/supervisor/conf.d
COPY ./files/supervisord.conf /etc/supervisor/supervisord.conf

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
