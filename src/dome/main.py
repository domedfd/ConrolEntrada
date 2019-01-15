#!/usr/bin/env python

import verificar_master as verMaster
import verificar as veri
import Cad_Master as cadMaster
import cadastrar
import leer
import porta
import display as d

import time

print("Bienvenidos")
d.printi(" Bienvenidos","  DGsistema")
time.sleep(2)
d.limpiar()
d.ip()
d.fecha()
time.sleep(2.5)

try:
	while True:
		idm, master = verMaster.veriMaster()
		if master == "Master":
			print("Pase su tarjeta")
			d.printi("Pase su tarjeta","")
			tarjeta = leer.leer()
		elif master != "Master":
			print("Parece que el sistema es nuevo, por que no se encontro Tarjeta Master")
			d.printi("Sistema nuevo", "pase la Master")
			cadMaster.cadastroMaster()
			tarjeta = 123
			time.sleep(2)

		if tarjeta == idm:
			print("\nTarjeta Master detectada, entrando al modo configuracion\nPorfavor aguarde...")
			d.printi("Entrando modo","Configuracion")
			time.sleep(2)
			cadastrar.cadastrar()
			time.sleep(2)
		elif veri.veriMaster(tarjeta):
			print(veri.veriMaster(tarjeta))
			porta.abrir()
		elif tarjeta == 123:
			print("Nueva Targeja Master Configurada!\n\n")
		else:
			print("Nao esta Cadastrado!")
			d.printi("La TARJETA","NO VALIDA! :(")
			time.sleep(2)
except KeyboardInterrupt:
	print("\nhasta luego!")
