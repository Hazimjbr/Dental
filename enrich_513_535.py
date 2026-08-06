import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q513_535_exps = {
    513: 'Pre-precordial thumping or locating the sternal compression point is assessed prior to starting chest compressions during basic life support.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    514: 'Suspected angina pectoris is immediately managed by placing the patient upright, administering sublingual glyceryl trinitrate (GTN), and providing high-flow oxygen.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 62)',
    515: 'The posterolateral border of the tongue contains foliate papillae which are rich in taste buds.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    516: 'Vitamin D resistant rickets (hypophosphatemic rickets) causes delayed tooth eruption, hypomineralization, and large pulp chambers with pulp horns extending to the ADJ.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    517: 'Dentinogenesis imperfecta pathognomonically presents on radiographs with early obliteration of pulp chambers and root canals ("bulbous crowns" with short roots).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    518: 'An asymptomatic, non-mobile non-vital primary tooth about to exfoliate requires no intervention other than monitoring.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    519: 'Blunt impact luxation trauma can sever the delicate apical blood supply, resulting in pulp necrosis despite intact crown structure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 238)',
    520: 'Primary oral malignant melanoma is an aggressive tumor with a poor prognosis, exhibiting a 5-year survival rate of approximately 15-20%.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    521: 'Heparin works almost instantaneously (onset within minutes intravenously or 20-30 min subcutaneously), so taking 8 hours to take effect is false.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    522: 'Water fluoridation provides maximum caries protection (up to 50% reduction) on smooth enamel surfaces compared to deep pits and fissures.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    524: 'Effective dietary counseling begins with obtaining a 3- to 7-day written diet diary to identify specific sucrose frequency patterns.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    525: 'Teeth associated with periapical cemento-osseous dysplasia remain characteristically vital and should not undergo endodontic treatment.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    526: 'Lidocaine (an amide local anesthetic) has extremely low allergenicity; true allergic reactions like angioneurotic edema are exceedingly rare compared to ester LAs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    527: 'Koplik\'s spots (bluish-white macules on inflamed buccal mucosa) are pathognomonic early diagnostic signs of Measles (Rubeola).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    528: 'The working cutting edge of a periodontal scaler or curette is formed by the junction of the face and the lateral surface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    529: 'Lateral periodontal cysts arise from remnants of the dental lamina (rests of Serres) developmental epithelial rests in the mandibular canine-premolar region.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 164)',
    530: 'Sialolithiasis (salivary duct stones), most commonly affecting Wharton\'s duct of the submandibular gland, causes classic mealtime pain and swelling.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    532: 'The Oculomotor nerve (CN III) carries parasympathetic fibers to the constrictor pupillae muscle; injury results in loss of constriction and pupil dilation (mydriasis).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    534: 'Aspirin produces analgesia and anti-inflammatory action by irreversibly inhibiting the cyclooxygenase (COX-1 & COX-2) enzymes, blocking prostaglandin synthesis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 64)',
    535: 'Haemophilia (A or B) causes a deficiency in intrinsic coagulation factors (VIII or IX), leading to a prolonged activated partial thromboplastin time (aPTT / clotting time).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)'
}

for q_id, exp in q513_535_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q513-Q535!")
