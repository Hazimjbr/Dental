import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q81_100_exps = {
    81: 'Aphthous ulcers are diagnosed clinically by history and clinical appearance. Biopsy is non-specific and least useful.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 172)',
    82: 'The IAN block needle passes through the buccinator muscle and close to the superior pharyngeal constrictor at the pterygomandibular space.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    83: 'Deciduous molars are extracted using a primary buccolingual (labial-lingual) expansion force due to the widely divergent roots.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 242)',
    84: 'The protrusive record adjusts the articulator\'s condylar guidance inclination to mimic the patient\'s individual sagittal condylar path.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 144)',
    85: 'The mesiobuccal pulp horn is the highest and most prominent pulp horn in permanent molars, making it highly susceptible to exposure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)',
    86: 'Before increasing OVD, we must ensure the patient\'s physiological rest position and freeway space remain adequate and acceptable.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    87: 'Diagnostic study casts are used for custom impression tray fabrication, surveying, and design planning before final preparation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 152)',
    88: 'Maximum coverage and physiological tissue support under the distal extension base minimizes torque and load on the abutment teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 158)',
    89: 'The orbicularis oris muscle directly bounds the anterior labial flange and borders of both maxillary and mandibular dentures.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 138)',
    90: 'Changing OVD on an articulator mounted without a facebow shifts the arc of closure, necessitating a new centric relation record.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 143)',
    91: 'Following molar extraction, the resorption pattern leaves a smaller ridge, typically shifting the ridge crest palatally.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 134)',
    92: 'Since natural teeth are still present, immediate complete dentures do not allow for a trial wax setup try-in of the anterior teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 148)',
    93: 'Acidogenic oral bacteria (e.g. S. mutans) require dietary simple carbohydrates (fermentable sugars) to produce acid and demineralize dentin.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 22)',
    94: 'Streptococcus mutans uses the enzyme glucosyltransferase to convert sucrose into extracellular polysaccharides (dextran/glucan).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 23)',
    95: 'At birth, calcification has begun for all primary teeth crowns and the cusps of the first permanent molars.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 221)',
    96: 'The primary enamel cuticle (Nasmyth\'s membrane) is formed by the final secretion of the ameloblasts before they degenerate.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 223)',
    97: 'Depression of the mandible (opening) is driven by the lateral pterygoid and accessory muscles like the digastric anterior belly.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 15)',
    98: 'Early loss of a primary tooth can lead to drifting, space loss, and malocclusion, impacting development of the entire dentition.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 272)',
    99: 'The soft tissue facial profile convexity angle is defined cephalometrically by Nasion, Subnasale, and Pogonion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 268)',
    100: 'Stress breakers decouple saddle movement from the abutment teeth, relieving them from excessive, damaging lateral forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 160)'
}

for q_id, exp in q81_100_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q81-Q100!")
