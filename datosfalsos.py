import requests
import threading
import string
import secrets

url = ""
num = 50
for x in range(num):
    card = ""
    for i in range(16):
        card += secrets.choice(string.digits)
        card = card.replace(card[0],"4")
        n = 4
        ncard = [card[i:i+n] for i in range(0,len(card), n)]
        ncard = " ".join(ncard)

    dni = ""
    for _ in range(8):
        dni += secrets.choice(string.digits)

    contra = ""
    for _ in range(9):
        contra += secrets.choice(string.digits)    

    data = {
        "password": "",
        "idoc": "",
        "icar": "",
    }
    for k, v in data.items():
        if k == "idoc":
            data[k] = dni

    for k, v in data.items():
        if k == "password":
            data[k] = contra

    for k, v in data.items():
        if k == "icar":
            data[k] = ncard
    print(data)

    def do_request():
        x = 0
        while x < 5:
            response = requests.post(url, data=data)
            print(response)
            x = x + 1

    threads = []

    for i in range(5):
        t = threading.Thread(target=do_request)
        t.deamon = True
        threads.append(t)

    for i in range(5):
        threads[i].start()

    for i in range(5):
        threads[i].join()    
