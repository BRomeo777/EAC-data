# EAC Immunization Recovery Analysis Code

**Repository for: "Trends and Recovery Patterns of Routine Childhood Immunization Coverage in East African Community Member States, 2019-2024"**

## Overview

This repository contains the analysis code for evaluating post-pandemic immunization recovery patterns across seven East African Community (EAC) member states: Burundi, DR Congo, Kenya, Rwanda, South Sudan, Tanzania, and Uganda.

## Study Description

**Objective:** To describe DTP1, DTP3, and MCV1 coverage trends in EAC member states from 2019 to 2024 and assess post-pandemic recovery patterns.

**Data Source:** WHO/UNICEF Estimates of National Immunization Coverage (WUENIC) accessed via WHO Global Health Observatory (GHO) API.

**Analysis Period:** 2019-2024 (pre-pandemic baseline through post-pandemic recovery period)

## Files

### Core Analysis Scripts

- **generate_manuscript.py** - Generates the complete manuscript document in Word format
- **generate_graphs.py** - Generates SPSS-style trend graphs for DTP1, DTP3, and MCV1 coverage
- **compute_onset.py** - Computes recovery onset years (first year ≥ 2019 baseline, sustained through 2024)
- **sensitivity_2025.py** - Sensitivity analysis using 2025 provisional data from WHO GHO API
- **threshold_sensitivity.py** - Threshold sensitivity analysis (1pp, 2pp, 3pp recovery cutoffs)
- **trend_test_diagnostic.py** - Mann-Kendall/Sen's slope diagnostic with exact permutation p-values
- **generate_references_doc.py** - Generates references document with DOIs and URLs

### Data

- **data/wuenic_eac_2019_2024.csv** - Extracted WUENIC coverage data for EAC countries (2019-2024)

### Requirements

```bash
pip install python-docx matplotlib numpy pandas
```

## Usage

### Generate Manuscript

```bash
cd analysis
python generate_manuscript.py
```

Output: `EAC_Immunization_Recovery_Manuscript.docx`

### Generate Graphs

```bash
python generate_graphs.py
```

Output: Graph files saved to `graphs/` directory

### Compute Recovery Onset

```bash
python compute_onset.py
```

Output: Console output showing recovery onset years for each country and indicator

### Sensitivity Analysis (2025 Data)

```bash
python sensitivity_2025.py
```

Output: Console output showing sensitivity of recovery status to 2025 data inclusion

### Threshold Sensitivity

```bash
python threshold_sensitivity.py
```

Output: Console output showing recovery classification under different threshold cutoffs

### Trend Test Diagnostic

```bash
python trend_test_diagnostic.py
```

Output: Console output showing Mann-Kendall test results and Sen's slope estimates

### Generate References Document

```bash
python generate_references_doc.py
```

Output: `References_DOIs_URLs.docx`

## Data Access

The analysis uses publicly available data from the WHO Global Health Observatory API:

- DTP1: `VACCINECOVERAGE_DTP1`
- DTP3: `WHS4_100`
- MCV1: `WHS8_110`

API endpoint: https://ghoapi.azureedge.net/api/

## Citation

If you use this code in your research, please cite the associated manuscript:

> [Authors]. Trends and Recovery Patterns of Routine Childhood Immunization Coverage in East African Community Member States, 2019-2024. [Journal]. [Year].

## License

This code is provided for research purposes. Please contact the authors for permission to use or modify.

## Contact

For questions about the analysis code, please contact: [corresponding author email]

## Version

- Version: 1.0
- Date: November 2026
- Python version: 3.12

## Notes

- The recovery framework used in this study is an operational descriptive tool, not a validated epidemiological classification
- Thresholds (±1pp, ±2pp) are pragmatic choices for interpretation, not biological or policy-defined cutoffs
- The framework has not been externally validated and its generalizability to other regions is unknown
