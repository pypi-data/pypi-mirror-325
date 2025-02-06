import sys
import os
import traceback


def insert(dir_name: str, env_index=0, dir_index=-1) -> bool:
    if os.path.isabs(dir_name):
        sys.path.insert(env_index, os.path.dirname(dir_name))
        return True
    stack = traceback.extract_stack()
    caller_file_path = stack[-2].filename
    current_path = os.path.abspath(caller_file_path)
    directories = current_path.split(os.sep)
    mygithub_path = []
    for i, part in enumerate(directories):
        if dir_name == part:
            dir_path = os.path.join(os.sep, *directories[:i + 1])
            if ':' in dir_path:
                dir_path = dir_path.replace(':',':\\')
            mygithub_path.append(dir_path)
    if not mygithub_path:
        raise "Insert env path error to not find dir_name."
    if os.path.isabs(mygithub_path[dir_index]):
        sys.path.insert(env_index, os.path.dirname(mygithub_path[dir_index]))
        return True
    else:
        raise "Insert env path failed."
