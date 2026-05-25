class Node:
    def __init__(self, nilai):
        self.nilai = nilai
        self.left = None
        self.right = None


class BSTNilai:
    def __init__(self):
        self.root = None

    def insert_node(self, root, nilai):
        if root is None:
            return Node(nilai)

        if nilai < root.nilai:
            root.left = self.insert_node(root.left, nilai)

        elif nilai > root.nilai:
            root.right = self.insert_node(root.right, nilai)

        return root

    def insert(self, nilai):
        self.root = self.insert_node(self.root, nilai)

    def search_node(self, root, nilai):
        if root is None:
            return False

        if root.nilai == nilai:
            return True

        if nilai < root.nilai:
            return self.search_node(root.left, nilai)

        return self.search_node(root.right, nilai)

    def search(self, nilai):
        return self.search_node(self.root, nilai)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.nilai, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.nilai, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.nilai, end=" ")

    def nilai_terendah(self, root):
        current = root

        while current.left is not None:
            current = current.left

        return current.nilai

    def nilai_tertinggi(self, root):
        current = root

        while current.right is not None:
            current = current.right

        return current.nilai

    def jumlah_data(self, root):
        if root is None:
            return 0

        return 1 + self.jumlah_data(root.left) + self.jumlah_data(root.right)

    def total_nilai(self, root):
        if root is None:
            return 0

        return (
            root.nilai
            + self.total_nilai(root.left)
            + self.total_nilai(root.right)
        )

    def rata_rata(self):
        jumlah = self.jumlah_data(self.root)

        if jumlah == 0:
            return 0

        return self.total_nilai(self.root) / jumlah


def main():
    bst = BSTNilai()
    pilih = 0

    while pilih != 9:

        print("\nBST NILAI UJIAN")
        print("1. Tambah Nilai")
        print("2. Cari Nilai")
        print("3. Tampilkan Inorder")
        print("4. Tampilkan Preorder")
        print("5. Tampilkan Postorder")
        print("6. Nilai Tertinggi")
        print("7. Nilai Terendah")
        print("8. Rata-rata Nilai")
        print("9. Keluar")

        pilih = int(input("Pilih menu: "))

        if pilih == 1:
            nilai = int(input("Masukkan nilai: "))
            bst.insert(nilai)
            print("Nilai berhasil ditambahkan")

        elif pilih == 2:
            nilai = int(input("Masukkan nilai yang dicari: "))

            if bst.search(nilai):
                print("Nilai ditemukan")
            else:
                print("Nilai tidak ditemukan")

        elif pilih == 3:
            print("Inorder: ", end="")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Preorder: ", end="")
            bst.preorder(bst.root)
            print()

        elif pilih == 5:
            print("Postorder: ", end="")
            bst.postorder(bst.root)
            print()

        elif pilih == 6:
            print("Nilai tertinggi:",
                  bst.nilai_tertinggi(bst.root))

        elif pilih == 7:
            print("Nilai terendah:",
                  bst.nilai_terendah(bst.root))

        elif pilih == 8:
            print("Rata-rata nilai:",
                  bst.rata_rata())

        elif pilih == 9:
            print("Program selesai")

        else:
            print("Menu tidak tersedia")


if __name__ == "__main__":
    main()