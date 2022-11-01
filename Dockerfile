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
# Install required packages
    && pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

VOLUME /site/markdown

COPY web /site/web/
COPY docker/gunicorn.cfg.py /site/web/
WORKDIR /site/web

EXPOSE 8000

CMD ["gunicorn", "-c", "gunicorn.cfg.py", "run:app"]
