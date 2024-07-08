import time
import multiprocessing

# def sleep():
#     print(f"sono nella funzione")

#     time.sleep(1)

#     print(f"sto uscendo dalla funzione")

# if __name__ == "__main__":

#     tic = time.time()

#     t1 = multiprocessing.Process(target=sleep)
#     t2 = multiprocessing.Process(target=sleep)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     toc = time.time()
#     time_elapsed = toc - tic

#     print(f"{time_elapsed=}")

def decorator(func):

    def wrapper(*args):

        tic = time.time()

        func(*args)

        print(f"{time.time() - tic}")

    return wrapper

@decorator
def esempio(name):
    print(f"ciao, {name}")

esempio("mario")