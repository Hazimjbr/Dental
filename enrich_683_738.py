import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q683_738_exps = {
    683: 'For children aged 3 to 6 years in a non-fluoridated area (<0.3 ppm), the daily recommended supplemental fluoride dosage is 0.50 mg.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    684: 'Nitrous oxide can induce hypoxia if not carefully titrated, making it contraindicated in patients with sickle cell anemia where hypoxia triggers sickling crises.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    686: 'Maxillary lateral incisors (12 and 22) have roots inclined palatally; hence, apical infections typically drain palatally, forming palatal abscesses.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 82)',
    690: 'In the "early lesion" of gingivitis (4 to 7 days of plaque accumulation), the cellular infiltrate is dominated by T-lymphocytes and PMN leukocytes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    691: 'At approximately 11 years of age, the mixed dentition is characterized by erupted permanent incisors, erupting premolars/canines, and absent second molars.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    692: 'An ANB angle greater than +4 degrees (such as +8) indicates a skeletal Class II relationship, commonly presenting as Class II division 1 malocclusion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    694: 'The pterygomandibular raphe serves as the boundary and site of origin/insertion for both the buccinator muscle anteriorly and the superior pharyngeal constrictor posteriorly.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    695: 'Periapical lesions are dominated by polymicrobial infections, transitioning from initial facultative aerobes to predominantly obligate anaerobes over time.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    698: 'A carbuncle is a deep, coalesced cluster of infected hair follicles (furuncles) characteristically caused by Staphylococcus aureus.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    702: 'Water fluoridation is globally recognized as the most cost-effective, equitable, and successful community-wide public health measure for caries prevention.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    703: 'When the drinking water fluoride concentration is between 0.3 and 0.6 ppm, no supplemental fluoride is recommended for children aged 3 years or younger.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    709: 'For pediatric patients with high caries risk, posterior bitewing radiographs are recommended at 12-to-18-month intervals (yearly).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    717: 'Squamous cell carcinoma of the lower lip (middle third) typically metastasizes first to the submental lymph nodes.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    718: 'A single large dose of radiation delivered at once causes greater biological damage because cells have no time to undergo DNA repair.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    719: 'High-risk cardiac conditions, including congenital heart valve diseases, require antibiotic prophylaxis before bacteremia-inducing dental treatments.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    720: 'Systemic antibiotics are not indicated for localized, chronic conditions like non-acute NUG, which are effectively managed via local debridement.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    725: 'A kinematic facebow (hinge-bow) is used to precisely locate the transverse horizontal axis of rotation (terminal hinge axis) of the condyles.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    726: 'The gingival third of a tooth displays a warmer, more saturated hue because of the thicker underlying dentin reflecting through thin enamel.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    729: 'The occipitomental projection (Water\'s view) is the gold standard plain film radiograph for evaluating the maxillary sinuses.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    730: 'Water fluoride levels exceeding 4.0 ppm consistently cause moderate-to-severe dental fluorosis (mottled enamel) in developing permanent teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    731: 'Water oral irrigators physically flush non-adherent food particles and bacteria without mechanical injury to healthy gingival tissues.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    733: 'Palpating the floor of the mouth between the tongue and mandibular border is performed to detect submandibular and cervical lymphadenopathy.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    736: 'The lateral pterygoid muscle inserts directly into the condylar neck and TMJ capsule, pulling the mandible forward and deviating it upon contraction.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    737: 'Dentinogenesis imperfecta is a hereditary defect of dentin matrix mineralization that initiates during the histodifferentiation stage of odontogenesis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    738: 'Die stones (alpha-hemihydrate) consist of dense, regularly shaped crystals that require significantly less gauging water than porous plaster (beta-hemihydrate).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)'
}

for q_id, exp in q683_738_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q683-Q738!")
