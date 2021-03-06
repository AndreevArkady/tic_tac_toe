# TicTacToe
## В данной программе представлен класс tic_tac_toe, с помощью которого можно играть в саму игру (известную на Руси как "Крестики-нолики") 

### Класс tic-tac-toe обладает следующими аттрибутами:
* player_names - массив имен игроков [0] = первое введенное имя, [1] = второе
* index_of_active_player - индекс, 0 или 1, того игрока, чей сейчас ход
* players_symbols_dict - словарь, сопоставляющий номеру игрока индексу игрока его символ
* field - игровое поле 3 на 3
* print_field_after_turns - параметр, отвечающий за то, нужно ли после каждого хода выводить игровое поле (по умолчанию равно 1, поле выводится)
* turns_made - количество совершенных игроками ходов (от 0 до 9)
* winner - если игра еще идет = -1, если игра завершилась, то если есть однозначный победитель, то он равен индексу победителя, если ничья то = 3

### Класс tic_tac_toe обладает следующими функциями
* get_first_player_name - вызывается в начале, чтобы инициализировать имя игрока, ходящего первым
* get_first_player_symbol - тоже вызывается в начале, чтобы инициализировать символ игрока, ходящего первым (а также символ другого игрока методом исключения)
* print_field - выводит значения аттрибута field в формате поля 3 на 3
* show_field - вызывает print_field, по своей сути является альтернативным неймингом функии вывода поля
* make_turn(* args) - функция хода, получает на вход  *args* , и если они представляют из себя два числа x, y от 1 до 3, то если клетка с координатой (x,y) не занята, ходим в нее символом текущего игрока и меняем очередность хода, попутно проверяя игру на завершенность, если эта клетка уже занята, то просто сообщаем об этом пользователю и больше ничего не делаем; если же *args* представляет из себя что-то иное, выводим текст о неверном формате хода. Так же в самом начале, в случае, если игра уже завершена, сообщаем об этом игроку и на этом заканчиваем
* whose_turn_now - возращает чей сейчас ход
* switch_field_printing - меняет значение поля index_of_active_player
* if_game_ended - проверяет, завершена ли игра с помощью следующей функции
* if_three_cells_equal
* if_game_ended_question - отвечает на вопрос о законченности игры, выводя ее исход в случае завершенности

## Как игрокам взаимодествовать с программой и играть в игру
* В начале подать имена двух игроков
* Подать имя игрока, собирающегося ходить первым
* Подать символ, за который первый игрок будет играть (крестик x или буковку o - строчные латинские буквы)
* Далее игра происходит в формате game.make_turn(x,y) где (x,y) координаты игрового поля, выглядящего в виде таблицы 3 х 3, x = координата по абсциссе, y = координата по ординате т.е.
первое число отвечает за номер столбца слева-направо, вторая за номер строчки снизу-вверх (как в шахматах), нумерация с 1 до 3
например число в нижней левой клетке имеет координату (1,1), а верхняя правая (3,3)
* Когда игра закончится, программа сообщит это и общий результат игры, после чего делать ходы будет уже нельзя
* В любой момент игроки могут:
  * Спросить чей сейчас ход: game.whose_turn_now() 
  * Текущий игрок может сходить game.make_turn(n, m) - где 1 <= m, n <= 3
  * Спросить, завершена ли игра game.game_ended_question()
  * Получить ответ на вопрос "кто выйграл?" game.who_won()
  * Попросить вывести текущее игровое поле: game.print_field() или game.show_field()
  * Выключить или отключить вывод поля после каждого хода: game.switch_field_printing()
