from __future__ import annotations


def merge_list(range_list, start_index=0):
    for i in range(start_index, len(range_list) - 1):
        if range_list[i][1] > range_list[i + 1][0]:
            new_start = range_list[i][0]
            new_end = max(range_list[i + 1][1], range_list[i][1])
            range_list[i] = [new_start, new_end]
            del range_list[i + 1]
            return merge_list(range_list.copy(), start_index=i)
    return range_list


def check_size_eq(lst: list[list[bool]], master_list: list[list[bool]]):
    phase_len = len(lst)
    usecase_len = len(lst[0])
    return phase_len == len(master_list) and usecase_len == len(master_list[0])
