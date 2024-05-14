import threading

x=0

def foo():
    global x
    for i in range(10000000):
        x+=1
def bar():
    global x
    for i in range(10000000):
        x-=1

t0 = threading.Thread(target=foo)
t1 = threading.Thread(target=bar)
t0.start()
t1.start()
t0.join()
t1.join()

print(x)

# Output: 0이 나오지 않는다. 왜냐하면 x를 동시에 읽고 쓰기 때문에 값이 꼬인다.