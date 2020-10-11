class tic_tac:
    turn_symbols = ['x', 'o']

    def __init__(self, player_1, player_2):
        self.player_names = [player_1, player_2]
        self.index_of_active_player = 0
        self.get_first_player_name()
        self.players_symbols_dict = self.get_first_player_symbol()
        self.f = []
        self.f.append(['_'] * 3)
        self.f.append(['_'] * 3)  # а по-другому у меня не получилось(
        self.f.append(['_'] * 3)

    def __repr__(self):
        if isinstance(self, tic_tac):
            s = self.f
        else:
            s = self
        return str(s)

    def __str__(self):
        return str(self.f)

    def get_first_player_symbol(self):  # заполняем словарь "номер игрока" -> "его символ x или o"
        symbol = input('What is "%s" symbol? x or o -' % str((self.player_names[self.index_of_active_player])))
        if symbol == 'x':
            return {self.index_of_active_player: 'x', 1 - self.index_of_active_player: 'o'}
        else:
            return {self.index_of_active_player: 'o', 1 - self.index_of_active_player: 'x'}

    def get_first_player_name(self):
        player_name = input('Who start the game? -')
        while not self.player_names.count(player_name):
            player_name = input("Please, enter first player name correctly. -")
        if player_name == self.player_names[1]:
            self.index_of_active_player = 1

    def print_field(self):
        for i in self.f:
            for j in i:
                print(j, end=' ')
            print()

    def make_turn(self, *args):
        try:
            if (1 <= args[0] <= 3) and (1 <= args[1] <= 3):
                column, row, value = args
                self.f[3 - row][column - 1] = value  # такая странная формула чтобы синхронизировать формат
                self.index_of_active_player = 1 - self.index_of_active_player  # ввода и формат хранения таблицы
                self.print_field()
            else:
                print("Wrong turn format, enter (column, row, <symbol>)")
        except ValueError:
            print("Wrong turn format, enter (column, row, <symbol>)")

    def whose_turn_now(self):
        return self.player_names[self.index_of_active_player]


if __name__ == '__main__':
    a = tic_tac('A', 'V')
