import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q739_764_exps = {
    739: 'A lower water-to-powder ratio increases density and compressive strength of gypsum casts, producing a significantly harder surface.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)',
    740: 'Immersing a dry gypsum cast in water saturated with calcium sulfate prevents dissolution, resulting in negligible/no dimensional change (unlike pure water).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)',
    741: 'Impression compound must have a fusion temperature above mouth temperature (around 45°C) so it remains rigid upon cooling in the oral cavity.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    742: 'ADA Specification No. 3 limits the maximum flow of Type I impression compound to 6.0% at 37°C to prevent distortion during removal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    743: 'Prolonged heating of compound in water leaches out soluble low-molecular-weight plasticizers, rendering the material brittle, grainy, and less plastic.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    744: 'ZOE impression pastes are commercially formulated with varying setting times (Type I Hard, Type II Soft) regulated by accelerators like zinc acetate.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    745: 'Agar and alginate hydrocolloids are classification-wise hydrophilic emulsoid polymers that transition from a sol to a gel phase.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    746: 'Traditional elastomeric materials (especially silicones and polysulfides) are hydrophobic, requiring a moisture-free field for accurate impressions.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    747: 'The polymerization (vulcanization) reaction of polysulfides is exothermic and highly accelerated by increases in ambient temperature and humidity.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    748: 'The elastic recovery and tear strength of elastomeric impression materials improve over the first 10-30 minutes as polymerization completes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    749: 'Gaseous porosity occurs in the thickest, internal parts of the acrylic because of localized heat exceeding the monomer\'s boiling point (100.8°C).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    750: 'Statistical clinical audits show that over 50% of amalgam failures (recurrent caries or fracture) stem from improper cavity design (e.g., poor depth/cavosurface margins).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    751: 'Narrowing the occlusal table (isthmus width) reduces exposure to direct biting forces, lowering the risk of amalgam restoration fracture.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    752: 'Minimizing residual mercury content (<50%) reduces the formation of the weak, corrosion-prone gamma-2 phase and decreases internal voids.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    753: 'High-copper amalgams contain sufficient copper to react preferentially with tin, preventing formation of the highly corrosive tin-mercury (gamma-2) phase.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    754: 'Direct cohesive gold requires meticulous, layer-by-layer hand or mechanical condensation; improper condensation leads to internal voids and clinical failure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    755: 'Untreated enamel is a low-energy, smooth surface that does not meet the wetting requirements for resin adhesion until it is acid-etched.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    756: 'Acid etching (with 37% phosphoric acid) is a conservative, non-invasive technique that creates micro-retentive enamel porosities for resin tag infiltration.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    757: 'Etch efficacy varies depending on tooth substrates—specifically whether it is aprismatic enamel, deciduous vs. permanent enamel, or hyper-mineralized fluorotic enamel.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    759: 'In permanent teeth, enamel rods run perpendicular from the dentino-enamel junction (DEJ) to the outer anatomical surface of the crown.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    760: 'Systemic/topical fluoride is bacteriostatic, rapidly deposits in hard tissue, and crosses the placenta, but it does not cause extrinsic staining (unlike chlorhexidine or iron).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    761: 'Methyldopa is a centrally acting alpha-2 adrenergic agonist historically prescribed for the management of hypertension.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    762: 'Sublingual glyceryl trinitrate (GTN) tablets or spray provide rapid-onset systemic vasodilation, relieving angina symptoms within 1-3 minutes.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 62)',
    763: 'Radiographs underestimate the true extent of proximal caries due to the three-dimensional mineral loss requiring at least 30-40% demineralization to show radiographically.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    764: 'In Paget\'s disease (osteitis deformans), the normal radiopaque lamina dura around teeth is characteristically absent or replaced by bone remodeling.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)'
}

for q_id, exp in q739_764_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q739-Q764!")
