import math

class kelp_segment:

    def __init__(self,start_point,start_angle, length, surface, pygameobj):
        self.start_point = start_point
       
        self.length = length
        self.angle = start_angle
        self.pg = pygameobj
        self.surface = surface
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
        return (dx,dy)

    def draw_segment(self,color,thickness):
        self.pg.draw.line(self.surface, color, self.start_point, self.end_point, thickness)
        self.pg.draw.circle(self.surface, color, self.start_point, thickness/2)
        self.pg.draw.circle(self.surface, color, self.end_point, thickness/2)

    def seg_follow_mouse(self, mouse_coords):
        # figure out location of mouse relative to first start_point
        #print("following..")

        dx = mouse_coords[0] - self.start_point[0]
        dy = mouse_coords[1] - self.start_point[1]

        new_angle = math.atan2(dy,dx)
        self.angle = new_angle
        self.end_point = self.calculate_end_point()

        # get angle
        # update angle of segment
        


        