#!/usr/bin/python3
"""
Contains one function: compile(). compile() searches a directory
for any file with a '.c' extension and compiles it into a shared object
file by calling gcc from the command line.
"""
import os


def compile(path='./') -> None:
    """Searches the directory at the provided path for .c files and compiles them
    into shared objects with gcc."""
    source_files = [x for x in os.listdir(path) if x[0] != '.' and x.split('.')[-1]=='c']
    for source_file in source_files:
        base = source_file.split('.')[0]
        so_name = base + '.so'
        print(f'{source_file} found')
        command = f'gcc -shared -O3 -o {so_name} -fPIC {source_file}'
        print(f'{source_file} compiled as shared object file')
        os.system(command)


if __name__ == '__main__':
    compile()
