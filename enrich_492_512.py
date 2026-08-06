import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q492_512_exps = {
    492: 'Occlusal interferences and prematurities during jaw closure trigger neuromuscular reflex responses that contribute to parafunctional habits like bruxism.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 144)',
    493: 'The oral mucosa is thin, non-resilient, and susceptible to trauma over bony prominences including the palatal raphe (midline), mylohyoid ridge, and palatal tori.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    495: 'Chemical pericementitis caused by medicament irritation is best managed by flushing the canal and placing an anti-inflammatory corticosteroid paste.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    496: 'The posterior palatal seal (PPS) area extends bilaterally from one hamular notch across the junction of the hard and soft palate to the opposite hamular notch.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    497: 'Washing the prepared cavity with water spray effectively removes debris and dentinal dust without causing chemical cytotoxicity or desiccation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    498: 'Herpes simplex virus type 1 (HSV-1) is shed in high concentrations within active vesicular fluid and infectious oral saliva.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    499: 'A periapical abscess typically involves a non-vital tooth with a history of deep caries/pulpitis, whereas a periodontal abscess involves a vital tooth with a deep pocket.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    500: 'Liver cirrhosis impairs the synthesis of vitamin K-dependent clotting factors (II, VII, IX, X), predisposing patients to severe post-extraction bleeding.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    501: 'Eruption of a permanent incisor palatally fails to resorb the primary tooth root normally, leading to prolonged retention of the primary incisor.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    502: 'Systemic toxicity of local anesthetics is directly proportional to the total absorbed systemic dose (mg/kg body weight) administered.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    503: 'Pierre-Robin sequence is classically defined by the triad of mandibular micrognathia, glossoptosis, and a high-arched or cleft secondary palate.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    504: 'Benzylpenicillin (Penicillin G) is acid-labile and destroyed by gastric acid, necessitating parenteral administration (unlike acid-stable Penicillin V).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 48)',
    505: 'The long buccal nerve (CN V3) is purely sensory to the buccal mucosa and skin; motor innervation to the buccinator muscle is supplied by the facial nerve (CN VII).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    506: 'Nitrous oxide is not metabolized by the body; 99.9% is rapidly eliminated unchanged via the lungs through exhalation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    507: 'Advanced Paget\'s disease of bone exhibits a pathognomonic "cotton-wool" radiopaque appearance on dental radiographs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    508: 'Aggregatibacter (Actinobacillus) actinomycetemcomitans is a Gram-negative, facultatively anaerobic, non-motile coccobacillus strongly implicated in aggressive periodontitis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    509: 'While A.a produces leukotoxin (kills PMNs) and immunosuppressive factors, tissue collagen destruction is primarily driven by host matrix metalloproteinases.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    510: 'Increasing mA, exposure time, or development time increases film density (darkness), whereas prolonged rinsing/washing can wash out silver grains and decrease density.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    511: 'A preserved, functional primary tooth (maintained via pulpectomy/root canal) serves as the natural and most ideal space maintainer.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    512: 'Paget\'s disease is characterized by markedly elevated serum alkaline phosphatase (reflecting high bone turnover) alongside normal serum calcium and phosphate levels.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)'
}

for q_id, exp in q492_512_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q492-Q512!")
