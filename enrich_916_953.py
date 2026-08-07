import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q916_953_exps = {
    916: 'The hallmark pathological signs of chronic periodontitis are mobility, apical migration of the junctional epithelium, true pocket formation, and subgingival calculus.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    917: 'A split-thickness flap preserves the periosteum on the bone surface, protecting the underlying alveolar bone and minimizing post-surgical bone loss.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    920: 'The subepithelial connective tissue graft (SCTG) is the gold standard for root coverage procedures, providing the best aesthetic and long-term outcomes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    921: 'When the ascending ramus severely limits the retromolar space distal to the last molar, a distal wedge procedure cannot be safely performed.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    922: 'Fluoride causes intrinsic tooth staining (dental fluorosis) during tooth formation, not extrinsic staining after eruption.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    923: 'Surface demineralization and enamel hypomineralization create porous zones with higher surface area, increasing fluoride uptake after eruption.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    924: 'Fluoride ions taken up by dental plaque bacteria inhibit the enzyme enolase, directly suppressing bacterial acid production.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    925: 'The amount of undercut engaged does not affect clasp flexibility; flexibility is determined by length, cross-section, material, and taper.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    929: 'Following direct pulp capping with calcium hydroxide, a calcific dentinal bridge forms within 6-8 weeks as confirmed by histological studies.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    930: 'The ideal crown-to-root ratio for a bridge abutment is 2:3 (crown length:root length), providing optimal leverage and stress distribution.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    937: 'Pulp capping is contraindicated when the tooth has had prolonged pain symptoms, indicating irreversible pulpitis has already progressed.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    938: 'Hyperaemic (reversible) pulpitis responds to corticosteroid pulp dressings, which reduce inflammation and allow pulpal recovery.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    940: 'During inhalation general anaesthesia, the inspired oxygen concentration must be maintained at no less than 30% to prevent hypoxia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    941: 'Bilateral symmetrical mandibular swellings in children are characteristic of bilateral cherubism (giant cell lesion) involving the angle and ramus.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    942: 'Applying sealants to newly erupted permanent molars with deep pits and fissures prevents bacterial colonization before caries can initiate.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    943: 'Periodontal pocket depth is measured clinically from the free gingival margin (top of the gingiva) to the base of the sulcus/pocket.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    945: 'Inflammatory cells like lymphocytes and plasma cells are associated with diseased periodontal tissue; they are not found in the normal, healthy PDL.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    946: 'Open/missing proximal contacts allow food packing, plaque accumulation, and bacteria to accumulate in the interproximal area, worsening periodontal disease.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    947: 'Placing an auxiliary rest adjacent to the edentulous space prevents the clasp assembly from rotating into the soft tissues under load.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    948: 'The weakest link in a pin-retained amalgam core with a full coverage crown is the cement lute between the amalgam core and the crown preparation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    949: 'Local anaesthetic toxicity causes CNS and cardiovascular depression (hypotension, respiratory depression); true hypertension is NOT a sign of toxicity.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    950: 'A thyroglossal duct cyst moves upward on swallowing and tongue protrusion because it is attached to the thyroid bone and base of the tongue.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 154)',
    951: 'Smoking creates an oxidizing environment (not a reducing one), which actually inhibits the growth of strict anaerobic periodontal pathogens.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    952: 'An asymptomatic 1 mm overfill of gutta-percha without signs of pathology is generally monitored without intervention until symptoms or failure occur.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    953: 'Similarly, an asymptomatic 1 mm cement overfill without pathological signs can be observed and left alone unless complications develop.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)'
}

for q_id, exp in q916_953_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q916-Q953!")
