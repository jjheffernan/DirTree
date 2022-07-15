import sys
import os

filename = '.'


def get_files(filename):
    # files = os.listdir(filename)
    for root, dirs, files in os.walk(filename, False, ):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))

    # for item in files:
    #     spec_file = print_dict() + item
    #     if os.path.isdir(spec_file):
    #         get_files(item)
    #     elif os.path.isfile(spec_file):
    #         print(item)
    #     else:
    #         print('unknown filetype')
    # return os.listdir()
    # pass


def print_dict():
    return os.getcwd()
    # pass


def print_file():
    files = [get_files()]
    print(files)
    # for expansion


def main(filename):
    # find_dir = input('input directory to print: ')
    print(str(get_files(filename)))
    # print_dict()
    return


if __name__ == '__main__':
    filename = sys.argv[0]
    if filename is None:
        filename = '/test'
    main(filename)
