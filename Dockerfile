# Build dock image:
#    docker build -t markdown-web:latest -f Dockerfile .
#
# In your MarkDown files directory, run dock container:
#    docker run -it --rm -p 80:8000 -v "$PWD":/site/markdown markdown-web:latest
# In browser, visit:
#    http://localhost

FROM python:3.11-alpine

LABEL maintainer="Fan Hongtao <fanhongtao@163.com>"

COPY requirements.txt ./

RUN set -eux \
# Switch mirrors for Alpine
    && cp /etc/apk/repositories /etc/apk/repositories.bak \
    && echo "http://mirrors.aliyun.com/alpine/v3.12/main/" > /etc/apk/repositories \
# Install gcc
    && apk add --no-cache --virtual .run-deps \
            icu-libs \
    && apk add --no-cache --virtual .build-deps \
            cmake \
            g++ \
            gcc \
            icu-dev \
            libc-dev \
            make \
# Install required packages
    && pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/ \
# Delete unnecessary packages
    && apk del .build-deps

VOLUME /site/markdown

COPY web /site/web/
COPY docker/gunicorn.cfg.py /site/web/
WORKDIR /site/web

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.cfg.py", "run:app"]
