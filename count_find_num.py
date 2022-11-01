import math


def count_qty(big_num, small_num):
    # Определяем, сколько раз большое число делится на маленькое
    count = 0
    res = big_num
    while res >= small_num:
        res = res // small_num
        count += 1
    return count


def count_find_num(primes_l, limit):
    prod = math.prod(primes_l)
    # Максимальное количество повторений возведения в степень (вычисляется по минимальному числу из списка primesL)
    range_limit = count_qty(limit // prod, min(primes_l)) + 1
    result = [prod] if prod <= limit else []
    for el in primes_l:
        for r in result:
            result = list(set(result))
            res = [r * el**i for i in range(range_limit) if r * el**i <= limit]
            result.extend(res)

    qty = len(set(result))
    max_value = max(result) if result else None

    return [qty, max_value] if max_value else []


if __name__ == "__main__":
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
