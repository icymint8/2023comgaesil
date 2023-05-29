class Machine:
    def __init__(self, x_speed, y_speed):
        self.x_pos = -1
        self.y_pos = -1
        self.x_speed = x_speed
        self.y_speed = y_speed

    def move_to(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move_time(self, x_pos, y_pos):
        return abs(x_pos - self.x_pos) / self.x_speed + abs(y_pos - self.y_pos) / self.y_speed

    def move_to_init(self):
        self.x_pos = -1
        self.y_pos = -1

    def __str__(self):
        return f'{self.x_pos}, {self.y_pos}'


class Rack:
    def __init__(self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size
        self.cells = dict(zip([(i, j) for i in range(x_size) for j in range(y_size)], ['X'] * (x_size * y_size)))

    def __str__(self):
        r_str = ''
        for j in range(self.y_size):
            for i in range(self.x_size):
                r_str += f'{self.cells[(i, self.y_size - j - 1)]} '
            r_str += '\n'
        return r_str


if __name__ == '__main__':
    r = Rack(2, 2)
    print(r)

    m = Machine(2, 3)
    print(m)
    print(m.move_time(1, 2))
