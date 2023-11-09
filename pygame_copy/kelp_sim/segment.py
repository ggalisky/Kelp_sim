import math

### constants
kelp_green = (167,230,70)
kelp_green_2 = (190,200,154)


###
class kelp_segment:

    def __init__(self,start_angle,length, surface, pygameobj,parent=None,start_point=None,  angle_recovery_delay =1,joint_stiffness = 1,angle_overshoot = 0, child = None):
        self.start_point = start_point
       
        self.length = length
        self.angle = start_angle
        self.pg = pygameobj
        self.surface = surface
        self.goal_angle = None
        self.angle_recovery_delay = angle_recovery_delay
        self.joint_stiffness = joint_stiffness
        self.angle_overshoot = angle_overshoot
        self.target_group = "UP" #can be up or surface
        self.anchor_segment = True
        self.parent_anchor_coord = None
        self.segment_number = 0
        self.child = child
        
        self.parent = parent
        if parent:
            self.segment_number = parent.segment_number + 1
            self.parent_anchor_coord = parent.parent_anchor_coord
            self.anchor_segment = False
            angle_recovery_reduction_factor = .6
            self.start_point = parent.end_point
            #self.angle_recovery_delay = self.joint_stiffness#(parent.angle_recovery_delay * angle_recovery_reduction_factor )
        else:
            self.parent_anchor_coord = self.start_point
        
        self.end_point = self.calculate_end_point()
        

        '''    Angles 
                 .5 pi
                   |
        pi---------| ------- 0 pi (2pi)
                   |
                 1.5 pi
        '''

    def calculate_end_point(self):
        dx = self.length * math.cos(self.angle) + self.start_point[0]
        dy = self.length * math.sin(self.angle) + self.start_point[1]
        return [dx,dy]

    def draw_segment(self,color,thickness):
        if self.parent:
            pass
            #print("self.angle = ", self.angle)

        self.pg.draw.line(self.surface, color, self.start_point, self.end_point, thickness)
        self.pg.draw.circle(self.surface, color, self.start_point, thickness/2)
        self.pg.draw.circle(self.surface, color, self.end_point, thickness/2)

    def angle_from_dx_dy(self, dx,dy):
        return math.atan2(dy,dx)

    def render_target_point(self, coords):
        self.pg.draw.circle(self.surface,"red", coords, 1)

    def seg_follow_mouse(self, mouse_coords):

        if self.parent:
            self.start_point[0] = self.parent.end_point[0]
            self.start_point[1] = self.parent.end_point[1]
            #print("has parent")
        # figure out location of mouse relative to first start_point
        #print("following..")
        
        dx = mouse_coords[0] - self.start_point[0]
        dy = mouse_coords[1] - self.start_point[1]
        #print("dx:", dx, "dy: ", dy)

        mult = 1
        if dx < self.start_point[0]:
            mult = -1

        new_angle = math.atan2(dy,dx)
        if self.parent:
            pass
            #print("current angle: ", self.angle, "new angle: ", new_angle)
        
        #prevents clockwise segment position correction bias



        self.goal_angle = new_angle #- self.angle_overshoot

        
        delta_angle = self.angle - self.goal_angle
       
        
        value = self.angle - delta_angle *self.joint_stiffness# (delta_angle * self.angle_recovery_delay)* self.joint_stiffness
        #print("updated angle ", value )
        #self.angle -= (delta_angle/.01)

        
        self.angle = value
        #self.angle = new_angle
        
  
            
        #flattens out segments as the reach the surface
        
        if self.angle > math.pi*.5 and self.angle < math.pi:
            #print("default to neg pi")
            self.angle = -math.pi
        elif self.angle > 0 and self.angle < math.pi*.5:
            self.angle = 0
            #print("default to zero")


        
        

        
        #else:
        #    self.angle = new_angle

        self.end_point = self.calculate_end_point()

        # get angle
        # update angle of segment

    
        
    def follow_wave(self, wave_y_coord, wave_amplitude, wave_curve_list,show_targets):
        '''
        follow wave enables a giant kelp piece to follow a wave in a natural looking way. 

        args:
        wave_y_coord: y coordinate of where the wave curve is
        wave_amplitude: float value of what the amplitude of the wave current is

        1. figure out if a segment is the anchor segment
        2. figure out if a 
        '''

        #calculate target point

        final_target_y_offset = -5 #sets how far below the water line kelp will rest

        target_x_sway_coefficient = 1 #sets how far left and right the kelp will sway proportional to the amplitude

        target_x = wave_curve_list.index(wave_y_coord)
        
        #shift X to the right
        target_x = target_x + -wave_amplitude * target_x_sway_coefficient
        
        target_y = wave_curve_list[int(target_x)] #get new y

        #shift start point if applicable
        if not self.anchor_segment:
            # we only need to shift the start points if the segment isn't the anchor segment
            self.start_point[0] = self.parent.end_point[0]
            self.start_point[1] = self.parent.end_point[1]
       
        #determine if segment in in group up or surface

        #if a segments starting Y value is with in segment_surface_gap from the surface, it is group surface
        segment_surface_gap = self.length * 20

        if self.start_point[1] - segment_surface_gap < wave_y_coord:
            self.target_group = "SURFACE"
           
        else:
            self.target_group = "UP"
            
        # get new angle for up
        if self.target_group == "UP":
            target_y -= final_target_y_offset
            dx = target_x - self.start_point[0]
            dy = target_y - self.start_point[1]
            
        elif self.target_group == "SURFACE":
            #shift X target to the right proportionately to the distance between the curve and the segments start point. 
            # The further it is the smaller the shift. the shift maxes out to the length of the segment so the segments begin to fit the curve

            #get distance from start point to curve when looking directly up

            distance_to_curve = self.start_point[1] - wave_y_coord

            target_x = self.start_point[0] + 1.5*self.length 
            target_y = wave_curve_list[int(target_x)]
            target_y -= final_target_y_offset

            dx = target_x - self.start_point[0]
            dy = target_y - self.start_point[1]



        new_angle = self.angle_from_dx_dy(dx,dy)

        self.goal_angle = new_angle #- self.angle_overshoot

        delta_angle = self.angle - self.goal_angle
       
        value = self.angle - delta_angle *self.joint_stiffness# (delta_angle * self.angle_recovery_delay)* self.joint_stiffness
 
        self.angle = value

        self.end_point = self.calculate_end_point()

        if show_targets:
            self.render_target_point((target_x,target_y))
   
