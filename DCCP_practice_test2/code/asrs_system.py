from base import *
from exceptions import *


class ASRS_Rack(Rack):
    def __init__(self, x_size, y_size):
        super().__init__(x_size, y_size)

    def search_product(self, product_name):
        r_list = []

        for key in self.cells:
            if self.cells[key] == product_name:
                r_list.append(key)

        if not r_list:
            raise NoProductException
        else:
            return r_list


class Crane(Machine):
    def __init__(self, x_speed, y_speed, shuttle_size):
        super().__init__(x_speed, y_speed)

        self.shuttle_size = shuttle_size
        self.shuttle = ['X'] * shuttle_size

    def store(self, rack, product_name):
        ind = self.shuttle.index(product_name)

        if rack.cells[(self.x_pos, self.y_pos)] == 'X':
            if self.shuttle[ind] != 'X':
                self.shuttle[ind] = 'X'
                rack.cells[(self.x_pos, self.y_pos)] = product_name
                print(f'product {product_name} is stored at {(self.x_pos, self.y_pos)}')
            else:
                raise NoProductException
        else:
            raise NoSpaceException

    def retrieve(self, rack):
        try:
            ind = self.shuttle.index('X')
        except ValueError:
            raise NoSpaceException


        self.shuttle[ind] = rack.cells[(self.x_pos, self.y_pos)]
        rack.cells[(self.x_pos, self.y_pos)] = 'X'
        print(f'product {self.shuttle[ind]} is retrieved from {(self.x_pos, self.y_pos)}')

    def load(self, product_name):
        try:
            ind = self.shuttle.index('X')
        except ValueError:
            raise NoSpaceException

        self.shuttle[ind] = product_name
        print(f'product {product_name} is loaded')

    def release(self):
        for i in range(self.shuttle_size):
            if self.shuttle[i] != 'X':
                print(f'product {self.shuttle[i]} is released')
                self.shuttle[i] = 'X'

    def __str__(self):
        return f'crane at {(self.x_pos, self.y_pos)} with {self.shuttle}'
    

class ASRS_System:
    def __init__(self, rack, crane):
        self.rack = rack
        self.crane = crane

    def start_cycle(self, names, srs):
        print(self.crane)

        for i in range(len(srs)):
            if srs[i] == 'S':
                self.crane.load(names[i])

    def end_cycle(self, srs):
        self.crane.move_to_init()

        if 'R' in srs[0:self.crane.shuttle_size]:
            self.crane.release()

    def operate_cycle(self, names, srs):
        print(self.crane)
        if len(srs) == 0:
            return

        if srs[0] == 'S':
            coord_list = self.rack.search_product('X')
            self.crane.move_to(*coord_list[0])
            self.crane.store(self.rack, names[0])
        else:
            coord_list = self.rack.search_product(names[0])
            self.crane.move_to(*coord_list[0])
            self.crane.retrieve(self.rack)

        if self.crane.x_pos >= self.rack.x_size or self.crane.y_pos >= self.rack.y_size:
            raise OutOfRackException

        self.operate_cycle(names[1:], srs[1:])

    def operate_system(self, names, srs):
        cycles = len(srs) // self.crane.shuttle_size + (1 if len(srs) % self.crane.shuttle_size else 0)

        for i in range(cycles):
            print(self.rack)
            sli = slice(i * self.crane.shuttle_size, (i + 1) * self.crane.shuttle_size)

            self.start_cycle(names[sli], srs[sli])
            self.operate_cycle(names[sli], srs[sli])
            self.end_cycle(srs[sli])

        print(self.rack)


if __name__ == '__main__':
    product_names = 'AABACABBC'
    sr_types = 'SSSSSRSRS'

    asrs_rack = ASRS_Rack(3, 3)
    asrs_crane = Crane(1, 1, 2)
    asrs = ASRS_System(asrs_rack, asrs_crane)
    asrs.operate_system(product_names, sr_types)
