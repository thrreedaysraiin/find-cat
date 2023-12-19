import random
import time

class Card:
    def __init__(self, color, action, pattern):
        self.color = color
        self.action = action
        self.pattern = pattern

    def __str__(self):
        return f"{self.color} {self.pattern} кот {self.action} "


class Board:
    def __init__(self):
        self.cards = []
        self.colors = ['голубой', 'зеленый', 'оранжевый', 'фиолетовый', 'красный', 'желтый', 'черный']
        self.actions = ['ест', 'спит', 'играет', 'умывается']
        self.patterns = ['однотонный', 'полосатый', 'пятнистый']

        # Генерация случайных карт и добавление их в игровое поле
        for i in range(10):
            color = random.choice(self.colors)
            action = random.choice(self.actions)
            pattern = random.choice(self.patterns)
            self.cards.append(Card(color, action, pattern))

        random.shuffle(self.cards)

    def get_card(self, index):
        return self.cards[index]

    def get_random_card(self):
        return random.choice(self.cards)

    def __str__(self):
        board_str = ''
        for i, card in enumerate(self.cards):
            index = i + 1
            board_str += f"{index}: {card}\n"
        return board_str


class Game:
    def __init__(self):
        self.board = Board()
        self.score = 0
        self.round = 1
        self.max_score = 5
        self.is_playing = True

    def play(self):
        print("Добро пожаловать в игру «Найди кота»!")
        print(f"Первый игрок, набравший {self.max_score} oчков, побеждает.")
        while self.is_playing:
            print(f"\nРаунд {self.round}")
            self.play_round()
            if self.score >= self.max_score:
                print("Поздравляем! Вы выиграли!")
                self.is_playing = False
            elif self.score < 0:
                print("Игра закончена! Вы проиграли.")
                self.is_playing = False
            else:
                self.round += 1

    def play_round(self):
        properties = self.roll_dice()  # Генерация свойств кота для текущего раунда
        print(f" {properties[0]} {properties[2]} кот {properties[1]}.")

        # Вывод всех карт на поле перед каждым ответом игрока
        print("Набор карт:")
        print(self.board)

        print("Запомните данные о кошке и найдите соответствующую карточку за 10 секунд.")
        time.sleep(1)  # Небольшая задержка перед выводом следующей строки

        start_time = time.time()
        correct_card = self.board.get_random_card()
        print(f"На правильной карточке изображен такой кот: {correct_card}")

        selection = input("Введите номер правильной карты: ")
        try:
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > 10:
                print("Время вышло! Вы теряете очко.")
                self.score -= 1
                print(f"Текущий счет: {self.score}")
                return
            index = int(selection) - 1
            card = self.board.get_card(index)
            if card == correct_card:
                print("Правильно! Вы получаете очко.")
                self.score += 1
            else:
                print("Неправильно! Вы теряете очко.")
                self.score -= 1
        except (ValueError, IndexError):
            print("Неверный Ввод. Вы теряете очко.")
            self.score -= 1

        print(f"Текущий счет: {self.score}")

    def roll_dice(self):
        card = random.choice(self.board.cards)
        return card.color, card.action, card.pattern


if __name__ == '__main__':
    game = Game()
    game.play()