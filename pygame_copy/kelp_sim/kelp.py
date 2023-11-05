class kelp_class:

    def __init__(self, num_segments, length, anchor_location, kelp_type):
        self.num_segments = num_segments
        self.length = length
        self.anchor_coords = anchor_location
        self.joint_angles = []
        self.joint_coords = []
        self.type = kelp_type #bull kelp vs giant kelp
    