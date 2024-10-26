import requests

med = [
    ["Paracetamol 500mg", "Crocin", "20.00"],
    ["Ibuprofen 400mg", "Brufen", "25.00"],
    ["Amoxicillin 500mg", "Amoxil", "60.00"],
    ["Metformin 500mg", "Glyciphage", "30.00"],
    ["Atorvastatin 10mg", "Lipitor", "90.00"],
    ["Lisinopril 10mg", "Hipril", "50.00"],
    ["Omeprazole 20mg", "Omez", "30.00"],
    ["Azithromycin 500mg", "Azithral", "70.00"],
    ["Levothyroxine 50mcg", "Thyronorm", "40.00"],
    ["Diclofenac 50mg", "Voveran", "15.00"],
    ["Losartan 50mg", "Losar", "45.00"],
    ["Sertraline 50mg", "Serlift", "100.00"],
    ["Montelukast 10mg", "Montair", "70.00"],
    ["Alprazolam 0.5mg", "Alprax", "15.00"],
    ["Ranitidine 150mg", "Zinetac", "10.00"],
    ["Amlodipine 5mg", "Amlong", "25.00"],
    ["Doxycycline 100mg", "Doxicap", "60.00"],
    ["Tramadol 50mg", "Ultram", "80.00"],
    ["Cetirizine 10mg", "Cetzine", "15.00"],
    ["Furosemide 40mg", "Lasix", "12.00"],
]

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
        "Shri Dhanvantari Generic Medical Store",
        "21.2497222",
        "81.6050291",
        "https://www.google.com/maps/place/Shri+Dhanvantari+Generic+Medical+Store/data=!4m7!3m6!1s0x3a28dd5f5c1285a3:0xa163ee4a58f80b82!8m2!3d21.2497222!4d81.6050291!16s%2Fg%2F11t9jqtb5l!19sChIJo4USXF_dKDoRggv4WEruY6E?authuser=0&hl=en&rclk=1",
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
# p = 0
# for i in med[:5]:
#     p += 1
#     data = {
#         "request_type": "add_med",
#         "email": "shop@gmail.com",
#         "Med_data": {
#             "id": p,
#             "name": i[0],
#             "brand": i[1],
#             "quantity": 100,
#             "price": i[2],
#         },
#     }
#     response = requests.post("http://127.0.0.1:8000/api/medicine", json=data)
#     print(response.text)


p = 0
for i in shop[:5]:
    p += 1
    data = {
        "request_type": "new_auth",
        "email": f"shop{p}@gmail.com",
        'type':'shop',
        'location':{
            'lat':i[1],
            'long':i[2],
        },
        
    }
    response = requests.post("http://127.0.0.1:8000/api/auth", json=data)
    print(response.text)
