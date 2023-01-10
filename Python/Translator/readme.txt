PyPi Translator
How to use: 
-In the test.txt file , please write you text in english
-Run the script, with one argument: the desired language for translation

Example:"python translator.py fr"
Give it the argument from the cmd or terminal when running the script!


all languages :https://en.wikipedia.org/wiki/ISO_639-1


Examples of ISO 639-1 codes
Code	ISO 639-1 language name	Endonym
English	French	German
en	English	anglais	Englisch	English
es	Spanish	espagnol	Spanisch	español
pt	Portuguese	portugais	Portugiesisch	português
zh	Chinese	chinois	Chinesisch	中文, Zhōngwén


Output will be in a file called translated text.txt
If you have another paths for the inputed text, please specifi it in the script:

Ex: with open("test.txt", mode="r") as my_file:

Replace here the path of the "test.txt" file with the path of your new file!