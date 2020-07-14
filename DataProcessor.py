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
if __name__ == '__main__':
    inflation, unemployment = load_data()
    # why not use mark real peaks, remove ambiguous peaks?
    mod_inf, peak_inf = PeakAnalysis.find_peak(inflation, 0.6)
    mod_une, peak_une = PeakAnalysis.find_peak(unemployment, 0.7)

    matched = match_peaks(mod_inf, peak_inf, mod_une, peak_une)
