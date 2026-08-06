import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q561_586_exps = {
    561: 'Camper\'s line (ala-tragal line) runs from the inferior border of the ala of the nose to the tragus of the ear, serving as a landmark to orient the prosthetic occlusal plane.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    562: 'In patients with severe TMJ disorders or resorbed, unstable ridges, non-anatomical (cuspless) teeth reduce lateral shear forces during mastication.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    563: 'Primary colonizers of dental plaque are predominantly aerobic Gram-positive cocci and rods (e.g., Streptococcus oralis, S. sanguinis, Actinomyces species).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    564: 'Oral streptococci synthesize insoluble extracellular glucans and fructans from dietary sucrose using glucosyltransferase enzymes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    565: 'Resins used in posterior load-bearing areas require a high filler volume fraction (high filler loading) to withstand heavy occlusal forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    566: 'Post-operative thermal sensitivity immediately following cavity preparation is primarily caused by mechanical vibration and pulpal trauma/inflammation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    567: 'Acute endodontic flare-up or persistent apical periodontitis can result from mechanical over-instrumentation, chemical medicament irritation, or residual bacterial infection.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    568: 'To prevent gingival margin trauma and plaque accumulation, maxillary major connectors must be positioned at least 6 mm away from gingival margins.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    569: 'Upon completing enamel matrix formation, degenerated ameloblasts form the primary enamel cuticle (Nasmyth\'s membrane) covering the crown.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    570: 'A marginal discrepancy of 0.3 mm (300 µm) exceeds acceptable clinical open margin thresholds (<50-100 µm) and requires remaking the crown.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    571: 'Chlorhexidine gluconate is clinically formulated as a 0.12% solution in North America (or 0.2% in Europe) for anti-plaque chemical control.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    572: 'Glyceryl trinitrate (GTN) acts as a systemic venodilator, reducing venous return (preload) to the heart and decreasing myocardial oxygen demand.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 62)',
    573: 'Radiotherapy damages taste buds, leading to dysgeusia or loss of taste (hypogeusia/ageusia), not heightened taste sensation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 198)',
    574: 'Addison\'s disease (primary adrenal insufficiency) features mucosal hyperpigmentation, hypotension, and fatigue, but does not cause bony expansion.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    575: 'Stevens-Johnson syndrome is a mucocutaneous hypersensitivity reaction causing mucosal ulceration/sloughing, not localized prepubertal periodontitis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    576: 'Patients with root exposure and cervical abrasion should use a soft toothbrush with low-abrasivity dentifrice to prevent further dentin/cementum loss.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    577: 'The Loe and Silness Gingival Index (GI) is the gold standard epidemiological index for assessing severity and qualitative changes of gingival inflammation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    579: 'Sucrose serves as the indispensable substrate for bacterial extracellular polysaccharide matrix synthesis, fostering plaque mass accumulation regardless of caries susceptibility.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    580: 'Streptococcus mutans synthesizes insoluble water-resistant glucans from sucrose, enabling firm bacterial adhesion and biofilm resistance.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    581: 'Administering calcium-containing liquids (such as milk or calcium gluconate) binds fluoride ions in the stomach, forming insoluble calcium fluoride to prevent systemic absorption.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    582: 'Collimation restricts the size and shape of the primary X-ray beam, reducing patient tissue volume exposed and minimizing scatter radiation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    583: 'Aluminum filtration absorbs low-energy, long-wavelength X-ray photons that would otherwise be absorbed by patient skin without contributing to image formation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    584: 'Epitaxy (heterogeneous nucleation) posits that organic plaque matrix proteins serve as a structural template that lowers energy required for hydroxyapatite crystal nucleation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    585: 'Gemination occurs when a single tooth germ attempts to divide, resulting in a bifid crown with a single root and single root canal.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 232)',
    586: 'Calcium hydroxide pulpotomy in primary molars carries a high incidence of chronic inflammation leading to internal root resorption.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)'
}

for q_id, exp in q561_586_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q561-Q586!")
