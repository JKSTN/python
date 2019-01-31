
import os


Wanted_WD = "~"


os.chdir(Wanted_WD)
os.getcwd()


import pikepdf as pike

input = "example"

pdf = pike.open(str(input) + '.pdf')
pdf.save(str(input) + ' - Unlocked.pdf')
