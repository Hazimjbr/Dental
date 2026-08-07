import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q984_1026_exps = {
    984: 'The critical pH at which enamel demineralization begins is approximately 5.5. Below this threshold, hydroxyapatite dissolves.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 26)',
    985: 'To prevent chronic occupational radiation exposure, the dentist or dental staff must never hold a film packet in the patient\'s mouth.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    997: 'Superficial dentin near the DEJ contains a lower density of dentinal tubules, with intertubular dentin forming the bulk of the dentin volume.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    1000: 'By covering the hard palate, complete dentures block minor taste buds and tactile receptors, leading to decreased taste and texture perception.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    1002: 'The mylohyoid muscle forms the muscular floor of the mouth and acts directly on the distolingual flange of a mandibular denture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    1003: 'The palatal root of the maxillary first molar characteristically curves toward the buccal aspect in its apical third (over 85% of cases).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    1004: 'Structural weakness in endodontically treated teeth is primarily caused by the loss of supporting coronal tooth structure during access cavity and caries removal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    1005: 'Dental extractions in irradiated bone carry a high risk of osteoradionecrosis. Management requires prophylactic hyperbaric oxygen therapy and primary surgical closure under antibiotics.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 198)',
    1006: 'A dark marginal stain surrounding a composite restoration indicates microleakage or recurrent caries, necessitating replacement of the restoration.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    1007: 'Mild post-operative sensitivity following recent amalgam placement is common and typically resolves within 4-6 weeks as secondary dentin deposits.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    1008: 'Complications following pulp capping in mature teeth include chronic pulpitis (pulpalgia), internal root resorption, or pulp canal obliteration (hypercalcification).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    1010: 'The metal framework must remain free of contamination between degasing (preheat) and the first opaque porcelain application to ensure proper oxide layer bond.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    1011: 'PFM bond failure (porcelain pop-off) can result from contamination, under-firing the opaque layer, or excessive gold conditioner thickness.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    1012: 'Continuous deposition of cementum at the root apices and bone remodeling at the alveolar fundus compensates for occlusal wear, maintaining occlusal contact.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    1013: 'Fibers and fibroblasts of the developing periodontal ligament generate the contractile forces necessary to guide active tooth eruption.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    1014: 'An increase in condylar guidance requires a corresponding increase in the compensating curve (Spee/Monson) or cusp height to maintain balanced occlusion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    1015: 'Fluoride is highly effective on smooth surfaces but is least effective in deep pits and fissures, which are best protected by resin sealants.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    1016: 'If severe post-operative sensitivity persists in a composite restoration, removing the composite and placing a ZOE sedative temporary dressing helps calm the pulp.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    1018: 'Conventional periodontal pocket surgery typically heals via the formation of a long junctional epithelium rather than true regeneration.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    1020: 'Frequent sugar exposure causes prolonged, repeated drops in plaque pH (Stephan curve) because acid diffusion through the plaque matrix is limited.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 26)',
    1021: 'Diabetes mellitus is a systemic modifying factor that exacerbates periodontal disease, but it is not a direct primary etiology (plaque is).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    1022: 'Diazepam is a long-acting benzodiazepine with an elimination half-life typically ranging between 20 to 50 hours (active metabolites extend this further).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    1023: 'Myxedema is the clinical presentation of severe hypothyroidism (hyposecretion of thyroid hormones) in adult patients.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 44)',
    1025: 'Cicatricial (benign mucous membrane) pemphigoid characteristically affects ocular tissues, leading to conjunctival scarring (symblepharon) and blindness.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    1026: 'Treponema pallidum (the spirochete causing syphilis) disseminates systemically via lymphatics and blood vessels within 24 hours of local inoculation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)'
}

for q_id, exp in q984_1026_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q984-Q1026!")
