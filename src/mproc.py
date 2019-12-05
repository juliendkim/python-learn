import os
from multiprocessing import Pool, Manager
import psutil
import codecs
import time


def read_lines(filename):
    with open(filename) as f:
        content = f.readlines()
        return [element.strip() for element in content]


def read_terms(filename):
    content = read_lines(filename)
    content.sort()
    content.sort(key=len, reverse=True)
    return content


def save_to_file(filename, list_to_save):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with codecs.open(filename, 'w', 'utf-8') as f:
        f.write('\n'.join(list_to_save))


def worker(args):
    proc_stime = time.time()
    proc_idx, haystack, needles = args
    for needle in needles:
        haystack = haystack.replace(needle, '#' * len(needle))

    print(proc_idx, os.getpid(), (time.time() - proc_stime), 'sec')

    return proc_idx, haystack


if __name__ == '__main__':

    stime = time.time()
    path = f'{os.path.dirname(os.path.abspath(__file__))}'
    terms = read_terms(f'{path}/mproc-term.txt')
    lines = read_lines(f'{path}/mproc-data.txt')

    cpu_cores = psutil.cpu_count()

    print(cpu_cores, len(lines))

    p = Pool(cpu_cores * 8)
    results = []
    print((time.time() - stime), 'sec')
    for idx, line in enumerate(lines):
        results = p.map(worker, [(idx, line, terms)])
        print((time.time() - stime), 'sec')
    for idx, row in results:
        lines[idx] = row
    save_to_file(f'{path}/mproc-result.txt', lines)
    print((time.time() - stime), 'sec')
