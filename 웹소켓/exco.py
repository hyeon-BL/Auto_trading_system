import asyncio
async def make_americano():
    print("Americano Start")
    await asyncio.sleep(3)
    print("Americano End")

async def make_latte():
    print("latte Start")
    await asyncio.sleep(5)
    print("latte End")

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    await asyncio.gather( # 동시에 실행
        coro1, 
        coro2
    )
print("Main Start")
asyncio.run(main())
print("Main End")