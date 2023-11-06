import math


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
        self.pg.draw.line(self.surface, color, self.start_point, self.end_point, thickness)
        self.pg.draw.circle(self.surface, color, self.start_point, thickness/2)
        self.pg.draw.circle(self.surface, color, self.end_point, thickness/2)

    def seg_follow_mouse(self, mouse_coords):

        if self.parent:
            self.start_point[0] = self.parent.end_point[0]
            self.start_point[1] = self.parent.end_point[1]
        # figure out location of mouse relative to first start_point
        #print("following..")

        dx = mouse_coords[0] - self.start_point[0]
        dy = mouse_coords[1] - self.start_point[1]

        new_angle = math.atan2(dy,dx)
        self.goal_angle = new_angle #- self.angle_overshoot

        #if self.parent:
        delta_angle = self.angle - self.goal_angle
        #print("self.angle: ", self.angle, "self.goal_angel", self.goal_angle, "delta angle", delta_angle)
        value = self.angle - delta_angle *self.joint_stiffness# (delta_angle * self.angle_recovery_delay)* self.joint_stiffness
        #print("updated angle ", value )
        #self.angle -= (delta_angle/.01)
        self.angle = value
        #else:
        #    self.angle = new_angle

        self.end_point = self.calculate_end_point()

        # get angle
        # update angle of segment
        


        