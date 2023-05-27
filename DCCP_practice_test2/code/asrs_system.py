from base import *
from exceptions import *


class ASRS_Rack(Rack):
    def __init__(self, x_size, y_size):
        ###############################

        pass

        ###############################


    def search_product(self, product_name):
        ###############################

        pass

        ###############################



class Crane(Machine):
    def __init__(self, x_speed, y_speed, shuttle_size):
        ###############################
        
        pass
        
        ###############################
    
    
    def store(self, rack, product_name):
        ###############################

        pass

        ###############################

    
    def retrieve(self, rack):
        ###############################

        pass

        ###############################

    
    def load(self, product_name):
        ###############################

        pass

        ###############################

    
    def release(self):
        ###############################

        pass

        ###############################


    def __str__(self):
        ###############################
        
        pass
        
        ###############################
    


class ASRS_system:
    def __init__(self, rack, crane):
        ###############################
        
        pass
        
        ###############################
    
    
    def start_cycle(self, names, srs):
        ###############################
        
        pass
        
        ###############################
    
    
    def end_cycle(self, srs):
        ###############################
        
        pass
        
        ###############################
    
    
    def operate_cycle(self, names, srs):
        ###############################
        
        pass
        
        ###############################
    
    
    def operate_system(self, names, srs):
        ###############################
        
        pass
        
        ###############################



if __name__ == '__main__':
    product_names = 'AABACABBC'
    sr_types = 'SSSSSRSRS'

    asrs_rack = ASRS_Rack(3, 3)
    asrs_crane = Crane(1, 1, 2)
    asrs = ASRS_system(asrs_rack, asrs_crane)
    asrs.operate_system(product_names, sr_types)