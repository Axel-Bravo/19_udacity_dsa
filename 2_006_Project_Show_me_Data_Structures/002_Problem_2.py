#%% Import and function declaration
import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if len(os.listdir(path)) == 0:  # Stopping condition
        return []

    path_elements = os.listdir(path)
    path_files = [file for file in path_elements if '.' + suffix in file]
    path_folders = [file for file in path_elements if '.' not in file]

    for folder in path_folders:
        path_files.extend(find_files(suffix='c', path=path + '/' + folder))

    return path_files


#%% Testing

path_base = os.getcwd() + '/testdir'
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']
