import qrcode

texto = "https://www.youtube.com/@ArmandoRuizTech"

imagen = qrcode.make(texto) #genera el QR

imagen.save("mi_qr.png") #guarda la imagen

print("Codigo QR generado correctamente")
