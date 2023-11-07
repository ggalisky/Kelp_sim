import pygame
import math

from segment import kelp
from segment import kelp_segment

#from kelp.py import kelp

sky_blue = (204,255,255)

def clear_screen(surface):
    blue_ = (0,177,190)
    white = (255,255,255)
    surface.fill(blue_) #fills window with white

def draw_sine_wave(surface, offset, frequency, amplitude,overallY):


    no_pts = surface.get_width()
    saved_yval = 0
    for i in range(no_pts):
        x = (i/no_pts * 2 * math.pi) - offset
        y = (amplitude * math.cos(x * frequency)) + overallY
        if (i == no_pts*(.5)):
            saved_yval = y
        if i > 0:
            pygame.draw.aaline(surface, (0, 0, 0),  prev_pt, (i, y))
            pygame.draw.line(surface,sky_blue,(i,y),(i,0))
        prev_pt = (i, y)

    return saved_yval

def main():
    screen_dim_x = 1700 #<--X--->
    screen_dim_y = screen_dim_x/2 #up --y--  down  
    pygame.init()
    screen = pygame.display.set_mode((screen_dim_x, screen_dim_y)) # creates display window
    screen.fill((255, 255, 255)) #fills window with white
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)


    # choose a desired audio format
    pygame.mixer.init(11025)  # raises exception on fail

    # load the sound
    #sound = pygame.mixer.Sound("Kelp Depths.wav")

    # start playing
    #print("Playing Sound...")
    #channel = sound.play()
  
  
    pygame.display.flip()

    start_x = 700
    start_y = 750
    kelp_new_1 = kelp(2,160,[start_x+0,start_y],screen,pygame)
    kelp_new_2 = kelp(20,15,[start_x+10,start_y],screen,pygame)
    kelp_new_3 = kelp(17,13,[start_x+20,start_y],screen,pygame)
    kelp_new_4 = kelp(18,17,[start_x+30,start_y],screen,pygame)
    kelp_new_5 = kelp(25,10,[start_x+40,start_y],screen,pygame)
    kelp_new_6 = kelp(20,15,[start_x+50,start_y],screen,pygame)
    kelp_new_7 = kelp(17,13,[start_x+60,start_y],screen,pygame)
    kelp_new_8 = kelp(18,17,[start_x+70,start_y],screen,pygame)
    kelp_new_9 = kelp(25,10,[start_x+80,start_y],screen,pygame)
    kelp_new_10 = kelp(20,15,[start_x+90,start_y],screen,pygame)
    kelp_new_11 = kelp(17,13,[start_x+100,start_y],screen,pygame)
    kelp_new_12 = kelp(18,17,[start_x+110,start_y],screen,pygame)
    kelp_new_13 = kelp(25,10,[start_x+120,start_y],screen,pygame)
    kelp_new_14 = kelp(20,15,[start_x+130,start_y],screen,pygame)
    kelp_new_15 = kelp(17,13,[start_x+140,start_y],screen,pygame)
    kelp_new_16 = kelp(18,17,[start_x+150,start_y],screen,pygame)
 

    kelp_group =  [
        kelp_new_1,
        kelp_new_2,
        kelp_new_3,
        kelp_new_4,
    ]
 

    #kelp_seg_test_pi = kelp_segment((math.pi),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_2pi = kelp_segment((math.pi*2),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_halfpi = kelp_segment((math.pi*.5),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_zero = kelp_segment((0),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_15pi = kelp_segment((math.pi*(1.5)),40,screen,pygame,None,[300,300],1,1)
    counter = 0

    offset = 0
    frequency = 2
    amplitude = 20
    overallY = 370

    lobster_x = 300
    lobster_y = 300
    try: #game loop
        while True:
  
            keys = pygame.key.get_pressed()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if keys[pygame.K_p]:
                    while keys[pygame.K_p]:
                        for event in pygame.event.get():
                            keys = pygame.key.get_pressed()
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                quit()
                        #if keys[pygame.K_p]:
                            




            clear_screen(screen)

            #mouse_coords = pygame.mouse.get_pos()
            value = draw_sine_wave(screen,offset,frequency,amplitude,overallY)
            print("value: ", value)
            target_y = ((value*2 - 350))
            target_x = 800 -(value -350) *4

            mouse_coords = [target_x,target_y]

            #for kelp_strand in kelp_forest:
            kelp_new_1.render_segments([mouse_coords[0]+0,mouse_coords[1]])
            kelp_new_2.render_segments([mouse_coords[0]+10,mouse_coords[1]])
            kelp_new_3.render_segments([mouse_coords[0]+20,mouse_coords[1]])
            kelp_new_4.render_segments([mouse_coords[0]+30,mouse_coords[1]])
            kelp_new_5.render_segments([mouse_coords[0]+40,mouse_coords[1]])
            kelp_new_6.render_segments([mouse_coords[0]+50,mouse_coords[1]])
            kelp_new_7.render_segments([mouse_coords[0]+60,mouse_coords[1]])
            kelp_new_8.render_segments([mouse_coords[0]+70,mouse_coords[1]])
            kelp_new_9.render_segments([mouse_coords[0]+80,mouse_coords[1]])
            kelp_new_10.render_segments([mouse_coords[0]+90,mouse_coords[1]])
            kelp_new_11.render_segments([mouse_coords[0]+100,mouse_coords[1]])
            kelp_new_12.render_segments([mouse_coords[0]+110,mouse_coords[1]])
            kelp_new_13.render_segments([mouse_coords[0]+120,mouse_coords[1]])
            kelp_new_14.render_segments([mouse_coords[0]+130,mouse_coords[1]])
            kelp_new_15.render_segments([mouse_coords[0]+140,mouse_coords[1]])
            kelp_new_16.render_segments([mouse_coords[0]+150,mouse_coords[1]])

            

            offset +=.002
            
            if keys[pygame.K_q]:
                frequency+=.01
            elif keys[pygame.K_a]:
                frequency-=.01

            if keys[pygame.K_w]:
                amplitude+=.1
            elif keys[pygame.K_s]:
                amplitude-=.1

            if keys[pygame.K_e]:
                overallY+=1
            elif keys[pygame.K_d]:
                overallY-=1

            if keys[pygame.K_UP]:
                lobster_y -=1
            elif keys[pygame.K_DOWN]:
                lobster_y +=1

            if keys[pygame.K_LEFT]:
                lobster_x -=1
            elif keys[pygame.K_RIGHT]:
                lobster_x +=1
            

            #kelp_new_B.render_segments(mouse_coords)
            kelp_seg_test_pi = kelp_segment((math.pi),40,screen,pygame,None,[lobster_x,lobster_y],1,1)
            kelp_seg_test_pi.draw_segment("red",8)
            #kelp_seg_test_pi.seg_follow_mouse(mouse_coords)

            
 

                
            pygame.display.flip()
  
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
