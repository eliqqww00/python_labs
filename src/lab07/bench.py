import csv
import timeit
import random
from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

def new_data():
    ''' генерирует списки с рандомными числами'''
    sizes = (1_000,10_000,100_000)
    for n in sizes:
        nums = [random.randint(-1_000_000,1_000_000) for _ in range(n)]
        rows = [[x] for x in nums]
        write_csv(rows,f'data/lab07/samples/{n}_sort.csv',header=('value',))

def read_numbers(path):
    ''' считывает данные из csv '''
    with open(path, encoding="utf-8") as f:
        return [int(row["value"]) for row in csv.DictReader(f)]

def bench_sorts():
    rows=[]
    for n in (1_000,10_000,100_000):
        data = read_numbers(f'data/lab07/samples/{n}_sort.csv')
        funcs = [("bubble_sort", bubble_sort), ("insertion_sort", insertion_sort), ("selection_sort", selection_sort)]

        for name, fc in funcs:
            if n<=10_000:
                time = timeit.timeit(lambda: fc(data), number=1)
                rows.append(("sorting", n, name, f"{time:.6f}"))
            else:
                rows.append(("sorting", n, name, ">60"))
    return rows

def bench_search():
    rows=[]
    data = read_numbers(f'data/lab07/samples/100000_sort.csv')
    targets = [random.choice(data) for _ in range(10_000)]

    # --- линейный поиск ---
    time_ls = timeit.timeit(lambda: [linear_search(data,t) for t in targets],  number =1)
    rows.append(("search", 100_000, "linear_search", f"{time_ls:.6f}"))

    # --- бинарный поиск ---
    time_sbb=timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("search", 100_000, "sort_before_binary", f"{time_sbb:.6f}"))
    sorted_data= sorted(data)

    time_bs = timeit.timeit(lambda: [binary_search(sorted_data,t) for t in targets],  number =1)
    rows.append(("search", 100_000, "binary_search", f"{time_bs:.6f}"))

    # --- суммы ---
    for n in (1_000,10_000):
        data_ts = read_numbers(f'data/lab07/samples/{n}_sort.csv')
        a, b = random.sample(data_ts, 2)
        target = a+b

        time_tsb = timeit.timeit(lambda: two_sum_brute(data_ts,target), number=1)
        rows.append(("search", n, "two_sum_brute", f"{time_tsb:.6f}"))

        time_tsf = timeit.timeit(lambda: two_sum_fast(data_ts,target), number=1)
        rows.append(("search", n, "two_sum_fast", f"{time_tsf:.6f}"))

    return rows

def main():
    random.seed(42)
    new_data() #создаем три файла

    header = ("task", "n", "func", "seconds")
    rows=[]
    rows.extend(bench_sorts())
    rows.extend(bench_search())

    write_csv(rows, 'data/lab07/bench_result.csv', header)

    print("Результаты бенчмарка")
    print(f"{'Task':<12} | {'N':<8} | {'Func':<20} | {'Seconds':<12}")
    print('-'*60)
    for t, n, f, s in rows:
        print(f"{t:<12} | {n:<8} | {f:<20} | {s:<12}")
    print('-'*60)
    print("Результаты сохранены в data/lab07/bench_result.csv")


if __name__ == "__main__":
    main()