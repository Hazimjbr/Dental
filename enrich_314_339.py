import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q314_339_exps = {
    314: 'Lateral condensation of gutta-percha is the gold standard obturation method for maxillary lateral incisors to ensure a three-dimensional seal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    315: 'Teeth contact and morphologic intercuspation represent the primary mechanical factor controlling static occlusion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    316: 'The mandibular second premolar (35) has a straight, single, conical root, allowing extraction using primary rotational forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 82)',
    317: 'The lingual cortical plate of the mandible in the third molar region is significantly thinner than the dense buccal plate, facilitating lingual luxation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 82)',
    318: 'The maximum recommended dose of plain 2% lidocaine without epinephrine is 4.4 mg/kg, which is approximately 200 mg (10 mL / 5 cartridges).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    319: 'Debonding of Maryland (resin-bonded) bridges most commonly occurs at the resin-to-metal framework interface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 126)',
    320: 'The gypsum binder in gold casting investments provides strength and rigidity to withstand the high forces of molten metal casting.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 128)',
    321: 'The retentive terminal tip of a clasp arm must be placed below the height of contour (in the undercut area) to resist displacement forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    323: 'The most common and critical failure in removable partial denture fabrication is incorrect overall framework design.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    324: 'Radiographs can only show bone loss on proximal surfaces (mesial and distal); buccal and lingual bone loss is obscured by the tooth structure.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    325: 'Restoring the occlusal surface must prioritize function (harmonious occlusion and masticatory efficiency) over pure anatomy.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    326: 'All dental plaques contain bacteria capable of metabolizing carbohydrates to produce organic acids, lowering local pH.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 23)',
    327: 'A gangrenous, necrotic tooth requires thorough pulpal debridement and disinfection via root canal therapy.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    328: 'Eugenol inhibits the free-radical polymerization of composite resins and bonding agents, making ZOE strictly contraindicated under composites.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    329: 'Occlusal trauma manifests as bone resorption, pulp necrosis, hypercementosis, and widening of the PDL space / triangulation (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 183)',
    330: 'Carbamazepine is the first-line anticonvulsant medication specifically used to manage the neuropathic pain of trigeminal neuralgia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    331: 'The long buccal nerve block is injected into the mucous membrane distal and buccal to the last molar, near the anterior border of the ramus.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    332: 'According to the bisecting angle technique, too small of a vertical angulation causes elongation of the radiographic image of the tooth root.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 120)',
    333: 'Isolated cleft palate is epidemiologically more common in females; cleft lip with or without cleft palate is more common in males.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    334: 'Periodontitis is biologically communicable as key periodontal pathogens (e.g. P. gingivalis) can be transmitted between close family members.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    335: 'A ceramic jacket crown requires a minimum thickness of 1.0mm to 1.5mm to withstand occlusal forces; anything thinner will fracture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    336: 'A pontic (typically modified ridge-lap) should be in light, pressure-free contact with the edentulous ridge mucosa for aesthetics and hygiene.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 125)',
    337: 'Correcting a labially displaced tooth with a crown aligned in the arch requires bringing the incisal edge palatally, which visually makes the crown appear narrower.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    338: 'Root canal sealers should have a slow setting time to allow adequate working time for complete adaptation and compacting.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    339: 'Pins must be placed in sound dentin where there is maximum tooth structure bulk and thickness, away from the pulp and external surface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 112)'
}

for q_id, exp in q314_339_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q314-Q339!")
