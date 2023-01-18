import os
import requests
import time
ip_address = "192.168.1.43"
previous_status = ""

while True:
    response = os.system("ping -c 1 " + ip_address)
    time.sleep(20)


    if response != 0:
        if previous_status == "up":
            print("Server sudah down, melakukan request...")
            try:
                r = requests.get("https://api.telegram.org/bot786786482742387462/sendMessage?chat_id=123123123123?disable_notification=true&text=Server 192.168.1.43 down")
                print(r.text)
            except requests.exceptions.RequestException as e:
                print("Request gagal:", e)
            previous_status = "down"
    else:
        previous_status = "up"
        #r = requests.get("https://api.telegram.org/bot5454378564735643765478563874/sendMessage?chat_id=4654646456456456?disable_notification=true&text=Server sudah up")
        print("Server sudah up")
