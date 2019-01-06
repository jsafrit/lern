"""
This week, we'll write a function that takes a function as an argument.  Actually, the function takes two arguments:
    - a directory name (string)
    - a function
The function will be applied to each file in the directory.

The output from the function's execution on each file will be returned as part of a dictionary, in which the
filenames are the keys and the results are the values.

For example, if we call
    import os

    def file_length(filename):
    return os.stat(filename).st_size

    success_dict, failure_dict = filefunc('/etc/', file_length)

The result will be two dictionaries:
    - first dictionary's keys are the filenames and the output from running the function, when no exception was raised
    - second dictionary's keys are the filenames and the exception object when one was raised.
So in the above call, if no exceptions were raised, then the first dictionary returned would consist of the
fienames in /etc/, with the length of each file as a value.  The second dictionary would be empty.
"""
import os
from pathlib import Path


def file_length(filename):
    return os.stat(filename).st_size


def filefunc(dir_name, func):
    good_dict=dict()
    bad_dict=dict()
    p = Path(dir_name)
    for child in p.iterdir():
        print(child)
        try:
            result=func(child)
            good_dict[child]=result
        except Exception as e:
            bad_dict[child]=e
    return good_dict, bad_dict


def filefunc2(dir_name, func):
    good_dict=dict()
    bad_dict=dict()
    for directory, subdirectories, files in os.walk(dir_name):
        for file in files:
            print(file)
            try:
                full_filename=os.path.join(directory, file)
                result=func(full_filename)
                good_dict[file]=result
            except Exception as e:
                bad_dict[file]=e
    return good_dict, bad_dict


if __name__ == '__main__':
    success_dict, failure_dict = filefunc('c:\\bin\\', file_length)
    print(success_dict, failure_dict)
