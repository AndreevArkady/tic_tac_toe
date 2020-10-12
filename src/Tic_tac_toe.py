class tic_tac:

    def __init__(self, player_0, player_1):
        self.player_names = [player_0, player_1]
        self.index_of_active_player = self.get_first_player_name()
        self.players_symbols_dict = self.get_first_player_symbol()
        self.field = []
        self.field.append(['_'] * 3)
        self.field.append(['_'] * 3)  # а по-другому у меня не получилось(
        self.field.append(['_'] * 3)
        self.print_field()
        self.print_field_after_turns = 1
        self.moves_made = 0
        self.winner = -1

    def __repr__(self):
        if isinstance(self, tic_tac):
            s = self.field
        else:
            s = self
        return str(s)

    def __str__(self):
        return str(self.field)

    def get_first_player_name(self):
        player_name = input('Who start the game? -')
        while not self.player_names.count(player_name):
            player_name = input("Please, enter first player name correctly. -")
        return player_name == self.player_names[1]

    def get_first_player_symbol(self):  # заполняем словарь "индекс игрока" -> "его символ x или o"
        symbol = input(
            'What symbol is "%s" going to play for? x or o -' % str((self.player_names[self.index_of_active_player])))
        if symbol == 'x':
            return {self.index_of_active_player: 'x', 1 - self.index_of_active_player: 'o'}  # indexes are 0 or 1
        else:
            return {self.index_of_active_player: 'o', 1 - self.index_of_active_player: 'x'}

    def print_field(self):
        for row in self.field:
            for item_in_row in row:
                print(item_in_row, end=' ')
            print()

    def show_field(self):
        self.print_field()

    def make_turn(self, *args):
        if self.moves_made == 9:
            print("Game ended in a draw.")
        elif self.winner != -1:
            print("%s won! Thanks for playing the game." % self.player_names[self.index_of_active_player])
        else:
            try:
                if (1 <= args[0] <= 3) and (1 <= args[1] <= 3):
                    column, row = args
                    if self.field[3 - row][column - 1] != '_':
                        print("This cell is already occupied by", self.field[3 - row][column - 1])
                    else:
                        self.field[3 - row][column - 1] = self.players_symbols_dict.get(self.index_of_active_player)
                        self.moves_made += 1
                        if self.print_field_after_turns:
                            self.print_field()
                        if self.if_game_ended():
                            self.winner = self.index_of_active_player
                            print("%s, who played for %s, won the game!" % (
                                self.player_names[self.index_of_active_player],
                                self.players_symbols_dict[
                                    self.index_of_active_player]))
                        else:
                            if self.moves_made == 9:
                                print("DRAW, thanks for playing the game!")
                                self.winner = 3
                            self.index_of_active_player = 1 - self.index_of_active_player
                else:
                    print("Wrong turn format, enter (column, row)")
            except ValueError:
                print("Wrong turn format, enter (column, row)")

    def whose_turn_now(self):
        print(self.player_names[self.index_of_active_player], "'s turn (playing for ",
              self.players_symbols_dict.get(self.index_of_active_player), ")", sep='')

    def switch_field_printing(self):
        self.print_field_after_turns = 1 - self.print_field_after_turns

    def if_game_ended(self):
        game_ended = False
        for i in range(3):
            game_ended |= self.if_three_cells_equal(0, i, 1, i, 2, i)
            game_ended |= self.if_three_cells_equal(i, 0, i, 1, i, 2)
        game_ended |= self.if_three_cells_equal(0, 0, 1, 1, 2, 2)
        game_ended |= self.if_three_cells_equal(0, 2, 1, 1, 2, 0)
        return game_ended

    def if_three_cells_equal(self, a1, a2, b1, b2, c1, c2):
        return self.field[a1][a2] == self.field[b1][b2] == self.field[c1][c2] != '_'

    def game_ended_question(self):
        if self.if_game_ended():
            if self.winner == 3:
                print("Yes, game ended in a draw.")
            else:
                print("Yes, game over, %s won." % self.player_names[self.index_of_active_player])
        else:
            print("No, game is not over yet,", end=' ')
            self.whose_turn_now()


if __name__ == '__main__':
    print("Please, enter player names:")
    a = tic_tac(input(), input())
