import os
from flask import Flask, redirect
import random
import requests

app = Flask(__name__)


@app.route('/rando')
def get():
    rando = [
        "https://i.ibb.co/7yrW3Yg/1-D586-F4-A-DBDF-4221-99-E5-35-B6-C5-FDF0-EF.jpg",
        "https://i.ibb.co/JvmnmXW/60661557-5610-4335-A865-A6-E1-CAE4716-E.jpg",
        "https://i.ibb.co/52D6LZ7/69851-B74-6635-42-CA-A730-AD4688-B3-A139.jpg",
        "https://i.ibb.co/Wv3BMRk/59509-F79-CE80-439-F-BFD0-80-D5-BFA59-A8-D.jpg",
        "https://i.ibb.co/6vSk9Lp/B9-C1-C218-3-B0-D-4-AB5-AB3-C-99-E0-A704-A810.jpg",
        "https://i.ibb.co/NLBrGhY/3-ED2-BCF9-3738-49-B0-9-D92-CB0-B4-A36-F377.jpg",
        "https://i.ibb.co/GtSn42X/6-F7-DD1-C0-4-C7-F-45-AF-B7-D4-269-E45-E63614.jpg",
        "https://i.ibb.co/DWzBmHQ/8-CF656-A2-E377-48-B5-B7-C0-2-E414-A40-CABB.jpg",
        "https://i.ibb.co/v33jC96/F8871-F27-3-A5-A-4-D55-9-E85-E4-CAC415492-B.jpg",
    ]
    random_rando = random.choice(rando)
    url = "https://chat.ipnet.co.id/hooks/wygxi9efdtdo3nftay3jryk6gr"
    payload = "{\n    \"text\": \"%s\"\n}" % random_rando
    headers = {
        'Content-Type': "application/json",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "chat.ipnet.co.id",
        'accept-encoding': "gzip, deflate",
        'content-length': "90",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.text, "Rando succesfully generated"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 15000))
    app.run(host='0.0.0.0', port=port)
