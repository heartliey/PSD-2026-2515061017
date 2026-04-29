def menu():
    print("Sistem Barang Hilang")
    print("1. Tampilkan daftar barang")
    print("2. Tambah barang")
    print("3. Hapus barang")
    print("4. Keluar")


def main():
    barang = []

    while True:
        print()
        menu()
        choice = input("Masukkan pilihan (1-4): ")

        if choice == "1":
            print()
            print(f"Daftar Barang Hilang")
            if not barang:
                print("Belum ada barang.")
            else:
                for i, b in enumerate(barang, start=1):
                    print(f"{i}. {b}")

        elif choice == "2":
            print()
            print(f"Tambah Barang")
            nama = input("Masukkan nama barang: ")
            barang.append(nama.strip())
            print(f"Barang '{nama}' berhasil ditambahkan.")

        elif choice == "3":
            print()
            print(f"Hapus Barang")
            if not barang:
                print("Belum ada barang.")
            else:
                for i, b in enumerate(barang, start=1):
                    print(f"{i}. {b}")
                
                try:
                    x = int(input("Masukkan nomor barang yang ingin dihapus: "))
                    if 1 <= x <= len(barang):
                        print(f"Barang '{barang[x-1]}' berhasil dihapus.")
                        barang.pop(x-1)
                    else:
                        print("Nomor tidak valid.")
                except:
                    print("Input harus angka!")

        elif choice == "4":
            print()
            print(f"Program selesai.")
            break

        else:
            print("Pilihan tidak valid, silakan coba lagi.")


main()