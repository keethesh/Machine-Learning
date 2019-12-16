import datetime
import multiprocessing

from selenium import webdriver
from queue import Queue
from multiprocessing import Pool
import time


def daterange(date1, date2):
    for n in range(int((date2 - date1).days) + 1):
        yield date1 + datetime.timedelta(n)


dates = []
start_date = datetime.date(2015, 12, 5)
# Data as from 5 december 2015
end_date = datetime.date.today()

months = ["Jan", "Fév", "Mars", "Avr", "mai", "Juin", "Jui", "Août", "Sep", "Oct", "Nov", "Dec"]
for dt in daterange(start_date, end_date):
    if dt.weekday() == 2 or dt.weekday() == 5:
        dt = str(dt).split('-')
        dt[0], dt[1], dt[2] = dt[2], dt[1], dt[0]
        month = dt[1]
        dt[1] = months[int(dt[1]) - 1]
        dates.append(dt)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
driver = webdriver.Chrome(options=chrome_options)


def get_data(date_from):
    url = (
            "https://www.loterienationale.mu/fr/tirages-et-archives?field_date_du_tirage_value%5Bvalue%5D%5Bdate%5D=" +
            date_from[0] + "+" + date_from[1] + "+" + date_from[2])
    driver.get(url)
    try:
        for a in range(1, 7):
            element = driver.find_element_by_xpath("//*[@id=\"num-gagnants\"]/span[" + str(a) + "]")
            num = element.text
            # lock.acquire()
            lottery_nums[-1].o
            lottery_nums.append(num)
            # lock.release()
            print(lottery_nums)
    except:
        print("Error")
        return


# def init(l):
#     global lock
#     lock = l


if __name__ == '__main__':
    start_time = time.time()
    manager = multiprocessing.Manager()
    lottery_nums = manager.list()
    print("c", lottery_nums)
    # l = multiprocessing.Lock()
    # pool = Pool(processes=7, initializer=init, initargs=(l,))
    pool = Pool(processes=7)
    pool.map(get_data, dates)  # process data_inputs iterable with pool
    pool.close()
    pool.join()
    # lottery_numbers = list(filter(None, lottery_numbers))
    print("--- %s seconds ---" % (time.time() - start_time))
# for i in range(1,41):
