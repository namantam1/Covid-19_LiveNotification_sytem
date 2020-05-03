from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "covid19.ico",
        timeout = 5
    )

def getdata(url):
    data = requests.get(url)
    return data.text

# notifyme("hello","This is naman")



if __name__ == "__main__":
    while True:
        html_doc = getdata("https://www.mygov.in/covid-19")
        soup = BeautifulSoup(html_doc, 'html.parser')
        k = soup.tbody.get_text()
        k = (("\n"+k).split("\n\n"))[1:-1]

        datarow = []
        for item in k:
            value = item.split("\n")
            datarow.append(value[1:])

        time1 = time.time()
        index = 0

        while True:
            # print(time.time())
            if time.time() - time1 > 10:
                state = datarow[index][0]
                confirmed = datarow[index][1]
                active = datarow[index][2]
                recovered = datarow[index][3]
                deceased = datarow[index][4]

                title = f"corona case in {state}"
                message = f"confirmed: {confirmed}\nactive: {active}\nrecoverded: {recovered}\ndeceased: {deceased}"

                notifyme(title,message)
                # print(title,"\n"+message)

                time1 = time.time()
                index = index + 1
                
                if index>31:
                    break
