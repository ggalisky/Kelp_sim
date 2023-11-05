import pygame
import math
from kelp import kelp
#from kelp.py import kelp

#####


####

def restore_angle(angle,restore_amt):
    if angle > 0:
        new_angle = angle - restore_amt
        return new_angle
    elif angle == 0:
        return angle
    else:
        new_angle = angle + restore_amt
        return new_angle

def control_arm(A_angle,B_angle,C_angle,pygameobj,movement_distance):

    restore_amt = 0.01
    updated_A_angle = A_angle
    updated_B_angle = B_angle
    updated_C_angle = C_angle
    keys = pygameobj.key.get_pressed()

    if keys[pygameobj.K_a]:
        updated_A_angle += movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    elif keys[pygameobj.K_s]:
        updated_B_angle += movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    elif keys[pygameobj.K_d]:
        updated_C_angle += movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    elif keys[pygameobj.K_q]:
        updated_A_angle -= movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    elif keys[pygameobj.K_w]:
        updated_B_angle -= movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    elif keys[pygameobj.K_e]:
        updated_C_angle -= movement_distance
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    else:
        print("tick"+ str(updated_A_angle))
        updated_A_angle = restore_angle(updated_A_angle,restore_amt)
        updated_B_angle = restore_angle(updated_B_angle,restore_amt)
        updated_C_angle = restore_angle(updated_C_angle,restore_amt)
        return(updated_A_angle,updated_B_angle,updated_C_angle)

    return(updated_A_angle,updated_B_angle,updated_C_angle)

def calculate_B_coord(segment_length, angle, start_coords):
    return (segment_length*math.cos(angle)+start_coords[0],segment_length*math.sin(angle)+start_coords[1])

def display_arm_from_points(A_coord,A_angle,B_angle,C_angle,segment_length, surface, pygame_obj, seg_color):
    surface.fill((255, 255, 255)) #fills window with white
    arm_segment_thickness = 5
    joint_circle_d = 7
    #draw red pivot
    pygame_obj.draw.circle(surface, "red", (250, 250), 15)

    #draw arm segment 1
    #calculate Bcoord
    B_coord = calculate_B_coord(segment_length,A_angle,A_coord)
    pygame_obj.draw.circle(surface, seg_color, A_coord, joint_circle_d)
    pygame_obj.draw.line(surface, seg_color, A_coord, B_coord, arm_segment_thickness)
    #draw arm segment 2
    C_coord = calculate_B_coord(segment_length,B_angle,B_coord)
    pygame_obj.draw.circle(surface, seg_color, B_coord, joint_circle_d)
    pygame_obj.draw.line(surface, seg_color, B_coord, C_coord, arm_segment_thickness)
    #draw arm segment 3
    D_coord = calculate_B_coord(segment_length,C_angle,C_coord)
    pygame_obj.draw.circle(surface, seg_color, C_coord, joint_circle_d)
    pygame_obj.draw.circle(surface, seg_color, D_coord, joint_circle_d)
    pygame_obj.draw.line(surface, seg_color, C_coord, D_coord, arm_segment_thickness)

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
    arm_length = 80
    middle_of_screen = (screen_dim_x/2,screen_dim_y/2)
    A_start = middle_of_screen
    A_angle = 90
    B_angle = A_angle
    C_angle = A_angle

    kelp_color = "green"
    kelp_A_A_seg_length = 80
    kelp_A_A_start = (20,450)
    kelp_A_A_angle = 200
    kelp_A_B_angle = 200
    kelp_A_C_angle = 200

    display_arm_from_points(kelp_A_A_start,kelp_A_A_angle,kelp_A_B_angle,kelp_A_C_angle,kelp_A_A_seg_length,screen,pygame,kelp_color)

    #B, C, D should always be referenced against the state of the A-B segment

    # I need to calculate the next location of the coordinate.

    #how to get distance between two points
    #d=√((x_2-x_1)²+(y_2-y_1)²)
    #x = r cosθ and y = r sinθ.



    display_arm_from_points(A_start,A_angle,B_angle,C_angle,arm_length,screen,pygame,"black")

    kelpA = kelp(300,(45,45),"giant")




    pygame.display.flip()

    #game loop


    try: #game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return



            '''
            angles = control_arm(A_angle,B_angle,C_angle,pygame,0.1)
            A_angle = angles[0]
            B_angle = angles[1]
            C_angle = angles[2]
            display_arm_from_points(A_start,A_angle,B_angle,C_angle,arm_length,screen,pygame,(10,235,10))
            #display_arm_from_points(kelp_A_A_start,kelp_A_A_angle,kelp_A_B_angle,kelp_A_C_angle,kelp_A_A_seg_length,screen,pygame,kelp_color)
            
            '''  
        pygame.display.flip()

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
