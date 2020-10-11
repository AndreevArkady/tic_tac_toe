class tic_tac:
    def __init__(self, player_1, player_2):
        self.player_names = [player_1, player_2]
        self.whose_turn = 0
        self.get_first_player_name()
        self.f = []
        self.f.append(['_', '_', '_'])
        self.f.append(['_', '_', '_'])
        self.f.append(['_', '_', '_'])

    def get_first_player_name(self):
        player_name = input('Who start the game? -')
        while self.player_names.count(player_name):
            player_name = input("Please, enter first player name correctly. -")
        if player_name == self.player_names[1]:
            self.whose_turn = 1


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
        try:
            if (1 <= args[0] <= 3) and (1 <= args[1] <= 3):
                column, row, value = args
                self.f[3 - row][column - 1] = value
                self.whose_turn = 1 - self.whose_turn
                self.print_field()
            else:
                print("Wrong turn format, enter (column, row, <symbol>)")
        except ValueError:
            print("Wrong turn format, enter (column, row, <symbol>)")

    def whose_turn_now(self):
        return self.player_names[self.whose_turn]


if __name__ == '__main__':
    a = tic_tac('Arkady', 'Vlad')
