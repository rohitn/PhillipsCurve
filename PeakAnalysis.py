def find_peak(data, cutoff):
    slope = None
    peak_value = None
    peak_diff_list = []
    for i, v in enumerate(data):
        if i == 0:
            peak_value = v
            continue
        new_slope = v - data[i - 1]
        if slope is None:
            slope = new_slope
        else:
            if slope * new_slope < 0:
                diff = data[i - 1] - peak_value
                peak_diff_list.append((diff, i - 1))
                peak_value = data[i - 1]
                slope = new_slope

    selected = []
    modified = data.copy()

    real_peak = _mark_real_peaks_v2(peak_diff_list, cutoff)
    _remove_ambiguous_peak(real_peak, peak_diff_list, data)

    for i, t in enumerate(peak_diff_list):
        if i < len(peak_diff_list) - 1:
            if real_peak[i] == 1:
                if real_peak[i + 1] == 1:
                    continue
                else:
                    for j in range(i + 1, len(peak_diff_list)):
                        if real_peak[j] == 1:
                            idx = t[1]
                            next_idx = peak_diff_list[j][1]
                            slope = (modified[next_idx] - modified[idx]) / (next_idx - idx)
                            for k in range(idx, next_idx):
                                modified[k] = modified[idx] + (k - idx) * slope
                            break
  
    _remove_duplicate_peak(real_peak)
    for i, rp in enumerate(real_peak):
        if rp == 1:
            selected.append(peak_diff_list[i][1])

    return modified, selected


def _remove_duplicate_peak(real_list):
    for i in range(len(real_list)):
        if real_list[i] == 0:
            continue
        else:
            # 다음 1이 같은 parity면 자기 자신을 제거
            for j in range(i + 1, len(real_list)):
                if real_list[j] == 1:
                    if i % 2 == j % 2:
                        real_list[i] = 0
                    break
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
