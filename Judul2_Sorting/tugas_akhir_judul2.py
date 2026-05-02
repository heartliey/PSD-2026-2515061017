def insertion_sort(deadline, jarak, nama, n):
    for i in range(1, n):
        temp_deadline = deadline[i]
        temp_jarak = jarak[i]
        temp_nama = nama[i]
        j = i - 1

        while j >= 0 and (deadline[j] > temp_deadline or 
                         (deadline[j] == temp_deadline and jarak[j] > temp_jarak)):
            deadline[j + 1] = deadline[j]
            jarak[j + 1] = jarak[j]
            nama[j + 1] = nama[j]
            j -= 1

        deadline[j + 1] = temp_deadline
        jarak[j + 1] = temp_jarak
        nama[j + 1] = temp_nama


def main():
    try:
        n = int(input("Masukkan jumlah paket: "))
    except ValueError:
        print("Input tidak valid!")
        return

    nama = []
    deadline = []
    jarak = []

    print("\nMasukkan data paket:")
    for i in range(n):
        print(f"\nPaket ke-{i+1}")

        nama.append(input("Nama paket: "))

        while True:
            try:
                d = int(input("Deadline (hari): "))
                deadline.append(d)
                break
            except ValueError:
                print("Input tidak valid!")

        while True:
            try:
                j = int(input("Jarak (km): "))
                jarak.append(j)
                break
            except ValueError:
                print("Input tidak valid!")

    print("\nData sebelum diurutkan:")
    for i in range(n):
        print(nama[i], "dalam", deadline[i], "hari dengan jarak", jarak[i], "km")

    insertion_sort(deadline, jarak, nama, n)

    print("\nData setelah diurutkan (Insertion Sort):")
    for i in range(n):
        print(nama[i], "dalam", deadline[i], "hari dengan jarak", jarak[i], "km")


if __name__ == "__main__":
    main()