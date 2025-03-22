# таблица 3х3
tabl = [1, 2, 3,
        4, 5, 6,
        7, 8, 9]
# победные комбинации
win = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [1, 4, 7],
       [2, 5, 8],
       [3, 6, 9],
       [1, 5, 9],
       [3, 5, 7]]


#печать таблицы
def print_tabl():
    print(tabl[0], end="|")
    print(tabl[1], end="|")
    print(tabl[2])

    print(tabl[3], end="|")
    print(tabl[4], end="|")
    print(tabl[5])

    print(tabl[6], end="|")
    print(tabl[7], end="|")
    print(tabl[8])


#принятие хода
def take_input(playar_token):
    while True:
        value = input("введите номер клетки: " + playar_token + " ? ")
        if not (value in '123456789'):
            print("Ошибка.повторите ввод.")
            continue
        value = int(value)
        if str(tabl[value - 1]) in "X O":
            print("Эта клетка занята")
            continue
        tabl[value - 1] = playar_token
        break

#проверка на победителя
def check_win():
    for i in win:
        if (tabl[i[0] - 1] == tabl[i[1] - 1] == tabl[i[2] - 1]):
            return tabl[i[1] - 1]
    else:
        return False
#логика хода игры
def main():
    counter = 0
    while True:
        print_tabl()
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if counter > 3:
            winner = check_win()
            if winner:
                print_tabl()
                print(winner, "выиграл!")
                break
        counter += 1
        if counter > 8:
            print_tabl()
            print("Ничья")
            break
#запуск игры
main()
