import pygame
import time
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import io
import webbrowser
import socket
import os
import sys
from subprocess import Popen,PIPE

time.sleep(10)

movie1 = ("/media/pi/LINK/video1.mp4")

URL_open = False

pygame.init()
gameDisplay = pygame.display.set_mode((1024,720),pygame.FULLSCREEN)
clock = pygame.time.Clock()
back = pygame.image.load('/media/pi/LINK/background.png')
gameDisplay.blit(back,(0,0))

file = open('/media/pi/LINK/link_rtmp.txt')
for line in file:
    LINK = line.rstrip()

file2 = open('/media/pi/LINK/link_http.txt')
for line2 in file2:
    LINK2 = line2.rstrip()


def internetCheck():
    try:
        urlopen(LINK2, timeout=1)
        return True
    except URLError as err:
        return False
    except HTTPError as err:
        return False
    except socket.timeout:
        return False
    except socket.error:
        return False
  
player = False

while(True):
    internetConnection = internetCheck()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            os.system('killall omxplayer.bin')
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
    print(internetConnection)
   # k = cv.waitKey(1)
    if internetConnection == False and player == False:
        myprocess = Popen(['omxplayer','-b','/media/pi/LINK/video.mp4'],stdin=PIPE)
        #os.system('omxplayer /media/pi/LINK/video.mp4')
        player = True
    elif internetConnection == True:
        #CLOSE VIDEO
        try:
            os.system('killall omxplayer.bin')
            player = False
        except:
            pass
        os.system("omxplayer "+LINK)
