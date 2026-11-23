import urllib.request, urllib.parse, json

countries = {
    'RWA': 'Rwanda', 'KEN': 'Kenya', 'UGA': 'Uganda',
    'TZA': 'Tanzania', 'BDI': 'Burundi', 'SSD': 'South Sudan', 'COD': 'DR Congo',
}

indicators = {'DTP1': 'VACCINECOVERAGE_DTP1', 'DTP3': 'WHS4_100', 'MCV1': 'WHS8_110'}

# 2019 baselines from Table 2
baselines = {
    'Rwanda': {'DTP1': 99, 'DTP3': 98, 'MCV1': 96},
    'Kenya': {'DTP1': 96, 'DTP3': 93, 'MCV1': 92},
    'Uganda': {'DTP1': 96, 'DTP3': 93, 'MCV1': 87},
    'Tanzania': {'DTP1': 95, 'DTP3': 91, 'MCV1': 89},
    'Burundi': {'DTP1': 97, 'DTP3': 93, 'MCV1': 92},
    'South Sudan': {'DTP1': 68, 'DTP3': 61, 'MCV1': 65},
    'DR Congo': {'DTP1': 84, 'DTP3': 73, 'MCV1': 65},
}

# 2024 values from Table 2
vals_2024 = {
    'Rwanda': {'DTP1': 99, 'DTP3': 98, 'MCV1': 97},
    'Kenya': {'DTP1': 93, 'DTP3': 91, 'MCV1': 82},
    'Uganda': {'DTP1': 97, 'DTP3': 94, 'MCV1': 92},
    'Tanzania': {'DTP1': 87, 'DTP3': 83, 'MCV1': 84},
    'Burundi': {'DTP1': 89, 'DTP3': 89, 'MCV1': 86},
    'South Sudan': {'DTP1': 76, 'DTP3': 73, 'MCV1': 72},
    'DR Congo': {'DTP1': 82, 'DTP3': 65, 'MCV1': 55},
}

print("SENSITIVITY CHECK: Would including 2025 data change recovery status?")
print("=" * 80)

for ind_name, ind_code in indicators.items():
    params = urllib.parse.urlencode({'$filter': 'TimeDim eq 2025'})
    url = f'https://ghoapi.azureedge.net/api/{ind_code}?{params}'
    data = json.loads(urllib.request.urlopen(url, timeout=30).read())
    
    for code3, name in countries.items():
        records = [r for r in data['value'] if r['SpatialDim'] == code3]
        if records:
            val_2025 = int(records[0]['NumericValue'])
            base = baselines[name][ind_name]
            v24 = vals_2024[name][ind_name]
            diff_2024 = v24 - base
            diff_2025 = val_2025 - base
            
            # Check if recovery status would change
            status_2024 = "recovered" if diff_2024 >= 0 else "not recovered"
            status_2025 = "recovered" if diff_2025 >= 0 else "not recovered"
            change = " *** STATUS CHANGE ***" if status_2024 != status_2025 else ""
            
            if change or name in ['Rwanda', 'Uganda']:  # Show borderline countries always
                print(f"  {name:15s} {ind_name}: 2019={base}, 2024={v24} ({diff_2024:+d}), 2025={val_2025} ({diff_2025:+d}){change}")

print("\n" + "=" * 80)
print("FULL 2025 DATA FOR ALL COUNTRIES:")
print("=" * 80)
for ind_name, ind_code in indicators.items():
    params = urllib.parse.urlencode({'$filter': 'TimeDim eq 2025'})
    url = f'https://ghoapi.azureedge.net/api/{ind_code}?{params}'
    data = json.loads(urllib.request.urlopen(url, timeout=30).read())
    print(f"\n  {ind_name}:")
    for code3, name in countries.items():
        records = [r for r in data['value'] if r['SpatialDim'] == code3]
        if records:
            val = int(records[0]['NumericValue'])
            base = baselines[name][ind_name]
            print(f"    {name:15s}: 2025={val} (vs 2019={base}, diff={val-base:+d})")
