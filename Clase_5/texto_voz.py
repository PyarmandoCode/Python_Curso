import pyttsx3

motor = pyttsx3.init()

while True:
    texto = input("Tu:")
    
    if texto.lower()=="salir":
        motor.say("Hasta Luego")
        motor.runAndWait()
        break
    
    motor.say(texto)
    motor.runAndWait()