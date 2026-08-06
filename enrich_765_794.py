import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q765_794_exps = {
    765: 'The Clark rule (SLOB rule) shows that anatomical structures like the incisive foramen shift relative to the central incisor apex when tube angulation changes.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    766: 'Osteoradionecrosis is managed with hyperbaric oxygen, prolonged antibiotic coverage, local sequestrectomy, or surgical resection of the necrotic jaw segment.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 198)',
    767: 'Systemic sclerosis (Scleroderma) characteristically presents radiographically as diffuse, uniform widening of the periodontal ligament (PDL) space.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    768: 'The lamina dura represents the radiographic appearance of the bundle bone lining the socket, anatomically known as the cribriform plate (alveolar bone proper).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    769: 'Bitewing radiographs are primarily indicated for the early detection of proximal (interproximal) enamel caries and bone loss.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    770: 'The nasopalatine (incisive) foramen appears as a well-defined oval or heart-shaped radiolucency between the roots of the maxillary central incisors.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    771: 'By age 4, crown calcification of all permanent teeth (except third molars) has commenced or is well underway.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    772: 'Cephalometric analysis evaluates dentofacial relationships by assessing the position of the dentition and jaws relative to the cranial base landmarks.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    773: 'At birth, dental follicles for all 20 primary teeth and the 4 permanent first molars (total 24) are present in the infantile jaws.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    777: 'Early resin-bonded bridges (Rochette type) relied on retentive perforations through the cast metal framework to lock the resin cement.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    780: 'Direct or indirect pulp capping applies a protective dressing (calcium hydroxide/MTA) to preserve the vitality of the entire pulp organ.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    781: 'A pulpotomy involves removing the inflamed coronal pulp to preserve the vitality and function of the remaining radicular pulp.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    782: 'Direct pulp capping is strictly contraindicated if clinical signs of irreversible pulpitis or radicular pulpal inflammation exist.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    783: 'Modern endodontics relies on mechanical debridement and chemical irrigation; two negative cultures are no longer considered mandatory for success.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    784: 'Apical surgery (apicoectomy) is indicated when non-surgical retreatments are blocked by rigid posts/fillings that pose a root fracture risk upon removal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    785: 'Inflammatory external root resorption is driven by necrotic pulp bacteria; it stops following thorough root canal disinfection and obturation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    786: 'Combined endo-perio lesions should be diagnosed beforehand using probing depths, vitality testing, and radiographs to establish a proper prognosis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    787: 'Radiography is essential in all phases of endodontics: for pre-operative diagnosis, working length determination, and post-obturation assessment (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    788: 'Cavity outline forms and pulp protection are dictated by pulpal anatomy (size/horns), which varies significantly with patient age and dental wear.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    789: 'Frequent irrigation suspends dentinal debris, prevents canal blockage, and dissolves organic tissue to avoid extruding toxic material apically.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    790: 'Accurate working length requires combining pre-operative films, adequate straight-line coronal access, a millimeter ruler, and a stable reference cusp (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    791: 'Dental gold alloys are categorized as Type I (soft), Type II (medium), Type III (hard), and Type IV (extra-hard) based on their yield strength (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    792: 'Because of thin enamel and large pulp horns in primary teeth, occlusal steps are prepared shallowly and may omit non-carious fissures to preserve tooth structure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    793: 'Early loss of a permanent first molar leads to tipping of adjacent teeth, extrusion of antagonists, and overall occlusal collapse affecting the entire dentition (Full mouth).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    794: 'Premature loss of primary molars leads to rapid mesial migration of the permanent first molar, resulting in loss of dental arch length and premolar crowding.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)'
}

for q_id, exp in q765_794_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q765-Q794!")
