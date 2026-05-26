## a. Judul Program 
Pengolahan Nilai Ujian Menggunakan Binary Search Tree

## b. Deskripsi Singkat 
Program Pengolahan Nilai Ujian Menggunakan Binary Search Tree merupakan tugas akhir sederhana yang digunakan untuk mengelola data nilai ujian siswa atau mahasiswa secara terstruktur. Pada program ini, setiap nilai disimpan ke dalam struktur Binary Search Tree sehingga proses penyimpanan dan pencarian data dapat dilakukan dengan lebih cepat dan teratur. Nilai yang lebih kecil akan ditempatkan di sisi kiri node, sedangkan nilai yang lebih besar ditempatkan di sisi kanan node. Dengan susunan tersebut, data nilai dapat ditampilkan secara berurutan dari nilai terkecil hingga terbesar.

Program ini memiliki beberapa fungsi utama seperti menambahkan nilai, mencari nilai tertentu, menampilkan data menggunakan traversal inorder, preorder, dan postorder, mencari nilai tertinggi, nilai terendah, serta rata-rata nilai ujian. Melalui tugas akhir ini diharapkan dapat memahami cara kerja struktur data Binary Search Tree dalam mengolah data numerik. Selain itu, program juga dapat membantu meningkatkan pemahaman mengenai proses pengurutan dan pencarian data pada struktur pohon biner.

## c. Source Code 
<img width="654" height="909" alt="image" src="https://github.com/user-attachments/assets/2171a380-ab08-419a-b718-66732902ca4a" />
<img width="638" height="859" alt="image" src="https://github.com/user-attachments/assets/2b4790ed-8624-4758-90d4-d3b2fa8c2a72" />
<img width="830" height="838" alt="image" src="https://github.com/user-attachments/assets/ff47016a-c450-4745-aa0f-f249edb4b8ec" />
<img width="725" height="870" alt="image" src="https://github.com/user-attachments/assets/3d54d848-7da1-4602-a373-065b68aa9075" />
<img width="551" height="612" alt="image" src="https://github.com/user-attachments/assets/75daa4b3-b3cf-4056-b2d3-239c6fe5a207" />

1. *(baris 1-5)* class Node:, def __init__(self, nilai):, self.nilai = nilai, self.left = None, self.right = None
* Class Node digunakan untuk membuat node pada struktur Binary Search Tree. Setiap node menyimpan satu data nilai ujian pada atribut nilai. Selain itu, terdapat atribut left dan right yang berfungsi untuk menghubungkan node ke cabang kiri dan cabang kanan. Pada saat node pertama kali dibuat, kedua cabang tersebut masih kosong atau bernilai None. Class ini menjadi dasar utama dalam pembentukan struktur pohon pada program.

2. *(baris 8-10)* class BSTNilai:, def __init__(self):, self.root = None
* Class BSTNilai digunakan untuk mengatur seluruh proses pengolahan data nilai ujian menggunakan metode Binary Search Tree. Pada class ini terdapat atribut root yang berfungsi sebagai akar atau node utama dari tree. Nilai awal root adalah None karena pada awal program belum terdapat data yang dimasukkan. Class ini nantinya akan menampung berbagai fungsi seperti penambahan data, pencarian data, traversal, serta pengolahan nilai lainnya.

3. *(baris 12-22)* def insert_node(self, root, nilai):, if root is None:, return Node(nilai), if nilai < root.nilai:, root.left = self.insert_node(root.left, nilai), elif nilai > root.nilai:, root.right = self.insert_node(root.right, nilai), return root
* Fungsi insert_node() digunakan untuk menambahkan data nilai ke dalam Binary Search Tree. Jika node masih kosong, maka program akan membuat node baru menggunakan nilai yang dimasukkan. Apabila nilai lebih kecil dari node saat ini, data akan ditempatkan pada cabang kiri. Sebaliknya, jika nilai lebih besar, data akan ditempatkan pada cabang kanan. Proses ini dilakukan secara rekursif hingga posisi yang sesuai ditemukan sehingga susunan data pada tree tetap teratur.

4. *(baris 24-25)* def insert(self, nilai):, self.root = self.insert_node(self.root, nilai)
* Fungsi insert() digunakan sebagai pemanggil utama untuk proses penambahan data nilai ke dalam tree. Fungsi ini akan memanggil insert_node() dengan mengirimkan root dan nilai yang dimasukkan pengguna. Setelah proses selesai, root akan diperbarui sesuai hasil penyisipan node baru. Fungsi ini mempermudah proses input data karena pengguna cukup memanggil satu fungsi utama saja.

