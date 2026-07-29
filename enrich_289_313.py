import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q289_313_exps = {
    289: 'While pins weaken amalgam bulk strength, they do not significantly degrade the clinical strength of composite resin restorations.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    290: 'Retained roots under an overdenture are highly susceptible to caries and periodontal disease if not meticulously kept clean.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 150)',
    291: 'A major aesthetic disadvantage of immediate dentures is the inability to perform an anterior wax try-in before extraction.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 148)',
    292: 'Brown skin pigmentation (melanin) is associated with endocrine disorders like Addison\'s or hyperparathyroidism, not Von Willebrand\'s.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 92)',
    293: 'Dental plaque is a structured, resilient biofilm composed primarily of bacteria in an organic matrix that cannot be rinsed away by water alone.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    294: 'Nasmyth\'s membrane (primary enamel cuticle) is worn away soon after eruption and is not a parameter for diagnosing gingival health.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    295: 'Following enamel maturation, ameloblasts secrete the primary enamel cuticle and degenerate into the reduced enamel epithelium.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 202)',
    296: 'Microfilled composite resins have lower filler loading, resulting in a higher coefficient of thermal expansion and lower compressive strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    297: 'Mercury vapor is highly toxic because it is lipid-soluble, crosses the blood-brain barrier, and accumulates in the central nervous system.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    298: 'The elastic limit is the greatest stress a material can withstand without undergoing permanent (plastic) deformation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 82)',
    299: 'Alginate is the most flexible (highest strain in compression), followed by silicone and polysulfide, while ZOE is rigid and inelastic.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    300: 'Denture acrylic is supplied as a powder (polymethyl methacrylate polymer) and a liquid (methyl methacrylate monomer).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    301: 'Gypsum stone dies lack the high-detail edge strength and surface definition compared to electroplated or resin dies.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 132)',
    302: 'GIC sets via an acid-base reaction between polymeric acid liquid and fluoroaluminosilicate glass powder.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    303: 'Unlike most synovial joints lined with hyaline cartilage, the articular surfaces of the TMJ are covered by dense fibrous connective tissue.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    304: 'Wrought gold clasps have a low modulus of elasticity and high flexibility, allowing them to safely engage deeper undercuts (0.75mm) than base metals.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    305: 'TMD pain is characteristically musculoskeletal, frequently presenting as tenderness in the muscles of mastication (masseter, temporalis).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 144)',
    306: 'Incisal guidance represents the mechanical equivalent of the vertical (overbite) and horizontal (overjet) overlap of anterior teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    307: 'While Ledermix reduces acute symptoms, long-term pulp capping in immature teeth can result in silent pulpal necrosis or calcification.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    308: 'Replacing cariogenic sucrose in pediatric syrups with non-acidogenic sugar substitutes (like sorbitol) significantly reduces caries risk.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 22)',
    309: 'The optimal fluoridation level in drinking water for temperate climates is historically established at 1.0 ppm (parts per million).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    310: 'Deciduous teeth have thinner enamel, higher pulp horns, larger chambers, and flatter contact areas than permanent teeth (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    311: 'Composite resins containing macrofilled glass or quartz particles offer the highest fracture toughness for stress-bearing Class IV incisal edges.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    312: 'Standard dentin bonding (total-etch system) requires acid etching to remove the smear layer and expose collagen, followed by adhesive application.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    313: 'Aspiration should be performed using gentle, short backward pressure on the syringe plunger before injecting local anesthetic.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)'
}

for q_id, exp in q289_313_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q289-Q313!")
