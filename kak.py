import urllib, os
i = 0
while i <= 33:
    os.system('wget https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture%i.pdf' % i) #used to download file : Lecture2.pdf - Lecture32.pdf
    i = i + 1
