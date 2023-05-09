# 파일 입출력/실습문제 1(count_each_letter)
import os.path


def read_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            return [line.rstrip() for line in f.readlines()]


def count_letter(line, str_to_cnt):
    return line.count(str_to_cnt)


def get_statistics(freq_list):
    return sum(freq_list), sum(freq_list) / len(freq_list), max(freq_list), min(freq_list)


def write_result(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def main(read_path, write_path, str_to_cnt):
    line_list = read_file(read_path)
    freq_list = [count_letter(line, str_to_cnt) for line in line_list]
    freq_dict = dict(zip(['sum', 'avg', 'max', 'min'], get_statistics(freq_list)))
    print_str = ''
    for k, v in freq_dict.items():
        print_str = print_str + f'{k}: {v}\n'
    print(print_str)
    print_str = f'statics of {str_to_cnt}\n' + print_str
    write_result(write_path, print_str)


letter_to_check = input("which letter? (a-z): ")

file_path_to_read = 'example.txt'
file_path_to_write = 'statistics.txt'

main(file_path_to_read, file_path_to_write, letter_to_check)
print("file is saved at: %s" % file_path_to_write)
