import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q1062_1074_exps = {
    1062: 'At-home nightguard vital bleaching routinely utilizes 10% to 15% carbamide peroxide, which breaks down into roughly 3.3% to 5% hydrogen peroxide.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    1063: 'A plain fissure carbide bur rotating at high speed produces the smoothest cut on enamel surfaces compared to cross-cut burs or diamond instruments.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 88)',
    1064: 'Biologic width comprises the combined height of the junctional epithelium and connective tissue attachment, measuring approximately 2.04 mm from the sulcus base to the alveolar crest.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    1065: 'The oxygen-inhibited layer contains unpolymerized monomer that chemically copolymerizes with the next composite increment, maximizing incremental bond strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    1066: 'IRM (Intermediate Restorative Material) is a polymer-reinforced ZOE cement, where the powder contains zinc oxide reinforced with polymethyl methacrylate (PMMA) beads.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    1067: 'To prevent accidental pulpal exposure or external root perforation, retentive pinholes must be prepared parallel to the adjacent external tooth surface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    1068: 'Self-threading pins achieve optimal retention in dentin at a depth of 2.0 mm; deeper pin insertion does not increase retention and raises perforation risk.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    1069: 'High-copper amalgam alloys are harder and require higher energy (speed and time) during trituration to achieve a homogenous mix.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    1070: 'Co-polymerization between RMGI and composite occurs via the resin monomers (HEMA), making acid etching of the RMGI surface unnecessary for bonding.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    1073: 'In a four-number Black\'s instrument formula, the fourth number (14) indicates the angle that the blade makes with the long axis of the handle in centigrades.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 88)',
    1074: 'Due to low tensile strength and brittleness, conventional GIC is not suitable as a core build-up material for anterior teeth subject to lateral forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)'
}

for q_id, exp in q1062_1074_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q1062-Q1074!")
