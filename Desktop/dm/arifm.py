from decimal import Decimal, getcontext
import math

getcontext().prec = 150

class Interval:
    def init(self, left, right):
        self.left = left
        self.right = right


class LetterInterval(Interval):
    def init(self, letter, left, right):
        super().init(left, right)
        self.letter = letter


def create(freq):
    letter_intervals = {}
    current_left = Decimal('0')
    for letter, prob in freq.items():
        current_right = current_left + prob
        letter_intervals[letter] = LetterInterval(letter, current_left, current_right)
        current_left = current_right
    return letter_intervals


def calc(fio):
    length = len(fio)
    freq = {}
    for char in fio:
        freq[char] = freq.get(char, 0) + 1
    for char in freq:
        freq[char] = Decimal(freq[char]) / Decimal(length)
    return dict(sorted(freq.items(), key=lambda item: item[1]))


def encode(fio):
    freq = calc(fio)
    letter_intervals = create(freq)
    for interval in letter_intervals.values():
        print(interval.letter, interval.left, interval.right)

    main_interval = Interval(Decimal('0'), Decimal('1'))

    for i, char in enumerate(fio):
        width = main_interval.right - main_interval.left
        main_interval = Interval(
            main_interval.left + width * letter_intervals[char].left,
            main_interval.left + width * letter_intervals[char].right
        )

    L_left = main_interval.left
    L_right = main_interval.right
    diff = L_right - L_left
    print("\nФинальный интервал: [{}, {})".format(L_left, L_right))
    q = math.ceil(math.log2(float(1 / diff)))
    print(f"Количество бит: {q}")
    multiplier = 2 ** q
    left = int(L_left * multiplier)
    P = left
    print(f"Целое число: {P}")
    result = bin(P)[2:].zfill(q)
    print(f"Результат: {result}")

    return main_interval, q, P, result

if name == "main":
    fio = "сорокинвладиславвячеславович"
    encode(fio)