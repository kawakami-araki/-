import asyncio
import time
# 创建一个待执行的代码块
start = time.time()
urls = str(x for x in range(1,100))
async def func(url):
    print('开始',url)
    await asyncio.sleep(3)
    print('结束',url)
# 创建一个协程函数对象
tasks = []
for url in urls:
    print(url)
    f = func(url)
# 封装一个协程对象
    task = asyncio.ensure_future(f)
    tasks.append(task)
# 创建一个事件循环对象
loop = asyncio.get_event_loop()
# 将封装好的协程对象注册到事件循环对象中去
loop.run_until_complete(asyncio.wait(tasks))
print(time.time()-start)