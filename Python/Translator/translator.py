from translate import Translator
import sys
import os
import time

try:
    language = str(sys.argv[1])
except IndexError as err:
    print("You did not specify a correct language parameter for the translation. \n")
    print(f"Error : {err} \n")
    print("Rerun the script with the following parameter \n Example: 'python translator.py es' ")

translator = Translator(to_lang=language)

try:
    with open("test.txt", mode="r") as my_file:
        text = my_file.read()
        my_file.close()
        translation = translator.translate(text)
        with open("translated_text.txt", mode='w', encoding='utf-8') as my_file_translated:
            my_file_translated.write(translation)
            my_file_translated.close()
            print("Translation done!")
except FileNotFoundError as err:
    print("check your file path!")


time.sleep(2)
print("\n HELP    ######### RUN IN SHELL: \n")
os.system("translate-cli --help")
