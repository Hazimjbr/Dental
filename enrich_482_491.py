import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q482_491_exps = {
    482: 'In the maxilla, bone resorption after tooth loss occurs predominantly from the labial/buccal aspect, shifting the ridge centripetally (palatally).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 140)',
    483: 'Nickel contact allergy is relatively common, particularly in females (due to ear piercing/jewelry exposure), requiring careful material selection for baseplates.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 148)',
    484: 'In a young patient with an immature tooth and vital pulp exposure, a Cvek (calcium hydroxide) pulpotomy preserves pulp vitality and permits root completion (apexogenesis).\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 238)',
    485: 'If dentin is exposed during rest seat preparation or mouth preparation, a protective restoration (e.g., amalgam, composite, or crown) is mandatory to prevent caries and sensitivity.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 156)',
    486: 'When seating an RPD reline impression, positive finger pressure must be maintained exclusively on the metal framework/rest seats against abutment teeth.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 158)',
    487: 'Ameloblasts (enamel-forming cells) are lost during tooth eruption upon enamel maturation, making enamel incapable of cellular regeneration.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 2)',
    488: 'The buccinator muscle compresses the cheek against the teeth during mastication, keeping food positioned on the occlusal surfaces.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 12)',
    489: 'The genioglossus muscle is the primary muscle responsible for protruding the tongue forward.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 14)',
    490: 'Increasing the filler loading (volumetric concentration) of dental composite directly enhances its mechanical properties, including compressive and tensile strength.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)',
    491: 'Hybrid and micro-hybrid composites combine high filler content and strength with polishability, resisting fracture in high-stress incisal edge restorations.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 92)'
}

for q_id, exp in q482_491_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q482-Q491!")
