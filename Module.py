from Numbers_in_words import *

if(len(num)==4):
    thousand(num)
elif(len(num)==3):
    hundred(num)
elif(len(num)==2):
    tens(num)
elif(len(num)==1):
    last(num)
