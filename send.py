import time


def slenium_chrome(url, browser):
    oraginal_domain = url.split("/")[2].strip('www.')
    start = time.time()
    try:
        browser.get(url)
        time.sleep(2)
        while True:
            out_url = browser.current_url
            out_domain = out_url.split("/")[2].strip('www.')
            page_loaded = browser.execute_script("return document.readyState === 'complete';")
            print(time.time() - start)
            if time.time() - start > 50:
                return ''
            if page_loaded:
                if out_domain in oraginal_domain:
                    time.sleep(1)
                else:
                    return out_url
    except Exception as e:
        return ''