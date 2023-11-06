import math

### constants
kelp_green = (167,230,70)


###
class kelp_segment:

    def __init__(self,start_angle,length, surface, pygameobj,parent=None,start_point=None,  angle_recovery_delay =1,joint_stiffness = 1,angle_overshoot = 0):
        self.start_point = start_point
       
        self.length = length
        self.angle = start_angle
        self.pg = pygameobj
        self.surface = surface
        self.goal_angle = None
        self.angle_recovery_delay = angle_recovery_delay
        self.joint_stiffness = joint_stiffness
        self.angle_overshoot = angle_overshoot
        
        self.parent = parent
        if parent:
            angle_recovery_reduction_factor = .6
            self.start_point = parent.end_point
            #self.angle_recovery_delay = self.joint_stiffness#(parent.angle_recovery_delay * angle_recovery_reduction_factor )
            pass
        
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
            print("self.angle = ", self.angle)
        self.pg.draw.line(self.surface, color, self.start_point, self.end_point, thickness)
        self.pg.draw.circle(self.surface, color, self.start_point, thickness/2)
        self.pg.draw.circle(self.surface, color, self.end_point, thickness/2)

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
            print("current angle: ", self.angle, "new angle: ", new_angle)
        
        #prevents clockwise segment position correction bias



        self.goal_angle = new_angle #- self.angle_overshoot

        
        delta_angle = self.angle - self.goal_angle
       
        
        value = self.angle - delta_angle *self.joint_stiffness# (delta_angle * self.angle_recovery_delay)* self.joint_stiffness
        #print("updated angle ", value )
        #self.angle -= (delta_angle/.01)

        
        self.angle = value
        
  
            
        #flattens out segments as the reach the surface
        if self.angle > math.pi*.5 and self.angle < math.pi:
            print("default to neg pi")
            self.angle = -math.pi
        elif self.angle > 0 and self.angle < math.pi*.5:
            self.angle = 0
            print("default to")
        

        
        #else:
        #    self.angle = new_angle

        self.end_point = self.calculate_end_point()

        # get angle
        # update angle of segment
        


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

        self.segments.append(kelp_segment((math.pi*.5),
            self.segments_lengths[0],self.screen,self.pygame_obj,None,self.anchor_coord,1,.01))
        print("len: ", len(self.segments_lengths))
        for x in range(0, int(len(self.segments_lengths))):
            print("len of self.segments: ", str(len(self.segments)))
            self.segments.append(kelp_segment((math.pi*.5),
            self.segments_lengths[x],self.screen,self.pygame_obj,self.segments[x],None,1,.02))

    def render_segments(self, mouse_coords):
        
        for segment in self.segments:
            segment.draw_segment(kelp_green, 5)
            segment.seg_follow_mouse(mouse_coords)

        




        

