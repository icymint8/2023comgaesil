import map
import player
import event


class Game(object):
    def __init__(self, num_player):
        self.num_player = num_player
        self.players = [player.Player(i) for i in range(num_player)]
        self.map = map.Map()
        self.global_time = 0
        # 기능 추가 3
        self.end = False

        print(self)
        for p in self.players:
            print(p)
        print()

    def __str__(self):
        return f'Time: {self.global_time}, Target Location: {self.map.target_location}'

    def advance_tick(self):
        self.players = list(filter(lambda x: x.status == 'alive', self.players))
        if len(self.players) == 1:
            self.end = True
            return

        self.global_time += 1
        print(self)

        # 기능 추가 2
        loc_list = [p.location for p in self.players]
        for loc in set(loc_list):
            if loc_list.count(loc) > 1:
                event.battle(list(filter(lambda x: x.location == loc, self.players)))

        for p in self.players:
            p.run(self.map.target_location)
            self.map.safe_zone_effect(p, self.global_time)
            p.status_update()
            print(p)

        print()


n_player = 50
new_game = Game(n_player)
# 기능 추가 3
while not new_game.end:
    new_game.advance_tick()
print(f'Winner is: Player {new_game.players[0].id}')
