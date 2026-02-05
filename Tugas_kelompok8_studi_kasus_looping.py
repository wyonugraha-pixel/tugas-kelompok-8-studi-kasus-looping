"""
=======================================================
SISTEM KASIR MINI MARKET SEDERHANA
Tugas Kelompok 8 - Algoritma dan Pemrograman 1
Program ini menggunakan Nested Loop untuk mengelola
transaksi belanja dan menampilkan struk pembelian
=======================================================
"""

def tampilkan_header():
    """Fungsi untuk menampilkan header program"""
    print("=" * 60)
    print(" " * 15 + "MINI MARKET SEJAHTERA")
    print(" " * 12 + "Jl. Pemrograman No. 123")
    print(" " * 15 + "Telp: (021) 12345678")
    print("=" * 60)

def tentukan_diskon(total):
    """
    Fungsi untuk menentukan persentase diskon berdasarkan total belanja
    Parameter: total (float) - total belanja
    Return: diskon_persen (float) - persentase diskon
    """
    if total >= 500000:
        return 15
    elif total >= 300000:
        return 10
    elif total >= 100000:
        return 5
    else:
        return 0

def main():
    """Fungsi utama program"""
    
    tampilkan_header()
    print("\n✨ Selamat Datang di Sistem Kasir Mini Market ✨\n")
    
    # LOOP UTAMA - untuk transaksi berulang
    while True:
        # Input untuk memulai transaksi baru
        mulai = input("Apakah Anda ingin memulai transaksi baru? (Y/N): ").upper()
        
        if mulai != 'Y':
            print("\n" + "=" * 60)
            print(" " * 15 + "Terima kasih telah berbelanja!")
            print(" " * 18 + "Sampai jumpa lagi!")
            print("=" * 60)
            break
        
        # Inisialisasi list untuk menyimpan data belanjaan
        daftar_belanja = []
        
        print("\n" + "-" * 60)
        print(" " * 20 + "TRANSAKSI BARU")
        print("-" * 60)
        
        # NESTED LOOP 1 - untuk menambah item belanja
        while True:
            print("\n--- Input Data Barang ---")
            
            # Input data barang
            nama_barang = input("Nama Barang    : ")
            
            # Validasi input harga (harus angka)
            while True:
                try:
                    harga = float(input("Harga Satuan   : Rp "))
                    if harga <= 0:
                        print("❌ Harga harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print("❌ Input harus berupa angka!")
            
            # Validasi input jumlah (harus angka bulat positif)
            while True:
                try:
                    jumlah = int(input("Jumlah         : "))
                    if jumlah <= 0:
                        print("❌ Jumlah harus lebih dari 0!")
                        continue
                    break
                except ValueError:
                    print("❌ Input harus berupa angka bulat!")
            
            # Hitung subtotal untuk barang ini
            subtotal = harga * jumlah
            
            # Simpan data barang ke dalam list
            daftar_belanja.append({
                'nama': nama_barang,
                'harga': harga,
                'jumlah': jumlah,
                'subtotal': subtotal
            })
            
            print(f"✅ Subtotal: Rp {subtotal:,.2f}")
            
            # Tanyakan apakah ingin menambah barang lagi
            tambah_lagi = input("\nTambah barang lagi? (Y/N): ").upper()
            if tambah_lagi != 'Y':
                break
        
        # Hitung total keseluruhan belanja
        total_belanja = sum(item['subtotal'] for item in daftar_belanja)
        
        # Tentukan diskon berdasarkan total belanja
        diskon_persen = tentukan_diskon(total_belanja)
        diskon_nominal = total_belanja * (diskon_persen / 100)
        total_bayar = total_belanja - diskon_nominal
        
        # Tampilkan struk pembelian
        print("\n" + "=" * 60)
        print(" " * 22 + "STRUK PEMBELIAN")
        print("=" * 60)
        
        # Header tabel
        print(f"{'No':<4} {'Barang':<20} {'Harga':<12} {'Qty':<5} {'Subtotal':<15}")
        print("-" * 60)
        
        # NESTED LOOP 2 - menampilkan detail setiap item belanja
        nomor = 1
        for item in daftar_belanja:
            print(f"{nomor:<4} {item['nama']:<20} Rp {item['harga']:<10,.0f} "
                  f"{item['jumlah']:<5} Rp {item['subtotal']:<13,.2f}")
            nomor += 1
        
        print("-" * 60)
        print(f"{'Total Belanja':<45} Rp {total_belanja:>12,.2f}")
        
        # Tampilkan diskon jika ada
        if diskon_persen > 0:
            print(f"{'Diskon (' + str(diskon_persen) + '%)':<45} "
                  f"Rp {diskon_nominal:>12,.2f}")
        
        print("=" * 60)
        print(f"{'TOTAL BAYAR':<45} Rp {total_bayar:>12,.2f}")
        print("=" * 60)
        
        # Input pembayaran dan hitung kembalian
        while True:
            try:
                uang_dibayar = float(input("\nUang Dibayar   : Rp "))
                if uang_dibayar < total_bayar:
                    print(f"❌ Uang tidak cukup! Kurang Rp {total_bayar - uang_dibayar:,.2f}")
                    continue
                break
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        kembalian = uang_dibayar - total_bayar
        
        print(f"Kembalian      : Rp {kembalian:,.2f}")
        
        # Tampilkan pesan terima kasih
        print("\n" + "=" * 60)
        print(" " * 15 + "Terima kasih atas pembelian Anda!")
        print(" " * 20 + "Selamat berbelanja!")
        print("=" * 60 + "\n")

# Jalankan program
if __name__ == "__main__":
    main()