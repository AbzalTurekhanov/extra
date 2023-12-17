import os
import shutil
from functools import wraps
from time import perf_counter


def timer(printable=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = perf_counter()
            result = func(*args, **kwargs)
            end_time = perf_counter()
            elapsed_time = f"{(end_time - start_time):.6f} seconds"
            if printable:
                print(result)
            print(f'Execution time of {func.__name__}: {elapsed_time}')
            return result

        return wrapper
    return decorator


def error_catcher(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            raise CommandPromptError(f'Invalid input for {func.__name__} method. Please enter  valid choice.')
    return wrapper


class CommandPromptError(BaseException):
    pass


class CommandPrompt:

    #operations with both directories and files
    @staticmethod
    @timer(False)
    @error_catcher
    def mv(old_name, new_name):
        return os.rename(old_name, new_name)


    #operations with directories
    @staticmethod
    @timer()
    @error_catcher
    def ls():
        text = "\n".join(os.listdir())
        return f'files in the current directory:\n {text}'

    @staticmethod
    @timer(False)
    @error_catcher
    def cd(path):
        return os.chdir(path)

    @staticmethod
    @timer()
    @error_catcher
    def pwd():
        return os.getcwd()

    @staticmethod
    @timer(False)
    @error_catcher
    def mkdir(path):
        try:
            return os.mkdir(path)
        except:
            return os.mkdirs(path)

    @staticmethod
    @timer(False)
    @error_catcher
    def rmdir(path):
        return shutil.rmtree(path)


    #operations with files
    @staticmethod
    @timer()
    @error_catcher
    def cat(file):
        return open(file).read()

    @staticmethod
    @timer(False)
    @error_catcher
    def touch(file):
        return open(file, 'w')

    @staticmethod
    @timer(False)
    @error_catcher
    def rm(file):
        return os.remove(file)

