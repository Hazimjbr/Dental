import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q587_612_exps = {
    587: 'The embossed raised dot on dental X-ray film identifies the tube-facing side, allowing proper orientation (right vs. left) during mounting.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    588: 'Fixer solution clears unexposed, unreduced silver halide crystals from the emulsion, making the image permanent and light-stable.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    589: 'Excessive developer temperature accelerates chemical reduction of silver halide, resulting in overdevelopment and a dark (dense) radiograph.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 130)',
    590: 'Kaposi\'s sarcoma is the most common intraoral malignant vascular neoplasm in HIV/AIDS, occurring predominantly on the hard palate and gingiva.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    591: 'Chronic regurgitation of gastric acid in pyloric stenosis or bulimia causes severe perimylolysis (acid erosion) on palatal surfaces of maxillary incisors.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    592: 'The oral cavity of a newborn infant is sterile at birth; microbial colonization begins within hours through contact with maternal flora.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    593: 'Circumvallate (vallate) papillae contain hundreds of lateral taste buds and house the serous glands of Von Ebner in their deep trenches.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    594: 'Severe cervical constriction in primary teeth and premolars narrows the gingival floor, increasing the risk of pulpal exposure or lack of enamel support.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 90)',
    595: 'Increased intracranial pressure (ICP) following head trauma triggers Cushing\'s reflex, presenting with hypertension and bradycardia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    597: 'Long-acting benzodiazepines produce active hepatic metabolites, leading to persistent daytime sedation and "hangover" effects.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    598: 'The lingual nerve lies anterior and medial to the inferior alveolar nerve within the pterygomandibular space.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    599: 'Maxillary teeth are supplied by superior alveolar branches, while mandibular teeth are supplied by the inferior alveolar artery—all arising from the maxillary artery.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    600: 'Severe Haemophilia (X-linked recessive Factor VIII/IX deficiency) classically causes spontaneous joint hemorrhages (hemarthrosis).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    601: 'Amoxicillin is a broad-spectrum bactericidal beta-lactam that remains first-line therapy against most odontogenic mixed aerobic/anaerobic infections.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 48)',
    602: 'Post-operative inflammatory edema following third molar surgery peaks clinically at 24 to 48 hours before gradually subsiding.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    603: 'Diabetic patients taking morning insulin must maintain normal food intake to prevent severe hypoglycemia during dental procedures.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    604: 'High-risk cardiac patients on Warfarin requiring surgery are bridged with Heparin (to control INR) and given prophylactic antibiotics against endocarditis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    605: 'Clinical attachment loss (CAL) is measured from the cemento-enamel junction (CEJ) to the base of the periodontal pocket/sulcus.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    606: 'Superimposition and variations in horizontal/vertical tube angulation frequently obscure or artifactually distort the radiopaque line of lamina dura.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    607: 'Cluster headache presents as severe unilateral retro-orbital paroxysmal pain, triggered by alcohol and stress, with autonomic signs.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    608: 'Unreplaced loss of a permanent first molar causes drifting, tilting, supra-eruption, and collapse of occlusal stability affecting the entire arch and mouth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    609: 'Mandibular arch lengthening for molar eruption occurs via osteoclastic resorption of the anterior border of the ramus and apposition on the posterior border.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    610: 'A longstanding parotid mass that develops rapid facial nerve involvement or paresthesia is indicative of malignant transformation (carcinoma).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 152)',
    611: 'The "established lesion" of gingivitis/early periodontitis (after 2-3 weeks) is dominated by B-lymphocytes and plasma cells with early collagen/bone destruction.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    612: 'HIV infection is characterized by severe selective CD4+ (T4) depletion, altering the helper-to-suppressor ratio, whereas HIV periodontitis presents with severe rapid destruction.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)'
}

for q_id, exp in q587_612_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q587-Q612!")
