import pygame.gfxdraw
import cv2

def get_list_from_bitmap(bitmap_path):
    img = cv2.imread(bitmap_path, 0)
    _, bit_map_list = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)
    return bit_map_list.tolist()

def draw_map (surface, color ,map_data, pos, pixel_size):
    x_coord = pos[0]
    y_coord = pos[1]
    coords = [x_coord,y_coord]

    for x in map_data:
        y_coord = pos[1]
        for y in x:
            #print("x: " + str(x_coord) + ", y: " + str(y_coord))

            if y == 0:
                draw_rect_filled(surface,color, (y_coord,x_coord),(pixel_size,pixel_size))
                #print("painted pixel!")

            y_coord+= pixel_size
        x_coord += pixel_size

def draw_single_pixel(surface, color, pos):
    surface.fill(color, (pos, (1, 1)))

def draw_rect_filled(surface, color, pos, size):
    surface.fill(color, (pos, size))

def find_spawn_point(map_data,map_origin):

    for x in range(1,len(map_data)):

        for y in range(1,len(map_data[x])):
            if map_data[x][y] == 1:
                print("found spawn, x: " + str(x) + ", y: " + str(y))
                return (x,y)

def draw_player(coords, pixel_magnfication,surface):
    draw_rect_filled(surface,"red",coords,(pixel_magnfication,pixel_magnfication))

def update_player_pos(current_pos,new_pos,surface,pixel_mag):
    draw_rect_filled(surface,"white",current_pos,(pixel_mag,pixel_mag))
    draw_rect_filled(surface,"red",new_pos,(pixel_mag,pixel_mag))

def check_player_collision(potential_pos,map_data):
    print("checking collision with, X: "+str(potential_pos))
    if map_data[potential_pos[1]][potential_pos[0]] == 0:
        print("COLLISION DETECTED")
        return True

def check_user_control_of_player(current_pos,current_pos_relative,pygameobj,movement_distance,surface, event,map_data):
    new_pos_r = current_pos
    new_pos_relative_r = current_pos_relative

    keys = pygameobj.key.get_pressed()

    if keys[pygameobj.K_DOWN]:
        new_pos = (current_pos[0],current_pos[1]+movement_distance)
        new_pos_relative = (current_pos_relative[0],current_pos_relative[1] + 1)
        if not check_player_collision(new_pos_relative,map_data):
            print("up")
            print("relative pos: " +str(new_pos_relative))
            update_player_pos(current_pos,new_pos,surface,movement_distance)
            return (new_pos,new_pos_relative)
    elif keys[pygameobj.K_UP]:
        new_pos = (current_pos[0],current_pos[1]-movement_distance)
        new_pos_relative = (current_pos_relative[0],current_pos_relative[1] - 1)
        if not check_player_collision(new_pos_relative,map_data):
            print("moved down")
            print("relative pos: " +str(new_pos_relative))
            update_player_pos(current_pos,new_pos,surface,movement_distance)
            return (new_pos,new_pos_relative)
    elif keys[pygameobj.K_LEFT]:
        new_pos = (current_pos[0]-movement_distance,current_pos[1])
        new_pos_relative = (current_pos_relative[0] - 1,current_pos_relative[1])
        if not check_player_collision(new_pos_relative,map_data):
            print("left")
            update_player_pos(current_pos,new_pos,surface,movement_distance)
            return (new_pos,new_pos_relative)
    elif keys[pygameobj.K_RIGHT]:
        new_pos = (current_pos[0]+movement_distance,current_pos[1])
        new_pos_relative = (current_pos_relative[0]+1,current_pos_relative[1])
        if not check_player_collision(new_pos_relative,map_data):
            print("right")
            print("relative pos: " +str(new_pos_relative))
            update_player_pos(current_pos,new_pos,surface,movement_distance)
            return (new_pos,new_pos_relative)


    return  (new_pos_r,new_pos_relative_r)
