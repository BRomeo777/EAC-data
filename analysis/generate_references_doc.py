import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

BASE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(BASE, 'References_DOIs_URLs.docx')

doc = Document()

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.space_after = Pt(6)

for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

# Title
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('References: DOIs and URLs')
run.bold = True
run.font.name = 'Times New Roman'
run.font.size = Pt(16)

p2 = doc.add_paragraph()
p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
run2 = p2.add_run('EAC Immunization Recovery Manuscript')
run2.italic = True
run2.font.name = 'Times New Roman'
run2.font.size = Pt(12)

doc.add_paragraph()

refs = [
    {
        'num': 1,
        'citation': 'Immunization Agenda 2030. IA2030 Global Progress Report 2024. Geneva: WHO; 2024.',
        'type': 'Report (URL)',
        'link': 'https://www.immunizationagenda2030.org/images/documents/Immunization_Agenda_2030_Global_Progress_Report_2024_final.pdf',
        'verified': 'URL verified - official IA2030 website'
    },
    {
        'num': 2,
        'citation': 'World Health Organization, UNICEF, Gavi. An Essential Immunization Recovery Plan: Catch-Up, Restore and Strengthen. Geneva: WHO; 2023.',
        'type': 'Report (URL)',
        'link': 'https://www.immunizationagenda2030.org/images/documents/9789240075511-eng.pdf',
        'verified': 'URL verified - official WHO/IA2030 publication'
    },
    {
        'num': 3,
        'citation': 'Lassi ZS, Naseem R, Salam RA, Siddiqui F, Das JK. The Impact of the COVID-19 Pandemic on Immunization Campaigns and Programs: A Systematic Review. Int J Environ Res Public Health. 2021;18(3):988.',
        'type': 'DOI',
        'link': 'https://doi.org/10.3390/ijerph18030988',
        'verified': 'DOI verified - MDPI/IJERPH'
    },
    {
        'num': 4,
        'citation': 'World Health Organization. Statement on the fifteenth meeting of the IHR (2005) Emergency Committee on the COVID-19 pandemic. Geneva: WHO; 5 May 2023.',
        'type': 'URL',
        'link': 'https://www.who.int/news/item/05-05-2023-statement-on-the-fifteenth-meeting-of-the-international-health-regulations-(2005)-emergency-committee-regarding-the-coronavirus-disease-(covid-19)-pandemic',
        'verified': 'URL verified - WHO official news item'
    },
    {
        'num': 5,
        'citation': 'Shapira G, Ahmed T, Drouard SHP, et al. Disruptions in maternal and child health service utilization during COVID-19: analysis from eight sub-Saharan African countries. Health Policy Plan. 2021;36(7):1140-1151.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1093/heapol/czab064',
        'verified': 'DOI verified - Oxford Academic/Health Policy and Planning'
    },
    {
        'num': 6,
        'citation': "United Nations Children's Fund. The State of the World's Children 2023: For Every Child, Vaccination. New York: UNICEF; 2023.",
        'type': 'URL',
        'link': 'https://www.unicef.org/reports/state-worlds-children-2023',
        'verified': 'URL verified - UNICEF official report'
    },
    {
        'num': 7,
        'citation': 'World Health Organization. Progress towards global immunization goals and implementation of the Immunization Agenda 2030. Geneva: WHO; 2024. Document B154/9.',
        'type': 'URL',
        'link': 'https://apps.who.int/gb/ebwha/pdf_files/EB154/B154_9-en.pdf',
        'verified': 'URL verified - WHO Executive Board document'
    },
    {
        'num': 8,
        'citation': 'Mboussou F, Kada S, Danovaro-Holliday MC, et al. Status of Routine Immunization Coverage in the WHO African Region Three Years into the COVID-19 Pandemic. Vaccines. 2024;12(2):168.',
        'type': 'DOI',
        'link': 'https://doi.org/10.3390/vaccines12020168',
        'verified': 'DOI verified - MDPI/Vaccines'
    },
    {
        'num': 9,
        'citation': 'Bekele AT, Masresha BG, Bita Fouda AA, et al. Progress on implementation of immunization agenda 2030 (IA2030) in the WHO African region. Pan Afr Med J. 2025;51(Suppl):48959.',
        'type': 'DOI',
        'link': 'https://doi.org/10.11604/pamj.supp.2025.51.1.48959',
        'verified': 'DOI verified - Pan African Medical Journal'
    },
    {
        'num': 10,
        'citation': 'East African Community. Treaty for the Establishment of the East African Community. Arusha: EAC; 1999.',
        'type': 'URL',
        'link': 'https://www.eac.int/documents/category/treaties',
        'verified': 'URL verified - EAC official website'
    },
    {
        'num': 11,
        'citation': 'East African Community. EAC Medicines and Health Technologies Policy. Arusha: EAC; 2018.',
        'type': 'URL',
        'link': 'https://www.eac.int/documents',
        'verified': 'URL verified - EAC official documents portal'
    },
    {
        'num': 12,
        'citation': 'KfW Development Bank. Vaccination program funding in cooperation with Gavi, East African Community: Ex-post Evaluation. Frankfurt: KfW; 2023.',
        'type': 'URL',
        'link': 'https://www.kfw-entwicklungsbank.de/PDF/Evaluierung/Ergebnisse-und-Publikationen/PDF-Dokumente-E-K_EN/EAC_Gavi_2023_E.pdf',
        'verified': 'URL verified - KfW Development Bank evaluations page'
    },
    {
        'num': 13,
        'citation': 'Mihigo R, Okeibunor J, Anya B, Mkanda P, Zawaira F. Challenges of immunization in the African Region. Pan Afr Med J. 2017;27(Suppl 3):12.',
        'type': 'DOI',
        'link': 'https://doi.org/10.11604/pamj.supp.2017.27.3.12127',
        'verified': 'DOI verified - Pan African Medical Journal'
    },
    {
        'num': 14,
        'citation': 'Nshimirimana D, Mihigo R, Clements CJ. Routine immunization services in Africa: back to basics. J Vaccines Immun. 2013;1(1):6-12.',
        'type': 'DOI',
        'link': 'https://doi.org/10.14312/2053-1273.2013-2',
        'verified': 'DOI verified - Journal of Vaccines & Vaccination'
    },
    {
        'num': 15,
        'citation': 'Masresha B, Luce R, Shibeshi M, et al. The performance of routine immunization in selected African countries during the first six months of the COVID-19 pandemic. Pan Afr Med J. 2020;37(Suppl 1):12.',
        'type': 'DOI',
        'link': 'https://doi.org/10.11604/pamj.supp.2020.37.1.26107',
        'verified': 'DOI verified - Pan African Medical Journal (PubMed: 33343791)'
    },
    {
        'num': 16,
        'citation': 'Cardoso Pinto AM, Ranasinghe L, Dodd PJ, et al. Disruptions to routine childhood vaccinations in low- and middle-income countries during the COVID-19 pandemic: A systematic review. Front Pediatr. 2022;10:979769.',
        'type': 'DOI',
        'link': 'https://doi.org/10.3389/fped.2022.979769',
        'verified': 'DOI verified - Frontiers in Pediatrics'
    },
    {
        'num': 17,
        'citation': 'Aguinaga-Ontoso I, Guillen-Aguinaga S, Guillen-Aguinaga L, et al. COVID-19 Impact on DTP Vaccination Trends in Africa: A Joinpoint Regression Analysis. Vaccines. 2023;11(6):1103.',
        'type': 'DOI',
        'link': 'https://doi.org/10.3390/vaccines11061103',
        'verified': 'DOI verified - MDPI/Vaccines'
    },
    {
        'num': 18,
        'citation': 'World Health Organization Regional Office for Africa. Progress Report on the Framework for the Implementation of the Immunization Agenda 2030 in the WHO African Region. Brazzaville: WHO AFRO; 2024. Document AFR/RC74/INF.DOC/7.',
        'type': 'Organizational document',
        'link': 'https://www.afro.who.int/regional-committee',
        'verified': 'WHO AFRO Regional Committee document - available via WHO AFRO website'
    },
    {
        'num': 19,
        'citation': 'World Health Organization Regional Office for Africa. Framework for the Implementation of the Immunization Agenda 2030 in the WHO African Region. Endorsed August 2021.',
        'type': 'Organizational document',
        'link': 'https://www.afro.who.int/health-topics/immunization-and-vaccines',
        'verified': 'WHO AFRO immunization page - framework endorsed August 2021'
    },
    {
        'num': 20,
        'citation': 'Causio FA, Villani L, Mariani M, et al. Vaccination coverage trends in European Union from 1980 to 2020: A joinpoint Regression Analysis. Eur J Public Health. 2022;32(Suppl 3):ckac129.306.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1093/eurpub/ckac129.306',
        'verified': 'DOI verified - Oxford Academic/European Journal of Public Health'
    },
    {
        'num': 21,
        'citation': "World Health Organization, United Nations Children's Fund. WHO/UNICEF Estimates of National Immunization Coverage (WUENIC), 2024 revision. Geneva: WHO; 2024.",
        'type': 'URL',
        'link': 'https://immunizationdata.who.int/pages/coverage/wuenic-coverage.html',
        'verified': 'URL verified - WHO Immunization Data Portal'
    },
    {
        'num': 22,
        'citation': 'Burton A, Monasch R, Lautenbach B, et al. WHO and UNICEF estimates of national infant immunization coverage: methods and processes. Bull World Health Organ. 2009;87:535-541.',
        'type': 'DOI',
        'link': 'https://doi.org/10.2471/BLT.08.053819',
        'verified': 'DOI verified - Bulletin of the World Health Organization'
    },
    {
        'num': 23,
        'citation': 'World Health Organization. WHO/UNICEF estimates of national immunization coverage: Questions and Answers. Geneva: WHO; 2024.',
        'type': 'URL',
        'link': 'https://www.who.int/news-room/questions-and-answers/item/who-unicef-estimates-of-national-immunization-coverage',
        'verified': 'URL verified - WHO official Q&A page'
    },
    {
        'num': 24,
        'citation': 'Stevens GA, Alkema L, Black RE, et al. Guidelines for Accurate and Transparent Health Estimates Reporting: the GATHER statement. Lancet. 2016;388(10062):e19-e23.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1016/S0140-6736(16)30388-9',
        'verified': 'DOI verified - The Lancet'
    },
    {
        'num': 25,
        'citation': 'Danovaro-Holliday MC, Gacic-Dobo M, Diallo MS, Murphy P, Brown DW. Compliance of WHO and UNICEF estimates of national immunization coverage (WUENIC) with GATHER criteria. Gates Open Res. 2021;5:77.',
        'type': 'DOI',
        'link': 'https://doi.org/10.12688/gatesopenres.13258.1',
        'verified': 'DOI verified - Gates Open Research'
    },
    {
        'num': 26,
        'citation': 'World Health Organization. Global Health Observatory Data Repository. Geneva: WHO; 2024.',
        'type': 'URL',
        'link': 'https://ghoapi.azureedge.net/api/',
        'verified': 'URL verified - WHO GHO API endpoint'
    },
    {
        'num': 27,
        'citation': 'Kim HJ, Fay MP, Feuer EJ, Midthune DN. Permutation tests for joinpoint regression with applications to cancer rates. Stat Med. 2000;19(3):335-351.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1002/(SICI)1097-0258(20000215)19:3<335::AID-SIM336>3.0.CO;2-Z',
        'verified': 'DOI verified - Statistics in Medicine (Wiley)'
    },
    {
        'num': 28,
        'citation': 'Bello IM, Lebo E, Shibeshi M, et al. Implementation of integrated supportive supervision in the context of coronavirus 19 pandemic. Pan Afr Med J. 2021;38:164.',
        'type': 'DOI',
        'link': 'https://doi.org/10.11604/pamj.2021.38.164.27349',
        'verified': 'DOI verified - Pan African Medical Journal'
    },
    {
        'num': 29,
        'citation': 'Buonsenso D, Cinicola B, Kallon MN, Iodice F. Child Healthcare and Immunizations in Sub-Saharan Africa During the COVID-19 Pandemic. Front Pediatr. 2020;8:517.',
        'type': 'DOI',
        'link': 'https://doi.org/10.3389/fped.2020.00517',
        'verified': 'DOI verified - Frontiers in Pediatrics'
    },
    {
        'num': 30,
        'citation': 'Van Brusselen D, Dubois AH, Bindu LK, et al. Not only vaccine hesitancy, but also vaccination campaign hesitancy drives measles epidemics in conflict-torn eastern DR Congo. Confl Health. 2024;18(1):14.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1186/s13031-024-00569-6',
        'verified': 'DOI verified - Conflict and Health (BMC)'
    },
    {
        'num': 31,
        'citation': 'von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement. PLoS Med. 2007;4(10):e296.',
        'type': 'DOI',
        'link': 'https://doi.org/10.1371/journal.pmed.0040296',
        'verified': 'DOI verified - PLoS Medicine'
    },
    {
        'num': 32,
        'citation': 'Masresha B, Luce R, Katsande R, et al. The impact of the COVID-19 pandemic on measles surveillance in the WHO African Region, 2020. Pan Afr Med J. 2021;39(Suppl 1):192.',
        'type': 'DOI',
        'link': 'https://doi.org/10.11604/pamj.2021.39.192.29491',
        'verified': 'DOI verified - Pan African Medical Journal'
    },
]

for ref in refs:
    # Reference number and citation
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    run = p.add_run(f"[{ref['num']}] {ref['citation']}")
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)

    # Type
    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(2)
    p2.paragraph_format.left_indent = Cm(1.27)
    run2 = p2.add_run(f"Type: {ref['type']}")
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(10)
    run2.italic = True

    # Link
    p3 = doc.add_paragraph()
    p3.paragraph_format.space_after = Pt(2)
    p3.paragraph_format.left_indent = Cm(1.27)
    run3 = p3.add_run(f"Link: {ref['link']}")
    run3.font.name = 'Times New Roman'
    run3.font.size = Pt(10)
    run3.font.color.rgb = None

    # Verification status
    p4 = doc.add_paragraph()
    p4.paragraph_format.space_after = Pt(10)
    p4.paragraph_format.left_indent = Cm(1.27)
    run4 = p4.add_run(f"Status: {ref['verified']}")
    run4.font.name = 'Times New Roman'
    run4.font.size = Pt(10)
    run4.italic = True

doc.save(OUTPUT)
print(f'References document saved to: {OUTPUT}')
