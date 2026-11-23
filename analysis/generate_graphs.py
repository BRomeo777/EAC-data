import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# SPSS-style settings
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['axes.edgecolor'] = '#333333'
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['xtick.major.size'] = 4
plt.rcParams['ytick.major.size'] = 4
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'

GRAPH_DIR = os.path.join(os.path.dirname(__file__), 'graphs')
os.makedirs(GRAPH_DIR, exist_ok=True)

countries = ['Burundi', 'DR Congo', 'Kenya', 'Rwanda', 'South Sudan', 'Tanzania', 'Uganda']
years = [2019, 2020, 2021, 2022, 2023, 2024]

# WUENIC data from WHO GHO API
dtp1 = {
    'Burundi':      [97, 98, 96, 93, 89, 89],
    'DR Congo':     [84, 83, 81, 81, 80, 82],
    'Kenya':        [96, 97, 99, 99, 97, 93],
    'Rwanda':       [99, 94, 94, 98, 94, 99],
    'South Sudan':  [68, 71, 73, 76, 76, 76],
    'Tanzania':     [95, 95, 90, 91, 87, 87],
    'Uganda':       [96, 94, 97, 94, 95, 97],
}

dtp3 = {
    'Burundi':      [93, 93, 94, 91, 89, 89],
    'DR Congo':     [73, 70, 65, 65, 60, 65],
    'Kenya':        [93, 93, 95, 94, 93, 91],
    'Rwanda':       [98, 91, 88, 98, 94, 98],
    'South Sudan':  [61, 67, 69, 73, 73, 73],
    'Tanzania':     [91, 91, 86, 87, 83, 83],
    'Uganda':       [93, 89, 91, 89, 91, 94],
}

mcv1 = {
    'Burundi':      [92, 90, 90, 89, 86, 86],
    'DR Congo':     [65, 62, 55, 56, 52, 55],
    'Kenya':        [92, 89, 88, 85, 85, 82],
    'Rwanda':       [96, 94, 87, 99, 96, 97],
    'South Sudan':  [65, 69, 74, 72, 72, 72],
    'Tanzania':     [89, 87, 80, 84, 84, 84],
    'Uganda':       [87, 89, 90, 91, 91, 92],
}

# Distinct professional color palette
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2']
markers = ['o', 's', '^', 'D', 'v', 'p', '*']
linestyles = ['-', '-', '-', '-', '-', '-', '-']

def style_axis(ax, title, xlabel, ylabel):
    ax.set_title(title, fontsize=12, fontweight='bold', pad=12)
    ax.set_xlabel(xlabel, fontsize=10, fontweight='bold')
    ax.set_ylabel(ylabel, fontsize=10, fontweight='bold')
    ax.set_ylim(40, 105)
    ax.set_xticks(years)
    ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d%%'))
    ax.grid(True, linestyle='--', linewidth=0.5, color='#cccccc', axis='y')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ============ FIGURE 1: DTP1 Coverage Trends ============
fig, ax = plt.subplots(figsize=(10, 6))
for i, country in enumerate(countries):
    ax.plot(years, dtp1[country], color=colors[i], marker=markers[i],
            markersize=6, linewidth=1.5, linestyle=linestyles[i], label=country)
style_axis(ax, 'Figure 1. DTP1 Immunization Coverage Trends in EAC Member States, 2019-2024',
           'Year', 'DTP1 Coverage (%)')