5. *(baris 27-37)* def search_node(self, root, nilai):, if root is None:, return False, if root.nilai == nilai:, return True, if nilai < root.nilai:, return self.search_node(root.left, nilai), return self.search_node(root.right, nilai)
* Fungsi search_node() digunakan untuk mencari data nilai tertentu pada Binary Search Tree. Program akan memeriksa apakah node saat ini kosong. Jika kosong, berarti data tidak ditemukan sehingga fungsi mengembalikan nilai False. Jika nilai pada node sama dengan nilai yang dicari, fungsi akan mengembalikan True. Apabila nilai yang dicari lebih kecil, pencarian dilakukan ke cabang kiri, sedangkan jika lebih besar pencarian dilakukan ke cabang kanan. Proses pencarian dilakukan secara rekursif hingga data ditemukan atau node kosong tercapai.

6. *(baris 39-40)* def search(self, nilai):, return self.search_node(self.root, nilai)
* Fungsi search() digunakan sebagai fungsi utama untuk menjalankan proses pencarian nilai pada tree. Fungsi ini memanggil search_node() dengan root sebagai titik awal pencarian. Dengan adanya fungsi ini, proses pencarian menjadi lebih sederhana karena pengguna tidak perlu memanggil fungsi rekursif secara langsung.

7. *(baris 42-46)* def inorder(self, root):, if root is not None:, self.inorder(root.left), print(root.nilai, end=" "), self.inorder(root.right)
* Fungsi inorder() digunakan untuk menampilkan data menggunakan metode traversal inorder. Proses traversal dilakukan dengan mengunjungi cabang kiri terlebih dahulu, kemudian menampilkan nilai node, lalu dilanjutkan ke cabang kanan. Pada Binary Search Tree, traversal inorder menghasilkan data yang tersusun dari nilai terkecil hingga terbesar sehingga cocok digunakan untuk melihat urutan nilai secara teratur.

8. *(baris 48-52)* def preorder(self, root):, if root is not None:, print(root.nilai, end=" "), self.preorder(root.left), self.preorder(root.right)
* Fungsi preorder() digunakan untuk menampilkan data dengan metode traversal preorder. Pada traversal ini, node utama akan ditampilkan terlebih dahulu sebelum mengunjungi cabang kiri dan cabang kanan. Metode preorder biasanya digunakan untuk melihat susunan awal atau struktur tree dari node akar hingga node anak.

9. *(baris 54-58)* def postorder(self, root):, if root is not None:, self.postorder(root.left), self.postorder(root.right), print(root.nilai, end=" ")
* Fungsi postorder() digunakan untuk menampilkan data menggunakan traversal postorder. Proses traversal dilakukan dengan mengunjungi cabang kiri terlebih dahulu, kemudian cabang kanan, dan terakhir node utama. Metode ini sering digunakan pada proses penghapusan atau pemeriksaan node dari bagian paling bawah tree.

10. *(baris 60-66)* def nilai_terendah(self, root):, current = root, while current.left is not None:, current = current.left, return current.nilai
* Fungsi nilai_terendah() digunakan untuk mencari nilai paling kecil pada Binary Search Tree. Program akan bergerak terus ke cabang kiri karena pada BST nilai terkecil selalu berada di sisi kiri tree. Setelah mencapai node paling kiri, nilai pada node tersebut akan dikembalikan sebagai nilai terendah.

11. *(baris 68-74)* def nilai_tertinggi(self, root):, current = root, while current.right is not None:, current = current.right, return current.nilai
* Fungsi nilai_tertinggi() digunakan untuk mencari nilai terbesar pada Binary Search Tree. Program akan bergerak menuju cabang kanan secara terus-menerus karena nilai terbesar pada BST berada di sisi kanan tree. Ketika node paling kanan ditemukan, nilai pada node tersebut akan ditampilkan sebagai nilai tertinggi.

12. *(baris 76-80)* def jumlah_data(self, root):, if root is None:, return 0, return 1 + self.jumlah_data(root.left) + self.jumlah_data(root.right)
* Fungsi jumlah_data() digunakan untuk menghitung jumlah seluruh node atau data nilai yang terdapat pada tree. Program akan menghitung node saat ini kemudian menjumlahkannya dengan jumlah node pada cabang kiri dan cabang kanan secara rekursif hingga semua node selesai dihitung.

