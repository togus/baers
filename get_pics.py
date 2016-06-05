from slacker import Slacker
import sys
import shutil
import requests
import time

if len(sys.argv) < 2:
    sys.exit(0)

slack = Slacker(sys.argv[1])

#encoded baers channel
CHANNEL = u'C1E8T4FLZ'
#get the timestamp for 5 min ago
TIMESTAMP = int(time.time())-300
#add auth token to requests
HEADERS = {"Authorization": "Bearer " + sys.argv[1]}

x = slack.files.list(types="images", ts_from=TIMESTAMP)

for i in  x.body['files']:
    if CHANNEL in i['channels']:
        print i['url_private_download']
        name = i['url_private_download'].rsplit('/', 1)[-1]
        response = requests.get(i['url_private_download'], headers=HEADERS, stream=True)
        with open('images/'+name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)

