from datetime import datetime

def sort_numbers(nums: list[int]) -> list[int]:
    ret = sorted(nums)
    return ret


if __name__ == '__main__':
    w = [1 ,53,2 , 6, 100,3 ,2 ,7 ]
    repetitions = 1000
    time_sum = 0
    for i in range(repetitions):
        st = datetime.now().timestamp()
        ret = sort_numbers(w)
        en = datetime.now().timestamp()
        time_sum += (en-st)

    print(f'czas wykowyaniwa {time_sum / repetitions: .6f} s')