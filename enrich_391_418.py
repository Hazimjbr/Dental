import sqlite3

db_path = r"C:\Users\admin\.gemini\antigravity\brain\6776ae56-d1c4-4149-9279-1f3eb725967a\scratch\dental_bot.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

q391_418_exps = {
    391: 'Periodontal inflammation begins as gingivitis, originating in the marginal gingiva in response to accumulated bacterial plaque.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    392: 'Dental calculus acts as a non-vital, plaque-retentive scaffold, serving as the most important local promoting factor for periodontal disease.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    393: 'Periodontal ligament (PDL) collagen fibers have a wavy (undulating) course, allowing slight tooth movement during mastication.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    394: 'Injecting the patient in a supine position prevents syncope and lowers systemic distress, making it the least likely to trigger systemic toxicity symptoms.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    395: 'Congenital absence of teeth (anodontia) leads to lack of alveolar process development, severely affecting vertical height and growth of the whole face.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    396: 'Premature loss of a primary molar allows the adjacent first permanent molar to drift mesially, causing loss of arch length and subsequent crowding.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 268)',
    397: 'After age 6, mandibular growth occurs primarily by bone deposition at the posterior border of the ramus, distal to the first permanent molar.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 220)',
    398: 'Angle\'s Class II Division 2 malocclusion is characteristically defined by the retrusion (palatal tilt) of the maxillary central incisors.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 260)',
    399: 'Although the theoretical maximum safe dose of plain 2% lidocaine is 4.4 mg/kg (approx. 200-300 mg), clinical guidelines emphasize minimal dosing.\n\n🏛️ Book Reference: Master Dentistry Vol. 1 (p. 66)',
    400: 'Increasing the pH (making it more basic) decreases the uptake of fluoride; acidifying the agent (lower pH) actually increases fluoride absorption by enamel.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    401: 'Many liquid cough syrups are highly concentrated sugar-based vehicles (containing up to 60-80% sucrose) posing a severe caries risk if used long-term.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 22)',
    402: 'Systemic fluoride supplementation is adjusted based on local water fluoridation levels; supplementary dosing is not required if water contains >0.6 ppm.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 28)',
    403: 'Class II Division 2 malocclusion is primarily skeletal in origin, driven by retrognathic mandibular growth and strong lip pressure.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 260)',
    404: 'An ankylosed tooth does not erupt with the growing alveolar process, appearing submerged and failing to maintain normal occlusal height.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 222)',
    405: 'Intruded primary incisors should be allowed to re-erupt spontaneously; immediate treatment involves control of bleeding and monitoring.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 254)',
    406: 'If the successor premolar is congenitally missing, the primary molar should be preserved long-term using pulpectomy/endodontic treatment.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    407: 'In primary teeth, accessory canals frequently open into the furcation area, causing pathological bone resorption at the interradicular septum.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 234)',
    408: 'The primary mandibular second molar anatomically mimics the permanent mandibular first molar, typically possessing 5 pulp horns.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 210)',
    409: 'Crevicular (sulcular) epithelium is non-keratinized, allowing fluid exchange and cellular defense mechanisms against plaque.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 180)',
    410: 'Bacterial plaque (biofilm) is the primary initiating etiological factor responsible for gingival inflammation and irritation.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 182)',
    412: 'Dental floss is highly effective for mechanical removal of bacterial plaque and food debris from tight interproximal contacts.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 184)',
    413: 'Shifting the oral microflora from acidogenic to non-acidogenic species requires long-term dietary modification maintained over several months.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 24)',
    414: 'Saccharin is a synthetic, non-nutritive (zero-calorie) artificial sweetener, unlike mannitol and xylitol which are sugar alcohols.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 22)',
    417: 'Overextension of a cavity liner internally does not impact the surrounding periodontium, unlike flat contacts or rough cervical margins.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 114)',
    418: 'Occlusal trauma causes localized, vertical bone defects (angular bone loss) adjacent to teeth under excessive lateral forces.\n\n🏛️ Book Reference: Master Dentistry Vol. 2 (p. 183)'
}

for q_id, exp in q391_418_exps.items():
    c.execute('UPDATE questions SET explanation = ? WHERE id = ?', (exp, q_id))

conn.commit()
conn.close()
print("Successfully enriched Q391-Q418!")
