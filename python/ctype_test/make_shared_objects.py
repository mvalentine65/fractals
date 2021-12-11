#!/usr/bin/python3
import os

def compile(path='./') -> None:
    source_files = [x for x in os.listdir(path) if x[0] != '.' and x.split('.')[-1]=='c']
    for source_file in source_files:
        base = source_file.split('.')[0]
        so_name = base + '.so'
        print(f'{source_file} found')
        command = f'gcc -shared -o {so_name} -fPIC {source_file}'
        print(f'{source_file} compiled as shared object file')
        os.system(command)


if __name__ == '__main__':
    compile()