ax.legend(loc='lower left', fontsize=8, framealpha=0.9, ncol=2)
fig.tight_layout()
fig.savefig(os.path.join(GRAPH_DIR, 'fig1_dtp1_trends.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ============ FIGURE 2: DTP3 Coverage Trends ============
fig, ax = plt.subplots(figsize=(10, 6))
for i, country in enumerate(countries):
    ax.plot(years, dtp3[country], color=colors[i], marker=markers[i],
            markersize=6, linewidth=1.5, linestyle=linestyles[i], label=country)
style_axis(ax, 'Figure 2. DTP3 Immunization Coverage Trends in EAC Member States, 2019-2024',
           'Year', 'DTP3 Coverage (%)')
ax.legend(loc='lower left', fontsize=8, framealpha=0.9, ncol=2)
fig.tight_layout()
fig.savefig(os.path.join(GRAPH_DIR, 'fig2_dtp3_trends.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ============ FIGURE 3: MCV1 Coverage Trends ============
fig, ax = plt.subplots(figsize=(10, 6))
for i, country in enumerate(countries):
    ax.plot(years, mcv1[country], color=colors[i], marker=markers[i],
            markersize=6, linewidth=1.5, linestyle=linestyles[i], label=country)
style_axis(ax, 'Figure 3. MCV1 Immunization Coverage Trends in EAC Member States, 2019-2024',
           'Year', 'MCV1 Coverage (%)')
ax.legend(loc='lower left', fontsize=8, framealpha=0.9, ncol=2)
fig.tight_layout()
fig.savefig(os.path.join(GRAPH_DIR, 'fig3_mcv1_trends.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ============ FIGURE 4: DTP1-to-DTP3 Dropout Rates ============
# Dropout rate = ((DTP1 - DTP3) / DTP1) * 100
fig, ax = plt.subplots(figsize=(10, 6))
for i, country in enumerate(countries):
    dropout = [((dtp1[country][j] - dtp3[country][j]) / dtp1[country][j]) * 100 for j in range(len(years))]
    ax.plot(years, dropout, color=colors[i], marker=markers[i],
            markersize=6, linewidth=1.5, linestyle=linestyles[i], label=country)
ax.set_title('Figure 4. DTP1-to-DTP3 Dropout Rates in EAC Member States, 2019-2024',
             fontsize=12, fontweight='bold', pad=12)
ax.set_xlabel('Year', fontsize=10, fontweight='bold')
ax.set_ylabel('Dropout Rate (%)', fontsize=10, fontweight='bold')
ax.set_xticks(years)
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter('%d%%'))
ax.grid(True, linestyle='--', linewidth=0.5, color='#cccccc', axis='y')
ax.set_axisbelow(True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.legend(loc='upper left', fontsize=8, framealpha=0.9, ncol=2)
fig.tight_layout()
fig.savefig(os.path.join(GRAPH_DIR, 'fig4_dropout_rates.png'), dpi=300, bbox_inches='tight')
plt.close(fig)

# ============ FIGURES 5-7: Net Change from 2019 Baseline (Diverging Bar) ============
# Shows percentage point change from 2019 pre-pandemic baseline for each vaccine
# Positive bars (blue) = improvement above baseline; Negative bars (red) = decline below baseline

vaccines = [('DTP1', dtp1), ('DTP3', dtp3), ('MCV1', mcv1)]
fig_nums = [5, 6, 7]

for fig_idx, (vname, vdata) in enumerate(vaccines):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Compute changes
    changes_2021 = [vdata[c][2] - vdata[c][0] for c in countries]
    changes_2024 = [vdata[c][5] - vdata[c][0] for c in countries]
    
    # Sort by 2024 change (best to worst)
    sorted_idx = sorted(range(len(countries)), key=lambda i: changes_2024[i], reverse=True)
    sorted_countries = [countries[i] for i in sorted_idx]
    sorted_2021 = [changes_2021[i] for i in sorted_idx]
    sorted_2024 = [changes_2024[i] for i in sorted_idx]
    
    y = np.arange(len(sorted_countries))
    height = 0.35
    
    bars1 = ax.barh(y - height/2, sorted_2021, height, label='2021 vs 2019 (Pandemic disruption)',
                     color=['#d62728' if v < 0 else '#2ca02c' for v in sorted_2021],
                     edgecolor='#333333', linewidth=0.5)
    bars2 = ax.barh(y + height/2, sorted_2024, height, label='2024 vs 2019 (Post-pandemic recovery)',
                     color=['#ff7f0e' if v < 0 else '#1f77b4' for v in sorted_2024],
                     edgecolor='#333333', linewidth=0.5)
    
    ax.axvline(x=0, color='#000000', linewidth=0.8)
    ax.set_xlim(-15, 15)
    ax.set_yticks(y)
    ax.set_yticklabels(sorted_countries, fontsize=10)
    ax.set_xlabel('Percentage Point Change from 2019 Baseline', fontsize=10, fontweight='bold')
    ax.set_title(f'Figure {fig_nums[fig_idx]}. {vname} Coverage Change from 2019 Pre-Pandemic Baseline in EAC Member States',
                 fontsize=12, fontweight='bold', pad=12)
    ax.legend(fontsize=9, loc='lower right', framealpha=0.9)
    ax.grid(True, linestyle='--', linewidth=0.5, color='#cccccc', axis='x')
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add value labels on bars
    for bar in bars1:
        w = bar.get_width()
        ax.text(w - 1 if w < 0 else w + 0.5, bar.get_y() + bar.get_height()/2,
                f'{w:+d}', ha='right' if w < 0 else 'left', va='center', fontsize=8, fontweight='bold')
    for bar in bars2:
        w = bar.get_width()
        ax.text(w - 1 if w < 0 else w + 0.5, bar.get_y() + bar.get_height()/2,
                f'{w:+d}', ha='right' if w < 0 else 'left', va='center', fontsize=8, fontweight='bold')
    
    fig.tight_layout()
    fig.savefig(os.path.join(GRAPH_DIR, f'fig{fig_nums[fig_idx]}_{vname.lower()}_change.png'), dpi=300, bbox_inches='tight')
    plt.close(fig)

print("All 7 figures generated successfully.")
