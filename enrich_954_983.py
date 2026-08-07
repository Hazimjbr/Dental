import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q954_983_exps = {
    954: 'Corticosteroids are incorporated into endodontic materials to suppress the inflammatory response and reduce post-operative pain.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 212)',
    957: 'If the distance between punched holes is too small, the rubber sheet gets stretched tightly, leaving insufficient material to cover the interdental papillae and strangulating the gingival tissue.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    960: 'A clasp arm must engage a specific, predetermined amount of undercut (e.g., 0.25 mm for cast cobalt-chromium) based on the alloy elasticity.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    961: 'Fibrotic gingival hyperplasia (such as phenytoin-induced enlargement) consists of dense collagenous tissue that does not resolve with scaling alone and requires surgical gingivectomy.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    962: 'Cortical bone is characterized histologically by osteons (Haversian systems), containing concentric lamellae of bone matrix surrounding a central Haversian canal.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    964: 'In Class II division 2 malocclusion, the deep bite and retroclined maxillary incisors impose excessive shear forces, making Maryland bridges highly prone to debonding.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    965: 'For lower premolars where aesthetics are primary on the buccal, the porcelain veneer can be restricted to the buccal cusp (leaving the lingual in metal) to conserve tooth structure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 124)',
    966: 'Angular cheilitis (cheilosis) can be caused by a loss of vertical dimension (causing saliva pooling) or systemic nutritional deficiencies, particularly riboflavin (Vitamin B2).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    967: 'Long-span fixed bridges require high-strength, hard alloys (such as Type IV gold or base metal alloys) to resist flexure under occlusal loading.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    968: 'Maryland bridges require alloys with high yield strength and modulus of elasticity (extra hard, like Nickel-Chromium or Cobalt-Chromium) to allow thin, rigid retainer wings.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 122)',
    969: 'The superior (condylar) fragment of a fractured condylar neck is displaced anteromedially due to the pull of the lateral pterygoid muscle inserted into the fovea.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 82)',
    970: 'For patients on warfarin with an INR of 3.0, minor oral surgery can be safely performed without altering anticoagulants, provided local hemostatic measures are used alongside antibiotic prophylaxis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    971: 'A chronic oroantral fistula will not close spontaneously and requires surgical closure (usually a buccal advancement flap or palatal rotation flap).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    972: 'Oral pigmented nevi are rare but have a risk of malignant transformation to melanoma (estimated around 10-15% in some historical literature, warranting biopsy).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 188)',
    973: 'The lateral border of the tongue and the floor of the mouth are the most common sites for oral squamous cell carcinoma (OSCC).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    974: 'Pemphigus vulgaris is characterized histopathologically by intraepithelial suprabasilar splitting and acantholysis (loss of cell-to-cell adhesion).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 184)',
    975: 'Physiological (ethnic) pigmentation is the most common cause of generalized oral mucosal pigmentation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 188)',
    976: 'Osteogenesis imperfecta is a genetic collagen disorder characterized by bone fragility, blue sclera, and progressive hearing loss (deafness).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    977: 'According to the inverse square law, increasing the distance from the focal spot to the film decreases the intensity of the X-ray beam, reducing film density.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    978: 'A smaller focal spot size minimizes the penumbra (geometric unsharpness), thereby increasing the sharpness of the radiographic image.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    979: 'Staphylococcus aureus is the most common cause of localized skin infections, such as furuncles (boils) and carbuncles.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    980: 'Basal cell carcinoma (BCC) arises exclusively from hair-bearing skin exposed to sunlight; it does not occur on the oral mucosa.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    981: 'In active periodontitis, the probe penetrates past the inflamed junctional epithelium into the underlying connective tissue, overestimating the pocket depth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    982: 'Mucogingival involvement (or defect) occurs when the pocket depth extends to or beyond the mucogingival junction, leaving no attached gingiva.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    983: 'GTR utilizes a barrier membrane to prevent rapidly proliferating epithelial cells from migrating apically, allowing slower-growing PDL cells to populate the root.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)'
}

for q_id, exp in q954_983_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

# Also fix the correct_option_id for question ID 971 to 0
c.execute('UPDATE questions SET correct_option_id = 0 WHERE id = 971')

conn.commit()
conn.close()
print("Successfully enriched Q954-Q983 and fixed correct option ID for 971!")
