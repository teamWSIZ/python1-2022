from complete_scan_thru_subsequences import get_bin_representation


def get_best_value_package(costs: list[int], values: list[int], max_total_cost: int) -> int:
    # znaleźć najlepszą możliwą wartość podzbioru itemów, ale takich by łączny "cost" tych itemów nie przekraczał
    # wartości max_total_cost
    pass

    if len(costs) == len(values):
        N = len(values)
        for mask in range(2 ** N):
            list_val = []
            list_cost = []
            maska = get_bin_representation(mask, N)
            for i in range(N):
                list_val.append(values[i]) if maska[i] == "1" else None
                list_cost.append(costs[i]) if maska[i] == "1" else None

            if sum(list_cost) == max_total_cost:
                return sum(list_val)
    else:
        return 0