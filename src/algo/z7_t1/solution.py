
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""
word = 'abc'

def split_to_syllables(word: str) -> list[str]:
    if len(word) < 2:
        return 'Word has to be at least 2 characters'
    else:
        list_of_syllables = []
        for i in range(len(word)-1):
            syllable = word[i]+word[i+1]
            list_of_syllables.append(syllable)
        return list_of_syllables

result = split_to_syllables(word)
print(result)
