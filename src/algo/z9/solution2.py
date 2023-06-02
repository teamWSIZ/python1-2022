"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def parse_version(version: str) -> list[int]:
    return [int(x) for x in version.split('.')]


def verbose_version(version: list[int]):
    return '.'.join([str(x) for x in version])


def get_latest(versions: list[str]) -> str:
    """
    :return: Latest semantic version from the given `versions`
    """
    max_ = [0, 0, 0]
    for v in versions:
        max_ = max(max_, parse_version(v))
    return verbose_version(max_)


def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """
    # todo: your code
    ver = parse_version(version)
    if level == 2:
        ver[2] += 1
    elif level == 1:
        ver[1] += 1
        ver[2] = 0
    else:
        ver[0] += 1
        ver[1] = 0
        ver[2] = 0
    return verbose_version(ver)
