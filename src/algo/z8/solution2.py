
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

Zadanie -- mamy dostępny zbiór sylab, oraz pewne słowo `word`; pytanie -- czy przy użyciu tych sylab
(każdą można użyć dowolną liczbę razy, również 0) można utworzyć dane słowo.

"""


def construct_word(syllables: set[str], word: str) -> bool:
    if len(word) < 2:
        return 'Word has to be at least 2 characters'
    else:
        list_of_syllables = []
        for i in range(len(word)-1):
            syllable = word[i]+word[i+1]
            list_of_syllables.append(syllable)
        for j in list_of_syllables:
            if j in syllables:
                continue 
            else:
                return False 
                break
        return True
