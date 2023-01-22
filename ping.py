import os

status = "down"

while True:
    response = os.system("ping -c 1 192.168.1.43")
    if response == 0:
        if status == "down":
            print("Up")
            r = requests.get("https://api.telegram.org/bot786786482742387462/sendMessage?chat_id=123123123123?disable_notification=true&text=Server 192.168.1.43 down")
            status = "up"
    else:
        if status == "up":
            print("Down")
            r = requests.get("https://api.telegram.org/bot786786482742387462/sendMessage?chat_id=123123123123?disable_notification=true&text=Server 192.168.1.43 down")
            status = "down"
    time.sleep(1)
