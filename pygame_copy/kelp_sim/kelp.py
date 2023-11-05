class kelp:

    def __init__(self, length, anchor_location, kelp_type):
        
        self.length = int(length)
        self.anchor_coords = anchor_location
        self.joint_angles = []
        self.joint_coords = []
        self.num_points = 0
        self.type = kelp_type #bull kelp vs giant kelp
        self.num_segments = self.get_num_segments(self.length,self.anchor_coords)

    def get_c_seg(self,default_segment_length, decrement,section_C_length):
        num_C_segments = 0
        for x in range(100):
            if(section_C_length < 0):
                return num_C_segments
            else:
                section_C_length = section_C_length - default_segment_length - (x* decrement)
                num_C_segments +=1
        return num_C_segments

    def get_num_segments(self, length, anchor):
        #|--------A SECTION --------|------B-------|-------C-----|         
        #anchor------------------HALFWAY-----------3/4----------TIP
        #all segments in A are equal length, same for B, C are progressively smaller

        default_joint_angle = 3.14
        self.joint_coords.append(anchor)
        self.joint_angles.append(default_joint_angle)
        section_A_default_segment_length = 20
        section_B_default_segment_length = 15
        section_C_default_segment_length = 15
        section_C_decrement = 1
        section_C_decrement_extra = .3

        section_A_length = int(length/2)
        section_B_length = int(length/4)
        section_C_length = int(length/4)
        #print("sectionAL: ", section_A_length,"sectionBL: ", section_B_length, "sectionCL: ", section_C_length)

        num_A_segments = int(section_A_length/section_A_default_segment_length)
        num_B_segments = int(section_B_length/section_B_default_segment_length)

        num_C_segments = self.get_c_seg(section_C_default_segment_length, section_C_decrement,section_C_length)
        

        x_coord = anchor[0]
        y_coord = anchor[1]
        #generate joint coords and angles for A section

        print("A segments: ", num_A_segments, "b seg: ", num_B_segments, "Cseg: ", num_C_segments)
        for x in range(1,num_A_segments):
            self.joint_coords.append( (x_coord,y_coord - (x*section_A_default_segment_length) ) )
            self.joint_angles.append(default_joint_angle)

        b_start = self.joint_coords[len(self.joint_angles)-1][1]

        #print("b_start: " , b_start)

        for x in range(0,num_B_segments):
            self.joint_coords.append( (x_coord, b_start - (x*section_B_default_segment_length)) )
            self.joint_angles.append(default_joint_angle)

        c_start = self.joint_coords[len(self.joint_angles)-1][1]
        for x in range(0,num_C_segments):
            self.joint_coords.append( (x_coord,+ c_start - (x*section_C_default_segment_length - (x *section_C_decrement))))
            self.joint_angles.append(default_joint_angle)
            section_C_decrement += section_C_decrement_extra

        
        for x in range(len(self.joint_coords)):
            print("coords: ", str(self.joint_coords[x]), " angles: ", str(self.joint_angles[x]))
        print ("len coords: ", len(self.joint_coords), " len angles: ", len(self.joint_angles))
        