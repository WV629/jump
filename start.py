# -*- coding:utf-8 -*-

from send import slenium_chrome
# 2. 生成APP
from flask import request, Flask
from selenium_out_url import chrome_driver

app = Flask(__name__)

@app.route('/', methods = ["POST"])
def hello():
    url = request.form.get("url")
    out_utl = slenium_chrome(url, browser)
    return out_utl


if __name__ == '__main__':
    browser = chrome_driver().selenium_out_url()
    app.run(host='0.0.0.0', port=35000, debug=False)

