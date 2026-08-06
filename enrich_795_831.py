import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q795_831_exps = {
    795: 'As the tooth erupts, the reduced enamel epithelium (REE) fuses with the oral epithelium to form the junctional (attachment) epithelium.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    796: 'Lateral cephalometric and panoramic radiographs are indispensable diagnostic tools for orthodontic skeletal and dental analysis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    797: 'Uncooperative children requiring advanced behavioral techniques are best referred to a pediatric dental specialist (pedodontist).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    798: 'Behavioral issues and dental anxiety are the most frequent reasons general practitioners refer pediatric patients to specialists.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    799: 'Excessive or rapid orthodontic tooth separation compromises the periodontal blood supply, leading to ischemia and localized aseptic bone necrosis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    800: 'Unreplaced tooth loss leads to posterior bite collapse, shifting mandibular chewing paths, and eventual TMJ dysfunction.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 144)',
    801: 'Ameloblasts secrete the primary enamel cuticle (Nasmyth\'s membrane) on the outer enamel surface just before degenerating.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    803: 'Mandibular growth in 5-to-6-year-old children occurs predominantly in posterior length to accommodate the erupting permanent molars.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    804: 'Glass Ionomer Cement (GIC) is highly recommended for primary teeth due to chemical dentin bonding and continuous fluoride release.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    805: 'Torsion (or rotation) describes a malposition where a tooth is rotated along its longitudinal axis.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    806: 'Baseline radiographic screening (bitewings/panoramic) is recommended around age 3 to 5 years once posterior proximal contacts close.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    810: 'The Hawley retainer (with an active labial bow) is frequently used to close minor maxillary midline diastemas.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    812: 'Cavity varnish (Copalite) seals dentinal tubules and reduces short-term microleakage at amalgam margins before corrosion products seal the gap.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    814: 'Heating the casting investment too rapidly causes steam pressure build-up, resulting in investment cracking and casting flashes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    815: 'Pre- and post-carve burnishing of dental amalgam margins removes the mercury-rich matrix phase, increasing edge strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    816: 'All resin composite restoratives undergo polymerization shrinkage (contraction) toward the center of the mass.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    818: 'Repetitive cyclic flexural stress during chewing leads to flexural fatigue failure along the midline of maxillary dentures.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    820: 'Enamel hypoplasia appears radiographically as a localized or generalized thinning of the radiopaque outer enamel cap.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    821: 'The primary function of a matrix band is to temporarily replace a missing proximal wall, allowing adequate condensation of restorative materials.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    823: 'The orifice of the large palatal canal in maxillary first molars is anatomically located directly beneath the mesiolingual cusp.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    824: 'Retention and peripheral seal of a cleft palate palatal obturator depend on muscular adaptation and atmospheric pressure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    825: 'In a fixed-movable bridge design, the non-rigid connector keyway (slot) is typically prepared in the distal aspect of the anterior abutment retainer.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    828: 'A minimum facial/labial reduction of 1.5 mm is required for PFM crowns to provide sufficient bulk for metal, opaque, and body porcelain layers.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    830: 'The boiling point of pure methyl methacrylate monomer is 100.8°C, which is slightly higher than the boiling point of water.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    831: 'Dental ceramics are highly brittle materials that exhibit high compressive strength but very low tensile strength (strongest in compression).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)'
}

for q_id, exp in q795_831_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q795-Q831!")
