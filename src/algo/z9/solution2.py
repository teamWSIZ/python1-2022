"""
Semantic versioning
https://devopedia.org/images/article/279/7179.1593248779.png

{Major}.{Minor}.{Patch}

np.

'1.3.6' oznacza major=1, minor=3, path=6


"""


def get_latest(versions: list[str]) -> str:
    """
    :return: Latest semantic version from the given `versions`
    """
    latest_version = versions[0]
    
    for version in versions[1:]:
        if is_higher_version(version, latest_version):
            latest_version = version

    return latest_version

def is_higher_version(version: str, compared_version: str) -> bool:
    version_parts = version.split('.')
    compared_parts = compared_version.split('.')

    for i in range(3):
        if int(version_parts[i]) > int(compared_parts[i]):
            return True
        elif int(version_parts[i]) < int(compared_parts[i]):
            return False

    return False


def next_version(version: str, level: int) -> str:
    """
    :param version: Current version
    :param level: Which part should be incremented; 0: major, 1: minor, 2: patch
    :return: Properly incremented version
    """
    version_list = version.split('.')
    for i in range(len(version_list)):
        version_list[i] = int(version_list[i])
    if level == 0:
        version_list[0] += 1
        version_list[1] = 0
        version_list[2] = 0
    elif level == 1:
        version_list[1] += 1
        version_list[2] = 0
    elif level == 2:
        version_list[2] += 1

    final_version = str(version_list[0]) + '.' + str(version_list[1])+ '.' + str(version_list[2])
    return final_version
