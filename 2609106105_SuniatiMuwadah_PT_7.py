import os

data_atm = {
    "9999": {"nama": "Sumi", "saldo": 0, "peran": "admin"},
    "1234": {"nama": "Suniati", "saldo": 500000, "peran": "user"},
    "5678": {"nama": "Suni", "saldo": 750000, "peran": "user"}
}
pin_login = None
status_aplikasi = "Belajar"
def bersihkan_layar():
    """Membersihkan tampilan terminal."""
    perintah = "cls" if os.name == "nt" else "clear"
    os.system(perintah)

def bersihkan_layar():
    """Prosedur 1: Membersihkan tampilan terminal."""

def tampilkan_header(judul):
    """Menampilkan judul halaman."""
    garis = "=" * 40
    print(garis)
    print(judul.center(40))
    print(garis)

def input_menu():
    """Membaca pilihan menu utama."""
    try:
        return int(input("Pilih menu (1-3): "))
    except ValueError:
        return 0

def buat_rekening_baru():
    """Mendaftarkan rekening nasabah baru."""
    bersihkan_layar()
    tampilkan_header("PENDAFTARAN REKENING")

    pin_baru = input("Buat PIN baru: ").strip()

    if not pin_baru.isdigit():
        print("\nPIN harus berupa angka.")
    elif pin_baru in data_atm:
        print("\nPIN tersebut sudah digunakan.")
    else:
        nama = input("Masukkan nama lengkap: ").strip()

        if not nama:
            print("\nNama tidak boleh kosong.")
        else:
            try:
                saldo_awal = int(input("Setoran awal: Rp "))
                if saldo_awal < 0:
                    print("\nSetoran awal tidak boleh kurang dari nol.")
                else:
                    data_atm[pin_baru] = {
                        "nama": nama,
                        "saldo": saldo_awal,
                        "peran": "user"
                    }
                    print("\nRekening berhasil dibuat.")
            except ValueError:
                print("\nSetoran awal harus berupa angka.")

    input("\nTekan Enter untuk kembali...")

def tambah_saldo(saldo, jumlah):
    """Mengembalikan saldo setelah setor tunai."""
    return saldo + jumlah

def cek_penarikan(saldo, jumlah):
    """Memeriksa apakah penarikan bisa dilakukan."""
    if jumlah <= 0:
        return False, "Jumlah penarikan harus lebih dari nol."
    if jumlah > saldo:
        return False, "Saldo tidak mencukupi."
    return True, "Penarikan bisa dilakukan."


def menu_nasabah(pin):
    """Menu yang digunakan oleh nasabah."""
    while True:
        bersihkan_layar()
        nama = data_atm[pin]["nama"]
        tampilkan_header("SELAMAT DATANG, " + nama.upper())
        print("1. Cek saldo")
        print("2. Setor tunai")
        print("3. Tarik tunai")
        print("4. Logout")
        print("=" * 40)

        try:
            pilihan = int(input("Pilih menu (1-4): "))
        except ValueError:
            print("\nMasukkan pilihan berupa angka.")
            input("Tekan Enter...")
            continue

        if pilihan == 1:
            bersihkan_layar()
            tampilkan_header("INFORMASI SALDO")
            print("Nama  :", data_atm[pin]["nama"])
            print("Saldo : Rp", data_atm[pin]["saldo"])
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 2:
            bersihkan_layar()
            tampilkan_header("SETOR TUNAI")
            try:
                jumlah = int(input("Masukkan jumlah setoran: Rp "))
                if jumlah <= 0:
                    print("\nSetoran harus lebih dari nol.")
                else:
                    data_atm[pin]["saldo"] = tambah_saldo(
                        data_atm[pin]["saldo"], jumlah
                    )
                    print("\nSetoran berhasil.")
                    print("Saldo sekarang: Rp", data_atm[pin]["saldo"])
            except ValueError:
                print("\nJumlah setoran harus berupa angka.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 3:
            bersihkan_layar()
            tampilkan_header("TARIK TUNAI")
            try:
                jumlah = int(input("Masukkan jumlah penarikan: Rp "))
                boleh_tarik, pesan = cek_penarikan(
                    data_atm[pin]["saldo"], jumlah
                )

                if boleh_tarik:
                    data_atm[pin]["saldo"] -= jumlah
                    print("\nPenarikan berhasil.")
                    print("Sisa saldo: Rp", data_atm[pin]["saldo"])
                else:
                    print("\n" + pesan)
            except ValueError:
                print("\nJumlah penarikan harus berupa angka.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 4:
            break
        else:
            print("\nPilihan tidak tersedia.")
            input("Tekan Enter...")

def menu_admin(nama_admin):
    """Menu untuk mengelola akun nasabah."""
    while True:
        bersihkan_layar()
        tampilkan_header("PANEL ADMIN - " + nama_admin.upper())
        print("1. Lihat semua akun")
        print("2. Hapus akun nasabah")
        print("3. Logout")
        print("=" * 40)

        try:
            pilihan = int(input("Pilih menu (1-3): "))
        except ValueError:
            print("\nMasukkan pilihan berupa angka.")
            input("Tekan Enter...")
            continue

        if pilihan == 1:
            bersihkan_layar()
            tampilkan_header("DAFTAR AKUN")
            for nomor, (pin, info) in enumerate(data_atm.items(), start=1):
                print(
                    f"{nomor}. PIN: {pin} | Nama: {info['nama']} | "
                    f"Saldo: Rp {info['saldo']} | Peran: {info['peran']}"
                )
            input("\nTekan Enter untuk kembali...")

        elif pilihan == 2:
            bersihkan_layar()
            tampilkan_header("HAPUS AKUN")
            pin_hapus = input("Masukkan PIN akun yang ingin dihapus: ").strip()

            if pin_hapus not in data_atm:
                print("\nAkun tidak ditemukan.")
            elif data_atm[pin_hapus]["peran"] == "admin":
                print("\nAkun admin tidak bisa dihapus dari menu ini.")
            else:
                konfirmasi = input("Yakin ingin menghapus akun ini? (y/t): ")
                if konfirmasi.lower() == "y":
                    del data_atm[pin_hapus]
                    print("\nAkun berhasil dihapus.")
                else:
                    print("\nPenghapusan dibatalkan.")
            input("\nTekan Enter untuk kembali...")        

        elif pilihan == 3:
            break
        else:
            print("\nPilihan tidak tersedia.")
            input("Tekan Enter...")

def main():
    global pin_login

    while True:
        bersihkan_layar()
        tampilkan_header("APLIKASI ATM SEDERHANA")
        print("1. Login")
        print("2. Buat rekening baru")
        print("3. Keluar")
        print("=" * 40)

        pilihan = input_menu()

        
        if pilihan == 1:
            bersihkan_layar()
            tampilkan_header("LOGIN ATM")

            pin_input = input("Masukkan PIN Anda: ").strip()
            
            if pin_input in data_atm:
                pin_login = pin_input
                peran = data_atm[pin_login]["peran"]
                nama = data_atm[pin_login]["nama"]
                
                print(f"\nLogin berhasil! Selamat datang, {nama}.")
                input("Tekan Enter untuk melanjutkan...")
                
                if peran == "admin":
                    menu_admin(nama)
                else:
                    menu_nasabah(pin_login)
            else:
                print("\nPIN salah atau akun tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

        elif pilihan == 2:
            buat_rekening_baru()

        elif pilihan == 3:
            print("\nTerima kasih sudah menggunakan aplikasi ATM.")
            break

        else:
            print("\nPilihan menu tidak valid.")
            input("Tekan Enter...")

        
if __name__ == "__main__":
    main()
