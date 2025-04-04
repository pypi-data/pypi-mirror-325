from pathlib import Path
from typing import Union

__NOT_FOUND = -1

UNIX_NAME_SEPARATORS = "/"
WINDOWS_NAME_SEPARATORS = "\\"


def __require_non_null_chars(filepath: Union[str, Path]) -> str:
    if filepath is None:
        raise ValueError("Filepath is null")
    if str(filepath).find("\x00") > -1:
        raise ValueError(
            "Null character present in file/path name. There are no known legitimate use cases for such data, but several injection attacks may use it"
        )
    return str(filepath)


def index_of_last_separator(filepath: Union[str, Path]) -> int:
    if filepath is None:
        return __NOT_FOUND
    last_unix_pos = str(filepath).rfind(UNIX_NAME_SEPARATORS)
    last_windows_pos = str(filepath).rfind(WINDOWS_NAME_SEPARATORS)
    return max(last_unix_pos, last_windows_pos)


def get_name(filepath: Union[str, Path]) -> str | None:
    """
    Gets the name minus the path from a full file name.
    This method will handle a file in either UNIX or Windows format. The text after the last forward or backslash is returned.

     a/b/c.txt --> c.txt
     a\b\c.txt --> c.txt
     a.txt     --> a.txt
     a/b/c     --> c
     a/b/c/    --> ""

    The output will be the same irrespective of the machine that the code is running on.

    :param filepath: the file name, null returns null
    :return: the name of the file without the path, or an empty string if none exists
    """

    if filepath is None:
        return None

    return __require_non_null_chars(filepath)[index_of_last_separator(filepath) + 1:]
