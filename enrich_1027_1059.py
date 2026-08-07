import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q1027_1059_exps = {
    1027: 'Syphilis disseminates rapidly (within 24 hours of contact), and its primary (chancre) and secondary (mucous patch) lesions are highly contagious.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    1028: 'Warfarin acts as a Vitamin K antagonist, affecting factors II, VII, IX, and X, thereby prolonging the prothrombin time (PT) which reflects the extrinsic pathway.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    1029: 'Staphylococcus aureus is the most common causative pathogen isolated in acute and chronic hematogenous osteomyelitis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 198)',
    1030: 'A mixed dentition analysis (like Moyer\'s or Tanaka-Johnston) is indicated at age 10 to estimate the space available for unerupted canines and premolars.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    1032: 'Microbiological studies of primary endodontic infections and periapical lesions demonstrate a polymicrobial infection dominated by obligate anaerobes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    1033: 'Immediate management for syncope or shock symptoms involves placing the patient in a supine position with elevated legs and securing the airway.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 62)',
    1034: 'A mandibular anterior inclined plane (or active maxillary bite plane) is used to guide a retroclined maxillary incisor labially out of crossbite.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 230)',
    1035: 'For effective subgingival scaling and root planing, the angle between the face of the curette blade and the tooth surface must be less than 90 degrees (ideally 70-80°).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    1036: 'Aphthous ulcers (canker sores) initiate directly as erythematous macules that quickly ulcerate without a preceding vesicular or bullous stage.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    1037: 'Squamous papilloma is a benign, exophytic, finger-like (cauliflower-like) epithelial projection commonly caused by HPV-6 or HPV-11.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 188)',
    1038: 'Thiamine (Vitamin B1) serves as a coenzyme (thiamine pyrophosphate) essential for carbohydrate metabolism and cellular energy production.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 44)',
    1039: 'Topical fluoride is highly effective at remineralizing early, non-cavitated, decalcified enamel (white spot lesions) by forming fluorapatite.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    1040: 'Rheumatic fever develops as a nonsuppurative sequela of Group A streptococcal pharyngitis, presenting with fever, migratory polyarthritis, and carditis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 62)',
    1041: 'The liver metabolizes toxic ammonia generated from amino acid deamination into water-soluble urea via the urea cycle.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 44)',
    1042: 'Any chronic oral ulceration that persists after eliminating mechanical irritation (like sharp cusps) must be biopsied to rule out squamous cell carcinoma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    1043: 'Osteosarcoma is a primary bone malignancy not linked to HIV infection, unlike Kaposi sarcoma and non-Hodgkin lymphoma, which are AIDS-defining conditions.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    1044: 'Initial management of ANUG in HIV patients focuses on mechanical debridement, plaque control, and chlorhexidine antimicrobial rinses.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    1045: 'Prothrombin Time (PT) / International Normalized Ratio (INR) is the standard laboratory test used to monitor patients taking coumarin-based oral anticoagulants.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    1046: 'Garre\'s osteomyelitis (proliferative periostitis) is a chronic osteomyelitis variant characterized by subperiosteal new bone formation (reactive periosteal hypertrophy).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 198)',
    1050: 'To prevent posterior separation (Christensen\'s phenomenon) and maintain balanced contacts during protrusion, the curve of Spee (anteroposterior curve) must be increased.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    1051: 'Christensen\'s phenomenon (posterior separation during protrusion) is compensated for in dentures by increasing the curve of Spee (compensatory curve).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 142)',
    1053: 'Burning mouth syndrome (glossodynia) in post-menopausal women frequently has a strong psychogenic or neuropathic component, after ruling out nutritional deficiencies.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    1055: 'The bilaminar zone (retrodiscal tissue) consists of loose connective tissue, elastic fibers, and blood vessels situated behind the articular disc.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    1058: 'Immediate investing of the wax pattern is critical to minimize the release of internal stresses within the wax, preventing pattern distortion.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 118)',
    1059: 'These anatomical areas represent potential pressure points (e.g., tori, midline suture, mental and incisive foramina) that require relief in denture bases.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)'
}

for q_id, exp in q1027_1059_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q1027-Q1059!")
