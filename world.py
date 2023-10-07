class world():
    def __init__(self):
        self.world_objects = []
    
    def add_object(self, object):
        self.world_objects.append(object)
    
    def add_objects(self, objects_list):
        for object in objects_list:
            self.world_objects.append(object)