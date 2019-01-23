
import os


Wanted_WD = "/Users/Stevenson/Desktop"


os.chdir(Wanted_WD)
os.getcwd()


import pikepdf as pike

input = "12-31-2018_-_Risk_Reports"

pdf = pike.open(str(input) + '.pdf')
pdf.save(str(input) + ' - Unlocked.pdf')
