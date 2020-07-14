import PeakAnalysis

def load_data():

    f = open('data/data.csv')

    # create empty list
    inflation = []
    unemployment = []

    # infinite loop
    while True:
        # read a single line from file
        line = f.readline()
        # stops when the content is empty
        if len(line) == 0:
            break
        # split line by ','
        [inf, unemp] = line.split(',')
        # cast to float and append to the list
        inflation.append(float(inf))
        unemployment.append(float(unemp))

    # closes the file
    f.close()

    return inflation, unemployment

def match_peaks(inf, peak_inf, une, peak_une):
    is_upward = inf[peak_inf[0]] < inf[peak_inf[1]]
# inflation 이 unemployment 의 변화에 영향을 미친다 -- inflation 의 첫 peak 를 가지고 첫번째 opposite 을 찾아냄
    first_opposite = 0
    while first_opposite < len(peak_une):
        if is_upward and (une[peak_une[first_opposite]] > une[peak_une[first_opposite + 1]]):
            break
        if not is_upward and (une[peak_une[first_opposite]] < une[peak_une[first_opposite + 1]]):
            break
        first_opposite += 1

    matched = []
    j = 0
    for i in range(first_opposite, len(peak_une)):
        matched.append((peak_inf[j], peak_une[i]))
        j += 1
    return matched

# peaks: list of integers --> each element indicates the position of peak in data
# peak 사이 diff 를 num slices 20 만큼으로 나눠서 그 step 만큼 data 를 가지고 interpolate

def interpolate_peaks(data, peaks: list, num_slices=20):
    new_data = []
    for curr_idx in range(len(peaks) - 1):
        next_idx = curr_idx + 1

        curr_peak = peaks[curr_idx]
        next_peak = peaks[next_idx]

        step = (next_peak - curr_peak) / num_slices
        for s in range(num_slices):
            pos = curr_peak + s * step
            smaller = int(pos)
            if pos == smaller:
                new_data.append(data[smaller])
            else:
                # smaller == pos 인 경우 smaller == larger 이니까 이렇게 else를 larger = smaller + 1 으로
                larger = smaller + 1
                slope = data[larger] - data[smaller]
                new_data.append(data[smaller] + slope * (pos - smaller))

    new_data.append(data[peaks[-1]])
    return new_data



if __name__ == '__main__':
    inflation, unemployment = load_data()
    # why not use mark real peaks, remove ambiguous peaks?
    mod_inf, peak_inf = PeakAnalysis.find_peak(inflation, 0.6)
    mod_une, peak_une = PeakAnalysis.find_peak(unemployment, 0.7)

    matched = match_peaks(mod_inf, peak_inf, mod_une, peak_une)

    interpolated_inf = interpolate_peaks(mod_inf, list(map(lambda t: t[0], matched)))
    interpolated_une = interpolate_peaks(mod_une, list(map(lambda t: t[1], matched)))

    assert(len(interpolated_inf) == len(interpolated_une))

    # with EXPRESSION as NAME:
    with open('interpolated_data.csv', 'w') as f:
        for idx in range(len(interpolated_inf)):
            f.write(str(interpolated_inf[idx]) + ',' + str(interpolated_une[idx]) + '\n')