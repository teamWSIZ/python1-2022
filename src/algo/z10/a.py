
def longest_streak(s):
    longest_streak = 0 
    streak = 1 
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            streak += 1
        else: 
            if streak > longest_streak:
                longest_streak = streak
            streak = 1
    return longest_streak


