import os
from multiprocessing import Pool, Manager
import psutil
import codecs


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
    idx, haystack, needles = args
    for needle in needles:
        haystack = haystack.replace(needle, '#' * len(needle))

    print(os.getpid())

    return idx, haystack


if __name__ == '__main__':

    path = f'{os.path.dirname(os.path.abspath(__file__))}'
    terms = read_terms(f'{path}/mproc-term.txt')
    lines = read_lines(f'{path}/mproc-data.txt')

    cpu_cores = psutil.cpu_count()

    p = Pool(cpu_cores * 2)
    for idx, line in enumerate(lines):
        print(p.map(worker, [(idx, line, terms)]))

    save_to_file(f'{path}/mproc-result.txt', lines)
