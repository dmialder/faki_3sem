import urllib.request
import threading
import time

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def thread_job(i, url):
    read_url(url)


def run_threads(urls):
    threads = [
        threading.Thread(target=thread_job, args=(i, urls[i]))
        for i in range(len(urls))
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


start = time.time()

run_threads(urls)

print(time.time() - start)


#time with no threading = 3.7562944889068604
#time with threading = 1.1933693885803223