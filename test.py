import requests

med = (
    [
        "Meloxicam",
        "Mobic",
        "20",
        "Stomach pain, nausea, and occasional drowsiness are common with initial doses.",
        "Avoid long-term use to reduce stomach risks. Consult doctor if experiencing prolonged discomfort.",
        "Once daily",
    ],
    [
        "Tramadol",
        "Ultram",
        "45",
        "Dizziness, nausea, and constipation, especially with increased doses.",
        "Avoid combining with other opioids. Report severe drowsiness or dizziness immediately.",
        "Every 4-6 hours as needed",
    ],
    [
        "Montelukast",
        "Singulair",
        "35",
        "Drowsiness, fatigue, and occasional gastrointestinal discomfort may appear.",
        "Avoid usage near bedtime to reduce drowsiness. Take consistently as prescribed for effectiveness.",
        "Once daily, in the evening",
    ],
    [
        "Ondansetron",
        "Zofran",
        "60",
        "Headaches, stomach cramps, and rare dizziness may occur with use.",
        "Avoid mixing with alcohol. Take at least 30 minutes before meals for maximum effect.",
        "Every 8 hours as needed",
    ],
    [
        "Acetazolamide",
        "Diamox",
        "40",
        "Increased urination, nausea, or dizziness can result with high doses.",
        "Stay hydrated to avoid electrolyte imbalance. Monitor for changes in urination frequency.",
        "Once or twice daily",
    ],
    [
        "Allopurinol",
        "Zyloprim",
        "50",
        "Rash, drowsiness, or stomach cramps may appear, especially at higher doses.",
        "Do not exceed dosage as it can lead to rash or liver issues. Take with food if GI upset occurs.",
        "Once daily",
    ],
    [
        "Amitriptyline",
        "Elavil",
        "38",
        "Drowsiness, dry mouth, or blurred vision may occur with use.",
        "Avoid tasks requiring focus after dosage due to drowsiness. Best taken in the evening.",
        "Once daily, before bedtime",
    ],
    [
        "Carvedilol",
        "Coreg",
        "72",
        "Dizziness, light-headedness, or shortness of breath may occur.",
        "Monitor blood pressure regularly. Take with meals to avoid GI discomfort.",
        "Twice daily",
    ],
    [
        "Enalapril",
        "Vasotec",
        "67",
        "Dizziness, fatigue, and potential kidney issues, especially if high doses are taken.",
        "Avoid potassium-rich foods. Regular blood pressure checks are recommended.",
        "Once daily",
    ],
    [
        "Glimepiride",
        "Amaryl",
        "53",
        "Fatigue, mild nausea, or hunger can occur with altered blood sugar levels.",
        "Monitor blood sugar regularly. Avoid if you experience consistent nausea or fatigue.",
        "Once daily, with breakfast",
    ],
    [
        "Hydrochlorothiazide",
        "Microzide",
        "47",
        "Dizziness, frequent urination, and, in rare cases, light-headedness.",
        "Avoid combining with other diuretics. Take in the morning to avoid frequent urination at night.",
        "Once daily, in the morning",
    ],
    [
        "Isosorbide",
        "Isordil",
        "62",
        "Headaches, light-headedness, and in some cases, mild GI issues.",
        "Take at least 30 minutes before meals. Avoid if prone to dizziness or light-headedness.",
        "Twice daily",
    ],
    [
        "Lamotrigine",
        "Lamictal",
        "58",
        "Drowsiness, headache, or blurred vision may occur over prolonged use.",
        "Take with water to reduce side effects. Regular blood tests may be necessary.",
        "Once or twice daily",
    ],
    [
        "Methotrexate",
        "Rheumatrex",
        "30",
        "Nausea, dizziness, and potential liver issues with long-term use.",
        "Take only as directed to avoid liver damage. Avoid alcohol during use.",
        "Once weekly",
    ],
    [
        "Naproxen",
        "Aleve",
        "36",
        "Stomach cramps, heartburn, and dizziness are common with increased dosage.",
        "Avoid prolonged use to reduce stomach upset. Monitor for consistent GI discomfort.",
        "Every 8-12 hours as needed",
    ],
    [
        "Prednisolone",
        "Omnipred",
        "29",
        "Weight gain, mood changes, and upset stomach may occur during dosage changes.",
        "Take only as prescribed. Avoid sudden changes in dosage to minimize side effects.",
        "Once daily, in the morning",
    ],
    [
        "Propranolol",
        "Inderal",
        "49",
        "Fatigue, drowsiness, or light-headedness may result with dose changes.",
        "Take consistently each day. Avoid high doses due to drowsiness risks.",
        "Once or twice daily",
    ],
    [
        "Quetiapine",
        "Seroquel",
        "37",
        "Drowsiness, dizziness, or blurred vision may occur with higher doses.",
        "Avoid alcohol as it increases drowsiness. Do not operate heavy machinery post-use.",
        "Once daily, before bedtime",
    ],
    [
        "Ranitidine",
        "Zantac",
        "55",
        "Stomach discomfort, nausea, and sometimes mild drowsiness.",
        "Avoid taking with antacids for better absorption. Take before meals if possible.",
        "Once or twice daily",
    ],
    [
        "Spironolactone",
        "Aldactone",
        "68",
        "Nausea, dehydration, and in rare cases, electrolyte imbalances.",
        "Avoid high potassium foods. Monitor blood levels if on long-term use.",
        "Once daily, in the morning",
    ],
    [
        "Sulfamethoxazole",
        "Bactrim",
        "52",
        "Rash, mild dizziness, or GI discomfort may appear in sensitive individuals.",
        "Avoid sun exposure without protection due to photosensitivity. Consult for persistent GI upset.",
        "Twice daily",
    ],
    [
        "Tamsulosin",
        "Flomax",
        "43",
        "Drowsiness, light-headedness, or occasional dizziness may appear.",
        "Avoid other alpha-blockers to reduce dizziness. Take consistently for effect.",
        "Once daily, 30 minutes after a meal",
    ],
    [
        "Valsartan",
        "Diovan",
        "66",
        "Stomach upset, dizziness, or, in rare cases, liver issues with prolonged use.",
        "Monitor blood pressure regularly. Avoid potassium supplements without doctor advice.",
        "Once daily",
    ],
    [
        "Venlafaxine",
        "Effexor",
        "71",
        "Drowsiness, nausea, or sweating may appear with initial doses.",
        "Avoid activities requiring focus post-use. Take consistently to prevent mood swings.",
        "Once daily",
    ],
    [
        "Verapamil",
        "Calan",
        "78",
        "Headache, dizziness, and mild GI upset over longer periods.",
        "Take regularly at bedtime. Avoid operating heavy machinery or driving post-use.",
        "Once or twice daily",
    ],
    [
        "Zolpidem",
        "Ambien",
        "60",
        "Drowsiness, dizziness, and sometimes mild nausea in sensitive individuals.",
        "Take regularly at bedtime. Avoid operating heavy machinery or driving post-use.",
        "Once daily, before bedtime",
    ],
)

