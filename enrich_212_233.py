import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q212_233_exps = {
    212: 'A long path of insertion (longer and more parallel axial walls) provides the greatest frictional retention for a full veneer crown.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    213: 'Wrought metals are plastically deformed and subjected to cold working (and controlled annealing) to modify grain structure and increase strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    215: 'The most common sequela of dental caries and subsequent pulpal necrosis in children is an acute or chronic apical abscess.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    216: 'Suprabony pockets are typically associated with horizontal bone loss, where the base of the pocket is coronal to the alveolar crest.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    217: 'Periodontitis is defined by the inflammatory destruction of the periodontal ligament (membrane) and alveolar bone attachment.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    218: 'A probing depth of 0 to 3 mm is considered clinically healthy and within the normal physiological range.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    219: 'Fibroblasts are the most abundant cell type in the periodontal ligament, responsible for collagen synthesis and remodeling.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    220: 'A false pocket (pseudopocket) is caused by gingival hyperplasia (enlargement) without any apical migration of the junctional epithelium.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    221: 'Mastication does not prevent calculus buildup; self-cleansing mechanisms, saliva flow, and anatomy help but chewing alone cannot clean stagnant plaque.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    222: 'Erosion and soft cementum are managed by removing the soft necrotic surface layer and restoring with Fluoride-releasing GIC.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 25)',
    223: 'Ethyl alcohol is a poor root canal disinfectant and is not useful for eradicating intrapulpal and periapical infections.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    224: 'Apical third root fractures have a high rate of natural healing; initial management is observation and monitoring pulp vitality.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 256)',
    225: 'An immediate radiograph is mandatory to assess the depth of intrusion, root fracture, and alveolar bone damage.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 254)',
    226: 'Electrical pulp testing is least useful/not possible on crowns or teeth with thick restorations (capped teeth) as currents cannot pass.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
    227: 'The palatal pulp canal of maxillary molars originates under the mesiolingual cusp, which is the largest cusp.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    229: 'Patients with a history of rheumatic heart disease (rheumatic fever) require antibiotic cover to prevent infective endocarditis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    230: 'Dental sedatives, analgesics, and anesthetics are safely managed if drug-drug interactions are monitored.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 104)',
    231: 'Opioids bind to mu receptors, mimicking the actions of endogenous opioid peptides (enkephalins and endorphins) to block pain.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    232: 'Accidental intravenous injection of local anesthetic causes rapid systemic absorption, leading to severe toxicity.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    233: 'Standard local anesthetics (without vasoactive amines) and simple analgesics do not interact with MAOIs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)'
}

for q_id, exp in q212_233_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q212-Q233!")
