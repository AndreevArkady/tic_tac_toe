class tic_tac:
    def __init__(self, player_1, player_2):
        self.player_1 = str(player_1)
        self.player_2 = str(player_2)
        player_name = input('Who start the game? -')
        while player_name != player_1 and player_name != player_2:
            player_name = input("Please, enter first player name correctly. -")
        if player_name == player_2:
            self.whos_first = 1
        else:
            self.whos_first = 2
        self.whos_turn = self.whos_first
        self.f = []
        self.f.append(['_', '_', '_'])
        self.f.append(['_', '_', '_'])
        self.f.append(['_', '_', '_'])

    '''def __setitem__(self, key1, value):
        ans = value if isinstance(value, int) else value
        self.f[key1] = ans'''

    def __repr__(self):
        if isinstance(self, tic_tac):
            s = self.f
        else:
            s = self
        return str(s)

    def __str__(self):
        return str(self.f)

    def print_field(self):
        for i in self.f:
            for j in i:
                print(j, end=' ')
            print()

    def make_turn(self, *args):
        if len(args) < 3:
            return "Wrong turn format"
        else:
            raw, column, value = args
            self.f[raw][column] = value
            self.whos_turn = 1 - self.whos_turn
            self.print_field()


if __name__ == '__main__':
    a = tic_tac('Arkady', 'Vlad')
