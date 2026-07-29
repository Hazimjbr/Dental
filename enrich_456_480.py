import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q456_480_exps = {
    456: 'Linear Gingival Erythema (LGE) in HIV/AIDS is characterized by a red band on the free gingiva that does not respond to conventional plaque control.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    457: 'Basal cell carcinoma is highly invasive locally (rodent ulcer) and can extensively erode surrounding tissues and bone, though it rarely metastasizes.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    458: 'Erosive oral lichen planus carries a documented risk of malignant transformation into oral squamous cell carcinoma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 185)',
    459: 'Pulpal necrosis in primary molars characteristically leads to accessory canal microleakage, causing bone resorption in the furcation (bifurcation) area.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    460: 'Deciduous maxillary molars are extracted using a primary buccal luxation force to expand the thinner buccal alveolar plate.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 242)',
    461: 'If the successor premolar (35) is congenitally missing, perform a pulpotomy on the primary molar (75) to retain it indefinitely in the arch.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    462: 'Periodontitis is epidemiologically established as the primary cause of tooth loss in adults over the age of 35.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    463: 'Class III composite restorations demonstrate the longest clinical longevity due to being protected in interproximal spaces with minimal occlusal stress.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    464: 'Pin retention is most effective and essential for stabilizing extensive, complex dental amalgam restorations in teeth with broken-down crowns.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    465: 'Emergency management of an acute apical flare-up involves immediate root canal debridement (cleaning) and placement of Ledermix paste.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    466: 'The most common and earliest clinical symptom of temporomandibular joint (TMJ) internal derangement is joint clicking.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 144)',
    467: 'The sensory limb of the gag reflex is mediated by the Glossopharyngeal nerve (CN IX), while the motor limb is mediated by the Vagus nerve (CN X).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    468: 'Polyether impression materials are highly hydrophilic; storing them in water causes water absorption, swelling, and severe dimensional distortion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    469: 'High-copper amalgams prevent formation of the highly unstable, corrosive tin-mercury gamma-2 phase, yielding superior corrosion resistance.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    470: 'Gaseous porosity is caused by rapid boiling of monomer, whereas contraction porosity is caused by insufficient packing pressure during flasking.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 146)',
    471: 'The vertical dimension of occlusion (VDO) is established at maximum intercuspation, which represents the shortest clinical face height.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    472: 'Placing a lower denture in an edentulous patient restores lost vertical dimension of occlusion (VDO), increasing the lower face height.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    473: 'Gutta-percha points cannot withstand heat autoclaving; they are rapidly sterilized chairside using chemical agents like 5.25% sodium hypochlorite.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 214)',
    475: 'Zinc oxide-eugenol (ZOE) cement has low strength and high solubility, making it the ideal choice for temporary crown cementation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 128)',
    476: 'Guiding planes are prepared on proximal tooth surfaces parallel to each other and aligned with the planned path of insertion and removal of the RPD.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 157)',
    477: 'Polyether impressions must be stored dry (to prevent water absorption and distortion) and can be poured up to several days later.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 130)',
    478: 'If the translucent body porcelain layer is too thin, the underlying bright white opaque porcelain reflects through, causing an opaque appearance.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    479: 'Among conventional luting agents, glass ionomer cement (GIC) demonstrates the lowest clinical solubility in the oral environment.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    480: 'Aesthetic composite preparations require beveling of enamel margins (occlusal and gingival) to increase surface area for acid etching and transition colors.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)'
}

for q_id, exp in q456_480_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q456-Q480!")
