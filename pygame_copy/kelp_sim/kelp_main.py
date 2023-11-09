import pygame
import math

from segment import kelp
from segment import kelp_segment
from segment import kelp_forest

sky_blue = (204,255,255)
monastery_blue = (0,177,190)
white = (255,255,255)

#clock = pygame.time.Clock()

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
    print("Playing Sound...")
    channel = sound.play()
  

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
        (320,700),

        (400,700),
        (425,700),
        (432,700),

        (500,700),
        (550,700),
        (623,700),
        (650,700),
        (700,700),
        (800,700),
        (850,700),
        (900,700),

        (1000,700),
        (1100,700),
        (1200,700),
        (1300,700),
        (1400,700),
    
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
        130,

        140,
        120,
        90,
        45,
        200,
        215,
        145,
        160,
        20,
        10,
        176,


        200,
        200,
        200,
        200,
        200,

    ]

    print("len lenghts; ", len(lengths), "len locations, ", len(locations))

    forest_A = kelp_forest(locations,lengths,pygame,screen)

    offset = 0
    frequency = 2
    amplitude = 20
    overallY = 370

    lobster_x = 300
    lobster_y = 300

    counter_amp = 0
    counter_amp_output = 0

    wave_offset_loop_inc = .0005

    amp_mult = 1

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

            wave_cords = draw_sine_wave(screen,offset,frequency,11* counter_amp_output,overallY)
     
            #kelp_new_test.render_segments_tracking_wave(wave_cords[kelp_new_test.anchor_coord[0]],counter_amp_output*11,wave_cords)

            forest_A.render_kelp_forest(overallY,wave_cords,show_targets,counter_amp_output*11)

            y_value = wave_cords[300]

            #print("overall Y, ", overallY, " local y,", y_value, "delta: ", overallY-y_value)
    
            #print("freq: ", frequency, " amp: ", amplitude, "overally", overallY)

            offset += wave_offset_loop_inc
            
            if keys[pygame.K_q]:
                frequency+=.01
            elif keys[pygame.K_a]:
                frequency-=.01

            if keys[pygame.K_w]:
                amp_mult+=.1
            elif keys[pygame.K_s]:
                amp_mult-=.1

            if keys[pygame.K_e]:
                overallY+=1
            elif keys[pygame.K_d]:
                overallY-=1

            if keys[pygame.K_z]:
                wave_offset_loop_inc+=.0001
            elif keys[pygame.K_x]:
                wave_offset_loop_inc-=.0001

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



            counter_amp_output = math.sin(counter_amp)*amp_mult
            #print("counter amp output ", counter_amp_output )

            pygame.draw.rect(screen,"grey",pygame.Rect(0, 700, 1700, 1000))
            



            

            
 

                
            pygame.display.flip()

            #clock.tick(120)
  
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
