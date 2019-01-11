
import os


Wanted_WD = "/Users/Stevenson/Desktop/Jana"


os.chdir(Wanted_WD)
os.getcwd()


import pikepdf as pike


pdf = pike.open('input.pdf')
pdf.save('output - Unlocked.pdf')
