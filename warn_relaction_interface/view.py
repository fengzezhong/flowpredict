from django.http import HttpResponse
from . import settings
from .core.warn_realation import file_deal
from .core.flowpredict import predict_flow
from .core import systen_unit as su
import threading
import os
import re
import json
import logging

logger = logging.getLogger('log')


def start(req):
    return HttpResponse(json.dumps({
        "success": True,
        "msg": "心跳检测成功..."
    }))


# 请求告警回应
def warn_realtion(req):
    work_id = su.get_unique_str()

    if req.method == "POST" and req.body != None:

        try:
            down_un = su.download_unit()

            req_para = json.loads(req.body)
            print(req_para)
            warn_data_url = str(req_para["warn_data_url"])
            upload_url = str(req_para["warn_data_url"])
            if su.isURL(warn_data_url):

                save_url = os.path.join(settings.DWON_RESU_URL, work_id + "." + str(warn_data_url).split(".")[-1])
                predict_f = file_deal(settings.UPLOAD_URL, work_id + "." + str(warn_data_url).split(".")[-1], work_id)

                down_thread = threading.Thread(target=down_un.download_file, args=(warn_data_url, save_url, work_id))
                core_thread = threading.Thread(target=predict_f)
                down_thread.start()
                down_thread.join()
                if down_un.get_result():
                    logger.info("[" + work_id + "]:请求成功，任务开始启动")
                    core_thread.start()
                    return HttpResponse(json.dumps({
                        "code": 200,
                        "msg": "Check successed.",
                        "body": {
                            "ret": "4000",
                            "pre_time": str(
                                down_un.get_len() / 4000 + down_un.get_len() / 300000 + down_un.get_len() / 25000),
                            "work_id": work_id,
                            "download_url": upload_url.split("upload")[0] + "download/" + work_id + ".csv",

                        }
                    }))
                else:
                    logger.error("[" + work_id + "]:没有告警文件下载url，或者告警文件url不合法，下载地址为" + str(warn_data_url))
                    return HttpResponse(json.dumps({
                        "code": 201,
                        "msg": "warn file download address error",
                        "body": {
                            "ret": "4003"
                        }
                    }))
            else:
                logger.error("[" + work_id + "]:告警文件下载失败，或者告警文件不符合要求，下载地址为" + str(warn_data_url))
                return HttpResponse(json.dumps({
                    "code": 201,
                    "msg": "warn data download failed",
                    "body": {
                        "ret": "4001"
                    }
                }))
        except Exception as e:
            logger.error("[" + work_id + "]:" + str(e))
            return HttpResponse(json.dumps({
                "code": 500,
                "msg": "unknown exception",
                "body": {
                    "ret": "4002"
                }
            }))
    else:
        return HttpResponse(json.dumps({
            "code": 201,
            "msg": "wrong request type",
            "body": {
                "ret": "4004"
            }
        }))


def get_resu_process(req):
    if req.method == "POST":
        req_para = json.loads(req.body)
        work_id = str(req_para["work_id"])
        resu_file_url = os.path.join(settings.DWON_RESU_URL, work_id + ".csv")
        process_file_url = os.path.join(settings.PROCESS_URL, "process_" + work_id)
        if os.path.exists(resu_file_url):
            return HttpResponse(json.dumps({
                "code": 200,
                "msg": "task complete",
                "body": {
                    "ret": "5000",
                    "process": "100%"
                }
            }))
        else:
            if os.path.exists(process_file_url):
                with open(process_file_url, 'r') as process:
                    lines = process.readlines()
                if len(lines) >= 2:
                    current_process = str(lines[-1]).split("：")[-1].strip()
                    if current_process == "100%":
                        current_process = "98.7%"
                    return HttpResponse(json.dumps({
                        "code": 200,
                        "msg": "task in progress",
                        "body": {
                            "ret": "5000",
                            "process": current_process
                        }
                    }))
                else:
                    return HttpResponse(json.dumps({
                        "code": 200,
                        "msg": "task in progress",
                        "body": {
                            "ret": "5000",
                            "process": "0%"
                        }

                    }))

            else:
                return HttpResponse(json.dumps({
                    "code": 201,
                    "msg": "work err,please upload file again to start task",
                    "body": {
                        "ret": "5001",
                        "process": "0%"
                    }
                }))
    else:
        return HttpResponse(json.dumps({
            "code": 201,
            "msg": "wrong request type",
            "body": {
                "ret": "5002",
                "process": "0%"
            }
        }))


def FileDown(req):
    # if req.method == "POST" and req.POST.get("data", "") != "":
    #     req_para = json.loads(str(req.POST.get("data", "")))
    if req.method == "POST":
        req_para = json.loads(req.body)
        work_id = str(req_para["work_id"])
        file_path = os.path.join(settings.DWON_RESU_URL)
        if work_id + ".csv" in os.listdir(file_path):
            with open(os.path.join(file_path, work_id + ".csv")) as file:
                resp = HttpResponse(file)
                resp['Content-Type'] = 'application/octet-stream'
                resp['Content-Disposition'] = 'attachment;filename="' + work_id + '.csv"'
                return resp
        else:
            return HttpResponse(json.dumps({
                "code": 201,
                "msg": "request err,please use post request",
                "body": {
                    "ret": "6001"
                }
            }))
    else:
        return HttpResponse(json.dumps({
            "code": 201,
            "msg": "request err,please use post request",
            "body": {
                "ret": "6002"
            }
        }))


from django import forms


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


# 处理上传文件
def handle_uploaded_file(f, file_name):
    file_path = os.path.join(settings.UPLOAD_URL)
    print(file_path)
    with open(os.path.join(file_path, file_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


from uuid import uuid4


def FileUp(request):
    if request.method == 'POST':
        myFile = request.FILES.get("warn_file", None)
        if myFile:
            file_name = str(uuid4()) + ".csv"
            handle_uploaded_file(myFile, file_name)
            return HttpResponse(json.dumps({
                "code": 200,
                "msg": "upload success",
                "body": {
                    "file_url": "static/upload/" + file_name,
                    "ret": "6000"
                }
            }))
        else:
            return HttpResponse(json.dumps({
                "code": 201,
                "msg": "file upload fail,please do upload again,make sure use http-post",
                "body": {
                    "file_url": "",
                    "ret": "6001"
                }
            }))

    else:
        pass
    return HttpResponse(json.dumps({
        "code": 201,
        "msg": "file upload fail,please do upload again,make sure use http-post",
        "body": {
            "file_url": "",
            "ret": "6002"
        }
    }))
