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
