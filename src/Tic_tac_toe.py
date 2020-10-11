def start_new_game(name):
    game = tic_tac(name)


class tic_tac:
    def __init__(self, player_1, player_2):
        self.player_1 = str(player_1)
        self.player_2 = str(player_2)
        self.f = [[] * 3] * 3

    def __setitem__(self, key1, value):
        ans = value if isinstance(value, int) else value
        self.f[key1] = ans

    def __repr__(self):
        if isinstance(self, tic_tac):
            s = self.f
        else:
            s = self
        return str(s)

    def __str__(self):
        return self.f

    def print_field(self):
        for i in self.f:
            for j in i:
                print(j, end=' ')


if __name__ == '__main__':
    a = tic_tac('asdad')


