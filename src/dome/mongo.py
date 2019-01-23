#!/var/bin/env python

import requests

def update (codigo):
	url = "http://172.16.0.14:3000/tarjetas"

	payload = "codigo=" + str(codigo) + "&cliente=%20Tarjeta%20Nueva&perfil=0&contador=0.00&undefined="
	headers = {
	    'Content-Type': "application/x-www-form-urlencoded",
	    'cache-control': "no-cache",
	    'Postman-Token': "88b74c11-97dd-41d6-ada6-74a0e00831f2"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)
	return
