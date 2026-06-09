class SlotState:
    EMPTY = 0
    OCCUPIED = 1
    DELETED = 2


class Entry:
    def __init__(self):
        self.nim = None
        self.nilai = None
        self.state = SlotState.EMPTY


class HashMapOpenAddressing:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [Entry() for _ in range(self.SIZE)]

    def hash_function(self, key):
        return key % self.SIZE

    def insert(self, nim, nilai):
        idx = self.hash_function(nim)
        first_deleted = -1

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.OCCUPIED:
                if self.table[i].nim == nim:
                    self.table[i].nilai = nilai
                    return True

            elif self.table[i].state == SlotState.DELETED:
                if first_deleted == -1:
                    first_deleted = i

            else:
                if first_deleted != -1:
                    i = first_deleted

                self.table[i].nim = nim
                self.table[i].nilai = nilai
                self.table[i].state = SlotState.OCCUPIED
                return True

        return False

    def search(self, nim):
        idx = self.hash_function(nim)

        for step in range(self.SIZE):
            i = (idx + step) % self.SIZE

            if self.table[i].state == SlotState.EMPTY:
                return None

            if (self.table[i].state == SlotState.OCCUPIED and
                    self.table[i].nim == nim):
                return self.table[i]

        return None

    def remove_key(self, nim):
        data = self.search(nim)

        if data is None:
            return False

        data.state = SlotState.DELETED
        return True

    def display(self):
        print("\nData Nilai Mahasiswa:")

        for i in range(self.SIZE):
            print(f"{i}: ", end="")

            if self.table[i].state == SlotState.EMPTY:
                print("EMPTY")

            elif self.table[i].state == SlotState.DELETED:
                print("DELETED")

            else:
                print(f"(NIM: {self.table[i].nim}, "
                      f"Nilai: {self.table[i].nilai})")


def main():
    hashmap = HashMapOpenAddressing()

    # Menambahkan data mahasiswa
    hashmap.insert(231001, 90)
    hashmap.insert(231011, 85)
    hashmap.insert(231021, 88)
    hashmap.insert(231002, 95)

    hashmap.display()

    # Mencari data mahasiswa
    hasil = hashmap.search(231011)

    if hasil is not None:
        print("\nData ditemukan")
        print(f"NIM   : {hasil.nim}")
        print(f"Nilai : {hasil.nilai}")
    else:
        print("\nData tidak ditemukan")

    # Menghapus data mahasiswa
    hashmap.remove_key(231011)

    print("\nSetelah data dihapus:")
    hashmap.display()


if __name__ == "__main__":
    main()