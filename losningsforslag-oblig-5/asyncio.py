import asyncio, random
from CounterClass import Counter

MAX_ACCOUNTS = 500000
async def execute_io(ind: int, c: Counter) -> int:
    #print(f"Start task {ind}!")
    c.increment()
    await asyncio.sleep(2*random.random())
    #print(f"Finished task {ind}!")
    test1 = tverrsum(5)
    return tverrsum(ind)

def tverrsum(tall):
    sum = 0
    for digit in str(tall): 
      sum += int(digit)      
    return sum

async def run():
    counter = Counter(0)
    clients = [asyncio.create_task(execute_io( number, counter)) for number in range(1,MAX_ACCOUNTS+1)]
    try:
        results = await asyncio.gather(*clients,  return_exceptions=True)
    except Exception as ex:
            print("Caught error executing task", ex)
            raise
    print(f"Finished processing, result {sum(results)}, got counter: {counter.get()}")

if __name__ == '__main__':
    asyncio.run(run())
