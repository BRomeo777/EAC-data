import os
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

BASE = os.path.dirname(os.path.abspath(__file__))
GRAPH_DIR = os.path.join(BASE, 'graphs')
OUTPUT = os.path.join(BASE, 'EAC_Immunization_Recovery_Manuscript.docx')

doc = Document()

# ---- Style setup ----
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 2.0
style.paragraph_format.space_after = Pt(0)

# Margins
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

def add_heading(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = 'Times New Roman'
        run.font.color.rgb = RGBColor(0, 0, 0)
    # Also set the heading style itself to black
    heading_style = doc.styles[f'Heading {level}']
    heading_style.font.color.rgb = RGBColor(0, 0, 0)
    heading_style.font.name = 'Times New Roman'
    return h

def add_para(text, bold=False, italic=False, align=None, size=12, space_after=0):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 2.0
    p.paragraph_format.space_after = Pt(space_after)
    if align:
        p.alignment = align
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    return p

def add_figure(path, caption, width=6.0):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run()
    run.add_picture(path, width=Inches(width))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap.paragraph_format.space_after = Pt(12)
    cap_run = cap.add_run(caption)
    cap_run.font.name = 'Times New Roman'
    cap_run.font.size = Pt(10)
    cap_run.italic = True

# ===================== TITLE PAGE =====================
add_para('', space_after=0)
add_para('Trends and Recovery Patterns of Routine Childhood Immunization Coverage in East African Community Member States, 2019-2024',
         bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_after=12)

add_para('', space_after=0)
add_para('Author Name(s)', align=WD_ALIGN_PARAGRAPH.CENTER, size=12)
add_para('Affiliation(s)', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('', space_after=0)
add_para('Corresponding author:', align=WD_ALIGN_PARAGRAPH.CENTER, size=11)
add_para('Email: [corresponding author email]', align=WD_ALIGN_PARAGRAPH.CENTER, size=11)
add_para('Address: [full postal address]', align=WD_ALIGN_PARAGRAPH.CENTER, size=11)
add_para('', space_after=0)
add_para('Word count: Approximately 8,000 (main text)', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('Number of tables: 4', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('Number of figures: 7', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('Running title: Post-Pandemic Immunization Recovery and Operational Recovery Assessment in EAC Member States', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('', space_after=0)
add_para('Funding: None declared', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)
add_para('Conflicts of interest: None declared', align=WD_ALIGN_PARAGRAPH.CENTER, size=11, italic=True)

doc.add_page_break()

# ===================== ABSTRACT =====================
add_heading('Abstract', level=1)

add_para('Background:', bold=True, space_after=0)
add_para('The COVID-19 pandemic caused unprecedented disruptions to routine childhood immunization services globally, with particularly severe consequences in low- and middle-income countries. The East African Community (EAC) member states experienced substantial setbacks in vaccination coverage during 2020-2021. This study examines trends and recovery patterns of routine immunization coverage across all seven EAC member states from 2019 to 2024.')

add_para('Methods:', bold=True, space_after=0)
add_para('A descriptive trend analysis was conducted using WUENIC coverage estimates for DTP1, DTP3, and MCV1 from 2019 to 2024 for all seven EAC member states, accessed via the WHO Global Health Observatory API. An operational four-tier recovery decision aid (baseline-relative, marginal, not recovered, inconclusive) was applied using 2019 baselines, with sensitivity analysis using 2025 provisional data. The framework is proposed as a pragmatic descriptive tool, not a validated epidemiological classification. DTP1-to-DTP3 dropout rates were calculated as a program quality indicator.')

add_para('Results:', bold=True, space_after=0)
add_para('Recovery patterns were highly heterogeneous. South Sudan met the operational criterion for baseline-relative recovery (all indicators \u2265+2pp above baseline), though absolute coverage remained insufficient and identical 2022–2024 values may reflect non-updated estimates. Rwanda\'s status was inconclusive (marginal margins that reversed under 2025 sensitivity data); Uganda showed marginal recovery based on +1pp margins on two indicators, robust to 2025 data but sensitive to threshold choice. Kenya, Tanzania, Burundi, and DR Congo had not recovered by 2024. DR Congo experienced the steepest declines (DTP3: 73% in 2019 to 65% in 2024) with widening dropout rates. Kenya declined from 2022 onward (DTP1: 99% to 93%). Rwanda and Uganda maintained stable dropout rates despite transient pandemic-era increases.')

add_para('Conclusions:', bold=True, space_after=0)
add_para('Post-pandemic immunization recovery in the EAC has been uneven and incomplete. Under the operational recovery framework, South Sudan met the criterion for baseline-relative recovery, though absolute coverage remained insufficient; Rwanda\'s status was inconclusive and Uganda\'s marginal. Persistent declines in Kenya, Tanzania, Burundi, and DR Congo underscore the need for intensified catch-up interventions and targeted support for zero-dose children. Regional cooperation through EAC frameworks and the Big Catch-Up initiative remains critical for progress toward IA2030 targets.')

add_para('Keywords:', bold=True, space_after=0)
add_para('Immunization coverage; COVID-19 pandemic; post-pandemic recovery; East African Community; DTP1; DTP3; MCV1; WUENIC; dropout rate; trend analysis', italic=True)

doc.add_page_break()

# ===================== INTRODUCTION =====================
add_heading('1. Introduction', level=1)

add_para('Routine childhood immunization is one of the most cost-effective public health interventions, averting an estimated 154 million deaths since the inception of the Expanded Programme on Immunization (EPI) in 1974 (1,2). The COVID-19 pandemic caused the most severe disruption to global immunization services in 30 years (3,4). Lockdowns, diversion of health personnel and resources to the pandemic response, supply chain interruptions, and public fear of visiting health facilities collectively contributed to a precipitous decline in vaccination coverage worldwide (4,5). The number of zero-dose children \u2014 those not receiving the first dose of diphtheria-tetanus-pertussis-containing vaccine (DTP1) (6) \u2014 rose from 12.8 million in 2019 to a peak of 17.7 million in 2021, decreased to 13.9 million in 2022, but rose again to 14.5 million in 2023, remaining substantially above pre-pandemic levels (1,7). The WHO African Region bears the greatest burden of zero-dose children, with 6.7 million in 2023, still above the 2019 level (8). WUENIC estimates are subject to annual revision; for example, the 2024 revision revised the 2022 African Region estimate downward to 7.3 million (8).')

add_para('The East African Community (EAC) comprises seven partner states — Rwanda, Kenya, Uganda, Tanzania, Burundi, South Sudan, and the Democratic Republic of Congo — with a combined population of approximately 300 million and shared health cooperation frameworks under the EAC Treaty (9,10).')

add_para('Prior to the pandemic, immunization programs in the region already faced constraints including inadequate financing, workforce shortages, and cold chain limitations (11,12). The COVID-19 pandemic exacerbated these vulnerabilities. Studies have documented substantial declines in routine immunization service delivery across African countries during the first six months of the pandemic, with 13 of 15 countries showing a decline in the monthly average number of vaccine doses provided (13), and a study from Sierra Leone reporting a 50-80% drop in vaccination coverage during lockdown (14). A systematic review estimated an overall relative median decline of 10.8% across all vaccines in low- and middle-income countries during the pandemic (15). In Eastern and Southern Africa, DTP3 coverage fell by 5 percentage points between 2019 and 2021, and 2019 marked a critical inflection point after which regional coverage shifted from an increasing to a decreasing trend (16).')

add_para('In response to the pandemic-induced backsliding, global partners including WHO, UNICEF, and Gavi launched the Big Catch-Up initiative in 2023, with three strategic pillars: catching up on children missed during the pandemic years, restoring coverage to at least 2019 levels, and strengthening immunization programs within primary health care systems (3,17). The Immunization Agenda 2030 (IA2030), endorsed by the WHO African Region in 2021, provides the overarching framework for these recovery efforts, with a goal of reducing zero-dose children by 50% by 2030 (1,18).')

add_para('Although Aguinaga-Ontoso et al. (16) conducted an Africa-wide joinpoint regression analysis of DTP3 coverage that included EAC countries, no published study has specifically evaluated post-pandemic immunization recovery across the EAC bloc. A targeted search of PubMed, Scopus, and Google Scholar (January 2020 to July 2026) identified no original research reporting coverage trends or recovery outcomes for EAC member states as a group. This study addresses that gap by: (i) describing DTP1, DTP3, and MCV1 coverage trends in EAC member states from 2019 to 2024; (ii) identifying the year each country returned to or surpassed its pre-pandemic (2019) coverage level; and (iii) comparing DTP1-to-DTP3 dropout rates across EAC countries during the recovery period.')

# ===================== METHODS =====================
add_heading('2. Methods', level=1)

add_heading('2.1 Study Design', level=2)
add_para('This study employed a descriptive trend analysis of secondary, publicly available national immunization coverage data. The design is consistent with established methodologies for assessing immunization coverage trends using WUENIC data, as applied in previous studies in the European Union and African contexts (16,19).')

add_heading('2.2 Data Source', level=2)
add_para('Data were obtained from the WHO/UNICEF Estimates of National Immunization Coverage (WUENIC), which provide annual country-specific coverage estimates for 195 countries and 15 vaccines (20). WUENIC estimates are derived from administrative coverage, surveys, and contextual information through an independent technical assessment by WHO and UNICEF, not formal statistical modeling, and comply with GATHER criteria (21-24).')

add_para('Coverage estimates for DTP1, DTP3, and MCV1 were extracted for 2019 to 2024 via the WHO Global Health Observatory (GHO) API, using indicator codes VACCINECOVERAGE_DTP1, WHS4_100, and WHS8_110, respectively (25). The 2019 data point served as the pre-pandemic baseline, 2020-2021 as the pandemic disruption period, and 2022-2024 as the post-pandemic recovery period.')

add_para('Data were accessed on 27 July 2026, following the release of the 2025 WUENIC revision on 15 July 2026. Although 2025 estimates were available, the analysis was limited to 2019-2024 because the most recent year in any revision may undergo further revision (22), and because including 2025 would conflate spontaneous recovery with the effects of the Big Catch-Up initiative, which began in many countries in 2024. Future studies should incorporate 2025 and subsequent estimates to evaluate the incremental impact of targeted catch-up interventions.')

add_heading('2.3 Study Population', level=2)
add_para('The study population comprised all seven current EAC member states: Rwanda, Kenya, Uganda, Tanzania, Burundi, South Sudan, and the Democratic Republic of Congo. These countries represent a combined population of approximately 300 million people (9) and share regional health cooperation frameworks through the EAC Treaty and associated protocols (9,10).')

add_heading('2.4 Variables and Indicators', level=2)
add_para('Three key immunization coverage indicators were analyzed: (i) DTP1, representing access to immunization services; (ii) DTP3, representing completion of the primary DTP series and a proxy for overall program performance; and (iii) MCV1, representing measles-containing vaccine first-dose coverage. The DTP1-to-DTP3 dropout rate, calculated as [(DTP1 - DTP3) / DTP1] x 100, was used as an indicator of program quality and retention along the immunization cascade.')

add_heading('2.5 Data Analysis', level=2)
add_para('Coverage trends were plotted by country and year for each vaccine indicator. Trend inflection points and recovery onset years were identified through systematic year-over-year comparison of plotted coverage trends. This descriptive approach was chosen because the short time series (6 data points per country) precludes formal statistical modeling of trend significance, such as joinpoint regression, which requires a sufficient number of data points to estimate annual percent change and conduct permutation tests (16). The approach is consistent with descriptive trend analyses applied in previous immunization coverage studies in the European Union and African contexts (16,19). Non-parametric trend tests such as the Mann-Kendall test and Sen\'s slope estimator were considered but not adopted, for two reasons. First, these methods test for monotonic trend, whereas the pattern of interest here is non-monotonic — a pandemic-era decline followed by partial or complete rebound — so a null result would reflect the shape of the series rather than the absence of disruption. Second, WUENIC values are modelled estimates that are smoothed across adjacent years, which violates the independence assumption underlying the permutation distributions of these tests. The study question concerns whether coverage returned to a specified baseline level, which is a comparison of levels rather than a test of slope.')

add_para('An operational recovery decision aid was developed using a four-tier system applied to each country across all three indicators, with the fourth tier (inconclusive) derived from sensitivity analysis as described below. This framework is descriptive rather than statistically derived, and the labels should be interpreted as operational categories rather than definitive recovery statuses. The thresholds are pragmatic choices designed to facilitate interpretation of WUENIC trends, not biological or policy-defined cutoffs; they do not originate from an established guideline or consensus framework (unlike, for example, WHO definitions of zero-dose children or the 90% DTP3 coverage target). The recovery framework is proposed as an operational descriptive tool for summarizing post-pandemic immunization recovery within this study, not as a universally applicable or validated epidemiological classification. It has not been externally validated against independent datasets, expert consensus, or WHO country assessments, and its generalizability to other regions, baseline coverage levels, or data sources (e.g., administrative coverage, DHS/MICS surveys) remains unknown. Future research should evaluate whether the framework performs consistently when applied to other geographic regions, additional years of WUENIC data, or alternative immunization datasets. (i) "baseline-relative recovery" — 2024 coverage exceeded the 2019 baseline by \u22652 percentage points on a given indicator; (ii) "marginal recovery" — 2024 coverage was within \u00b11 percentage point of the 2019 baseline (i.e., equal to, 1 point above, or 1 point below); and (iii) "not recovered" — 2024 coverage was \u22652 percentage points below the 2019 baseline. A country\'s overall classification was determined by its worst-performing indicator: if any indicator was classified as "not recovered," the country was classified as "not recovered" overall; if all indicators showed baseline-relative or marginal recovery, the country was classified as "baseline-relative recovery" (if all three were baseline-relative) or "marginal recovery" (if at least one indicator was marginal). A fourth category, "inconclusive," was pre-specified for countries whose primary (2019–2024) classification was marginal but whose classification reversed to "not recovered" when 2025 provisional data were incorporated in the sensitivity analysis, indicating that the recovery status was not robust to the inclusion of the most recent data point. The \u22652pp threshold for baseline-relative recovery was chosen to exceed the typical magnitude of year-to-year WUENIC revisions, ensuring that baseline-relative recovery reflects a substantive change rather than estimation noise; the marginal category was included to acknowledge that WUENIC estimates are subject to revision between annual cycles, and that differences of 0\u20131 percentage points may not reflect genuine changes in program performance.\n\nIn addition to the endpoint classification, the year of first recovery was identified for each country and indicator. A country was considered to have first recovered on a given indicator in the first year (during 2020\u20132024) in which coverage was \u2265 the 2019 baseline. Recovery was classified as sustained if coverage remained \u2265 baseline in all subsequent years through 2024; if coverage fell below baseline in any later year, the onset year was marked with an asterisk to indicate a transient return, and the country\'s overall trajectory was classified as "Lost." Countries that never reached baseline on at least one indicator were classified as "Never." Where a country showed a mix of patterns across indicators, the overall trajectory was classified as "Lost" if at least one indicator recovered and later fell below baseline, and as "Never" only if no indicator ever reached baseline. This onset-year analysis uses a strict \u2265 baseline criterion (rather than the \u00b11pp threshold used for endpoint classification) because its purpose is to trace trajectory continuity, not to classify endpoint status.\n\nTo assess the robustness of recovery classifications, two sensitivity analyses were conducted. First, 2025 WUENIC estimates (which were available but excluded from the primary analysis; see Section 2.2) were compared against 2019 baselines to determine whether including the most recent year would change any country\'s classification. Countries whose marginal recovery classification reversed under 2025 data were reclassified as "inconclusive." Second, the baseline-relative recovery threshold was varied between 1 and 3 percentage points to test whether classifications were robust to alternative cutoffs.\n\nThe estimated zero-dose burden was calculated for each EAC country by applying DTP1 coverage to WHO surviving infant population estimates for 2024 (26), using the formula: estimated zero-dose children = surviving infant population \u00d7 (1 \u2212 DTP1 coverage / 100). Surviving infant populations were obtained from the World Population Prospects 2024 revision (27). These estimates represent modeled approximations rather than directly enumerated zero-dose children and assume uniform coverage distribution within each country; consequently, they may not capture geographic clustering of zero-dose populations. The estimates are intended to convey the relative scale of the zero-dose burden across EAC countries, not to produce precise counts.\n\nDropout rates were compared across countries and over time to assess changes in program performance during the recovery period. WUENIC estimates include a Grade of Confidence (GoC) reflecting the strength of underlying evidence; however, GoC data are not accessible through the WHO GHO API and could not be systematically incorporated into this analysis. For the 126 data points in this study (7 countries × 3 vaccines × 6 years), manual retrieval of GoC ratings from the WHO Immunization Data Portal would be feasible and is recommended for future studies (see Section 4.1). All analyses were performed using Python (version 3.12) with pandas (version 2.2), numpy (version 1.26), and matplotlib (version 3.9) libraries. Graphs were produced using matplotlib with professional formatting suitable for publication. The analysis code is available from the corresponding author upon reasonable request.')

add_heading('2.6 Ethical Considerations', level=2)
add_para('This study used only aggregate, publicly available, de-identified national-level data from the WHO/UNICEF WUENIC database, which is freely accessible through the WHO Immunization Data Portal and Global Health Observatory API. No primary data collection from human subjects was involved, and no identifiable individual-level data were used. Because all data are in the public domain and no human subjects were involved, this study did not require ethical clearance or institutional review board approval. The need for informed consent was waived as no individual-level data were used. This approach is consistent with the Committee on Publication Ethics (COPE) guidelines for secondary analyses of publicly available aggregate health data and with the ethical policies of journals such as BMC Public Health and the Pan African Medical Journal, which do not require ethics approval for analyses of publicly available national-level statistics.')

# ===================== RESULTS =====================
add_heading('3. Results', level=1)

add_heading('3.1 DTP1 Coverage Trends', level=2)
add_para('DTP1 coverage, a measure of access to immunization services, showed diverse trajectories across EAC member states from 2019 to 2024 (Figure 1). Rwanda maintained high DTP1 coverage overall, dipping from 99% in 2019 to 94% in 2020-2021, partially recovering to 98% in 2022, dipping again to 94% in 2023, and returning to 99% by 2024. Kenya initially increased DTP1 coverage from 96% in 2019 to 99% in 2021-2022 but subsequently declined to 93% in 2024, falling below its pre-pandemic level. Uganda showed a resilient pattern, with coverage fluctuating between 94% and 97% and ultimately exceeding the 2019 baseline (97% in 2024 vs 96% in 2019).')

add_para('Tanzania experienced an overall decline from 95% in 2019 to 87% in 2024, though the trajectory was non-monotonic: coverage fell to 90% in 2021, partially rebounded to 91% in 2022, then declined again to 87% by 2024, representing an 8 percentage-point net drop without sustained recovery. Burundi similarly declined from 97% in 2019 to 89% in 2024. South Sudan, starting from a low baseline of 68% in 2019, showed gradual improvement to 76% by 2022 but plateaued at that level through 2024. DR Congo declined from 84% in 2019 to 80% in 2023, with a slight recovery to 82% in 2024.')

add_figure(os.path.join(GRAPH_DIR, 'fig1_dtp1_trends.png'),
           'Figure 1. DTP1 immunization coverage trends in EAC member states, 2019-2024. Data source: WUENIC 2025 revision, accessed via WHO GHO API.')

add_heading('3.2 DTP3 Coverage Trends', level=2)
add_para('DTP3 coverage, reflecting completion of the primary DTP vaccination series, exhibited even more pronounced disparities (Figure 2). Rwanda demonstrated a rapid recovery, dropping from 98% in 2019 to 88% in 2021 before rebounding to 98% by 2022, dipping to 94% in 2023, and returning to 98% in 2024. Uganda showed a similar pattern, recovering from 89% in 2020 to 94% in 2024, surpassing the 2019 baseline of 93%. Kenya peaked at 95% in 2021 but declined to 91% in 2024, below the 2019 level of 93%.')

add_para('DR Congo experienced the most severe decline, with DTP3 coverage falling from 73% in 2019 to 60% in 2023, before a modest recovery to 65% in 2024, still 8 percentage points below the pre-pandemic level. Tanzania declined from 91% in 2019 to 83% in 2024. Burundi declined from 93% in 2019 to 89% in 2024. South Sudan, despite starting from the lowest baseline (61% in 2019), showed consistent improvement to 73% by 2022, surpassing its pre-pandemic level, and maintained that coverage through 2024.')

add_figure(os.path.join(GRAPH_DIR, 'fig2_dtp3_trends.png'),
           'Figure 2. DTP3 immunization coverage trends in EAC member states, 2019-2024. Data source: WUENIC 2025 revision, accessed via WHO GHO API.')

add_heading('3.3 MCV1 Coverage Trends', level=2)
add_para('MCV1 coverage, indicating first-dose measles vaccination, showed variable trends across EAC countries (Figure 3). Rwanda recovered strongly, from a nadir of 87% in 2021 to a peak of 99% in 2022, before settling at 97% in 2024, still exceeding the 2019 baseline of 96%. Uganda showed steady improvement from 87% in 2019 to 92% in 2024. South Sudan improved from 65% in 2019 to a peak of 74% in 2021, before declining and plateauing at 72% from 2022 through 2024.')

add_para('Kenya experienced a persistent decline in MCV1 coverage, from 92% in 2019 to 82% in 2024, representing a 10 percentage-point drop. Tanzania declined from 89% in 2019 to a trough of 80% in 2021, with partial recovery to 84% by 2022, where coverage remained through 2024. Burundi declined from 92% in 2019 to 86% in 2024. DR Congo showed the steepest decline, from 65% in 2019 to 52% in 2023, with a slight recovery to 55% in 2024.')

add_figure(os.path.join(GRAPH_DIR, 'fig3_mcv1_trends.png'),
           'Figure 3. MCV1 immunization coverage trends in EAC member states, 2019-2024. Data source: WUENIC 2025 revision, accessed via WHO GHO API.')

add_heading('3.4 DTP1-to-DTP3 Dropout Rates', level=2)
add_para('Dropout rates from DTP1 to DTP3, a key indicator of immunization program quality, varied substantially across EAC partner states and over time (Figure 4). In 2019, dropout rates were lowest in Rwanda (1.0%), Kenya (3.1%), and Uganda (3.1%), and highest in South Sudan (10.3%) and DR Congo (13.1%).')

add_para('By 2024, Rwanda maintained a low dropout rate of 1.0%, unchanged from 2019. However, Rwanda\'s dropout rate rose transiently to 3.2% in 2020 and 6.4% in 2021 during the pandemic disruption, before returning to 0% in 2022-2023. Uganda maintained its dropout rate at 3.1% in 2024, matching the 2019 level. Kenya\'s dropout rate decreased from 3.1% in 2019 to 2.2% in 2024, though this occurred in the context of declining absolute coverage. Tanzania\'s dropout rate remained relatively stable at approximately 4.6% in 2024 compared to 4.2% in 2019.')

add_para('DR Congo showed a widening dropout rate, increasing from 13.1% in 2019 to 20.7% in 2024, consistent with challenges in retention along the vaccination cascade and an increasing proportion of children who initiate but do not complete the DTP series. South Sudan improved its dropout rate from 10.3% in 2019 to 3.9% in 2024, though this occurred in the context of low overall coverage. Burundi\'s dropout rate declined from 4.1% in 2019 to 0% by 2023–2024.')

add_figure(os.path.join(GRAPH_DIR, 'fig4_dropout_rates.png'),
           'Figure 4. DTP1-to-DTP3 dropout rates in EAC member states, 2019-2024. Dropout rate = [(DTP1 - DTP3) / DTP1] x 100. Data source: WUENIC 2025 revision.')

add_heading('3.5 Comparison Across Recovery Periods', level=2)
add_para('Figures 5, 6, and 7 present the net percentage point change in coverage from the 2019 pre-pandemic baseline for DTP1, DTP3, and MCV1, respectively. Each figure shows the change during the pandemic period (2021 vs 2019) and the current recovery status (2024 vs 2019), with countries sorted from best to worst recovery. Positive values indicate coverage above the 2019 baseline, while negative values indicate coverage below baseline. These figures clearly illustrate the heterogeneous recovery patterns: Rwanda, South Sudan, and Uganda show positive or zero change in 2024 across all three indicators, while DR Congo, Tanzania, Burundi, and Kenya show persistent negative changes.')

add_figure(os.path.join(GRAPH_DIR, 'fig5_dtp1_change.png'),
           'Figure 5. DTP1 coverage change from 2019 pre-pandemic baseline in EAC member states. Blue bars indicate improvement above baseline; orange bars indicate decline below baseline. Data source: WUENIC 2025 revision.')

add_figure(os.path.join(GRAPH_DIR, 'fig6_dtp3_change.png'),
           'Figure 6. DTP3 coverage change from 2019 pre-pandemic baseline in EAC member states. Blue bars indicate improvement above baseline; orange bars indicate decline below baseline. Data source: WUENIC 2025 revision.')

add_figure(os.path.join(GRAPH_DIR, 'fig7_mcv1_change.png'),
           'Figure 7. MCV1 coverage change from 2019 pre-pandemic baseline in EAC member states. Blue bars indicate improvement above baseline; orange bars indicate decline below baseline. Data source: WUENIC 2025 revision.')

add_heading('3.6 Recovery Status Summary', level=2)
add_para('Table 1 summarizes the recovery status of each EAC member state as of 2024, using a four-tier operational decision aid. South Sudan achieved baseline-relative recovery. Uganda showed marginal recovery. Rwanda\'s classification was inconclusive: 2024 coverage met the marginal recovery criteria, but a sensitivity check using 2025 data reversed this classification to not recovered (see Section 4.1). Kenya, Tanzania, Burundi, and DR Congo had not recovered to pre-pandemic levels by 2024.')

# ---- TABLE 1: Recovery Status Summary (native Word table, replaces former Figure 6 image) ----
add_para('Table 1. Recovery status of EAC member states: 2024 coverage relative to 2019 pre-pandemic levels.',
         bold=True, size=11, space_after=6)

t1_data = [
    ['Country', 'DTP1 2024 (vs 2019)', 'DTP3 2024 (vs 2019)', 'MCV1 2024 (vs 2019)', 'Recovery Status'],
    ['Rwanda', '99% (+0)', '98% (+0)', '97% (+1)', 'Inconclusive†'],
    ['South Sudan', '76% (+8)', '73% (+12)', '72% (+7)', 'Baseline-relative'],
    ['Uganda', '97% (+1)', '94% (+1)', '92% (+5)', 'Marginal†'],
    ['Kenya', '93% (-3)', '91% (-2)', '82% (-10)', 'Not recovered'],
    ['Tanzania', '87% (-8)', '83% (-8)', '84% (-5)', 'Not recovered'],
    ['Burundi', '89% (-8)', '89% (-4)', '86% (-6)', 'Not recovered'],
    ['DR Congo', '82% (-2)', '65% (-8)', '55% (-10)', 'Not recovered'],
]

t1 = doc.add_table(rows=len(t1_data), cols=len(t1_data(0)))
t1.style = 'Table Grid'
t1.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, row_data in enumerate(t1_data):
    for j, cell_text in enumerate(t1_data[i]):
        cell = t1.cell(i, j)
        cell.text = cell_text
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True

add_para('', space_after=0)
add_para('Note: Values represent 2024 coverage with percentage point change from 2019 in parentheses. Countries are ordered by recovery status (inconclusive, baseline-relative, marginal, not recovered). Recovery status: Baseline-relative = all indicators \u2265+2pp above baseline; Marginal = no indicator \u22652pp below baseline, and at least one indicator within \u00b11pp of baseline; Not recovered = \u22651 indicator \u22652pp below baseline. Inconclusive = met marginal criteria in 2024 but reversed to not recovered under 2025 sensitivity check (pre-specified; see Methods 2.5). These categories are operational labels from an investigator-defined decision aid, not a validated epidemiological classification. \u2020See Section 4.1 for sensitivity analysis. Data source: WUENIC 2025 revision.',
         size=10, italic=True)

add_heading('3.7 Recovery Onset Years', level=2)
add_para('Table 2 reports the first year in which each country\'s coverage returned to or surpassed its 2019 baseline for each indicator, and whether that recovery was sustained through 2024. Note that Table 2 uses a strict criterion of coverage \u2265 the exact 2019 value, whereas Table 1 classifies endpoint status using \u00b11\u20132 percentage-point thresholds (marginal/baseline-relative/not recovered). These tables answer different questions: Table 1 assesses whether a country has recovered as of 2024, allowing for estimation uncertainty in near-baseline values, while Table 2 traces the trajectory of when baseline was first reached and whether that return was sustained. A country may therefore be classified as "marginal recovery" in Table 1 yet show "Lost" in Table 2 \u2014 for example, Uganda exceeded its 2019 baseline on all three indicators by 2024 (marginal recovery in Table 1) but DTP1 and DTP3 dipped below baseline in intervening years before returning (Lost in Table 2). South Sudan was the only country with a "Sustained" trajectory, where all three indicators recovered and remained above baseline from 2020 onward. Rwanda\'s DTP3 and MCV1 initially recovered in 2022 but DTP3 fell below baseline in 2023 before returning in 2024; DTP1 only returned to baseline in 2024. Uganda\'s MCV1 recovered earliest (2020) and was sustained, while DTP1 and DTP3 showed intermittent recovery before both reaching baseline by 2024. Kenya, Tanzania, and Burundi briefly touched or surpassed baseline on DTP1 and DTP3 in 2020 but subsequently fell below and never recovered. No country recovered on MCV1 except South Sudan, Uganda, and Rwanda. DR Congo never reached its 2019 baseline on any indicator during the study period.')

# ---- TABLE 2: Recovery Onset Years ----
add_para('Table 2. Year of first return to or surpassing 2019 pre-pandemic baseline, by country and indicator.',
         bold=True, size=11, space_after=6)

t2_onset_data = [
    ['Country', 'DTP1 onset', 'DTP3 onset', 'MCV1 onset', 'Recovery trajectory'],
    ['Rwanda', '2024', '2022*', '2022', 'Lost'],
    ['South Sudan', '2020', '2020', '2020', 'Sustained'],
    ['Uganda', '2021*', '2024', '2020', 'Lost'],
    ['Kenya', '2020*', '2020*', '\u2014', 'Lost'],
    ['Tanzania', '2020*', '2020*', '\u2014', 'Lost'],
    ['Burundi', '2020*', '2020*', '\u2014', 'Lost'],
    ['DR Congo', '\u2014', '\u2014', '\u2014', 'Never'],
]

t2onset = doc.add_table(rows=len(t2_onset_data), cols=len(t2_onset_data(0)))
t2onset.style = 'Table Grid'
t2onset.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, row_data in enumerate(t2_onset_data):
    for j, cell_text in enumerate(row_data):
        cell = t2onset.cell(i, j)
        cell.text = cell_text
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True

add_para('', space_after=0)
add_para('Note: Onset year = first year during 2020\u20132024 in which coverage was \u2265 2019 baseline. * = briefly reached baseline but subsequently fell below in a later year. \u2014 = never reached baseline during 2020\u20132024. Recovery trajectory: Sustained = all indicators remained \u2265 baseline from onset through 2024; Lost = reached baseline on at least one indicator but subsequently fell below on at least one indicator by 2024; Never = never reached baseline on any indicator during 2020\u20132024. Where indicators showed mixed patterns, the overall trajectory was classified as "Lost" if any indicator recovered and later fell below, and as "Never" only if no indicator ever reached baseline. Data source: WUENIC 2025 revision.',
         size=10, italic=True)

add_heading('3.8 Estimated Zero-Dose Children', level=2)
add_para('Zero-dose children — those not receiving DTP1 — represent the most severe form of immunization inequity. Using DTP1 coverage and WHO surviving infant population estimates for 2024 (26,27), the estimated zero-dose burden was calculated for each EAC member state using the formula: estimated zero-dose children = surviving infant population × (1 − DTP1 coverage / 100). The surviving infant populations used were: DR Congo 3,389,000; Tanzania 2,077,000; Kenya 1,429,000; South Sudan 354,000; Burundi 409,000; Uganda 1,333,000; and Rwanda 400,000. DR Congo accounted for the largest burden, with an estimated 610,000 zero-dose children in 2024, followed by Tanzania (approximately 270,000), Kenya (approximately 100,000), South Sudan (approximately 85,000), Burundi (approximately 45,000), and Uganda (approximately 40,000). Rwanda, with DTP1 coverage of 99%, had the smallest estimated burden at approximately 4,000 zero-dose children. These estimates represent modeled approximations and are intended to convey the relative scale of the zero-dose burden across EAC countries, not to produce precise counts. They underscore that even countries classified as recovered may still harbor unreached children — particularly South Sudan, whose 24% zero-dose rate reflects low absolute coverage despite baseline-relative recovery — and that DR Congo\'s burden warrants particular attention from regional immunization partners.')

doc.add_page_break()

# ---- TABLE 3: Full Data Table ----
add_para('Table 3. WUENIC immunization coverage estimates for EAC member states, 2019-2024.',
         bold=True, size=11, space_after=6)

t2_data = [
    ['Country', 'Vaccine', '2019', '2020', '2021', '2022', '2023', '2024'],
    ['Burundi', 'DTP1', '97', '98', '96', '93', '89', '89'],
    ['Burundi', 'DTP3', '93', '93', '94', '91', '89', '89'],
    ['Burundi', 'MCV1', '92', '90', '90', '89', '86', '86'],
    ['DR Congo', 'DTP1', '84', '83', '81', '81', '80', '82'],
    ['DR Congo', 'DTP3', '73', '70', '65', '65', '60', '65'],
    ['DR Congo', 'MCV1', '65', '62', '55', '56', '52', '55'],
    ['Kenya', 'DTP1', '96', '97', '99', '99', '97', '93'],
    ['Kenya', 'DTP3', '93', '93', '95', '94', '93', '91'],
    ['Kenya', 'MCV1', '92', '89', '88', '85', '85', '82'],
    ['Rwanda', 'DTP1', '99', '94', '94', '98', '94', '99'],
    ['Rwanda', 'DTP3', '98', '91', '88', '98', '94', '98'],
    ['Rwanda', 'MCV1', '96', '94', '87', '99', '96', '97'],
    ['South Sudan', 'DTP1', '68', '71', '73', '76', '76', '76'],
    ['South Sudan', 'DTP3', '61', '67', '69', '73', '73', '73'],
    ['South Sudan', 'MCV1', '65', '69', '74', '72', '72', '72'],
    ['Tanzania', 'DTP1', '95', '95', '90', '91', '87', '87'],
    ['Tanzania', 'DTP3', '91', '91', '86', '87', '83', '83'],
    ['Tanzania', 'MCV1', '89', '87', '80', '84', '84', '84'],
    ['Uganda', 'DTP1', '96', '94', '97', '94', '95', '97'],
    ['Uganda', 'DTP3', '93', '89', '91', '89', '91', '94'],
    ['Uganda', 'MCV1', '87', '89', '90', '91', '91', '92'],
]

t2 = doc.add_table(rows=len(t2_data), cols=len(t2_data(0)))
t2.style = 'Table Grid'
t2.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, row_data in enumerate(t2_data):
    for j, cell_text in enumerate(row_data):
        cell = t2.cell(i, j)
        cell.text = cell_text
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True

add_para('', space_after=0)
add_para('Note: All values are percentages. Data source: WHO/UNICEF Estimates of National Immunization Coverage (WUENIC), 2025 revision, accessed via WHO Global Health Observatory API (indicator codes: VACCINECOVERAGE_DTP1, WHS4_100, WHS8_110).',
         size=10, italic=True)

doc.add_page_break()

# ---- TABLE 3: Dropout Rates ----
add_para('Table 4. DTP1-to-DTP3 dropout rates (%) in EAC member states, 2019-2024.',
         bold=True, size=11, space_after=6)

t3_data = [
    ['Country', '2019', '2020', '2021', '2022', '2023', '2024', 'Change\n(2024-2019)'],
    ['Burundi', '4.1', '5.1', '2.1', '2.2', '0.0', '0.0', '-4.1'],
    ['DR Congo', '13.1', '15.7', '19.8', '19.8', '25.0', '20.7', '+7.6'],
    ['Kenya', '3.1', '4.1', '4.0', '5.1', '4.1', '2.2', '-0.9'],
    ['Rwanda', '1.0', '3.2', '6.4', '0.0', '0.0', '1.0', '0.0'],
    ['South Sudan', '10.3', '5.6', '5.5', '3.9', '3.9', '3.9', '-6.4'],
    ['Tanzania', '4.2', '4.2', '4.4', '4.4', '4.6', '4.6', '+0.4'],
    ['Uganda', '3.1', '5.3', '6.2', '5.3', '4.2', '3.1', '0.0'],
]

t3 = doc.add_table(rows=len(t3_data), cols=len(t3_data(0)))
t3.style = 'Table Grid'
t3.alignment = WD_TABLE_ALIGNMENT.CENTER
for i, row_data in enumerate(t3_data):
    for j, cell_text in enumerate(row_data):
        cell = t3.cell(i, j)
        cell.text = cell_text
        for paragraph in cell.paragraphs:
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in paragraph.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True

add_para('', space_after=0)
add_para('Note: Dropout rate = [(DTP1 - DTP3) / DTP1] x 100. Negative change indicates improvement (reduced dropout). Data source: WUENIC 2025 revision.',
         size=10, italic=True)

doc.add_page_break()

# ===================== DISCUSSION =====================
add_heading('4. Discussion', level=1)

add_para('This study examined post-pandemic recovery of routine childhood immunization coverage across all seven EAC partner states from 2019 to 2024, using WUENIC estimates from the 2025 revision. The findings reveal a highly heterogeneous recovery landscape, with South Sudan achieving baseline-relative recovery, Rwanda showing inconclusive recovery (marginal margins that reversed under 2025 data), Uganda showing marginal recovery, and Kenya, Tanzania, Burundi, and DR Congo remaining below their 2019 baselines.')

add_para('Rwanda\'s recovery trajectory is noteworthy, though its classification should be interpreted with caution given the inconclusive margins. DTP3 coverage dropped to 88% in 2021 but rebounded to 98% by 2022. The DTP1-to-DTP3 dropout rate rose transiently to 6.4% in 2021 but returned to near-zero levels by 2022.')

add_para('Uganda showed improvement across all three indicators, with DTP3 coverage exceeding the 2019 baseline by 2024. However, the +1pp margins on DTP1 and DTP3 are within the plausible range of year-to-year WUENIC revision changes, and the threshold sensitivity analysis confirmed that Uganda\'s classification shifts from marginal to baseline-relative recovery at a 1pp cutoff. The trajectory was non-monotonic: DTP1 and DTP3 dipped below baseline in 2020 and 2022 before recovering by 2024, while MCV1 remained above baseline throughout. Notably, 2025 data strengthened Uganda\'s position, with all three margins increasing to +2pp or greater, confirming baseline-relative recovery under the standard framework. Without formal uncertainty intervals or Grade of Confidence data, the distinction between marginal and baseline-relative recovery for Uganda cannot be considered robust, and the classification should be interpreted as indicative of a positive trend rather than a definitive recovery status.')

add_para('South Sudan showed improvement in all three indicators despite starting from the lowest baseline. However, absolute coverage levels remain critically low (DTP3: 73% in 2024), and the classification of baseline-relative recovery should be interpreted with particular caution: all three coverage values remained identical from 2022 through 2024 (DTP1 76%, DTP3 73%, MCV1 72%), a pattern consistent with WUENIC estimates being carried forward unchanged when no new administrative or survey data are reported. This is a known feature of the WUENIC estimation process in fragile and low-capacity settings (21,22), and raises the possibility that South Sudan\'s apparent recovery may partly reflect non-updated estimates rather than genuine programmatic improvement. Retrieval of Grade of Confidence ratings for these years from the WHO Immunization Data Portal would help clarify whether the flat values reflect strong empirical evidence or data gaps. Ongoing conflict, weak health infrastructure, and limited domestic financing continue to pose barriers (8,12). The dropout rate improved from 10.3% in 2019 to 3.9% in 2024, though this may partly reflect low overall coverage.')

add_para('Kenya\'s trajectory is concerning. DTP1 coverage initially rose to 99% in 2021–2022 before declining to 93% in 2024. MCV1 declined persistently from 92% in 2019 to 82% in 2024. The WHO African Region progress report noted that coverage remains below targets and equity gaps persist (8).')

add_para('Tanzania and Burundi showed persistent downward trends without baseline-relative recovery by 2024. Tanzania\'s DTP3 fell from 91% to 83% and Burundi\'s from 93% to 89%. These declines are consistent with Aguinaga-Ontoso et al. (16), who identified Tanzania as having marked DTP3 decreases during the pandemic. The lack of recovery suggests pandemic disruptions may have been compounded by supply chain weaknesses and inadequate catch-up efforts.')

add_para('DR Congo experienced the most severe decline, with DTP3 falling from 73% in 2019 to 60% in 2023 before a modest recovery to 65% in 2024. The dropout rate widened from 13.1% to a peak of 25.0% in 2023, suggesting challenges in retention along the vaccination cascade, though partial improvement to 20.7% in 2024 may signal early stabilization. DR Congo is among the ten countries accounting for 80.3% of zero-dose children in the WHO African Region during 2019–2022 (28). Vast territory, ongoing conflict, weak cold chain infrastructure, and fragmented governance contribute to these challenges (12,29); disentangling the pandemic\'s contribution from pre-existing structural barriers is not possible with available data.')

add_para('The heterogeneous recovery patterns are consistent with global assessments. The IA2030 Global Progress Report 2024 noted that initial post-pandemic recovery has not been sustained globally, though some progress was seen in the WHO African Region (1). The WHO Executive Board report highlighted that recovery has been uneven, with least progress in low-income countries (7). This study is partially consistent: while DR Congo and Burundi experienced minimal recovery, South Sudan, also low-income, achieved baseline-relative recovery from a low baseline, suggesting that income status alone does not determine outcomes.')

add_para('The observed differences in recovery trajectories across EAC countries may reflect multiple factors, including health system governance, adaptation of service delivery during and after the pandemic, integrated supportive supervision (30), catch-up campaign intensity, and the extent of pandemic-related disruption to routine immunization services, including health worker redeployment for COVID-19 response and reduced service utilization (13,14). However, this descriptive study cannot establish causal relationships between any specific factor and observed coverage changes. These potential explanations should be considered hypotheses for future investigation rather than evidence-based explanations.')

add_para('The Big Catch-Up initiative, launched in 2023 by WHO, UNICEF, and Gavi, represents a critical intervention for addressing the immunity gaps identified in this study (3,17). Its three pillars of catch-up, restore, and strengthen align directly with EAC needs. However, activities only began in 2024 (1), which may explain why recovery remains incomplete. The full impact may not be reflected in 2024 estimates and may become evident in future years.')

add_heading('4.1 Strengths and Limitations', level=2)
add_para('This study uses the most recent WUENIC estimates (2025 revision), includes all seven EAC partner states, and analyzes three key vaccine indicators (DTP1, DTP3, MCV1) and dropout rates. To our knowledge, it is the first to examine post-pandemic immunization recovery specifically within the EAC for the 2019–2024 period.')

add_para('The study has several limitations. First, WUENIC estimates depend on the quality and availability of underlying empirical data, which vary across countries and time (21,22). Estimates may be carried forward unchanged when no new data are reported: South Sudan\\u2019s values were identical across all three indicators from 2022 to 2024, DR Congo\\u2019s DTP1 and DTP3 were unchanged between 2021 and 2022, and Burundi\\u2019s DTP1 and DTP3 were identical in 2023 and 2024. These flat values may reflect data gaps rather than genuine stability. Grade of Confidence ratings, which could help distinguish empirically grounded estimates from carried-forward values, were not incorporated because they are unavailable through the WHO GHO API (24). Second, the short time series (6 data points per country) precludes formal statistical modeling; results should be interpreted as exploratory trend description rather than confirmatory. Third, national-level estimates may mask subnational disparities, particularly in large countries such as DR Congo and Tanzania; future studies should incorporate district-level data and equity stratifiers. Fourth, the study is descriptive and cannot establish causal relationships or assess the contribution of specific interventions to observed recovery patterns. Fifth, reliance on a single data source without triangulation against independent household surveys (DHS, MICS) limits robustness, particularly for the 0\\u20131 percentage-point differences that determine marginal classifications.')

add_para('Sixth, the four-tier recovery framework is an investigator-defined operational tool with heuristic thresholds that has not been previously validated. Classifications for Rwanda (margins of 0pp on two indicators) and Uganda (1pp on two indicators) are fragile, while South Sudan\\u2019s classification is robust with all margins \\u22657pp. The framework\\u2019s generalizability to other regions or data sources is uncertain. However, an informal comparison with WHO regional assessments shows broad agreement: DR Congo and Burundi are identified as having persistent coverage challenges (8), and South Sudan\\u2019s improvement is consistent with WHO documentation of gradual scale-up (28), providing tentative external support. Finally, subsequent WUENIC revisions may update earlier estimates, potentially altering the recovery patterns described.')

add_para('A sensitivity check using 2025 WUENIC data reclassified Rwanda from marginal recovery to not recovered (DTP3 and MCV1 each \\u20133pp vs 2019), while Uganda and South Sudan maintained their classifications. All four not-recovered countries (Kenya, Tanzania, Burundi, DR Congo) remained not recovered, with Kenya\\u2019s DTP3 margin worsening from \\u20132pp to \\u20135pp. A threshold sensitivity analysis varying the baseline-relative recovery cutoff between 1 and 3pp confirmed that classifications were robust except for Uganda, which shifted from marginal to baseline-relative recovery at a 1pp cutoff. These findings illustrate the fragility of marginal classifications rather than providing definitive reclassification (22). Future studies should incorporate subsequent estimates once informed by a fuller reporting cycle.')

add_para('This study is reported in accordance with the STROBE guidelines for observational studies using secondary data (31) and aligns with the GATHER criteria where applicable (23).')

add_heading('4.2 Implications for Policy and Practice', level=2)
add_para('The findings of this study have several important implications for EAC health ministries and immunization partners. First, the persistent coverage declines in DR Congo, Tanzania, Burundi, and Kenya underscore the urgent need for intensified catch-up vaccination activities, particularly targeting zero-dose and under-vaccinated children who have accumulated since 2019. The Big Catch-Up initiative provides a framework for these efforts, but its implementation must be accelerated and adequately resourced.')

add_para('Third, the regional cooperation framework provided by the EAC offers opportunities for cross-learning and mutual support. Rwanda\'s apparent recovery trajectory, whatever its underlying drivers, may offer lessons for other EAC partner states, though further investigation is needed to identify which specific factors contributed. The EAC Centre of Excellence for Vaccine, Immunization and Health Supply Chain Management, established with support from the German Development Bank (KfW) and hosted at the University of Rwanda (32), provides a platform for such knowledge exchange.')
add_para('Fourth, the declining MCV1 coverage in Kenya, Tanzania, and DR Congo is particularly alarming given the risk of measles outbreaks. The WHO African Region has reported ongoing outbreaks of vaccine-preventable diseases, including measles, with 66 large outbreaks recorded in 2023, and declining surveillance performance since the pandemic, exacerbating the risk of undetected transmission (8,33). Enhanced measles surveillance and supplementary immunization activities should be prioritized in countries with declining MCV1 coverage.')

add_para('Fifth, catch-up interventions must prioritize equity by targeting rural, conflict-affected, and displaced populations who are disproportionately represented among zero-dose and under-vaccinated children. Subnational micro-planning and district-level coverage monitoring are essential to ensure that national-level recovery does not mask persistent or widening geographic inequities.')

add_para('Finally, sustained political commitment and domestic financing for immunization are essential for long-term recovery and progress toward IA2030 goals. The finding that only 16 of 47 countries in the WHO African Region achieved the 90% DTP3 coverage target in 2023 (8) underscores the scale of the challenge and the need for renewed investment.')

# ===================== CONCLUSION =====================
add_heading('5. Conclusion', level=1)
add_para('Post-pandemic recovery of routine childhood immunization coverage in the EAC has been uneven and incomplete as of 2024. Under the operational recovery framework used in this study, South Sudan met the predefined criterion for baseline-relative recovery, but absolute coverage levels remain critically low (DTP3: 73% in 2024) and identical 2022–2024 estimates may partly reflect non-updated WUENIC values rather than genuine programmatic improvement. Rwanda\'s status was inconclusive (margins that reversed under 2025 data), and Uganda showed marginal recovery based on +1pp margins sensitive to threshold choice. Kenya, Tanzania, Burundi, and DR Congo remain below their 2019 baselines, with DR Congo experiencing the most severe decline and a widening dropout rate suggesting challenges in retention along the vaccination cascade, though partial improvement in 2024 warrants monitoring. The Big Catch-Up initiative provides a critical framework for recovery, but its implementation must be accelerated. Regional cooperation through EAC frameworks, sustained political commitment, and targeted support for zero-dose children are essential for achieving IA2030 goals.')

add_heading('Data Availability Statement', level=1)
add_para('All data used in this study are publicly available from the WHO/UNICEF Estimates of National Immunization Coverage (WUENIC) database, accessible through the WHO Immunization Data Portal (https://immunizationdata.who.int/) and the WHO Global Health Observatory API (https://ghoapi.azureedge.net/api/). The extracted dataset and analysis code are available from the corresponding author upon reasonable request.')
add_para('Data were accessed on 27 July 2026.', italic=True)
add_para('Data were accessed on 27 July 2026.', italic=True)

add_heading('Author Contributions', level=1)
add_para('[Author 1] conceptualized the study, designed the analysis, extracted the data, conducted the statistical analysis, and wrote the original draft. [Author 2] reviewed and edited the manuscript. All authors read and approved the final manuscript. This study used the CRediT (Contributor Roles Taxonomy) classification system.')

# ===================== REFERENCES =====================
doc.add_page_break()
add_heading('References', level=1)

refs = [
    'Immunization Agenda 2030. IA2030 Global Progress Report 2024. Geneva: WHO; 2024. Available from: https://www.immunizationagenda2030.org/images/documents/Immunization_Agenda_2030_Global_Progress_Report_2024_final.pdf',
    'Shattock AJ, Johnson HC, yoon Sim S, et al. Contribution of vaccination to improved survival and health: modelling 50 years of the Expanded Programme on Immunization. The Lancet. 2024;403(10441):2307-2316. doi:10.1016/S0140-6736(24)00850-X',
    'World Health Organization, UNICEF, Gavi. An Essential Immunization Recovery Plan: Catch-Up, Restore and Strengthen. Geneva: WHO; 2023. Available from: https://www.immunizationagenda2030.org/images/documents/9789240075511-eng.pdf',
    'Lassi ZS, Naseem R, Salam RA, Siddiqui F, Das JK. The Impact of the COVID-19 Pandemic on Immunization Campaigns and Programs: A Systematic Review. International Journal of Environmental Research and Public Health. 2021;18(3):988. doi:10.3390/ijerph18030988',
    'Shapira G, Ahmed T, Drouard SHP, Fernandez PA, Kandpal E, Nzelu C, et al. Disruptions in maternal and child health service utilization during COVID-19: analysis from eight sub-Saharan African countries. Health Policy and Planning. 2021;36(7):1140-1151. doi:10.1093/heapol/czab064',
    'United Nations Children\'s Fund. The State of the World\'s Children 2023: For Every Child, Vaccination. New York: UNICEF; 2023. Available from: https://www.unicef.org/reports/state-worlds-children-2023',
    'World Health Organization. Progress towards global immunization goals and implementation of the Immunization Agenda 2030. Geneva: WHO; 2024. Document B154/9. Available from: https://apps.who.int/gb/ebwha/pdf_files/EB154/B154_9-en.pdf',
    'Bekele AT, Masresha BG, Bita Fouda AA, Mitula P, Bwaka A, Wanyoike S, et al. Progress on implementation of immunization agenda 2030 (IA2030) in the WHO African region: achievements, lessons learned and priorities. Pan African Medical Journal. 2025;51(Suppl):48959. doi:10.11604/pamj.supp.2025.51.1.48959',
    'East African Community. Treaty for the Establishment of the East African Community. Arusha: EAC; 1999. Available from: https://www.eac.int/documents/category/treaties',
    'East African Community. EAC Medicines and Health Technologies Policy. Arusha: EAC; 2018. Available from: https://www.eac.int/documents',
    'Mihigo R, Okeibunor J, Anya B, Mkanda P, Zawaira F. Challenges of immunization in the African Region. Pan African Medical Journal. 2017;27(Suppl 3):12. doi:10.11604/pamj.supp.2017.27.3.12127',
    'Nshimirimana D, Mihigo R, Clements CJ. Routine immunization services in Africa: back to basics. Journal of Vaccines & Immunization. 2013;1(1):6-12. doi:10.14312/2053-1273.2013-2',
    'Masresha B, Luce R, Shibeshi M, Ntsama B, N\'Diaye A, Chakauya J, et al. The performance of routine immunization in selected African countries during the first six months of the COVID-19 pandemic. Pan African Medical Journal. 2020;37(Suppl 1):12. doi:10.11604/pamj.supp.2020.37.1.26107',
    'Buonsenso D, Cinicola B, Kallon MN, Iodice F. Child Healthcare and Immunizations in Sub-Saharan Africa During the COVID-19 Pandemic. Frontiers in Pediatrics. 2020;8:517. doi:10.3389/fped.2020.00517',
    'Cardoso Pinto AM, Ranasinghe L, Dodd PJ, Budhathoki SS, Seddon JA, Whittaker E. Disruptions to routine childhood vaccinations in low- and middle-income countries during the COVID-19 pandemic: A systematic review. Frontiers in Pediatrics. 2022;10:979769. doi:10.3389/fped.2022.979769',
    'Aguinaga-Ontoso I, Guillen-Aguinaga S, Guillen-Aguinaga L, Alas-Brun R, Onambele L, Aguinaga-Ontoso E, et al. COVID-19 Impact on DTP Vaccination Trends in Africa: A Joinpoint Regression Analysis. Vaccines. 2023;11(6):1103. doi:10.3390/vaccines11061103',
    'World Health Organization Regional Office for Africa. Progress Report on the Framework for the Implementation of the Immunization Agenda 2030 in the WHO African Region. Brazzaville: WHO AFRO; 2024. Document AFR/RC74/INF.DOC/7.',
    'World Health Organization Regional Office for Africa. Framework for the Implementation of the Immunization Agenda 2030 in the WHO African Region. Endorsed August 2021.',
    'Causio FA, Villani L, Mariani M, Pastorino R, De Waure C, Ricciardi W, et al. Vaccination coverage trends in European Union from 1980 to 2020: A joinpoint Regression Analysis. European Journal of Public Health. 2022;32(Suppl 3):ckac129.306. doi:10.1093/eurpub/ckac129.306',
    'World Health Organization, United Nations Children\'s Fund. WHO/UNICEF Estimates of National Immunization Coverage (WUENIC), 2025 revision. Geneva: WHO; 2026. Available from: https://immunizationdata.who.int/pages/coverage/wuenic-coverage.html',
    'Burton A, Monasch R, Lautenbach B, Gacic-Dobo M, Neill M, Karimov R, et al. WHO and UNICEF estimates of national infant immunization coverage: methods and processes. Bulletin of the World Health Organization. 2009;87:535-541. doi:10.2471/BLT.08.053819',
    'World Health Organization. WHO/UNICEF estimates of national immunization coverage: Questions and Answers. Geneva: WHO; 2024. Available from: https://www.who.int/news-room/questions-and-answers/item/who-unicef-estimates-of-national-immunization-coverage',
    'Stevens GA, Alkema L, Black RE, Boerma JT, Collins GS, Ezzati M, et al. Guidelines for Accurate and Transparent Health Estimates Reporting: the GATHER statement. The Lancet. 2016;388(10062):e19-e23. doi:10.1016/S0140-6736(16)30388-9',
    'Danovaro-Holliday MC, Gacic-Dobo M, Diallo MS, Murphy P, Brown DW. Compliance of WHO and UNICEF estimates of national immunization coverage (WUENIC) with Guidelines for Accurate and Transparent Health Estimates Reporting (GATHER) criteria. Gates Open Research. 2021;5:77. doi:10.12688/gatesopenres.13258.1',
    'World Health Organization. Global Health Observatory Data Repository. Geneva: WHO; 2024. Available from: https://ghoapi.azureedge.net/api/',
    'United Nations, Department of Economic and Social Affairs, Population Division. World Population Prospects 2024 Revision. New York: United Nations; 2024. Available from: https://population.un.org/wpp/',
    'World Health Organization. WHO-UNICEF estimates of national immunization coverage: surviving infant populations. Geneva: WHO; 2024. Available from: https://immunizationdata.who.int/pages/coverage/wuenic-coverage.html',
    'Mboussou F, Kada S, Danovaro-Holliday MC, Farham B, Gacic-Dobo M, Shearer JC, et al. Status of Routine Immunization Coverage in the World Health Organization African Region Three Years into the COVID-19 Pandemic. Vaccines. 2024;12(2):168. doi:10.3390/vaccines12020168',
    'Van Brusselen D, Dubois AH, Bindu LK, Moluh Z, Nzomukunda Y, Liesenborghs L. Not only vaccine hesitancy, but also vaccination campaign hesitancy drives measles epidemics in conflict-torn eastern DR Congo. Conflict and Health. 2024;18(1):14. doi:10.1186/s13031-024-00569-6',
    'Bello IM, Lebo E, Shibeshi M, Akpan GU, Chakauya J, Masresha B, et al. Implementation of integrated supportive supervision in the context of coronavirus 19 pandemic: its effects on routine immunization and vaccine preventable diseases indicators in the East and Southern African Countries. Pan African Medical Journal. 2021;38:164. doi:10.11604/pamj.2021.38.164.27349',
    'von Elm E, Altman DG, Egger M, Pocock SJ, Gøtzsche PC, Vandenbroucke JP. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. PLoS Medicine. 2007;4(10):e296. doi:10.1371/journal.pmed.0040296',
    'KfW Development Bank. Vaccination program funding in cooperation with Gavi, East African Community: Ex-post Evaluation. Frankfurt: KfW; 2023. Available from: https://www.kfw-entwicklungsbank.de/PDF/Evaluierung/Ergebnisse-und-Publikationen/PDF-Dokumente-E-K_EN/EAC_Gavi_2023_E.pdf',
    'Masresha B, Luce R, Katsande R, Dosseh A, Tanifum P, Lebo E, et al. The impact of the COVID-19 pandemic on measles surveillance in the World Health Organisation African Region, 2020. Pan African Medical Journal. 2021;39(Suppl 1):192. doi:10.11604/pamj.2021.39.192.29491'
]

for i, ref in enumerate(refs, 1):
    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    run = p.add_run(f'{i}. {ref}')
    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)

# ===================== SAVE =====================
doc.save(OUTPUT)
print(f'Manuscript saved to: {OUTPUT}')
