#Programa: Display LCD I2C com Raspberry Pi
#Autor: Arduino e Cia

import I2C_LCD_driver
import socket
import fcntl
import struct
import time

primero = "Bienvenido"
segundo = ""
lcdi2c = I2C_LCD_driver.lcd()

def limpiar ():
	#Apaga o display
	lcdi2c.lcd_clear()
def printi (pri, seg):
	limpiar()
	#Exibe informacoes iniciais
	lcdi2c.lcd_display_string(pri, 1,1)
	lcdi2c.lcd_display_string(seg, 2,1)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

def ip ():
	#Mostra o endereco IP
	lcdi2c.lcd_display_string("IP:", 1)
	lcdi2c.lcd_display_string(get_ip_address('wlan0'), 1,3)

def fecha ():
	#Mostra a data no display
	lcdi2c.lcd_display_string("Fecha: %s" %time.strftime("%d/%m/%y"), 2,0)


