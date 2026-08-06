import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q832_856_exps = {
    832: 'Accidental intravascular injection of lidocaine and vasoconstrictor causes rapid systemic toxicity and psychogenic/cardiovascular side effects.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    833: 'An osteolytic lesion associated with nerve paresthesia is highly suspicious for a malignant or aggressive benign neoplasm, requiring extraction and biopsy.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    834: 'Chronic periodontitis progresses via the "random burst theory," characterized by short periods of active tissue destruction followed by quiescent phases.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    835: 'Apically displaced flaps are designed to eliminate periodontal pockets while preserving the zone of attached gingiva and increasing clinical crown length.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    836: 'Trauma from occlusion causes bone loss, mobility, and PDL widening, but does not initiate gingival inflammation or true pocket formation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    837: 'The hallmark clinical features of periodontitis are the apical migration of the junctional epithelium and true periodontal pocket formation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    838: 'Down\'s syndrome (Trisomy 21) is frequently associated with hypodontia (congenitally missing teeth) and microdontia.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    839: 'Cleidocranial dysplasia is characterized by delayed fontanelle closure, clavicular aplasia, and multiple impacted supernumerary teeth (hyperdontia).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    840: 'The presence of antibodies to hepatitis B surface antigen (anti-HBs) indicates immunity, representing no transmission risk.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    841: 'Initial non-surgical periodontal therapy consisting of oral hygiene instruction and subgingival scaling/root planing is the most conservative treatment.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    842: 'An aluminum filter absorbs low-energy, non-diagnostic X-ray photons to reduce patient skin radiation dose.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    843: 'An eruption cyst (hematoma) over an erupting tooth is managed conservatively or by simple local excision of the overlying tissue roof.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    844: 'Since the successor first premolar is close to eruption at age 10, premature loss of a primary first molar rarely requires a space maintainer.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    845: 'Retrieving a root tip displaced into the maxillary sinus is typically performed surgically via the Caldwell-Luc approach through the canine fossa.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    846: 'Central hemangioma is a rare, slow-growing expansile vascular lesion of the jaw that can cause severe, life-threatening hemorrhage.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    847: 'The mandibular primary second molar is the most frequently retained deciduous tooth, due to congenital absence of the permanent successor.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    848: 'Streptococcus mutans utilizes glucosyltransferases to synthesize sticky, extracellular water-insoluble glucans from sucrose.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    849: 'Benzodiazepines provide anxiolysis, anterograde amnesia, and skeletal muscle relaxation, but do not produce postoperative headaches.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    850: 'Formocresol pulpotomy is indicated for primary teeth with vital carious pulpal exposures, fixing the coronal pulp tissue.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    851: 'If only upper first premolars (14, 24) are extracted to correct a Class II division 1 malocclusion, the final molar relationship remains in full unit Class II.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    852: 'The jugulodigastric lymph node (tonsillar node) is situated inferior to the angle of the mandible.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    853: 'Herpangina (caused by Coxsackievirus A) is clinically diagnosed, but confirmation is achieved via viral serology or PCR.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    854: 'The lead foil backing in a film packet absorbs backscatter radiation, protecting the patient\'s tissues and preventing film fogging.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    855: 'Complete fixation of radiographic film typically requires at least 10 minutes (double the clearing time) at standard room temperature.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    856: 'Manual film processing requires developing for exactly 5 minutes at 20°C (68°F) for optimum density and contrast.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)'
}

for q_id, exp in q832_856_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q832-Q856!")
