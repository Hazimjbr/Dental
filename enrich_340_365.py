import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q340_365_exps = {
    340: 'Light-cured Class V composite resins are finished and polished immediately after polymerization using fine diamonds or abrasive discs.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 94)',
    341: 'Deep caries close to the pulp is managed by indirect pulp capping with a calcium hydroxide liner to promote tertiary dentin formation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    342: 'Dental plaque bacteria metabolize fermentable dietary carbohydrates to produce organic acids, which initiate enamel demineralization.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 23)',
    343: 'High-copper amalgams eliminate the highly corrosive gamma-2 phase (Sn-Hg), significantly reducing corrosion and marginal breakdown.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    344: 'Self-threading pins induce high internal stresses in dentin during placement, which can cause microfractures or tooth cracking.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    345: 'Composite restorations are most durable in Class III cavities (interproximal anterior teeth) because they are subjected to minimal occlusal loading.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    346: 'Weakened cusps require a minimum of 2.0 mm of reduction to provide sufficient bulk and fracture resistance for the overlying amalgam.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    347: 'The mesial surface of maxillary first premolars has a distinct developmental root concavity, complicating matrix band adaptation at the gingival margin.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 110)',
    348: 'Acid etching of enamel provides micromechanical retention, sealing margins and minimizing marginal microleakage of restorations.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    349: 'Sjögren\'s syndrome is an autoimmune disease characterized by xerostomia (dry mouth), keratoconjunctivitis sicca (dry eyes), and rheumatoid arthritis (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 162)',
    350: 'Long-term tetracycline therapy suppresses normal oral bacterial flora, predisposing the patient to opportunistic Candida albicans (oral thrush) infections.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    351: 'Unexplained paresthesia (numbness) of the lip or chin is a hallmark sign of a malignant tumor invading the inferior alveolar nerve.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    352: 'Type IV (extra-hard) gold casting alloys are highly rigid and cannot be burnished or easily polished at the margins within the cavity preparation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 128)',
    353: 'Type IV casting gold (extra-hard, containing around 75% gold-platinum group metals) is used for bridges and high-stress partial denture frameworks.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 128)',
    355: 'Inlay waxes for the indirect technique are harder at room temperature to prevent distortion during handling and transit from the die.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 129)',
    356: 'Moisture contamination of zinc-containing amalgam causes delayed expansion, blister formation, reduced strength, and pain, but does not directly cause secondary caries.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    357: 'Unreplaced tooth extraction leads to drifting, tilting, loss of proximal contacts, periodontal pocketing, and TMJ dysfunction (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    358: 'Erythema migrans (geographic tongue) is a benign, inflammatory, self-limiting condition of the tongue, whereas leukoplakia has malignant potential.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    359: 'The lingual nerve lies close to the medial aspect of the mandibular ramus, approximately 1cm above the occlusal plane of the last lower molar.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    360: 'The PSA nerve innervates the maxillary first, second, and third molars, except for the mesiobuccal root of the first molar (supplied by the MSA nerve).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    361: 'Recurrent localized vesicles on the vermillion border of the lip triggered by sunlight or stress is characteristic of Herpes Simplex Virus 1 (herpes labialis).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    362: 'Histopathological features of Lichen Planus include a dense, band-like subepithelial lymphocytic infiltrate and basal cell liquefaction degeneration.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 185)',
    363: 'Denture stomatitis is a yeast infection (Candida) treated with topical antifungals such as Amphotericin B lozenges or oral suspensions.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    364: 'Early stages of Paget\'s disease of bone show osteolytic radiolucency or a \'ground glass\' appearance, progressing to a classic \'cotton wool\' pattern later.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 156)',
    365: 'Infections of the maxillary canine space can spread retrograde via the angular and ophthalmic veins, leading to life-threatening cavernous sinus thrombosis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 55)'
}

for q_id, exp in q340_365_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q340-Q365!")
