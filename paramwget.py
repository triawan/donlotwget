import urllib, os
i = 0
while i <= 21:
    os.system('wget http://paper.ijcsns.org/07_book/201407/201407%02i.pdf' % i) #untuk download file 20140701.pdf - 20140721.pdf
    i = i + 1
