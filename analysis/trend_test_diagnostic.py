"""
Diagnostic: would Mann-Kendall / Sen's slope be informative on these series?
Exact permutation p-values (n=6 -> 720 permutations, fully enumerable).
"""
from itertools import permutations
from statistics import median

DATA = {
    ('Burundi', 'DTP1'): [97, 98, 96, 93, 89, 89],
    ('Burundi', 'DTP3'): [93, 93, 94, 91, 89, 89],
    ('Burundi', 'MCV1'): [92, 90, 90, 89, 86, 86],
    ('DR Congo', 'DTP1'): [84, 83, 81, 81, 80, 82],
    ('DR Congo', 'DTP3'): [73, 70, 65, 65, 60, 65],
    ('DR Congo', 'MCV1'): [65, 62, 55, 56, 52, 55],
    ('Kenya', 'DTP1'): [96, 97, 99, 99, 97, 93],
    ('Kenya', 'DTP3'): [93, 93, 95, 94, 93, 91],
    ('Kenya', 'MCV1'): [92, 89, 88, 85, 85, 82],
    ('Rwanda', 'DTP1'): [99, 94, 94, 98, 94, 99],
    ('Rwanda', 'DTP3'): [98, 91, 88, 98, 94, 98],
    ('Rwanda', 'MCV1'): [96, 94, 87, 99, 96, 97],
    ('South Sudan', 'DTP1'): [68, 71, 73, 76, 76, 76],
    ('South Sudan', 'DTP3'): [61, 67, 69, 73, 73, 73],
    ('South Sudan', 'MCV1'): [65, 69, 74, 72, 72, 72],
    ('Tanzania', 'DTP1'): [95, 95, 90, 91, 87, 87],
    ('Tanzania', 'DTP3'): [91, 91, 86, 87, 83, 83],
    ('Tanzania', 'MCV1'): [89, 87, 80, 84, 84, 84],
    ('Uganda', 'DTP1'): [96, 94, 97, 94, 95, 97],
    ('Uganda', 'DTP3'): [93, 89, 91, 89, 91, 94],
    ('Uganda', 'MCV1'): [87, 89, 90, 91, 91, 92],
}

def sign(v):
    return (v > 0) - (v < 0)

def mk_S(x):
    n = len(x)
    return sum(sign(x[j] - x[i]) for i in range(n) for j in range(i + 1, n))

def sens_slope(x):
    n = len(x)
    return median([(x[j] - x[i]) / (j - i) for i in range(n) for j in range(i + 1, n)])

def exact_p(x):
    """Two-sided permutation p-value for Mann-Kendall S."""
    s_obs = abs(mk_S(x))
    perms = list(permutations(x))
    extreme = sum(1 for p in perms if abs(mk_S(list(p))) >= s_obs)
    return extreme / len(perms)

def n_ties(x):
    return len(x) - len(set(x))

print('=' * 88)
print('MANN-KENDALL / SEN\'S SLOPE DIAGNOSTIC (n=6 per series, exact permutation p)')
print('=' * 88)
print(f"{'Country':<13}{'Ind':<6}{'S':>5}{'Sen/yr':>9}{'p':>9}{'sig':>6}{'ties':>6}  shape")
print('-' * 88)

results = []
for (country, ind), vals in DATA.items():
    S = mk_S(vals)
    sen = sens_slope(vals)
    p = exact_p(vals)
    sig = 'YES' if p < 0.05 else 'no'
    t = n_ties(vals)
    # classify shape: monotonic vs turning
    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    nz = [d for d in diffs if d != 0]
    turns = sum(1 for i in range(len(nz) - 1) if sign(nz[i]) != sign(nz[i + 1]))
    shape = 'monotonic' if turns == 0 else f'{turns} turning pt(s)'
    results.append((country, ind, S, sen, p, sig, t, shape))
    print(f'{country:<13}{ind:<6}{S:>5}{sen:>9.2f}{p:>9.4f}{sig:>6}{t:>6}  {shape}')

print('-' * 88)
nsig = sum(1 for r in results if r[5] == 'YES')
print(f'Significant at p<0.05 (uncorrected): {nsig}/21')

# Bonferroni across 21 tests
alpha_b = 0.05 / 21
nsig_b = sum(1 for r in results if r[4] < alpha_b)
print(f'Significant after Bonferroni (alpha={alpha_b:.4f}): {nsig_b}/21')

print()
print('=' * 88)
print('THE CRITICAL PROBLEM: what MK says about the headline-finding countries')
print('=' * 88)
for country in ['Rwanda', 'Uganda', 'South Sudan']:
    print(f'\n{country}:')
    for c, ind, S, sen, p, sig, t, shape in results:
        if c == country:
            verdict = 'trend detected' if p < 0.05 else 'NO significant trend'
            print(f'   {ind}: S={S:>3}  Sen={sen:+.2f}pp/yr  p={p:.3f}  -> {verdict}   [{shape}]')

print()
print('Minimum attainable two-sided p at n=6 (perfectly monotonic, no ties):',
      f'{exact_p([1, 2, 3, 4, 5, 6]):.4f}')
print('Series with >=1 tie:', sum(1 for r in results if r[6] > 0), '/21')
print('Series that are NOT monotonic:', sum(1 for r in results if r[7] != 'monotonic'), '/21')
