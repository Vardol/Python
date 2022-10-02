import time
import math

def random_digit_from_timens():
    return int((time.time_ns() % 1000) / 100)

def random_digit_from_monotonicns():
    return int((time.monotonic_ns() % 10000000) / 1000000)

# сделал 2 варианта получения цифры из модуля time, но у меня почему-то выдает одинаковые цифры, при генерации нескольких подряд - 
# видимо, уикл выполняется внутри одной наносекунды. При этом, если программу запускать несколько раз, то цифры будут разные.

def my_very_own_rand(min: int, max: int):
    result = -1
    range_length = max-min
    number_of_digits = int(math.log10(range_length) + 1)
    digits_tuple = tuple(range(0, 10))
    if range_length < 10:
        result = digits_tuple[random_digit_from_monotonicns() % range_length]
    else:
        str_result = ""
        for i in range(0, number_of_digits):
            str_result += str(digits_tuple[random_digit_from_monotonicns()])
        result = int(str_result)
    if result > range_length:
        result %= range_length
    result += (min - 0)
    return result
        

#print(random_digit_from_monotonicns())
print(my_very_own_rand(0,1000000))


