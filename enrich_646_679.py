import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q646_679_exps = {
    646: 'Exogenous corticosteroid therapy results in adrenal suppression, delayed wound healing (impaired collagen synthesis), and osteoporosis (decreased bone formation).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    647: 'Severe, widespread mucosal ulcerations involving the oral cavity, esophagus, and GI tract can be a manifestation of Erythema Multiforme major (Stevens-Johnson syndrome).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    648: 'Cleidocranial dysplasia characteristically exhibits defective/absent clavicles, delayed fontanelle closure, maxillary hypoplasia, and multiple retained supernumerary/unerupted teeth (None of the above is correct, as all are typical features).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    649: 'Plummer-Vinson syndrome is characterized by the triad of microcytic hypochromic iron-deficiency anemia, esophageal webs (dysphagia), atrophic glossitis, and predisposing risk of oral/esophageal carcinoma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    650: 'Autoclaving destroys microbial life and resistant spores by denaturing and coagulating essential structural and enzymatic cellular proteins.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    651: 'Naloxone is a competitive opioid receptor antagonist used as the drug of choice to rapidly reverse respiratory depression in opioid overdose.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    653: 'Primary second molars are mesiodistally wider than their permanent successors (second premolars), creating the "leeway space" of Nance upon exfoliation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    655: 'Severe Von Willebrand\'s disease impairs platelet adhesion and decreases Factor VIII levels, requiring clotting factor/DDAVP hematological management identical to Hemophilia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    656: 'The zygomatic arch (specifically the zygomatic process of maxilla and temporal bone) serves as the anatomical origin for the masseter muscle.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    657: 'Primary herpetic gingivostomatitis is managed with supportive care (hydration, analgesics) and systemic Acyclovir if diagnosed within the first 72 hours.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    658: 'A mucocele (mucus extravasation phenomenon) typically presents as a painless, bluish, fluctuant swelling on the lower lip due to salivary duct trauma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    659: 'Pemphigus vulgaris is definitively diagnosed using direct immunofluorescence of perilesional tissue showing deposition of IgG autoantibodies in a fishnet pattern.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    662: 'Ankyloglossia (tongue-tie) is a congenital anomaly characterized by an abnormally short or thick lingual frenulum that restricts tongue movement.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    663: 'Early-stage oral squamous cell carcinoma is characteristically painless, presenting as an asymptomatic indurated ulcer or red/white plaque.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    664: 'A fracture of the left condylar neck impairs left lateral pterygoid function; upon opening, the unopposed right lateral pterygoid deviates the mandible to the fractured (left) side.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    665: 'Osteopetrosis (Albers-Schönberg or marble bone disease) is a rare genetic disorder characterized by impaired osteoclast function, yielding dense but brittle bones.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    666: 'Dentinogenesis imperfecta displays bulbous crowns, cervical constriction, short/blunt roots, and progressive pulp obliteration, with shell teeth seen in Type III.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    669: 'Acute life-threatening angioedema with airway compromise is immediately treated with intramuscular adrenaline (epinephrine) and intravenous corticosteroids.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    670: 'Excluding third molars, the mandibular second premolar is the most frequently congenitally missing permanent tooth, followed by the maxillary lateral incisor.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    671: 'Immunodeficient patients (e.g., in HIV/AIDS) exhibit high susceptibility to Epstein-Barr virus (EBV) reactivation, presenting clinically as oral hairy leukoplakia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    672: 'Odontogenic cysts arise from dental lamina remnants (rests of Serres), Hertwig\'s epithelial root sheath, or reduced enamel epithelium. The lamina dura is a radiographical bone shadow, not epithelial tissue.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 164)',
    674: 'According to the Inverse Square Law, doubling the distance from the source reduces the radiation intensity to one-fourth (1/d²).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    676: 'The immediate treatment priority for a horizontal root fracture is repositioning the coronal segment and rigid splinting (immobilization) for 4 weeks.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 238)',
    678: 'Gaseous porosity is caused by the vaporization of methyl methacrylate monomer (boiling point 100.8°C) when thick denture base sections overheat.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    679: 'In Class II amalgam preparations, insufficient depth (<1.5 mm) at the axiopulpal line angle (isthmus) leaves bulk amalgam too thin to resist occlusal fracture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)'
}

for q_id, exp in q646_679_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q646-Q679!")
