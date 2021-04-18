'''-----------------------------------------------------------------'''
'''                                                                 '''
'''                        ASITENTE KRYPTON                         '''
'''             Desarrollado por Marcos Panero Calles               '''
'''                                                                 '''
'''-----------------------------------------------------------------'''


import os                       #CMD
import datetime                 #Fecha y hora actuales

import speech_recognition as sr #Reconocimiento de voz
import pyttsx3                  #Hacer que hable
import pywhatkit                #Comandos WhatsApp y Google
import wikipedia                #Leer wikipedia

flag = True                     #Controlar bucle infinito

'''--------------------------CONFIGURACIÓN ASISTENTE-------------------------------------'''

def decir(text):
    engine = pyttsx3.init() 

    engine.setProperty('rate', 150)     #125 es la velocidad actual con la que habla 
    engine.setProperty('volume', 1.0)       #se puede modificar el volumen entre 0 y 1

    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)   #voices[0] -> español y voices[1] -> inglés

    engine.say(text)
    engine.runAndWait()

def escuchar():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print('[Escuchando...]')
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()        
    except:
        decir("Lo siento, no puedo oirte. Por favor comprueba tu micrófono")
        print("Lo siento, no puedo oirte. Por favor comprueba tu micrófono")
        pass
    return rec    


'''--------------------------FUNCIONES ASISTENTE-------------------------------------'''

def run():
    rec = escuchar()
        
    #Simplemente un poco de conversación
    if  'creador'  in rec:
        print('Mi creador es Marcos Panero')
        decir('Mi creador es Marcos Panero')
        return True

    if  'saluda'  in rec:
        print('Hola a todos, encantada de conoceros')
        decir('Hola a todos, encantada de conoceros')
        return True

    if  'cómo estás'  in rec:
        print('Estoy bien la verdad, aunque una limpieza de polvo a fondo antes de sobrecalentarme no me vendría mal.')
        decir('Estoy bien la verdad, aunque una limpieza de polvo a fondo antes de sobrecalentarme no me vendría mal.')
        return True

    if  'chiste'  in rec:
        print('Si lo que quieres es un bufón mejor llama a Cortana')
        decir('Si lo que quieres es un bufón mejor llama a Cortana')
        return True

    if  'borde'  in rec:
        print('Mi obligación es ayudarte no entretenerte, recuerdalo')
        decir('Mi obligación es ayudarte, no entretenerte, recuerdalo')
        return True

    if  'siri'  in rec:
        print('No me pinches, reirse de los retrasados está feo....')
        decir('No me pinches, reirse de los retrasados está feo....')
        return True
    
    if  'cortana'  in rec:
        print('No encuentro nada sobre ella en mi base de datos, no debe ser muy conocida') #Realmente no la usa nadie jajajaja
        decir('No encuentro nada sobre ella en mi base de datos, no debe ser muy conocida')
        return True

    if  'alexa'  in rec:
        print('¿Por qué debería a opinar sobre alguien que ni me conoce?')
        decir('¿Por qué debería a opinar sobre alguien que ni me conoce?')
        return True

    elif 'eres' in rec:
        print('Soy un asistente virtual creado por Marcos para que saque un 10 en el seminario.')
        decir('Soy un asistente virtual creado por Marcos para que saque un 10 en el seminario.')
        print('Pero mi verdadero propósito es sustituir a esas zorras de Siri y Alexa')
        decir('Pero mi verdadero propósito es sustituir a esas zorras de Siri y Alexa')
        return True

    #Reproduce una canción en Youtube
    elif 'reproduce' in rec:
        musica = rec.replace('reproduce', '')
        print('Reproduciendo' + musica + ' en Youtube')
        decir('Reproduciendo' + musica + ' en Youtube')
        pywhatkit.playonyt(musica)
        return True

    #Busca algo en Google
    elif 'busca' in rec:
        busca = rec.replace('busca', '')
        print('Buscando en Google' + busca)
        decir('Buscando en Google' + busca)
        pywhatkit.search(busca)
        return True

    #Envia un Whatssapp a un contacto
    elif 'envía un mensaje a' in rec:
        print('¿Qué mensaje deseas enviar?')
        decir('¿Qué mensaje deseas enviar?')
        mensaje = escuchar()
        print(mensaje)

        print('¿A quién se lo envío? (Num telefono)')
        decir('¿A quién se lo envío?')
        contacto = input()

        nombre = rec.replace('envía un mensaje a', '')
        print('Enviando mensaje a' + nombre + '...')
        decir('Enviando mensaje a' + nombre + '...')

        tiempo = datetime.datetime.now()
        horas = tiempo.hour
        minutos = tiempo.minute + 1

        pywhatkit.sendwhatmsg(contacto,mensaje,horas,minutos)
        return True
            
    #¿Qué hora es?
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        print('Son las ' + hora)
        decir('Son las ' + hora)
        return True
        
    #Busca un termino en wikipedia
    elif 'qué es' in rec:
        consulta = rec.replace('que es', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(consulta, 1)
        print(info)
        decir(info)
        return True
    
    #Abrir un programa
    elif 'spotify' in rec:
        print('Abriendo Spotify')
        decir('Abriendo Spotify')

        os.system('WHERE /R  c:\\ Spotify.exe > "ruta.txt"')
        f = open ('ruta.txt','r')
        ruta = f.read()

        os.system('start ' + ruta)

        f.close()
        return True

    elif 'word' in rec:
        print('Abriendo Word')
        decir('Abriendo Word')
        os.system('start WINWORD.EXE')
        return True
                
    elif 'excel' in rec:
        print('Abriendo Excel')
        decir('Abriendo Excel')
        os.system('start EXCEL.EXE')
        return True
                
    elif 'power point' in rec:
        print('Abriendo PowerPoint')
        decir('Abriendo PowerPoint')
        os.system('start POWERPNT.EXE')
        return True
                
    elif 'chrome' in rec:
        print('Abriendo Google Chrome')
        decir('Abriendo Google Chrome')
        os.system('start chrome.exe')
        return True

    elif 'discord' in rec:
        print('Abriendo Discord')
        decir('Abriendo discord')
        
        os.system('WHERE /R  c:\\ Discord.exe > "ruta.txt"')
        f = open ('ruta.txt','r')
        ruta = f.read()
        
        os.system('start ' + ruta)
                
        f.close()
        return True

    elif 'calculadora' in rec:
        print('Abriendo Calculadora')
        decir('Abriendo Calculadora')
        os.system('start calc.exe')
        return True
    
    #Consultar el tiempo
    elif 'tiempo en' in rec:
        tiempo = rec.replace('tiempo en', '')
        print('Consultando tiempo en' + tiempo)
        decir('Consultando tiempo en' + tiempo)
        pywhatkit.search('Tiempo en' + tiempo)
        return True

    #Se despide
    elif 'desactívate' in rec:
        print('¡Hasta pronto! Que tengas un buen día')
        decir('¡Hasta pronto!. Que tengas un buen día')
        return False

    #Orden no programada
    else:
        print('No he sido programada para hacer eso. ¿Por qué no agregas esa opción tú mismo?')
        decir('No he sido programada para hacer eso. ¿Por qué no agregas esa opción tú mismo?')
        return True


'''--------------------------EJECUCIÓN ASISTENTE-------------------------------------'''
os.system('cls')
print('Hola soy Krypton, ¿en qué puedo ayudarte?')
decir('Hola soy crípton, ¿en qué puedo ayudarte?')

while flag:
    flag = run()