shop = [
    [
        "Shikhar Medical Store,Raipur",
        "21.2468758",
        "81.6142746",
        "https://www.google.com/maps/place/Shikhar+Medical+Store,Raipur/data=!4m7!3m6!1s0x3a28dde89e319085:0xd2b64e59ff9ce65f!8m2!3d21.2468758!4d81.6142746!16s%2Fg%2F11g8npnh3b!19sChIJhZAxnujdKDoRX-ac_1lOttI?authuser=0&hl=en&rclk=1",
    ],
    [
        "Hanuman Medical Store",
        "21.2472102",
        "81.6158516",
        "https://www.google.com/maps/place/Hanuman+Medical+Store/@21.2472102,81.6158516,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28dd75051c2f03:0x91606c44c8245a78!8m2!3d21.2472102!4d81.6158516!16s%2Fg%2F11gzm92nyg?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Rama Medical Stores",
        "21.2436724",
        "81.6120709",
        "https://www.google.com/maps/place/Rama+Medical+Stores/@21.2436724,81.6120709,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28ddd4dec5e55d:0xb64dbf51bc6318ce!8m2!3d21.2436724!4d81.6120709!16s%2Fg%2F11wbz5pnj8?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Abhinav Medical Stores",
        "21.2464844",
        "81.6171336",
        "https://www.google.com/maps/place/Abhinav+Medical+Stores/@21.2464844,81.6171336,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28dde8e2d6a44f:0xc0fee095c08650e3!8m2!3d21.2464844!4d81.6171336!16s%2Fg%2F11b7jjvg63?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Laxmi Narayan Medical Stores",
        "21.2478491",
        "81.6136427",
        "https://www.google.com/maps/place/Laxmi+Narayan+Medical+Stores/data=!4m7!3m6!1s0x3a28dde60fd8f703:0x7369a2ff622198f4!8m2!3d21.2478491!4d81.6136427!16s%2Fg%2F11sbq_kn2n!19sChIJA_fYD-bdKDoR9JghYv-iaXM?authuser=0&hl=en&rclk=1",
    ],
    [
        "Om Medical Stores",
        "21.2511877",
        "81.6197072",
        "https://www.google.com/maps/place/Om+Medical+Stores/data=!4m7!3m6!1s0x3a28ddeb52581c75:0xc7cd065cbf89b961!8m2!3d21.2511877!4d81.6197072!16s%2Fg%2F11tjxm2jkd!19sChIJdRxYUuvdKDoRYbmJv1wGzcc?authuser=0&hl=en&rclk=1",
    ],
    [
        "Shree Laxmi Medical Store",
        "21.2512505",
        "81.6206026",
        "https://www.google.com/maps/place/Shree+Laxmi+Medical+Store/data=!4m7!3m6!1s0x3a28dd001aec6d95:0xb37168a821db3a92!8m2!3d21.2512505!4d81.6206026!16s%2Fg%2F11lmj5xbvr!19sChIJlW3sGgDdKDoRkjrbIahocbM?authuser=0&hl=en&rclk=1",
    ],
    [
        "Om Shree Mahalaxmi Medical Store",
        "21.2521248",
        "81.6247896",
        "https://www.google.com/maps/place/Om+Shree+Mahalaxmi+Medical+Store/@21.2521248,81.6247896,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28ddaf4d19a205:0x2ffb81b711cd8332!8m2!3d21.2521248!4d81.6247896!16s%2Fg%2F11ghzgnw31?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Jai Medical Stores",
        "21.2368907",
        "81.6001221",
        "https://www.google.com/maps/place/Jai+Medical+Stores/@21.2368907,81.6001221,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28df0ff4916fdb:0x35219d403d231b55!8m2!3d21.2368907!4d81.6001221!16s%2Fg%2F11n0wx2t0b?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Amrit Pharmacy",
        "21.2570191",
        "81.5808741",
        "https://www.google.com/maps/place/Amrit+Pharmacy/data=!4m7!3m6!1s0x3a28de22ec3fa9b3:0x212743b7b19b11dc!8m2!3d21.2570191!4d81.5808741!16s%2Fg%2F11d_y7q1qj!19sChIJs6k_7CLeKDoR3BGbsbdDJyE?authuser=0&hl=en&rclk=1",
    ],
    [
        "Apollo Pharmacy Sunder Nagar",
        "21.2352351",
        "81.6114876",
        "https://www.google.com/maps/place/Apollo+Pharmacy+Sunder+Nagar/@21.2352351,81.6114876,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28ddda3ae90e4f:0xe7cf4c0c225149d!8m2!3d21.2352351!4d81.6114876!16s%2Fg%2F11f54n8sd5?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "AMRITYAM PHARMA",
        "21.2340152",
        "81.5954988",
        "https://www.google.com/maps/place/AMRITYAM+PHARMA/@21.2340152,81.5954988,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28df4f5ae99e99:0xeeb1e3fb1c1f9365!8m2!3d21.2340152!4d81.5954988!16s%2Fg%2F11wbmg57lh?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Shrimaa Sharda Medical & General Stores",
        "21.2309059",
        "81.595528",
        "https://www.google.com/maps/place/Shrimaa+Sharda+Medical+%26+General+Stores/@21.2309059,81.595528,17z/data=!3m1!4b1!4m6!3m5!1s0x13fe027eab46fec3:0x21945b8c043c66bc!8m2!3d21.2309059!4d81.595528!16s%2Fg%2F11b7gqwqgx?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Amar medical stores",
        "21.2325737",
        "81.6053767",
        "https://www.google.com/maps/place/Amar+medical+stores/@21.2325737,81.6053767,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28dd0c070b65f9:0xc3a9aeff84fcd88b!8m2!3d21.2325737!4d81.6053767!16s%2Fg%2F11t3_8brzk?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Muskan Medical Stores",
        "21.2379632",
        "81.5961546",
        "https://www.google.com/maps/place/Muskan+Medical+Stores/@21.2379632,81.5961546,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28de73bb40074d:0xe5d440543c55f89d!8m2!3d21.2379632!4d81.5961546!16s%2Fg%2F11gbltjd8l?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Laxmi Medical Hall Sundar Nagar Branch",
        "21.2343903",
        "81.61052",
        "https://www.google.com/maps/place/Laxmi+Medical+Hall+Sundar+Nagar+Branch/@21.2343903,81.61052,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28dddbb854ea8f:0x6522b8d26166fba5!8m2!3d21.2343903!4d81.61052!16s%2Fg%2F11cs5xx_2q?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Tilak Medical Store",
        "21.2361592",
        "81.6153231",
        "https://www.google.com/maps/place/Tilak+Medical+Store/@21.2361592,81.6153231,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28dd90385964a3:0x3c01f16925b9cf8f!8m2!3d21.2361592!4d81.6153231!16s%2Fg%2F11hm4l6h0d?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Aarogyam Pharmacy",
        "21.2405452",
        "81.6013866",
        "https://www.google.com/maps/place/Aarogyam+Pharmacy+(MEDICAL+STORE)(MANSAROVAR+BHAVAN)/@21.2405452,81.6013866,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28df08b7c05755:0xe9fa87ea7b2add0a!8m2!3d21.2405452!4d81.6013866!16s%2Fg%2F11txvpf0gt?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
    [
        "Care Medical",
        "21.2367174",
        "81.5995577",
        "https://www.google.com/maps/place/Care+Medical/@21.2367174,81.5995577,17z/data=!3m1!4b1!4m6!3m5!1s0x3a28de74234c40cf:0x8227f89c554dcd06!8m2!3d21.2367174!4d81.5995577!16s%2Fg%2F11s4vd5s5z?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI0MTAyMy4wIKXMDSoASAFQAw%3D%3D",
    ],
]

import random


def generate_random_5_digit():
    return random.randint(10000, 99999)


def generate_random_price():
    return random.randint(30, 100)


p = 0
for i in shop:
    p += 1
    data = {
        "request_type": "new_auth",
        "email": f"shop{p}@gmail.com",
        "type": "shop",
        "location": {
            "lat": i[1],
            "long": i[2],
        },
        "name": i[0],
        "link": i[3],
        "password": "123",
        "phone": "1234567890",
    }
    response = requests.post("http://127.0.0.1:8000/api/auth", json=data)
    print(response.text)

    done = []

    for l in range(10):
        i = random.choice(med)
        if i[0] in done:
            continue

        done.append(i[0])
        price = generate_random_price()
        data = {
            "request_type": "add_med",
            "email": f"shop{p}@gmail.com",
            "Med_data": {
                "id": generate_random_5_digit(),
                "name": i[0],
                "brand": i[1],
                "price": int(price),
                "quantity": 100,
                "side_effects": i[3],
                "precautions": i[4],
                "dosage": i[5],
                "retail_price": int(price) + 20,
                "units_sold": 0,
            },
        }
        response = requests.post("http://127.0.0.1:8000/api/medicine", json=data)
        print(response.text)

print(len(med))
