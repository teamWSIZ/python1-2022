
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""


def split_to_syllables(word: str) -> list[str]:
    result = []
    first = word[0]
    last = word[-1]
    result.append(first*2)
    for i in range(len(word) - 1):
        short = word[i] + word[i+1]
        result.append(short)
    result.append(last*2)
    return result

