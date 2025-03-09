import asyncio

async def count_numbers(name, start, end, delay):
    for i in range(start, end + 1):
        print(f"{name}: {i}")
        await asyncio.sleep(delay)
    print(f"{name} completed!")

async def main():
    task1 = asyncio.create_task(count_numbers("Counter 1", 1, 5, 1))
    task2 = asyncio.create_task(count_numbers("Counter 2", 10, 15, 0.5))
    task3 = asyncio.create_task(count_numbers("Counter 3", 100, 102, 1.5))

    await asyncio.gather(task1, task2, task3)
    print("All counters finished!")

asyncio.run(main())
