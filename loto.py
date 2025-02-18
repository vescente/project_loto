from random import randint, shuffle


def generate_unique_numbers(count, min_value, max_value):
    if count > max_value - min_value + 1:
        raise ValueError('Incorrect input parameters')
    unique_numbers = set()
    while len(unique_numbers) < count:
        unique_numbers.add(randint(min_value, max_value))
    return list(unique_numbers)


class Keg:
    def __init__(self):
        self._number = randint(1, 90)

    @property
    def number(self):
        return self._number

    def __str__(self):
        return str(self._number)


class Card:
    def __init__(self, rows=3, cols=9, nums_in_row=5, empty_value=0, crossed_value=0):
        self._rows = rows
        self._cols = cols
        self._nums_in_row = nums_in_row
        self._empty_value = empty_value
        self._crossed_value = crossed_value
        self._data = self._generate_card_data()

    def _generate_card_data(self):
        unique_numbers = generate_unique_numbers(self._nums_in_row * self._rows, 1, 90)
        card_data = []
        for i in range(self._rows):
            row_numbers = sorted(unique_numbers[self._nums_in_row * i: self._nums_in_row * (i + 1)])
            empty_slots = self._cols - self._nums_in_row
            for _ in range(empty_slots):
                row_numbers.insert(randint(0, len(row_numbers)), self._empty_value)
            card_data.extend(row_numbers)
        return card_data

    def __contains__(self, item):
        return item in self._data

    def cross_number(self, number):
        if number in self._data:
            self._data[self._data.index(number)] = self._crossed_value
        else:
            raise ValueError(f'Number not in card: {number}')

    def is_closed(self):
        return all(num == self._empty_value or num == self._crossed_value for num in self._data)

    def __str__(self):
        card_str = ''
        for i in range(self._rows):
            row = self._data[i * self._cols: (i + 1) * self._cols]
            card_str += ' '.join(f'{num:2}' if num != self._empty_value else '  ' for num in row) + '\n'
        return card_str


class Game:
    def __init__(self):
        self._user_card = Card()
        self._computer_card = Card()
        self._kegs = generate_unique_numbers(90, 1, 90)
        shuffle(self._kegs)  # Shuffle kegs for random order
        self._game_over = False

    def play_round(self):
        if not self._kegs:
            self._game_over = True
            return 0

        keg = self._kegs.pop()
        print(f'New keg: {keg} (remaining {len(self._kegs)})')
        print(f'----- Your card ------\n{self._user_card}')
        print(f'-- Computer card ---\n{self._computer_card}')

        user_answer = input('Cross out the number? (y/n)').lower().strip()
        if (user_answer == 'y' and keg not in self._user_card) or \
           (user_answer != 'y' and keg in self._user_card):
            return 2

        if keg in self._user_card:
            self._user_card.cross_number(keg)
            if self._user_card.is_closed():
                return 1

        if keg in self._computer_card:
            self._computer_card.cross_number(keg)
            if self._computer_card.is_closed():
                return 2

        return 0
    
    def __str__(self):
        return f'Game with user card {self._user_card} and computer card {self._computer_card}'


if __name__ == '__main__':
    game = Game()
    while True:
        score = game.play_round()
        if score == 1:
            print('You win')
            break
        elif score == 2:
            print('You lose')
            break
