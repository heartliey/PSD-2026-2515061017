def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nomor antrian: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos


def main():
    try:
        n = int(input("Masukkan jumlah pasien: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    pasien = []

    print("Masukkan data nomor antrian dan nama pasien (urut menaik):")
    for i in range(n):
        while True:
            try:
                nomor = int(input(f"Nomor antrian ke-{i+1}: "))
                nama = input("Nama pasien: ")
                arr.append(nomor)
                pasien.append(nama)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")

    print("\nData Antrian:")
    for i in range(n):
        print(f"{arr[i]} ({pasien[i]})")

    while True:
        try:
            target = int(input("\nMasukkan nomor antrian yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")

    pos = binary_search(arr, n, target)

    if pos != -1:
        print(f"\nNomor antrian ditemukan: {target} ({pasien[pos]})")
    else:
        print("\nNomor antrian tidak ditemukan")


if __name__ == "__main__":
    main()