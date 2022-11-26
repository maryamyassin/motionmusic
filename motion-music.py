from gpiozero import LEDBoard
from gpiozero import MotionSensor
import pygame
import time

pir = MotionSensor(4)
leds = LEDBoard(5, 17, 22) #red, green, yellow

pygame.mixer.init()
speaker_volume = 0.2
pygame.mixer.music.set_volume(speaker_volume)
pygame.mixer.music.load("Lazy-Day.mp3")
print("loaded music file!")
music = "OFF"

    
def unpausemusic():

    global music
    music = "UNPAUSED"
    pir.wait_for_motion()
    pygame.mixer.music.unpause()
    leds[0].off()
    leds[1].on()
    leds[2].off()
    
    print("motion detected again!")  
    
    while music == "UNPAUSED":
        
        time.sleep(3)
        pir.wait_for_motion(2)
    
        if (pir.motion_detected == True):
            continue
            
        else:
            pausemusic()
            break
                  
        
def pausemusic():
    
    global music
    music = "PAUSED"
    pir.wait_for_no_motion()
    pygame.mixer.music.pause()
    
    leds[1].off()
    leds[2].blink()
    leds[0].on()
    
    print("motion stopped")
    time.sleep(3)
    
    while music == "PAUSED":
        
        pir.wait_for_motion(2)
    
        if (pir.motion_detected == False):
            continue
            
        else:
            unpausemusic()
            break
        
    
def playmusic():
    
    global music
    music = "ON"
    print("Motion detected!")
    pygame.mixer.music.play()
    leds[1].on()
    time.sleep(3)
    
    while music == "ON":
        
        time.sleep(3)
        pir.wait_for_motion(2)
    
        if (pir.motion_detected == True):
            continue
            
            
        else:
            pausemusic()
            break
        
        
def start():
    
    global music
    
    while music == "OFF":
        
        pir.wait_for_motion(2)
    
        if (pir.motion_detected == True):
            playmusic()
            break
            
        else:
            print("no motion detected even after 10 seconds")
            continue
      
         
while True:

    try:
        
        start()
        

        
    except:
        
        KeyboardInterrupt
        leds.off()
        pygame.mixer.music.stop()
        
            
