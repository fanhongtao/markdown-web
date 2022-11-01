# 1 From source

You can run from source code with one limitation, `.md` files must in 'markdown' sub-directory.

## 1.1 Install

Install the required libraries:

```sh
pip3 install -r requirements.txt
```

Or we can use arg `-i` to accelerate the installation.

```sh
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

## 1.2 Run

Start the web by

```sh
python3 web/run.py
```

and visit <http://localhost:5000/basic.md> to see the demo.


# 2 Docker

To show '.md' files in arbitrary directory, we need docker.

## 2.1 Build docker image

```sh
docker build -t markdown-web:latest -f Dockerfile .
```

## 2.2 Run dock container

In any directory where your '.md' files live,

```sh
docker run -it --rm -p 80:8000 -v "$PWD":/site/markdown markdown-web:latest
```
and visit <http://localhost:80> or <http://localhost> .
