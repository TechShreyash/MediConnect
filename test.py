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
p = 0
for i in med:
    p += 1
    data = {
        "request_type": "add_med",
        "email": "shop@gmail.com",
        "Med_data": {
            "id": p,
            "name": i[0],
            "brand": i[1],
            "quantity": 100,
            "price": i[2],
        },
    }
    response = requests.post("http://127.0.0.1:8000/api/medicine", json=data)
    print(response.text)
