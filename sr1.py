import sys
import os
import speech_recognition as sr
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
from os import path

input('Please press enter to list langages available\nWarning not all languages are transcribed perfectly!!!')
#In this part we are going to list languages that are supported by Google Speech Recognition

print('Afrikaans (South Africa)	af-ZA')
print('Albanian (Albania)		sq-AL')
print('Amharic (Ethiopia)		am-ET')
print('Arabic (Algeria) 		ar-DZ')
print('Arabic (Bahrain) 		ar-BH')
print('Arabic (Egypt)	        	ar-EG')
print('Arabic (Iraq)    		ar-IQ')
print('Arabic (Israel)	        	ar-IL')
print('Arabic (Jordan)	        	ar-JO')
print('Arabic (Kuwait)	        	ar-KW')
print('Arabic (Lebanon) 		ar-LB')
print('Arabic (Morocco)		ar-MA')
print('Arabic (Oman)			ar-OM')
print('Arabic (Qatar)			ar-QA')
print('Arabic (Saudi Arabia)		ar-SA')
print('Arabic (State of Palestine)	ar-PS')
print('Arabic (Tunisia)		ar-TN')
print('Arabic (United Arab Emirates)	ar-AE')
print('Arabic (Yemen)			ar-YE')
print('Azerbaijani (Azerbaijan)	az-AZ')
print('Basque (Spain)			eu-ES')
print('Bengali (Bangladesh)		bn-BD')
print('Bengali (India)			bn-IN')
print('Bosnian (Bosnia)                bs-BA')
print('Bulgarian (Bulgaria)		bg-BG')
print('Burmese (Myanmar)		my-MM')
print('Catalan (Spain)			ca-ES')
print('Chinese, Cantonese (Traditional Hong Kong)	yue-Hant-HK')
print('Chinese, Mandarin (Simplified, China)	zh (cmn-Hans-CN)')
print('Chinese, Mandarin (Traditional, Taiwan)	zh-TW (cmn-Hant-TW)')
print('Croatian (Croatia)		hr-HR')
print('Czech (Czech Republic)		cs-CZ')
print('Danish (Denmark)		da-DK')
print('Dutch (Belgium)			nl-BE')
print('Dutch (Netherlands)		nl-NL')
print('English (Australia)		en-AU')
print('English (Canada)		en-CA')
print('English (Ghana)			en-GH')
print('English (Hong Kong)		en-HK')
print('English (India)			en-IN')
print('English (Ireland)		en-IE')
print('English (Kenya)	                en-KE')
print('English (New Zealand)		en-NZ')
print('English (Nigeria)		en-NG')
print('English (Pakistan)		en-PK')
print('English (South Africa)		en-ZA')
print('English (United Kingdom)        en-GB')
print('English (United States)		en-US')
print('Estonian (Estonia)		et-EE')
print('Filipino (Philippines)		fil-PH')
print('Finnish (Finland)		fi-FI')
print('French (Belgium)		fr-BE')
print('French (Canada)			fr-CA')
print('French (France)			fr-FR')
print('French (Switzerland)		fr-CH')
print('Galician (Spain)		gl-ES')
print('Georgian (Georgia)		ka-GE')
print('Greek (Greece)			el-GR')
print('German (Germany)		de-DE')
print('Gujarati (India)		gu-IN')
print('Hungarian (Hungary)		hu-HU')
print('Icelandic (Iceland)		is-IS')
print('Indonesian (Indonesia)		id-ID')
print('Italian (Italy)			it-IT')
print('Japanese (Japan)		ja-JP')
print('Korean (South Korea)		ko-KR')
print('Lao (Laos)			lo-LA')
print('Latvian (Latvia)		lv-LV')
print('Lithuanian (Lithuania)		lt-LT')
print('Mongolian (Mongolia)		mn-MN')
print('Norwegian Bokmål (Norway)	no-NO')
print('Persian (Iran)			fa-IR')
print('Portuguese (Brazil)		pt-BR')
print('Polish (Poland)			pl-PL')
print('Portuguese (Portugal)		pt-PT')
print('Romanian (Romania)		ro-RO')
print('Russian (Russia)		ru-RU')
print('Serbian (Serbia)		sr-RS')
print('Sinhala (Sri Lanka)		si-LK')
print('Slovak (Slovakia)		sk-SK')
print('Spanish (Argentina)		es-AR')
print('Spanish (Bolivia)		es-BO')
print('Spanish (Chile)			es-CL')
print('Spanish (Mexico)		es-MX')
print('Spanish (United States)		es-US')
print('Sundanese (Indonesia)		su-ID')
print('Swahili (Tanzania)		sw-TZ')
print('Swedish (Sweden)		sv-SE')
print('Tamil (India)			ta-IN')
print('Tamil (Malaysia)		ta-MY')
print('Thai (Thailand)			th-TH')
print('Turkish (Turkey)		tr-TR')
print('Uzbek (Uzbekistan)		uz-UZ')
print('Vietnamese (Vietnam)		vi-VN')
print('Zulu (South Africa)		zu-ZA')
lang = input('Please enter language you want to transcribe(For example az-AZ):')

#opening a dialog to choose a file
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(filetypes=[("Audio files" , ".wav .aiff .flac")])


print('The file you have seleted is located at' + file_path)
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300

#this is where magic starts
with sr.AudioFile(file_path) as source:
    audio = recognizer.listen(source)
    print('Working on it, wait a minute please...')
    try:
        text = recognizer.recognize_google(audio, language=lang)

        text_file = open("transcribed.doc", "w") #this part creates a doc file in which transcribed text is written 
        n = text_file.write(text)
        text_file.close()
    except:
        print('Sorry, something went wrong...') #if speech is not recognizable it will throw this exception preventing program get into traceback



input("Please, press any key to exit...")
