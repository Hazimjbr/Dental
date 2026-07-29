import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q419_454_exps = {
    419: 'The primary physical function of the periodontal ligament is tooth anchorage, securing the root in the alveolar socket.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    420: 'Teeth out of function (non-functional) undergo disuse atrophy of the PDL, resulting in a significantly narrower ligament space.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    421: 'Periapical radiographs (using the paralleling technique) are the gold standard for assessing interproximal alveolar bone levels and periodontal lesions.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    423: 'Vertical releasing incisions must be placed at the line angles of the tooth (not bisecting papilla) to ensure proper healing and prevent gingival recession.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    424: 'Apical migration of the junctional epithelium accompanied by marginal gingival recession at the same level results in clinical gingival recession without pocket formation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    425: 'Calculus secures its strongest attachment to the tooth surface via mechanical interlocking into microscopic irregularities of cementum and dentin.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    426: 'The normal width of a healthy periodontal ligament space ranges from 0.15 mm to 0.38 mm (typically approximated as 0.25 to 0.5 mm).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    428: 'Gingivitis initiates at the marginal gingiva, specifically starting in the sulcus area where plaque bacteria accumulate.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    429: 'Calculus acts as a major plaque-retentive factor, representing the most important local contributing factor for periodontal disease.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    430: 'An incisive (nasopalatine) foramen superimposed over a maxillary central incisor apex can be mistaken for a periapical cyst or granuloma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    431: 'Pulp canal size is continuously reduced by secondary and tertiary dentin formation stimulated by caries, attrition, trauma, and aging (All of the above).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    432: 'Periodontal dressings protect the surgical wound, assist in tissue adaptation, and help control post-operative bleeding to secure the clot.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    436: 'Furcation involvements are clinically diagnosed using a curved Nabers probe inserted into the furcation entrances of multi-rooted teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    437: 'Topical fluoride incorporates into the crystalline structure of enamel (forming fluorapatite) and plaque, significantly reducing acid solubility.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    438: 'Nitrous oxide provides strong, rapid-onset analgesia at sub-anesthetic concentrations, but has very low anesthetic potency (high MAC of 104%).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    440: 'Plain 3% Mepivacaine is an amide local anesthetic frequently preferred for patients sensitive to preservatives (like sulfites in adrenaline solutions).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    441: 'Accidental intravascular injection is the most common cause of systemic LA toxicity and associated psychogenic side effects.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    442: 'Disinfection reduces pathogenic microbes to a safe level, killing vegetative bacteria and viruses but generally failing to destroy bacterial spores.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    443: 'Soaking instruments in a virucidal agent (like sodium hypochlorite) inactivates Hepatitis B virus before safe cleaning and autoclaving.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    444: 'Autoclaving destroys micro-organisms and highly resistant spores via moist heat, which causes rapid denaturation and coagulation of essential cellular proteins.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 52)',
    445: 'In a mucoperiosteal (full-thickness) flap, the mucosa and periosteum must be reflected together as a single layer, not separated.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    448: 'Pericoronitis (inflammation of tissue overlying a partially erupted third molar) classically presents with localized pain, trismus, and lymphadenopathy.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 168)',
    449: 'Trigeminal neuralgia causes severe, sharp, stabbing pain that can mimic severe toothache (odontalgia) in clinically healthy, pathology-free teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 102)',
    450: 'The buccinator is a muscle of facial expression supplied by the facial nerve (CN VII), not the motor branch of the mandibular nerve (CN V3).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    454: 'Tobacco smoking and heavy alcohol consumption are the two most significant synergistic risk factors for developing oral squamous cell carcinoma.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)'
}

for q_id, exp in q419_454_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q419-Q454!")
