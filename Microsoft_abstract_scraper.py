import http.client, urllib.request, urllib.parse, urllib.error, base64, requests

headers = { # Request headers
    'Ocp-Apim-Subscription-Key': 'a24a9e5734d140f28edb537e22ea9d0a',
}

#defining params to return
params = urllib.parse.urlencode({ # Request parameters
    'expr': "Composite(AA.AuN=='mike smith')",
    'model': 'latest',
    'count': '50',
    'offset': '0',
    'orderby': 'Ti:asc',
    'attributes': 'AA.AuN,Ti,Y,AW'
    
})
#https://academic.microsoft.com/search?q=%22primate%22%20AND%20%22threat%22%20AND%20%22solution%22&f=&orderBy=0&skip=0&take=10
#this is the section that works for microsoft
try:
    conn = http.client.HTTPSConnection('api.labs.cognitive.microsoft.com')
    conn.request("GET", f"/academic/v1.0/evaluate?%s" % params, headers=headers)
    response = conn.getresponse()
    data = response.read()
    print(data) #raw data, can print for debugging
    conn.close()
    
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

