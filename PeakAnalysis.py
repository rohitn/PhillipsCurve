def _remove_ambiguous_peak(real_list, peak_list, data):
    i = 0
    while i < len(real_list):
        is_peak = real_list[i] == 1

        if is_peak:
            peak_idx = peak_list[i][1]
            is_upward = peak_list[i][0] > 0
            j = i + 1
            while j < len(real_list):
                is_next_peak = real_list[j] == 1
                if is_next_peak:
                    break
                j += 1

            if j == len(real_list):
                break
            is_same_parity = i % 2 == j % 2
            if is_same_parity:
                # 값이 작아졌어야 하는데 커졌는가 (vice versa)
                # 잘못됐으면 j위치의 real_list = 0
                next_peak_idx = peak_list[j][1]
                if is_upward:
                    if data[peak_idx] <= data[next_peak_idx]:
                        i = j
                    else:
                        real_list[j] = 0
                else:
                    if data[peak_idx] >= data[next_peak_idx]:
                        i = j
                    else:
                        real_list[j] = 0
            else:
                i = j
        else:
            i += 1
def _mark_real_peaks_v2(peak_list, tol):
    real_list = [1 for _ in range(len(peak_list))]

    idx = 0
    while idx < len(peak_list):
        diff = peak_list[idx][0]
        if abs(diff) < tol:
            real_list[idx] = 0
            idx += 1

        idx += 1

    return real_list
