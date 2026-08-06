import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q536_560_exps = {
    536: 'The occlusal pulpal floor of a Class II cavity on a mandibular first premolar must be inclined lingually to parallel the occlusal plane and protect the large buccal pulp horn.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    537: 'Gingival margin microleakage in Class II restorations is primarily caused by poor condensation, excessively thick initial composite/amalgam increments, and moisture/debris contamination.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    538: 'Desiccation with air alone during high-speed cavity preparation causes rapid fluid movement in dentinal tubules, aspirating odontoblasts into the tubules (odontoblast displacement).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    539: 'The apical limit for root canal instrumentation and obturation is the apical constriction (dentino-cemental junction), typically 0.5 to 1 mm short of the radiographic apex.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    540: 'The narrowest part of the pulp canal is the apical constriction located at the dentino-cemental junction (DCJ).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    541: 'Electric or thermal pulp vitality testing is the definitive diagnostic tool: teeth with an apical abscess are non-vital, whereas teeth with a periodontal abscess remain vital.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    542: 'For maximum retention and stress distribution, post length should ideally equal 1.5 times the clinical crown height (or at least equal to crown length/two-thirds of root length).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    543: 'Shade matching must be performed at the beginning of the appointment before tooth dehydration alters natural translucency and color value.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    544: 'A 2.2 mg sodium fluoride (NaF) tablet yields exactly 1.0 mg of active fluoride ion (F-) upon dissociation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    545: 'Strain is defined as the relative deformation or change in dimension of a material in response to an applied external stress.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 88)',
    546: 'Pulp chamber dimensions decrease progressively due to secondary dentin deposition influenced by age, parafunction, and chronic irritation from caries or abrasion (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    547: 'Cold-cure (auto-polymerizing) acrylics have a lower degree of polymerization, resulting in a significantly higher residual monomer content (up to 3-5%).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    548: 'Firing dental porcelain under vacuum removes entrapped air between frit particles, significantly reducing internal porosity and improving translucency and strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    549: 'Porosity in cast gold/metal inlays is primarily caused by occluded molten gases or improper sprue design leading to solidification shrinkage.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    550: 'The mylohyoid muscle forms the muscular floor of the mouth and dictates the lingual flange extension of a mandibular complete denture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    551: 'Cervical (Class V) caries originates near the gingival margin where plaque accumulates due to poor oral hygiene.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    552: 'Retention for Class I occlusal amalgams is achieved by converging the buccal and lingual walls occlusally to create subtle mechanical undercuts.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    553: 'Approximately 40% of mandibular incisors possess two root canals, with the vast majority converging to exit through a single apical foramen.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    554: 'Splinting abutment teeth in a fixed partial denture increases periodontal ligament surface area, distributing heavy occlusal loads over multiple roots.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    555: 'After degas/heat treatment (degassing of the metal framework), surface grease or oil from finger contact will prevent proper bonding of the opaque porcelain layer.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    556: 'The flexible terminal tip of an RPD retentive clasp arm must be placed below the height of contour (survey line) in the gingival undercut region.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    557: 'Sodium hypochlorite solutions cause rapid corrosion, surface pitting, and tarnish of cobalt-chromium metal frameworks.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 148)',
    558: 'Denture-induced fibrous hyperplasia (epulis fissuratum) is caused by chronic low-grade trauma from an ill-fitting, mobile denture border.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    559: 'Inadequate posterior horizontal overlap (reduced overjet) allows the buccal mucosa to fall between the occluding cusps during mastication, resulting in cheek biting.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    560: 'Inserting a complete lower denture restores the vertical dimension of occlusion, increasing lower face height back toward normal resting levels.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)'
}

for q_id, exp in q536_560_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q536-Q560!")
