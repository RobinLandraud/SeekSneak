Menchart = [
    {'EU': 35.5, 'US': 3.5},
    {'EU': 36, 'US': 4},
    {'EU': 36.5, 'US': 4.5},
    {'EU': 37.5, 'US': 5},
    {'EU': 38, 'US': 5.5},
    {'EU': 38.5, 'US': 6},
    {'EU': 39, 'US': 6.5},
    {'EU': 40, 'US': 7},
    {'EU': 40.5, 'US': 7.5},
    {'EU': 41, 'US': 8},
    {'EU': 42, 'US': 8.5},
    {'EU': 42.5, 'US': 9},
    {'EU': 43, 'US': 9.5},
    {'EU': 44, 'US': 10},
    {'EU': 44.5, 'US': 10.5},
    {'EU': 45, 'US': 11},
    {'EU': 45.5, 'US': 11.5},
    {'EU': 46, 'US': 12},
    {'EU': 47, 'US': 12.5},
    {'EU': 47.5, 'US': 13},
    {'EU': 48, 'US': 13.5},
    {'EU': 48.5, 'US': 14},
    {'EU': 49.5, 'US': 15},
    {'EU': 50.5, 'US': 16},
    {'EU': 51.5, 'US': 17},
    {'EU': 52.5, 'US': 18}
]

def MenChartUEtoUS(size):
    for elem in Menchart:
        if elem['EU'] == size:
            return elem['US']
    return -1

def MenChartUStoEU(size):
    for elem in Menchart:
        if elem['US'] == size:
            return elem['EU']
    return -1