from send import slenium_chrome
from flask import request, Flask
from selenium_out_url import chrome_driver
from threading import Lock

app = Flask(__name__)
lock = Lock()
concurrent_requests = 0

@app.route('/', methods=["POST"])
def hello():
    global concurrent_requests

    with lock:
        if concurrent_requests >= 5:
            return "wait"
        concurrent_requests += 1

    browser = chrome_driver().selenium_out_url()
    url = request.form.get("url")
    out_utl = slenium_chrome(url, browser)

    with lock:
        concurrent_requests -= 1

    return out_utl

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=35000, debug=False)
