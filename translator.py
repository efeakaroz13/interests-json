#24th of june 2023
#Efe Akaroz


import googletrans
import json 
from googletrans import Translator
from colorama import Fore
import time

translator = Translator()

original = json.loads(open("data/interests.en.json","r").read())
allKeys = list(original.keys())
languages=list(googletrans.LANGUAGES.keys())

for l in languages:
    output = {}
    for key in allKeys:
        currentArray = original[key]
        try:
            keyTranslated = translator.translate(key, dest=l)
        except:
            time.sleep(10)
            try:
                keyTranslated = translator.translate(key, dest=l)
            except:
                continue
                
        output[keyTranslated.text] = []
        for c in currentArray:
            try:
                cTranslated = translator.translate(c, dest=l)
            except:
                time.sleep(10)
                try:
                    cTranslated = translator.translate(c, dest=l)
                except:
                    continue
            print(cTranslated.text)
            output[keyTranslated.text].append(cTranslated.text)
    print(Fore.GREEN,f"{l} successfully completed!",Fore.RESET)
    print("Continuing")
    open("data/interests.{}.json".format(l),"w").write(json.dumps(output,indent=4,ensure_ascii=False))




