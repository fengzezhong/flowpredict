FROM python:3.6-slim-stretch
RUN pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install django -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install requests -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install numpy -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install pandas  -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install datetime  -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install seaborn -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install matplotlib -i https://mirrors.aliyun.com/pypi/simple/

RUN	pip install keras -i https://mirrors.aliyun.com/pypi/simple/&&\	
	pip install sklearn -i https://mirrors.aliyun.com/pypi/simple/&&\
	pip install tqdm -i https://mirrors.aliyun.com/pypi/simple/

RUN	apt-get -y update &&\
	apt-get install -y git &&\
	mkdir /config &&\
	mkdir /src &&\
	cd /src &&\
	git clone https://gitee.com/fengzezhong/flowpredict_web.git

WORKDIR /src
CMD ["python","/src/flowpredict_web/manage.py","runserver","0.0.0.0:12002"]
