import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q264_288_exps = {
    264: 'Making precise depth-orientation cuts is the most reliable method to ensure uniform and sufficient reduction of the labial tooth surface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    266: 'By definition, an amalgam is a specific alloy of mercury with one or more other metals (such as silver, tin, or copper).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    267: 'Proximal cavosurface margins in a Class II amalgam preparation must be finished at a 90-degree right angle (butt-joint margin) to prevent amalgam fracture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    268: 'Immediate diagnostic radiography and vitality testing are mandatory to identify the odontogenic source of the acute space infection.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
    269: 'Teeth with inflammatory apical root resorption have a good prognosis if the root canal system can be completely cleaned and hermetically sealed.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    270: 'Tugback is the slight frictional resistance felt upon removing a master gutta-percha cone that fits snugly in the apical 1-2 mm of the canal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    271: 'The biological limit of root canal obturation is the dentinocemental junction (apical constriction), situated 0.5-1.0mm short of the radiographic apex.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    272: 'The mesiobuccal root of the maxillary first molar (MB1 and MB2) most commonly possesses two canals that merge to exit through a single apical foramen.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    273: 'Inadequate condensation (insufficient removal of water and air voids) is the primary cause of porosity in dental porcelain.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 102)',
    274: 'Ensure the interocclusal distance (freeway space) remains physiologically acceptable before permanently altering OVD in full mouth rehabilitation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    275: 'Metal-ceramic crowns allow conservative palatal reduction (0.5mm metal thickness) compared to all-ceramic crowns which require 1.0-1.5mm thickness.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    276: 'Adequately designed resin-bonded (Maryland) bridges utilizing modern translucent resin cements have no detrimental color effect on abutment teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 126)',
    277: 'A minimum of 1.5mm of labial reduction is required for PFM crowns (0.3-0.5mm metal, 0.2-0.3mm opaque porcelain, 0.8-1.0mm body porcelain).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    278: 'The gingival third of a tooth is darker and more saturated because the enamel is thin, exposing the underlying yellow dentin background.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
    279: 'The term saddle belongs strictly to removable partial dentures; in fixed prosthodontics, the edentulous area is referred to as the ridge.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 125)',
    280: 'A crown that fits the die but is open in the mouth indicates a distorted initial impression; remaking the impression and crown is required.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 132)',
    281: 'Minor connectors are rigid components that link auxiliary parts of the RPD (such as clasps, rests, or indirect retainers) to the major connector.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    282: 'Reciprocation is the process by which a rigid component (reciprocal arm) counteracts lateral forces exerted on the tooth by the retentive clasp arm.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    283: 'Indirect retainers prevent rotation of the distal extension base away from the residual ridge about the fulcrum line under sticky food forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 158)',
    284: 'Clasp deformation or fracture under repeated clinical flexure occurs due to inadequate fatigue strength or low ultimate tensile strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    285: 'Perforating a custom acrylic tray is a highly reliable mechanical method to secure elastomeric impression materials.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    286: 'Retentive clasp arms must be completely passive (exert no force) when the denture is terminally seated in the mouth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    287: 'A lingual bar is preferred over a lingual plate because it covers less tooth structure and gingiva, minimizing plaque accumulation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    288: 'The fovea palatinae are two minor salivary gland duct openings located on either side of the midline at the hard-soft palate junction.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 136)'
}

for q_id, exp in q264_288_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q264-Q288!")
