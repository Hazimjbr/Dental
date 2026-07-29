import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q234_263_exps = {
    234: 'A high restoration causes occlusal trauma and inflammation of the periodontal ligament, leading to acute apical periodontitis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 204)',
    235: 'Thorough preoperative clinical and radiographic assessment is the most critical factor for planning safe surgical extraction.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    236: 'Paresthesia (numbness) of the lip or nerve distribution is a classic warning sign of perineural invasion by a malignant oral lesion.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    237: 'Severe alveolar resorption in the mandible can expose the mental nerve, causing lower lip paresthesia from denture base pressure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    238: 'The auriculotemporal nerve (branch of V3) provides the primary sensory innervation to the temporomandibular joint (TMJ).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    239: 'Cleidocranial dysplasia is characterized by multiple supernumerary teeth, failure of eruption, and pseudo-anodontia.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    240: 'Mealtime swelling of the submandibular gland is a classic sign of salivary duct obstruction due to a sialolith (calculus).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 162)',
    241: 'Pemphigus vulgaris causes intraepithelial vesicle and bullae formation due to autoantibodies against desmogleins.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    242: 'Wickham\'s striae (fine lace-like white lines) are pathognomonic clinical features of reticular oral lichen planus.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 185)',
    243: 'Denture stomatitis is a Candida infection, treated with topical antifungals (like Nystatin) and improving denture hygiene.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    244: 'Excluding third molars, the mandibular second premolars (35, 45) are the most commonly congenitally missing teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 268)',
    245: 'The overall malignant transformation rate of oral leukoplakia is historically estimated around 3% to 6%.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    246: 'Koplik spots are prodromal signs of measles (Rubeola), not German measles (Rubella) which has no specific oral prodromal signs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    247: 'Fordyce\'s granules are ectopic sebaceous glands appearing as small yellow-white spots, not classified as pathological white lesions.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    248: 'Reduced occlusal vertical dimension (OVD) causes folding at the corners of the mouth, pooling saliva and leading to angular cheilitis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    249: 'Lamina dura is typically lost in hyperparathyroidism, Paget\'s, and fibrous dysplasia, but remains normal in osteogenesis imperfecta.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    250: 'Fever is the classic constitutional systemic response to circulating pyrogens from an active systemic infection.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 55)',
    251: 'An early radiographic sign of a periapical abscess is the thickening of the periodontal ligament space around the root apex.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    252: 'Hypoglycemia (insulin shock) presents with moist skin, sweating, and rapid pulse; immediate administration of oral glucose is indicated.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 56)',
    253: 'Oral squamous cell carcinoma is treated primarily using surgical wide local excision combined with adjuvant radiotherapy.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    254: 'Primary maxillary molars are extracted with a primary buccal expansion force due to the thin buccal cortical bone.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 242)',
    255: 'Addition silicone (vinyl polysiloxane) has excellent dimensional stability and can be poured up to two weeks after impression taking.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    256: 'Large restorations require sequential small mixes of amalgam to ensure proper trituration, adaptation, and prevent pre-setting.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    257: 'Polymerization shrinkage (setting contraction) of composite resins pulls the material away from cavity margins, causing microleakage.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    258: 'To provide bulk and prevent edge fracture of both tooth and amalgam, the optimum cavosurface angle is 90 to 110 degrees (95-110°).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    259: 'Light-curing triggers rapid polymerization and rapid contraction (shrinkage) compared to the slower, self-curing process.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    260: 'Etched enamel that is not bonded will remineralize back to normal within a week due to mineral deposition from saliva.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 25)',
    261: 'Cusps weakened by decay should be reduced flat by 2mm to provide adequate bulk and resistance form for the amalgam overlay.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    262: 'Mandibular first premolars have a dominant buccal cusp and small lingual cusp; tilting lingually protects the large buccal pulp horn and supports the lingual cusp.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)',
    263: 'Radiographically, early proximal caries appears as a triangle with its base at the outer enamel surface and apex pointing toward the dentinoenamel junction.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)'
}

for q_id, exp in q234_263_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q234-Q263!")
