import asyncio
import time

async def make_meal(delay, what):
    await asyncio.sleep(delay)
    print(what + ' finished')

async def main():
    print(f"started at {time.strftime('%X')}")
    await asyncio.gather(make_meal(3, 'Make coffee'), 
        make_meal(7, 'Boil two eggs'), 
        make_meal(6, 'Fry some bacon'), 
        make_meal(2, 'Toast two pieces'), 
        make_meal(1, 'Add butter and jam to the table'), 
        make_meal(1, 'Pour a glass of orange juice'))
    
    print('Breakfast is ready')
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())