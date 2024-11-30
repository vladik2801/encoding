from decimal import Decimal, getcontext
import math

getcontext().prec = 150


class Interval:
    def __init__(self, left, right):
        self.left = left
        self.right = right

class LetterInterval(Interval):
    def __init__(self, letter, left, right):
        super().__init__(left, right)
        self.letter = letter


def calc(message):
    length = len(message)
    freq = {}
    for char in message:
        freq[char] = freq.get(char, 0) + 1
    for char in freq:
        freq[char] = Decimal(freq[char]) / Decimal(length)
    return dict(sorted(freq.items(), key=lambda item: item[1]))


def create(freq):
    letter_intervals = {}
    current_left = Decimal('0')
    for letter, prob in freq.items():
        current_right = current_left + prob
        letter_intervals[letter] = LetterInterval(letter, current_left, current_right)
        current_left = current_right
    return letter_intervals


def encode(message):
    freq = calc(message)
    letter_intervals = create(freq)
    print("\nНачальные интервалы:")
    for interval in letter_intervals.values():
        print(interval.letter, interval.left, interval.right)

    main_interval = Interval(Decimal('0'), Decimal('1'))

    for i, char in enumerate(message):
        range_width = main_interval.right - main_interval.left

        main_interval = Interval(
            main_interval.left + range_width * letter_intervals[char].left,
            main_interval.left + range_width * letter_intervals[char].right
        )

    L_left = main_interval.left
    L_right = main_interval.right
    diff = L_right - L_left
    print("\nФинальный интервал: [{}, {})".format(L_left, L_right))

    q = math.ceil(math.log2(float(1 / diff)))
    multiplier = 2 ** q
    var = int(L_left * multiplier)
    P = var
    print(f"Целое число: {P}")

    result = bin(P)[2:].zfill(q)
    print(f"Результат: {result}")

    return main_interval, q, P, result

if __name__ == "__main__":
    message = "сорокинвладиславвячеславович"
    encode(message)
