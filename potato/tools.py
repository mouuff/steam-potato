
import urllib.parse
import urllib.request
import json


def request_json(link, values):
        '''Get json file from link
        '''
        request = urllib.parse.urlencode(values)
        url = "{url}?{req}".format(url=link, req=request)
        rep = urllib.request.urlopen(url)
        page = rep.read()
        json_file = json.loads(page.decode('utf-8'))
        return (json_file)