13. *(baris 82-90)* def total_nilai(self, root):, if root is None:, return 0, return (, root.nilai, + self.total_nilai(root.left), + self.total_nilai(root.right))
* Fungsi total_nilai() digunakan untuk menghitung total seluruh nilai yang tersimpan pada Binary Search Tree. Program akan menjumlahkan nilai pada node saat ini dengan total nilai dari cabang kiri dan cabang kanan secara rekursif hingga seluruh data selesai diproses.

14. *(baris 92-98)* def rata_rata(self):, jumlah = self.jumlah_data(self.root), if jumlah == 0:, return 0, return self.total_nilai(self.root) / jumlah
* Fungsi rata_rata() digunakan untuk menghitung rata-rata seluruh nilai ujian yang terdapat pada Binary Search Tree. Program akan menghitung jumlah seluruh data menggunakan fungsi jumlah_data(), kemudian menghitung total nilai menggunakan fungsi total_nilai(). Setelah itu total nilai dibagi dengan jumlah data sehingga diperoleh nilai rata-rata. Jika tree masih kosong, fungsi akan mengembalikan nilai 0 agar tidak terjadi kesalahan pembagian.

15. *(baris 101-103)* def main():, bst = BSTNilai(), pilih = 0
* Fungsi main() digunakan sebagai pusat pengendali jalannya program. Pada bagian ini dibuat objek bst dari class BSTNilai yang nantinya digunakan untuk menjalankan seluruh fitur pada program. Variabel pilih digunakan untuk menyimpan pilihan menu yang dimasukkan oleh pengguna.

16. *(baris 105)*  while pilih != 9:
* Perulangan while digunakan agar program terus berjalan selama pengguna belum memilih menu keluar. Selama nilai pilih tidak sama dengan 9, menu program akan terus ditampilkan sehingga pengguna dapat menggunakan fitur program secara berulang tanpa harus menjalankan ulang program.

17. *(baris 107-116)* print("\nBST NILAI UJIAN"), print("1. Tambah Nilai"), print("2. Cari Nilai"), print("3. Tampilkan Inorder"), print("4. Tampilkan Preorder"), print("5. Tampilkan Postorder"), print("6. Nilai Tertinggi"), print("7. Nilai Terendah"), print("8. Rata-rata Nilai"), print("9. Keluar")
* Bagian ini digunakan untuk menampilkan daftar menu program kepada pengguna. Setiap menu memiliki fungsi yang berbeda, seperti menambahkan nilai, mencari data, menampilkan traversal, hingga melihat nilai tertinggi dan rata-rata nilai. Menu ini mempermudah pengguna dalam memilih fitur yang ingin dijalankan.

18. *(baris 118)* pilih = int(input("Pilih menu: "))
* Baris program ini digunakan untuk menerima input pilihan menu dari pengguna. Nilai yang dimasukkan akan disimpan ke dalam variabel pilih dengan tipe data integer. Input tersebut nantinya digunakan untuk menentukan fitur apa yang akan dijalankan pada program BST nilai ujian.

19. *(baris 120-123)* if pilih == 1:, nilai = int(input("Masukkan nilai: ")), bst.insert(nilai), print("Nilai berhasil ditambahkan")
* Bagian ini dijalankan ketika pengguna memilih menu 1, yaitu fitur tambah nilai. Program akan meminta pengguna memasukkan nilai ujian yang kemudian disimpan ke dalam variabel nilai. Setelah itu, data akan dimasukkan ke dalam Binary Search Tree menggunakan fungsi insert(). Jika proses berhasil, program akan menampilkan pesan bahwa nilai berhasil ditambahkan.

20. *(baris 125-131)* elif pilih == 2:, nilai = int(input("Masukkan nilai yang dicari: ")), if bst.search(nilai):, print("Nilai ditemukan"), else:, print("Nilai tidak ditemukan")
* Bagian ini digunakan untuk menjalankan fitur pencarian nilai. Program akan meminta pengguna memasukkan nilai yang ingin dicari, kemudian fungsi search() digunakan untuk memeriksa apakah nilai tersebut terdapat pada Binary Search Tree. Jika data ditemukan, program akan menampilkan pesan “Nilai ditemukan”. Namun jika data tidak ada, program akan menampilkan pesan “Nilai tidak ditemukan”.

