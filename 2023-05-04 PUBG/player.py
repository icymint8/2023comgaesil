import event


class Player(object):
    def __init__(self, id):
        self.id = id
        self.health = 100
        self.location = event.get_random_location()
        # 기능 추가 2
        self.status = 'alive'

    def __str__(self):
        return f'Player {self.id:2d}: {self.health:3d} HP, located at {self.location:2d}, status: {self.status}'

    def run(self, target_location):
        if self.location > target_location:
            self.location -= 1
        elif self.location < target_location:
            self.location += 1

    def status_update(self):
        if self.health <= 0:
            self.status = 'dead'
