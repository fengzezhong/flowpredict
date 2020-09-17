import requests
import json

res = requests.post('http://127.0.0.1:12012/get_resu_process',
                    data={"work_id": "static/upload/ad854c895401a84cfcb32b1d46922a0b"})
# res = requests.post('http://127.0.0.1:12012/', data={'a': 3, 'b': 4})

print(res.text)
