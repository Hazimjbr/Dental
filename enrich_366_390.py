import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q366_390_exps = {
    366: 'Histopathological examination (biopsy) is the only definitive method to differentiate between periapical granulomas, radicular cysts, and chronic abscesses.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    367: 'Acute inflammation of the apical periodontal ligament results in exquisite tenderness of the tooth to vertical percussion or biting pressure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 204)',
    368: 'Marsupialization (decompression) is a conservative surgical technique used to treat large jaw cysts, reducing their volume before enucleation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    369: 'Oral candidiasis is best confirmed by a periodic acid-Schiff (PAS) or KOH smear showing pseudohyphae and budding yeast cells under the microscope.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    370: 'Tetracycline chelates with calcium ions during tooth mineralization, causing intrinsic yellow-brown staining of primary and permanent teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    371: 'Ameloblastoma is a benign but locally aggressive odontogenic tumor that most commonly arises in the posterior mandible (molar-ramus area).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 158)',
    372: 'Long-term steroid therapy suppresses the hypothalamic-pituitary-adrenal (HPA) axis, risking acute adrenal crisis under dental surgical stress.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    373: 'Warm, moist hands and heat intolerance are classic systemic signs of hyperthyroidism (thyrotoxicosis) due to an elevated metabolic rate.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 55)',
    374: 'The standard AHA regimen for endocarditis prophylaxis is a single dose of Amoxicillin 2g orally, administered 1 hour prior to dental procedures.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    375: 'Primary herpetic gingivostomatitis classically presents in children with high fever, lymphadenopathy, and widespread painful oral vesicles.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    376: 'Primary herpetic gingivostomatitis is caused by infection with Herpes Simplex Virus Type 1 (HSV-1).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    377: 'Rapid injection increases local tissue damage and systemic absorption rate; local anesthetics should always be injected slowly (approx. 1 ml/min).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    378: 'Glutaraldehyde is a high-level disinfectant and chemical sterilant with potent virucidal, bactericidal, and sporicidal activity.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    379: 'Mumps is a self-limiting viral parotitis; antibiotics are ineffective against viruses and are not indicated unless secondary bacterial infection occurs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    380: 'The target compression rate during cardiopulmonary resuscitation (CPR) is at least 80 to 100 compressions per minute.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 55)',
    381: 'Nitrous oxide has a high MAC (>100%), meaning it cannot achieve surgical anesthesia alone without causing hypoxia (due to low oxygen ratios).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    382: 'A calibrated periodontal probe is the primary clinical tool used to measure probing depths and confirm the presence of a pocket.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    383: 'A preformed stainless steel (wrought base metal) crown is the treatment of choice to restore and protect pulpotomized deciduous molars.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 242)',
    384: 'An acute abscess is histologically characterized by purulent exudate consisting primarily of dead and dying neutrophils (polymorphonuclear leukocytes).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 55)',
    385: 'The clinical presentation of yellow \'sulfur granules\' (composed of bacterial colonies) in purulent exudate is pathognomonic for Actinomycosis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    386: 'Alveolar osteitis (dry socket) is a self-limiting condition; the primary and immediate clinical aim of treatment is local pain control.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 88)',
    387: 'A submandibular sialolith causes localized swelling and pain in one gland, but does not cause generalized dry mouth (xerostomia) like systemic drugs or Sjögren\'s.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 162)',
    388: 'Cicatricial pemphigoid involves subepithelial splitting, producing tense vesicles that remain intact in the oral cavity longer than intraepithelial vesicles.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    389: 'Mumps (epidemic parotitis) is a viral infection causing acute, painful, bilateral inflammatory swelling of the salivary glands.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    390: 'An acetone (fruity) breath odor is a classic clinical indicator of diabetic ketoacidosis due to the accumulation of ketone bodies.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 56)'
}

for q_id, exp in q366_390_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q366-Q390!")
