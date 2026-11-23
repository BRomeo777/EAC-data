import urllib.request, urllib.parse, json

countries = {
    'RWA': 'Rwanda', 'KEN': 'Kenya', 'UGA': 'Uganda',
    'TZA': 'Tanzania', 'BDI': 'Burundi', 'SSD': 'South Sudan', 'COD': 'DR Congo',
}

# 2019 baselines and 2024 values from Table 2
data = {
    'Rwanda':       {'DTP1': (99, 99), 'DTP3': (98, 98), 'MCV1': (96, 97)},
    'Kenya':        {'DTP1': (96, 93), 'DTP3': (93, 91), 'MCV1': (92, 82)},
    'Uganda':       {'DTP1': (96, 97), 'DTP3': (93, 94), 'MCV1': (87, 92)},
    'Tanzania':     {'DTP1': (95, 87), 'DTP3': (91, 83), 'MCV1': (89, 84)},
    'Burundi':      {'DTP1': (97, 89), 'DTP3': (93, 89), 'MCV1': (92, 86)},
    'South Sudan':  {'DTP1': (68, 76), 'DTP3': (61, 73), 'MCV1': (65, 72)},
    'DR Congo':     {'DTP1': (84, 82), 'DTP3': (73, 65), 'MCV1': (65, 55)},
}

def classify(diff, threshold):
    if diff >= threshold:
        return 'clear'
    elif diff >= -1:  # within ±1pp
        return 'marginal'
    else:
        return 'not recovered'

def overall_class(indicators_status):
    if any(s == 'not recovered' for s in indicators_status):
        return 'Not recovered'
    elif all(s == 'clear' for s in indicators_status):
        return 'Clear'
    else:
        return 'Marginal'

print("THRESHOLD SENSITIVITY ANALYSIS")
print("=" * 90)
print(f"{'Country':15s} | {'2pp cutoff':20s} | {'1pp cutoff':20s} | {'3pp cutoff':20s}")
print("-" * 90)

for country, inds in data.items():
    results = {}
    for thresh in [1, 2, 3]:
        statuses = []
        for ind_name in ['DTP1', 'DTP3', 'MCV1']:
            base, val_2024 = inds[ind_name]
            diff = val_2024 - base
            statuses.append(classify(diff, thresh))
        results[thresh] = overall_class(statuses)
    
    print(f"{country:15s} | {results[2]:20s} | {results[1]:20s} | {results[3]:20s}")

print("\n" + "=" * 90)
print("\nDetailed per-indicator diffs:")
print(f"{'Country':15s} {'DTP1':>6s} {'DTP3':>6s} {'MCV1':>6s}")
for country, inds in data.items():
    diffs = []
    for ind_name in ['DTP1', 'DTP3', 'MCV1']:
        base, val_2024 = inds[ind_name]
        diffs.append(val_2024 - base)
    print(f"{country:15s} {diffs[0]:+6d} {diffs[1]:+6d} {diffs[2]:+6d}")

# Now get birth cohort data for zero-dose estimation
print("\n\nZERO-DOSE CHILDREN ESTIMATION")
print("=" * 90)

# Try to get birth cohort data from GHO API
# WHO indicator for births: WUENIC_BIRTHS or similar
birth_codes = ['WUENIC_BIRTHS', 'BIRTHS', 'WHS_BIRTHS']
birth_data = {}

for code in birth_codes:
    try:
        url = f'https://ghoapi.azureedge.net/api/{code}'
        data = json.loads(urllib.request.urlopen(url, timeout=15).read())
        print(f"{code}: Found! {len(data.get('value', []))} records")
        birth_data = data
        break
    except:
        pass

if not birth_data:
    # Try searching indicator metadata
    params = urllib.parse.urlencode({'$filter': "contains(IndicatorName, 'birth')"})
    url = f'https://ghoapi.azureedge.net/api/Indicator?{params}'
    data = json.loads(urllib.request.urlopen(url, timeout=15).read())
    print(f"\nIndicators matching 'birth': {len(data['value'])}")
    for ind in data['value'][:15]:
        print(f"  {ind['IndicatorCode']}: {ind['IndicatorName']}")
