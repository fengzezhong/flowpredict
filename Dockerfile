FROM python:3.6-slim-stretch
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install django -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install requests -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install numpy -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install pandas  -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install datetime  -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install seaborn -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install matplotlib -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install keras -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install sklearn -i https://mirrors.aliyun.com/pypi/simple/&&\
        pip install tqdm -i https://mirrors.aliyun.com/pypi/simple/

RUN echo 'deb http://mirrors.aliyun.com/debian/ stretch main non-free contrib \
    deb-src http://mirrors.aliyun.com/debian/ stretch main non-free contrib \
    deb http://mirrors.aliyun.com/debian-security stretch/updates main \
    deb-src http://mirrors.aliyun.com/debian-security stretch/updates main \
    deb http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib \
    deb-src http://mirrors.aliyun.com/debian/ stretch-updates main non-free contrib \
    deb http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib \
    deb-src http://mirrors.aliyun.com/debian/ stretch-backports main non-free contrib' > /etc/apt/sources.list

RUN apt-get -y update &&\
    apt-get install -y git

RUN mkdir /config &&\
    mkdir /src &&\
    cd /src &&\
    git clone  https://github.com/fengzezhong/flowpredict.git

WORKDIR /src
CMD ["python","/src/flowpredict/manage.py","runserver","0.0.0.0:12012"]