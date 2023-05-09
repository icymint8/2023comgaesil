import event


def get_safe_distance(time):
    dist_list = [30, 20, 10, 5, 1]
    return dist_list[time // 30 if time < 150 else 4]


class Map(object):
    def __init__(self):
        self.target_location = event.get_random_location()

    # 기능 추가 1
    def safe_zone_effect(self, player, time):
        if player.health > 0:
            really = True if abs(self.target_location - player.location) <= get_safe_distance(time) else False
            if not really:
                player.health -= 10
