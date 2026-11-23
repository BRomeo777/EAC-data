
data = {
    'Rwanda':       {'DTP1': [99, 94, 94, 98, 94, 99], 'DTP3': [98, 91, 88, 98, 94, 98], 'MCV1': [96, 94, 87, 99, 96, 97]},
    'Kenya':        {'DTP1': [96, 97, 99, 99, 97, 93], 'DTP3': [93, 93, 95, 94, 93, 91], 'MCV1': [92, 89, 88, 85, 85, 82]},
    'Uganda':       {'DTP1': [96, 94, 97, 94, 95, 97], 'DTP3': [93, 89, 91, 89, 91, 94], 'MCV1': [87, 89, 90, 91, 91, 92]},
    'Tanzania':     {'DTP1': [95, 95, 90, 91, 87, 87], 'DTP3': [91, 91, 86, 87, 83, 83], 'MCV1': [89, 87, 80, 84, 84, 84]},
    'Burundi':      {'DTP1': [97, 98, 96, 93, 89, 89], 'DTP3': [93, 93, 94, 91, 89, 89], 'MCV1': [92, 90, 90, 89, 86, 86]},
    'South Sudan':  {'DTP1': [68, 71, 73, 76, 76, 76], 'DTP3': [61, 67, 69, 73, 73, 73], 'MCV1': [65, 69, 74, 72, 72, 72]},
    'DR Congo':     {'DTP1': [84, 83, 81, 81, 80, 82], 'DTP3': [73, 70, 65, 65, 60, 65], 'MCV1': [65, 62, 55, 56, 52, 55]},
}
years = [2019, 2020, 2021, 2022, 2023, 2024]

print("RECOVERY ONSET YEARS (first year >= 2019 baseline, sustained through 2024):")
print("=" * 90)
print(f"{'Country':15s} {'DTP1 onset':>12s} {'DTP3 onset':>12s} {'MCV1 onset':>12s} {'Sustained?':>12s}")
print("-" * 90)

for country, inds in data.items():
    onset = {}
    sustained_all = True
    for ind in ['DTP1', 'DTP3', 'MCV1']:
        baseline = inds[ind][0]
        first_year = None
        for i, yr in enumerate(years[1:], 1):
            if inds[ind][i] >= baseline:
                first_year = yr
                break
        if first_year is None:
            onset[ind] = '\u2014'
            sustained_all = False
        else:
            sustained = True
            for i, yr in enumerate(years[1:], 1):
                if yr >= first_year and inds[ind][i] < baseline:
                    sustained = False
                    break
            if sustained:
                onset[ind] = str(first_year)
            else:
                onset[ind] = f'{first_year}*'
                sustained_all = False
    sustained_str = 'Yes' if sustained_all else 'No'
    print(f"{country:15s} {onset['DTP1']:>12s} {onset['DTP3']:>12s} {onset['MCV1']:>12s} {sustained_str:>12s}")

print()
print("* = briefly reached baseline but subsequently fell below")
print("\u2014 = never reached baseline during 2020-2024")
