# Fungsi untuk menghasilkan semua kombinasi subset dari sebuah himpunan
def generate_subsets(items):
    subsets = [[]]
    for item in items:
        new_subsets = [subset + [item] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets

# Fungsi untuk memilih camilan berdasarkan harga dengan algoritma brute force
def brute_force_select_by_price(uang, camilan):
    best_selection = []
    best_harga = 0
    best_gizi = 0

    # Generate semua subset dari camilan
    subsets = generate_subsets(camilan)

    # Cari subset dengan total harga maksimum yang tidak melebihi uang
    for subset in subsets:
        total_harga = sum(item[1] for item in subset)
        total_gizi = sum(item[2] for item in subset)
        if total_harga <= uang and total_gizi > best_gizi:
            best_selection = subset
            best_harga = total_harga
            best_gizi = total_gizi

    return best_selection, best_harga, best_gizi, uang - best_harga

camilan = [
    ("Chiki Balls", 7000, 150),
    ("Chitato", 10000, 300),
    ("Taro Net", 6000, 130),
    ("Cheetos", 8000, 160),
    ("Lays", 10000, 250),
    ("Qtela", 8000, 210),
    ("Doritos", 12000, 200),
    ("Beng Beng", 4000, 120),
    ("Kusuka", 5000, 180),
    ("Jetz", 5000, 170)
]

uang = 25000

# Panggil fungsi untuk algoritma Brute Force
camilan_terpilih_brute, total_harga_brute, total_gizi_brute, sisa_uang_brute = brute_force_select_by_price(uang, camilan)

# Menampilkan hasil dari algoritma Brute Force
print("Camilan yang terpilih dengan Algoritma Brute Force (Berdasarkan Harga):")
for camilan in camilan_terpilih_brute:
    print(f"Nama: {camilan[0]}, Harga: Rp{camilan[1]}, Kalori: {camilan[2]} kkal")

print(f"\nTotal Harga: Rp{total_harga_brute}")
print(f"Total Kalori: {total_gizi_brute} kkal")
print(f"Sisa Uang: Rp{sisa_uang_brute}")

# -------------------Algoritma Greedy-------------------

# Knapsack by Harga
def pilih_camilan_berdasarkan_harga(uang, camilan):
    camilan_terpilih = []
    total_harga = 0
    sisa_uang = uang

    # Urutkan camilan berdasarkan harga dari yang terendah
    camilan_urut_harga = sorted(camilan, key=lambda x: x[1])

    for c in camilan_urut_harga:
        if sisa_uang >= c[1]:
            camilan_terpilih.append(c)
            total_harga += c[1]
            sisa_uang -= c[1]

    total_gizi = sum(c[2] for c in camilan_terpilih)

    return camilan_terpilih, total_harga, total_gizi, sisa_uang

# Knapsack by Kalori
def pilih_camilan_berdasarkan_kalori(uang, camilan):
    camilan_terpilih = []
    total_gizi = 0
    sisa_uang = uang

    # Urutkan camilan berdasarkan nilai kalori dari yang tertinggi
    camilan_urut_gizi = sorted(camilan, key=lambda x: x[2], reverse=True)

    for c in camilan_urut_gizi:
        if sisa_uang >= c[1]:
            camilan_terpilih.append(c)
            total_gizi += c[2]
            sisa_uang -= c[1]

    total_harga = sum(c[1] for c in camilan_terpilih)

    return camilan_terpilih, total_harga, total_gizi, sisa_uang

# Knapsack by Density
def pilih_camilan_berdasarkan_density(uang, camilan):
    camilan_terpilih = []
    total_harga = 0
    total_gizi = 0
    sisa_uang = uang

    # Hitung density (rasio nilai gizi terhadap harga) untuk setiap camilan
    density = [(i, c[2] / c[1]) for i, c in enumerate(camilan, start=1)]

    # Urutkan camilan berdasarkan density (rasio tertinggi pertama)
    camilan_urut_density = sorted(density, key=lambda x: x[1], reverse=True)

    for c in camilan_urut_density:
        if sisa_uang >= camilan[c[0] - 1][1]:
            camilan_terpilih.append(camilan[c[0] - 1])
            total_harga += camilan[c[0] - 1][1]
            total_gizi += camilan[c[0] - 1][2]
            sisa_uang -= camilan[c[0] - 1][1]

    return camilan_terpilih, total_harga, total_gizi, sisa_uang

camilan = [
    ("Chiki Balls", 7000, 150),
    ("Chitato", 10000, 300),
    ("Taro Net", 6000, 130),
    ("Cheetos", 8000, 160),
    ("Lays", 10000, 250),
    ("Qtela", 8000, 210),
    ("Doritos", 12000, 200),
    ("Beng Beng", 4000, 120),
    ("Kusuka", 5000, 180),
    ("Jetz", 5000, 170)
]

uang = 25000

# Panggil Fungsi
# camilan_terpilih, total_harga, total_gizi, sisa_uang = pilih_camilan_berdasarkan_harga(uang, camilan)
# camilan_terpilih, total_harga, total_gizi, sisa_uang = pilih_camilan_berdasarkan_kalori(uang, camilan)
camilan_terpilih, total_harga, total_gizi, sisa_uang = pilih_camilan_berdasarkan_density(uang, camilan)


# Menampilkan hasil
print("Camilan yang terpilih dengan Algoritma Greedy (Berdasarkan Harga):")
for camilan in camilan_terpilih:
    print(f"Nama: {camilan[0]}, Harga: Rp{camilan[1]}, Kalori: {camilan[2]} kkal")

print(f"\nTotal Harga: Rp{total_harga}")
print(f"Total Kalori: {total_gizi} kkal")
print(f"Sisa Uang: Rp{sisa_uang}")
