import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q857_883_exps = {
    857: 'Camphorquinone, the most common photoinitiator in dental resins, absorbs light most efficiently at a peak wavelength of approximately 468-470 nm.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    858: 'Laminated (sandwich) restorations utilize GIC to chemically bond to dentin, eliminating the need for mechanical retention grooves like a gingival lock.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    859: 'Chemical corrosion of dental amalgam is primarily caused by sulfide ions in oral fluids reacting to form silver sulfide, leading to tarnish.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    860: 'Conservative management of early superficial amalgam ditching involves sealing the margin with a flowable resin sealant to arrest microleakage.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    862: 'The floor of an occlusal rest seat must be inclined slightly toward the center of the tooth, transmitting occlusal forces axially down the long axis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    863: 'Acute apical abscess with systemic symptoms (fever) and facial swelling requires immediate pulpal debridement for drainage, alongside analgesics and systemic antibiotics.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    864: 'Placing finish lines supragingivally preserves periodontal health, facilitates accurate impressions, and simplifies plaque control.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    865: 'Acid etching (with 37% phosphoric acid) is a conservative, non-invasive technique that creates micro-retentive enamel porosities for resin tag infiltration.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    866: 'In a full-thickness (mucoperiosteal) flap, the mucosa and periosteum must be reflected together as a single unit to avoid tearing and preserve blood supply.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    867: 'Gothic arch tracing (arrow point tracing) is used to record the horizontal relation (centric relation), not the vertical dimension.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    868: 'Zinc oxide-eugenol (ZOE) paste can cause chemical irritation, burning sensations, or tissue reactions in patients sensitive to eugenol.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    869: 'During electrosurgery, tissue sticking to the electrode indicates insufficient power (current intensity too low), causing lateral heat accumulation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    870: 'Ethylene diamine tetra-acetic acid (EDTA) is a chelating agent that removes the inorganic components of the dentinal smear layer.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    872: 'Restoring a labially positioned tooth in normal alignment within a crowded arch requires proximal reduction, resulting in a crown that appears narrower.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    873: 'Due to the lingual inclination of mandibular molars, the lingual cusps are non-supporting and receive high lateral forces, making them prone to shear fractures.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    874: 'Clasp flexibility is determined by mechanical parameters: longer length, smaller/round cross-section, lower elastic modulus material, and uniform taper (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    875: 'A pinhole for retention (such as self-threading TMS pins) must be prepared to a depth of exactly 2.0 mm into sound dentin.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    876: 'Amalgam margins must be finished to a 90-degree (right angle) butt-joint cavosurface margin to prevent fracture of both tooth and thin amalgam.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    877: 'Tripoding records the specific three-dimensional tilt of the cast on the surveyor, allowing it to be accurately reoriented later.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    878: 'An irregular surface void on a casting indicates that loose fragments of investment broke off and became trapped in the mold during gold inflow.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    879: 'Gutta-percha is highly flexible and lacks rigidity, making it difficult to introduce and condense into very narrow, curved root canals.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    880: 'Sealants prevent caries on sound surfaces and successfully arrest the progression of early, non-cavitated enamel lesions by cutting off nutrient supply.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    881: 'A major connector must be rigid to distribute occlusal forces evenly across the arch and prevent localized destructive forces on abutment teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    882: 'When pulp testing a suspect tooth, baseline responses must first be established using adjacent teeth and healthy contralateral counterparts.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    883: 'The periodontal ligament surface area (root surface area) of mandibular teeth decreases in the order of Canine > First Premolar > Second Premolar.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)'
}

for q_id, exp in q857_883_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q857-Q883!")
