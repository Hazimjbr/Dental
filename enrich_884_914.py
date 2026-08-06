import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q884_914_exps = {
    884: 'A marginal discrepancy of 0.3 mm (300 µm) is clinically unacceptable and indicates an impression distortion, requiring a new impression and crown remake.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    885: 'A large marginal gap at amalgam borders permits saliva and bacterial ingress, significantly increasing the risk of secondary (recurrent) caries.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    886: 'Histologically, pit and fissure caries initiate on the opposing lateral walls of the fissure, rather than at the absolute bottom.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 26)',
    887: 'During lateral mandibular excursions, the coronoid process moves forward and can impinge on the buccal flange of a maxillary denture if it is too thick.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    888: 'In Munsell\'s color system, Chroma represents the purity, intensity, or saturation of a color (Hue), while Value represents brightness.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    889: 'Auto-polymerizing acrylic special trays must be fabricated at least 12-24 hours prior to use to ensure complete polymerization shrinkage has occurred.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    890: 'Although dentures cover tissues, gingivitis in RPD wearers is primarily driven by poor plaque control and bacterial accumulation around abutments.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    891: 'If a non-rigid keyway is placed on the distal of an abutment, natural mesial drift of the posterior teeth will cause the key to unseat from the keyway.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    892: 'In a deep bite Class II Division 2 patient, a non-rigid connector is contraindicated on a central incisor abutment due to heavy rotational forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    893: 'The neutral zone is the potential space where the forces exerted by the tongue outwards are equal to the forces of the cheeks and lips inwards.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    895: 'Contraction of the temporalis muscle elevates and retracts the mandible; it does not depress (open) the jaw.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    896: 'The Knoop hardness scale ranks materials in descending hardness: Tungsten Carbide (~1800) > Feldspathic Porcelain (~460) > Enamel (~340) > Acrylic (~20).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 88)',
    897: 'Cuspal reduction for a functional cusp overlay requires a minimum of 2.0 mm of amalgam thickness to provide adequate resistance form against fracture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    898: 'Radiographic bone healing (osteogenesis) and reduction of periapical radiolucency are typically visible starting 6 months post-obturation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    899: 'Mentalis muscle hyperactivity is a secondary compensation commonly associated with tongue thrust habits and atypical swallowing patterns.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    900: 'A mucosal draining fistula (sinus tract) resolves spontaneously once the intra-canal necrotic pulp infection is eliminated via routine RCT.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    903: 'Boiling water at 100°C is a disinfection method, not sterilization, as it fails to destroy highly resistant bacterial endospores.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    904: 'Post-operative dental hemorrhage can be caused by systemic hypertension (elevated BP) or impaired coagulation pathways (elevated PT).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    905: 'Long bones grow in length via interstitial growth and chondrocyte proliferation within the epiphyseal plate cartilage.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    906: 'Reticular oral lichen planus presents as Wickham\'s striae; while most common on the buccal mucosa, lesions can manifest anywhere in the oral cavity.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    907: 'Autogenous cancellous bone and marrow grafts have the highest osteogenic potential due to viable osteoblasts and osteoprogenitor cells.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    908: 'Pleomorphic adenoma (benign mixed tumor) is the most common salivary gland tumor, presenting as a slow-growing, painless, firm nodule in the parotid.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    912: 'Fusion is the union of two normally separate tooth germs, resulting in a single large tooth with reduced total tooth count in the arch.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    913: 'In growing children, the nasal floor / hard palate serves as a stable local reference plane for evaluating vertical skeletal changes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    914: 'Orthodontic headgear (headcap therapy) is used to control or redirect maxillary skeletal growth in young, developing skeletal Class II cases.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)'
}

for q_id, exp in q884_914_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q884-Q914!")
