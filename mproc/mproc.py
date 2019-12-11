from multiprocessing import Pool, cpu_count, Array
import ctypes
import os


class Result(ctypes.Structure):
    _fields_ = [
        ('index', ctypes.c_int),
        ('term', ctypes.c_wchar_p),
        ('count', ctypes.c_int)
    ]


class ResultSentence(ctypes.Structure):
    _fields_ = [
        ('result_index', ctypes.c_int),
        ('index', ctypes.c_int),
        ('sentence', ctypes.c_wchar_p)
    ]


def worker(args):
    # result, result_sentence = args
    print(os.getpid(), args)
    # print(result.index.value, result_sentence.index.value)


def main():
    num_processes = cpu_count()

    rlen = 20
    results = []
    result_sentences = []
    for i in range(rlen):
        results.append((i, 'a' + ('b' * (i % 10)), 0))
        result_sentences.append((i, -1, ''))

    sh_results = Array(Result, results)
    sh_result_sentences = Array(ResultSentence, result_sentences)

    pool = Pool(processes=num_processes)
    pool.imap_unordered(worker, sh_results)
    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
