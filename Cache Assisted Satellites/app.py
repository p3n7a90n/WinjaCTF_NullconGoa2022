from flask import Flask, request
import urllib3
import json
from flask_caching import Cache

config = {
    "DEBUG": False,
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": 6379
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/")
def hello():
    return "Welcome to Winja CTF!!!"

# Search for python package CVE from public safety database
@app.route("/searchCVE")
def searchCVE():
    package = request.args.get('package')
    cacheResult = cache.get(package)
    if cacheResult:
        print("Present in cache:{}".format(cacheResult))
        return ' '.join(cacheResult)

    with open("/app/CVEData/insecure_full.json") as __f:
        try:
            INSECURE_FULL = json.loads(__f.read())
        except ValueError as e:
            INSECURE_FULL = []
    CVE=[]
    if INSECURE_FULL and INSECURE_FULL[package]:
        for data in INSECURE_FULL[package]:
            CVE.append(data['cve'])

    cache.set(package,CVE)
    return ' '.join(CVE)


@app.route("/checkStatus")
def checkStatus():
    pool_manager = urllib3.PoolManager(maxsize=10, block=True)
    host = request.args.get('host')
    print(host)
    url = "http://{}/".format(host)
    try:
        resp = pool_manager.request('GET', url)
        print(resp.status)
        return str(resp.status)
    except Exception as error:
        print("Exception Occurred {}".format(error))
        return '500'

