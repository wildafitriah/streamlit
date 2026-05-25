class KategoriNode:
    def __init__(self, nama_kategori):
        self.nama = nama_kategori
        self.sub_kategori = [] # Ini adalah 'anak' atau cabang dari kategori

    def tambah_sub(self, node_kategori):
        self.sub_kategori.append(node_kategori)
        return node_kategori # Mengembalikan node agar mudah disambung (chaining)

    def tampilkan_katalog(self, level=0):
        # Mengatur spasi agar terlihat bertingkat
        indentasi = "    " * level
        simbol = "↳ " if level > 0 else "🛒 "
        
        print(f"{indentasi}{simbol}{self.nama}")
        
        for sub in self.sub_kategori:
            sub.tampilkan_katalog(level + 1)

    def cari_kategori(self, target, path=""):
        # Menyimpan jalur pencarian (breadcrumb)
        jalur_saat_ini = path + " > " + self.nama if path else self.nama
        
        # Jika ketemu, kembalikan jalurnya
        if self.nama.lower() == target.lower():
            return jalur_saat_ini
            
        # Jika belum ketemu, cari ke dalam cabang-cabangnya (rekursi)
        for sub in self.sub_kategori:
            hasil = sub.cari_kategori(target, jalur_saat_ini)
            if hasil: # Jika berhasil ditemukan di cabang
                return hasil
                
        return None # Jika tidak ditemukan sama sekali di cabang ini

# ==========================================
# SIMULASI PENGGUNAAN DI TOKO ONLINE
# ==========================================

# 1. Membuat Kategori Utama (Root)
toko = KategoriNode("Semua Kategori")

# 2. Membuat Cabang Kategori Level 1
elektronik = toko.tambah_sub(KategoriNode("Elektronik"))
pakaian = toko.tambah_sub(KategoriNode("Pakaian"))
kebutuhan_rumah = toko.tambah_sub(KategoriNode("Kebutuhan Rumah"))

# 3. Membuat Cabang Level 2 (Sub-kategori Elektronik)
komputer = elektronik.tambah_sub(KategoriNode("Komputer & Laptop"))
hp = elektronik.tambah_sub(KategoriNode("Handphone & Tablet"))

# 4. Membuat Cabang Level 3 (Sub-kategori Komputer)
komputer.tambah_sub(KategoriNode("Laptop Gaming"))
komputer.tambah_sub(KategoriNode("Laptop Kantor"))
komputer.tambah_sub(KategoriNode("Komponen PC"))

# 5. Membuat Cabang untuk Pakaian
pakaian.tambah_sub(KategoriNode("Pakaian Pria"))
pakaian.tambah_sub(KategoriNode("Pakaian Wanita"))

# --- MARI KITA JALANKAN PROGRAMNYA ---

print("=== KATALOG PRODUK TOKO ONLINE ===")
toko.tampilkan_katalog()
print("\n" + "="*35 + "\n")

# Simulasi Fitur Pencarian
kata_kunci = "Laptop Gaming"
print(f"🔍 Mencari kategori: '{kata_kunci}'...")

hasil_pencarian = toko.cari_kategori(kata_kunci)

if hasil_pencarian:
    print(f" Ditemukan! Jalur kategori: {hasil_pencarian}")
else:
    print(" Kategori tidak ditemukan.")