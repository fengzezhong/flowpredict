from . import view
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', view.start),
    url(r'healthcheck.do', view.start),  # 检查心跳
    url(r'get_flow', view.get_predict_flow),  # 获取流量
    url(r'get_resu_process', view.get_resu_process),  # 获取/恢复过程
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}), #查询文件
    url(r'get_download_resu', view.FileDown),  # 获取下载结果
    url(r'upload_file', view.FileUp),  # 上传文件
    url(r'remove_files', view.RemoveFile),  # 上传文件
]