21. *(baris 133-136)* elif pilih == 3:, print("Inorder: ", end=""), bst.inorder(bst.root), print()
* Bagian ini digunakan untuk menampilkan traversal inorder pada Binary Search Tree. Fungsi inorder() akan menampilkan data dari nilai terkecil hingga terbesar karena traversal dilakukan dengan urutan cabang kiri, root, lalu cabang kanan. Hasil traversal akan ditampilkan pada layar secara berurutan.

22. *(baris 138-141)* elif pilih == 4:, print("Preorder: ", end=""), bst.preorder(bst.root), print()
* Bagian ini digunakan untuk menampilkan traversal preorder. Pada traversal ini, node utama akan ditampilkan terlebih dahulu sebelum cabang kiri dan cabang kanan. Fungsi ini berguna untuk melihat struktur awal tree dari root hingga node anak.

23. *(baris 143-146)* elif pilih == 5:, print("Postorder: ", end=""), bst.postorder(bst.root), print()
* Bagian ini digunakan untuk menampilkan traversal postorder pada Binary Search Tree. Traversal dilakukan dengan mengunjungi cabang kiri terlebih dahulu, kemudian cabang kanan, dan terakhir node utama. Hasil traversal akan ditampilkan sesuai urutan postorder.

24. *(baris 148-150)* elif pilih == 6:, print("Nilai tertinggi:", bst.nilai_tertinggi(bst.root))
* Bagian ini digunakan untuk menampilkan nilai tertinggi yang terdapat pada Binary Search Tree. Fungsi nilai_tertinggi() akan mencari node paling kanan pada tree karena nilai terbesar selalu berada di sisi kanan BST. Nilai tersebut kemudian ditampilkan kepada pengguna.

25. *(baris 152-154)* elif pilih == 7:, print("Nilai terendah:", bst.nilai_terendah(bst.root))
* Bagian ini digunakan untuk menampilkan nilai terendah pada Binary Search Tree. Fungsi nilai_terendah() akan mencari node paling kiri karena nilai terkecil selalu berada di sisi kiri BST. Setelah ditemukan, nilai tersebut akan ditampilkan pada layar.

26. *(baris 156-158)* elif pilih == 8:, print("Rata-rata nilai:", bst.rata_rata())
* Bagian ini digunakan untuk menghitung dan menampilkan rata-rata seluruh nilai ujian yang tersimpan pada Binary Search Tree. Fungsi rata_rata() akan menghitung total nilai dan jumlah data, kemudian membaginya untuk memperoleh hasil rata-rata.

27. *(baris 160-161)* elif pilih == 9:, print("Program selesai")
* Bagian ini dijalankan ketika pengguna memilih menu 9. Program akan menampilkan pesan bahwa program selesai dijalankan, kemudian perulangan akan berhenti sehingga program berakhir.

28. *(baris 163-164)* else:, print("Menu tidak tersedia")
* Bagian else digunakan untuk menangani input menu yang tidak sesuai dengan daftar pilihan yang tersedia. Jika pengguna memasukkan angka selain menu yang telah ditentukan, program akan menampilkan pesan “Menu tidak tersedia”.

29. *(baris 167-168)* if __name__ == "__main__":, main()
* Bagian ini digunakan untuk menjalankan fungsi main() saat file program dieksekusi secara langsung. Dengan adanya bagian ini, seluruh proses program seperti tampilan menu dan pengolahan data BST dapat berjalan secara otomatis ketika program dijalankan.

## d. Output Program 
<img width="352" height="908" alt="image" src="https://github.com/user-attachments/assets/812bdc56-c41c-4148-add8-00ac1790b819" />
<img width="363" height="914" alt="image" src="https://github.com/user-attachments/assets/e99bb574-0b96-4ef8-9da9-49c85a729ff0" />
<img width="389" height="857" alt="image" src="https://github.com/user-attachments/assets/381eebec-f5ba-4564-816f-dabc0f9c7554" />
<img width="329" height="866" alt="image" src="https://github.com/user-attachments/assets/e8b42e0d-97b8-486f-bda8-6f1d302016c3" />
<img width="233" height="288" alt="image" src="https://github.com/user-attachments/assets/b3a58e26-2db6-4465-87e3-dfaef87ea211" />
