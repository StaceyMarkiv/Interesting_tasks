from typing import Any
from functools import wraps
import time


def create_decorator(call_count, start_sleep_time, factor, border_sleep_time):
    def sleepy_decorator(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            count: int = 0
            t: int = start_sleep_time
            n: int = factor
            border: int = border_sleep_time
            while count < call_count:
                time.sleep(t)
                result: Any = func(*args, **kwargs)
                print(f'call No.{count + 1} | sleep time {t} | result {result}')

                t = t * (2 ** n)
                if t > border:
                    t = border

                count += 1
            return result

        return wrap

    return sleepy_decorator


sleep_time_decorator = create_decorator(3, 1, 2, 10)


@sleep_time_decorator
def count_func(my_number: int) -> int:
    res: int = my_number ** 5
    return res


if __name__ == '__main__':
    count_result = count_func(15)
