import pygame
import math

from segment import kelp
from segment import kelp_segment

#from kelp.py import kelp

def clear_screen(surface):
    surface.fill((255, 255, 255)) #fills window with white

def main():
    screen_dim_x = 1000 #<--X--->
    screen_dim_y = 500 #up --y--  down  
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

    kelp_new_A = kelp(5,40,[500,450],screen,pygame)

    kelp_new_B = kelp(80,1,[500,450],screen,pygame)
    '''
    kelp_new_B = kelp(22,10,[234,450],screen,pygame)
    kelp_new_C = kelp(22,10,[356,450],screen,pygame)
    kelp_new_D = kelp(22,10,[500,450],screen,pygame)
    kelp_new_E = kelp(22,10,[600,450],screen,pygame)
    kelp_new_F = kelp(22,10,[800,450],screen,pygame)
    kelp_new_G = kelp(22,10,[900,450],screen,pygame)
    kelp_new_H = kelp(22,10,[910,450],screen,pygame)
    kelp_new_I = kelp(22,10,[890,450],screen,pygame)
    kelp_new_J = kelp(22,10,[880,450],screen,pygame)
    kelp_new_K = kelp(22,10,[875,450],screen,pygame)
    kelp_new_L = kelp(22,10,[915,450],screen,pygame)
    kelp_new_M = kelp(22,10,[920,450],screen,pygame)
    kelp_new_N = kelp(22,10,[935,450],screen,pygame)

    kelp_forest = [
        kelp_new_A,
        kelp_new_B,
        kelp_new_C,
        kelp_new_D,
        kelp_new_E,
        kelp_new_F,
        kelp_new_H,
        kelp_new_I,
        kelp_new_J,
        kelp_new_K,
        kelp_new_L,
        kelp_new_M,
        kelp_new_N,
    ]
    '''

    kelp_seg_test_pi = kelp_segment((math.pi),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_2pi = kelp_segment((math.pi*2),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_halfpi = kelp_segment((math.pi*.5),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_zero = kelp_segment((0),40,screen,pygame,None,[300,300],1,1)
    kelp_seg_test_15pi = kelp_segment((math.pi*(1.5)),40,screen,pygame,None,[300,300],1,1)
    counter = 0
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
            mouse_coords = pygame.mouse.get_pos()

            #for kelp_strand in kelp_forest:
            kelp_new_A.render_segments(mouse_coords)

            #kelp_new_B.render_segments(mouse_coords)

            kelp_seg_test_pi.draw_segment("red",8)
            kelp_seg_test_pi.seg_follow_mouse(mouse_coords)

            
 

                
            pygame.display.flip()
  
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
