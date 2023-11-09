import pygame
import math

from segment import kelp
from segment import kelp_segment
from segment import kelp_forest

sky_blue = (204,255,255)
monastery_blue = (0,177,190)
white = (255,255,255)

clock = pygame.time.Clock()

def clear_screen(surface):

    surface.fill(monastery_blue) 

def draw_sine_wave(surface, offset, frequency, amplitude,overallY):

    coords = []

    no_pts = surface.get_width()

    for i in range(no_pts):
        x = (i/no_pts * 2 * math.pi) - offset
        y = (amplitude * math.cos(x * frequency)) + overallY
        if i > 0:
            pygame.draw.aaline(surface, monastery_blue,  prev_pt, (i, y))
            pygame.draw.line(surface,sky_blue,(i,y),(i,0))
        prev_pt = (i, y)
        coords.append(y)
    
    return coords

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
    sound = pygame.mixer.Sound("Kelp Depths.wav")

    # start playing
    #print("Playing Sound...")
    #c hannel = sound.play()
  

    pygame.display.flip()


    locations = [
        (100,700),
        (120,700),
        (150,700),
        (190,700),
        (200,700),
        (210,700),
        (240,700),
        (270,700),
        (290,700),
        (320,700)
    ]

    lengths = [
        160,
        144,
        190,
        112,
        34,
        200,
        167,
        180,
        120,
        130
    ]

    forest_A = kelp_forest(locations,lengths,pygame,screen)

    offset = 0
    frequency = 2
    amplitude = 20
    overallY = 370

    lobster_x = 300
    lobster_y = 300

    counter_amp = 0
    counter_amp_output = 0

    show_targets = False
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

            value = draw_sine_wave(screen,offset,frequency,11* counter_amp_output,overallY)
            wave_cords = value
     
            #kelp_new_test.render_segments_tracking_wave(wave_cords[kelp_new_test.anchor_coord[0]],counter_amp_output*11,wave_cords)

            forest_A.render_kelp_forest(counter_amp_output*11,wave_cords,show_targets)

            offset +=.0005
            
            if keys[pygame.K_q]:
                frequency+=.01
            elif keys[pygame.K_a]:
                frequency-=.01

            if keys[pygame.K_w]:
                amplitude+=.1
            elif keys[pygame.K_s]:
                amplitude-=.1

            if keys[pygame.K_e]:
                overallY+=.1
            elif keys[pygame.K_d]:
                overallY-=.1

            if keys[pygame.K_UP]:
                lobster_y -=1
            elif keys[pygame.K_DOWN]:
                lobster_y +=1

            if keys[pygame.K_LEFT]:
                lobster_x -=1
            elif keys[pygame.K_RIGHT]:
                lobster_x +=1

            if keys[pygame.K_r]:
                show_targets = True
            elif keys[pygame.K_t]:
                show_targets = False

            counter_amp +=.01

            if counter_amp >= 2*math.pi:
                counter_amp = 0

            #print("freq: ", frequency, " amp: ", amplitude, "overally", overallY)

            counter_amp_output = math.sin(counter_amp)
            #print("counter amp output ", counter_amp_output )

            pygame.draw.rect(screen,"grey",pygame.Rect(0, 700, 1700, 1000))
            



            

            
 

                
            pygame.display.flip()

            clock.tick(120)
  
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