class kelp:
    
    def __init__(self,length,num_segments,anchor_coord, screen, pygame_obj):

        self.length = length
        self.anchor_coord = anchor_coord
        self.num_segments = num_segments
        self.segments = []
        print("made it")
        self.segments_lengths = self.generate_segments_lengths(self.length, self.num_segments)
        self.screen = screen
        self.pygame_obj = pygame_obj

        self.generate_segments()

    def generate_segments_lengths(self, length, num_segments):
        segment_length_list =[]

        for x in range(num_segments):
            print("length: " , length)
            segment_length_list.append(length)
        

        return segment_length_list

    def generate_segments(self):

        self.segments.append(kelp_segment((-math.pi*.5),
            self.segments_lengths[0],self.screen,self.pygame_obj,None,self.anchor_coord,1,.01))
        print("len: ", len(self.segments_lengths))
        for x in range(0, int(len(self.segments_lengths))):
            print("len of self.segments: ", str(len(self.segments)))
            self.segments.append(kelp_segment((-math.pi*.5),
            self.segments_lengths[x],self.screen,self.pygame_obj,self.segments[x],None,1,.012))

        for x in range (len(self.segments),0):
            if not x == 0:
                segment = self.segments[x]
                segment.child = self.segments[x-1]

    def render_segments(self, mouse_coords):
        
        for segment in self.segments:
            segment.draw_segment(kelp_green_2, 5)
            segment.seg_follow_mouse(mouse_coords)

    def render_segments_tracking_wave(self, wave_y, wave_amp, wave_list,show_targets):
        
        for segment in self.segments:
            segment.draw_segment(kelp_green_2, 5)
            segment.follow_wave(wave_y,wave_amp,wave_list,show_targets)
        

class kelp_forest:

    def __init__(self,locations,lengths,pg,screen):
        self.locations = locations
        self.lengths = lengths
        self.pg = pg
        self.screen = screen
        self.segment_length = 2
        self.kelp_forest = []
        self.init_kelp_forest()
        
        

    def init_kelp_forest(self):
        for x in range (0,len(self.locations)):
            self.kelp_forest.append(kelp(self.segment_length,self.lengths[x],self.locations[x],self.screen,self.pg))

    def render_kelp_forest(self,wave_amp,wave_list,show_targets):
        for x in self.kelp_forest:
            x.render_segments_tracking_wave(wave_list[x.anchor_coord[0]],wave_amp,wave_list,show_targets)

        

