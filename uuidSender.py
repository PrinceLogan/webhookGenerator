import uuid
import sys
import json
import requests
import time

uuid_1 = str(uuid.uuid4())
uuid_2 = str(uuid.uuid4())
uuid_3 = str(uuid.uuid4())

url = sys.argv[2]
wait = int(sys.argv[3])
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
list_1 = [uuid_1, uuid_2, uuid_3]

for shark in list_1:
    arg_1 = sys.argv[1]
    x = {
      "uuid": '',
      "source": ''
    }
    x["uuid"] = shark
    x["source"] = arg_1

    y = json.dumps(x)

    r = requests.post(url, data=json.dumps(y), headers=headers)
    time.sleep(wait)

