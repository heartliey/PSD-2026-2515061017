class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, x):
        new_node = Node(x)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Nomor antrean {x} berhasil ditambahkan")

    def dequeue(self):
        if self.is_empty():
            print("Antrean kantin kosong")
            return

        temp = self.front_ptr
        print(f"Nomor antrean {temp.data} selesai dilayani")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean kantin kosong")
            return

        print(f"Antrean paling depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrean kantin kosong")
            return

        print("Isi antrean kantin:", end=" ")

        current = self.front_ptr

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


def main():
    queue = QueueLinkedList()
    pilih = 0

    while pilih != 5:
        print("\nSISTEM ANTREAN KANTIN")
        print("1. Tambah Antrean")
        print("2. Layani Antrean")
        print("3. Lihat Antrean Depan")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                nomor = int(input("Masukkan nomor antrean: "))
                queue.enqueue(nomor)
            except ValueError:
                print("Input harus angka!")

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()