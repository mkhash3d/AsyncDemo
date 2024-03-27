import asyncio
import time

def wait(n):
    for i in range(n):
        print(i)
        time.sleep(1)


wait(5)