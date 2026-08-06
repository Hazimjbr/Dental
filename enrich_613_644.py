import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q613_644_exps = {
    613: 'Topical or systemic Acyclovir inhibits viral DNA polymerase most effectively when initiated early during the prodromal tingling phase of recurrent herpes labialis.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    614: 'Plaque-induced inflammation is the most common cause of gingival enlargement, while Phenytoin, Cyclosporine, and Calcium Channel Blockers are the primary drug-induced causes.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    615: 'Management of Phenytoin-induced gingival overgrowth involves rigorous oral hygiene/scaling followed by surgical excision (gingivectomy/gingivoplasty) if tissue persists.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    616: 'In Dentinogenesis imperfecta, abnormal dentin lacks structural support, causing overlying enamel to chip off easily, along with early pulp chamber obliteration.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 132)',
    617: 'Oral irrigators (water jets) flush loose debris from interproximal areas but cannot disrupt or remove the tenacious acquired pellicle or mature plaque biofilm.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    619: 'If a fractured tuberosity segment remains firmly attached to periosteum, the extraction should be abandoned, the tooth/tuberosity stabilized, and left to heal for 6-8 weeks.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 84)',
    620: 'If a clinically suspicious/ulcerated lesion yields a non-diagnostic benign or inflammatory biopsy report, a repeat incisional biopsy is mandatory to rule out sampling error.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    622: 'Rescue breathing during adult basic life support is delivered at a rate of 10 to 12 breaths per minute (1 breath every 5-6 seconds).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    623: 'Laryngeal muscle paralysis or upper airway obstruction impairs airflow, dramatically reducing effective pulmonary ventilation.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    627: 'Koplik\'s spots (small, irregular erythematous macules with bluish-white centers on buccal mucosa) are pathognomonic early signs of Measles (Rubeola).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 182)',
    628: 'Von Recklinghausen disease (Neurofibromatosis Type 1) is a genetic disorder characterized by multiple neurofibromas, café-au-lait spots, and Lisch nodules.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 196)',
    629: 'Head tilt and neck extension (with chin lift) lifts the tongue away from the posterior pharyngeal wall, clearing the upper airway.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    630: 'Standard infective endocarditis antibiotic prophylaxis for high/moderate risk patients involves 2g Amoxicillin orally 30-60 minutes prior to surgical procedures.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    631: 'Routine antibiotic therapy does not impair platelet function or coagulation, making it least likely to cause post-operative surgical hemorrhage.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    632: 'Acute bacterial infections evoke a marked systemic inflammatory response characterized by leukocytosis with an elevated neutrophil count (neutrophilia).\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    633: 'Patients with a history of infective endocarditis require mandatory antibiotic prophylaxis before invasive dental procedures that induce bacteremia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    634: 'Addison\'s disease causes elevated ACTH levels due to adrenal insufficiency, stimulating melanocytes and producing diffuse bronzing of the skin and oral mucosa.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 190)',
    635: 'Immediate management of vasovagal syncope (fainting) is placing the patient in a flat supine position with legs slightly elevated to restore cerebral blood flow.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 60)',
    636: 'Thrombocytopenia (low platelet count <50,000/µL) impairs primary hemostasis, resulting in prolonged bleeding and post-operative hemorrhage.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    637: 'A massive elevation in white blood cell count exceeding 100,000/µL is indicative of hyperleukocytosis in acute or chronic Leukemia.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    638: 'Epidemiological studies confirm that chronic periodontitis is the primary cause of tooth loss in adults older than 35 years.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    639: 'Patients with a history of rheumatic heart disease with valvular damage require prophylactic antibiotic coverage before dental procedures.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 42)',
    642: 'In emergency trauma resuscitation, securing the airway and ensuring adequate breathing (the "A" and "B" of ATLS protocol) takes absolute priority.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    643: 'Key signs of intracranial trauma include loss of consciousness, persistent vomiting, severe headache, and un-reactive pupils.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 166)',
    644: 'For patients allergic to penicillin requiring infective endocarditis prophylaxis, Macrolides (Erythromycin/Azithromycin) or Clindamycin are the standard alternatives.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 48)'
}

for q_id, exp in q613_644_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q613-Q644!")
