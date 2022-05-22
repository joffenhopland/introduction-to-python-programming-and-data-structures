import asyncio
import random
import time


class Counter:
    def __init__(self):
        self.executed = 0

    def increment(self):
        self.executed += 1

    def get(self):
        return self.executed

    def __str__(self):
        return "Number of executed tasks: " + self.executed

async def execute_io(number: int, counter: Counter) -> int:
    sekunder = random.randint(0, 2)
    await asyncio.sleep(sekunder)
    counter.increment()
    return digit_sum(number)


def digit_sum(number: int) -> int:
    sum = 0

    while number != 0:
        current = number % 10
        sum += current
        number = number // 10
    return sum


async def main():
    print(f"started at {time.strftime('%X')}")
    no_tasks = 500000
    tasks = []
    counter = Counter()

    for i in range(no_tasks):
        tasks.append(asyncio.create_task(execute_io(i + 1, counter)))
    L = await asyncio.gather(*tasks, return_exceptions=False)

    sum = 0
    for value in L:
        sum += value

    print("Finished processing, result " + str(sum) + ", got counter: " + str(counter.get()))
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())


