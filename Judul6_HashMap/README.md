## a. Judul Program 
Implementasi Hash Map pada Data Nilai Mahasiswa

## b. Deskripsi Singkat 
Implementasi Hash Map pada Data Nilai Mahasiswa merupakan sistem yang digunakan untuk mengelola data nilai mahasiswa secara terstruktur dan efisien. 
Sistem ini memanfaatkan struktur data hash map dengan metode open addressing untuk mempermudah proses penyimpanan, pencarian, dan penghapusan data berdasarkan nomor
induk mahasiswa (NIM). Dengan metode tersebut, data dapat diakses lebih cepat sehingga proses pengolahan data menjadi lebih efektif.

Sistem ini menyediakan beberapa fitur utama, seperti menambahkan data mahasiswa, menampilkan data nilai, mencari data berdasarkan NIM, serta menghapus data yang 
udah tidak digunakan. Penerapan sistem dilakukan menggunakan bahasa pemrograman Python dengan tampilan sederhana agar mudah dipahami. Melalui sistem ini, pengguna 
dapat memahami penerapan struktur data hash map dalam pengelolaan data mahasiswa.

## c. Source Code 
<img width="674" height="832" alt="image" src="https://github.com/user-attachments/assets/e88bc45c-ef22-48b8-991d-0ef513352968" />
<img width="667" height="723" alt="image" src="https://github.com/user-attachments/assets/91fdd2be-2ed8-4874-8be5-ddb6222c8863" />
<img width="632" height="763" alt="image" src="https://github.com/user-attachments/assets/ba2fcfde-f5d2-4456-ac5a-8e3155874dcc" />
<img width="476" height="542" alt="image" src="https://github.com/user-attachments/assets/b04ebd71-50aa-4651-a21d-7240cccb2756" />

`class SlotState:`
Bagian ini digunakan untuk membuat kelas yang berfungsi sebagai penanda kondisi setiap slot pada hash table. Penanda ini sangat penting pada metode open addressing karena sistem harus mengetahui apakah suatu slot masih kosong, sedang digunakan, atau pernah digunakan tetapi datanya sudah dihapus. Dengan adanya status tersebut, proses pencarian dan penyimpanan data dapat berjalan dengan benar.

`EMPTY = 0`
Baris ini digunakan untuk menandai bahwa slot pada hash table masih kosong dan belum pernah digunakan untuk menyimpan data.

`OCCUPIED = 1`
Baris ini digunakan untuk menandai bahwa slot sudah terisi data mahasiswa.

`DELETED = 2`
Baris ini digunakan untuk menandai bahwa data pada slot telah dihapus, tetapi posisi slot tetap dipertahankan agar proses pencarian data lain tidak terganggu.

`class Entry:`
Bagian ini digunakan untuk membuat kelas penyimpanan data mahasiswa pada setiap slot hash table. Setiap slot nantinya akan memiliki data NIM, nilai mahasiswa, dan status slot.

`def __init__(self):`
Constructor ini akan otomatis dijalankan ketika objek `Entry` dibuat.

`self.nim = None`
Digunakan untuk menyimpan nomor induk mahasiswa. Nilai awal dibuat `None` karena slot masih kosong.

`self.nilai = None`
Digunakan untuk menyimpan nilai mahasiswa pada hash table.

`self.state = SlotState.EMPTY`
Menentukan bahwa kondisi awal slot adalah `EMPTY` atau kosong.

`class HashMapOpenAddressing:`
Kelas ini merupakan bagian utama dari sistem hash map yang menggunakan metode open addressing dengan teknik linear probing. Seluruh proses pengolahan data dilakukan di dalam kelas ini.

`def __init__(self, size=10):`
Fungsi ini digunakan untuk menentukan ukuran hash table saat objek dibuat.

`self.SIZE = size`
Baris ini menyimpan ukuran hash table ke dalam variabel `SIZE`.

`self.table = [Entry() for _ in range(self.SIZE)]`
Kode ini digunakan untuk membuat tabel hash kosong sesuai ukuran yang telah ditentukan. Setiap slot pada tabel akan berisi objek `Entry`.

`def hash_function(self, key):`
Fungsi ini digunakan untuk menentukan posisi awal penyimpanan data berdasarkan key atau NIM mahasiswa.

`return key % self.SIZE`
Baris ini menggunakan operasi modulus untuk menghasilkan indeks hash table. Hasil modulus digunakan sebagai lokasi penyimpanan data agar data dapat tersebar secara teratur.

`def insert(self, nim, nilai):`
Fungsi ini digunakan untuk menambahkan data mahasiswa ke dalam hash table.

`idx = self.hash_function(nim)`
Digunakan untuk mencari indeks awal penyimpanan data berdasarkan NIM mahasiswa.

`first_deleted = -1`
Variabel ini digunakan untuk menyimpan posisi slot pertama yang memiliki status `DELETED`.

`for step in range(self.SIZE):`
Perulangan ini digunakan untuk melakukan pencarian slot kosong pada hash table.

`i = (idx + step) % self.SIZE`
Baris ini digunakan untuk menjalankan proses linear probing apabila terjadi collision. Sistem akan berpindah ke indeks berikutnya sampai menemukan slot yang tersedia.

`if self.table[i].state == SlotState.OCCUPIED:`
Digunakan untuk mengecek apakah slot sedang terisi data.

`if self.table[i].nim == nim:`
Digunakan untuk mengecek apakah NIM yang dimasukkan sudah ada di dalam hash table.

`self.table[i].nilai = nilai`
Jika NIM sudah tersedia, maka nilai mahasiswa akan diperbarui dengan data terbaru.

`return True`
Menandakan bahwa proses pembaruan data berhasil dilakukan.

`elif self.table[i].state == SlotState.DELETED:`
Digunakan untuk mengecek apakah slot pernah digunakan tetapi datanya sudah dihapus.

`if first_deleted == -1:`
Digunakan untuk memastikan posisi slot `DELETED` pertama belum tersimpan.

`first_deleted = i`
Menyimpan indeks slot `DELETED` pertama agar dapat digunakan kembali untuk data baru.

`else:`
Bagian ini dijalankan apabila sistem menemukan slot kosong.

`if first_deleted != -1:`
Digunakan untuk mengecek apakah sebelumnya terdapat slot dengan status `DELETED`.

`i = first_deleted`
Jika ada slot `DELETED`, maka data baru akan disimpan pada slot tersebut.

`self.table[i].nim = nim`
Digunakan untuk menyimpan NIM mahasiswa ke dalam hash table.

`self.table[i].nilai = nilai`
Digunakan untuk menyimpan nilai mahasiswa.

`self.table[i].state = SlotState.OCCUPIED`
Mengubah status slot menjadi `OCCUPIED` karena slot sudah berisi data.

`return True`
Menandakan bahwa proses penambahan data berhasil dilakukan.

`return False`
Menandakan bahwa proses insert gagal karena hash table sudah penuh.

`def search(self, nim):`
Fungsi ini digunakan untuk mencari data mahasiswa berdasarkan NIM.

`idx = self.hash_function(nim)`
Digunakan untuk menentukan indeks awal pencarian data.

`for step in range(self.SIZE):`
Perulangan dilakukan untuk mencari data pada hash table.

`i = (idx + step) % self.SIZE`
Digunakan untuk melakukan linear probing selama proses pencarian.

`if self.table[i].state == SlotState.EMPTY:`
Jika sistem menemukan slot kosong, maka pencarian dihentikan karena data dianggap tidak tersedia.

`return None`
Mengembalikan nilai `None` jika data tidak ditemukan.

`if (self.table[i].state == SlotState.OCCUPIED and self.table[i].nim == nim):`
Digunakan untuk mengecek apakah slot berisi data dan memiliki NIM yang sesuai dengan pencarian.

`return self.table[i]`
Mengembalikan data mahasiswa jika berhasil ditemukan.

`def remove_key(self, nim):`
Fungsi ini digunakan untuk menghapus data mahasiswa berdasarkan NIM.

`data = self.search(nim)`
Digunakan untuk mencari data mahasiswa yang akan dihapus.

`if data is None:`
Digunakan untuk mengecek apakah data tidak ditemukan.

`return False`
Menandakan bahwa proses penghapusan gagal dilakukan.

`data.state = SlotState.DELETED`
Mengubah status slot menjadi `DELETED` agar slot tetap dikenali dalam proses probing.

`return True`
Menandakan bahwa data berhasil dihapus.

`def display(self):`
Fungsi ini digunakan untuk menampilkan seluruh isi hash table.

`print("\nData Nilai Mahasiswa:")`
Menampilkan judul output program.

`for i in range(self.SIZE):`
Perulangan digunakan untuk menampilkan seluruh slot hash table satu per satu.

`print(f"{i}: ", end="")`
Menampilkan nomor indeks pada hash table.

`if self.table[i].state == SlotState.EMPTY:`
Mengecek apakah slot kosong.

`print("EMPTY")`
Menampilkan tulisan `EMPTY` jika slot belum digunakan.

`elif self.table[i].state == SlotState.DELETED:`
Mengecek apakah slot sudah dihapus.

`print("DELETED")`
Menampilkan tulisan `DELETED` jika slot pernah digunakan tetapi datanya telah dihapus.

`else:`
Bagian ini dijalankan jika slot berisi data mahasiswa.

`print(f"(NIM: {self.table[i].nim}, Nilai: {self.table[i].nilai})")`
Menampilkan data mahasiswa berupa NIM dan nilai yang tersimpan pada hash table.

`def main():`
Merupakan fungsi utama yang digunakan untuk menjalankan seluruh proses pada program.

`hashmap = HashMapOpenAddressing()`
Digunakan untuk membuat objek hash map.

`hashmap.insert(231001, 90)`
Menambahkan data mahasiswa pertama ke hash table.

`hashmap.insert(231011, 85)`
Menambahkan data mahasiswa kedua.

`hashmap.insert(231021, 88)`
Menambahkan data mahasiswa ketiga.

`hashmap.insert(231002, 95)`
Menambahkan data mahasiswa keempat.

`hashmap.display()`
Digunakan untuk menampilkan seluruh isi hash table setelah data ditambahkan.

`hasil = hashmap.search(231011)`
Digunakan untuk mencari data mahasiswa dengan NIM `231011`.

`if hasil is not None:`
Mengecek apakah data berhasil ditemukan.

`print("\nData ditemukan")`
Menampilkan pesan bahwa data ditemukan.

`print(f"NIM   : {hasil.nim}")`
Menampilkan NIM mahasiswa yang ditemukan.

`print(f"Nilai : {hasil.nilai}")`
Menampilkan nilai mahasiswa yang ditemukan.

`else:`
Dijalankan apabila data tidak ditemukan.

`print("\nData tidak ditemukan")`
Menampilkan pesan bahwa data tidak tersedia.

`hashmap.remove_key(231011)`
Digunakan untuk menghapus data mahasiswa dengan NIM `231011`.

`print("\nSetelah data dihapus:")`
Menampilkan keterangan setelah proses penghapusan data dilakukan.

`hashmap.display()`
Menampilkan isi terbaru hash table setelah data dihapus.

`if __name__ == "__main__":`
Digunakan untuk memastikan bahwa file dijalankan secara langsung.

`main()`
Menjalankan fungsi utama program.

## d. Output Program 
<img width="470" height="654" alt="image" src="https://github.com/user-attachments/assets/d33ee157-de7c-494e-adae-344fe659abfb" />

Output pertama menampilkan isi hash table setelah data mahasiswa berhasil ditambahkan menggunakan fungsi `insert()`. Pada tampilan tersebut, indeks `1`, `2`, `3`, 
dan `4` berisi data mahasiswa berupa NIM dan nilai, sedangkan indeks lainnya masih berstatus `EMPTY` karena belum digunakan. Data disimpan berdasarkan hasil 
perhitungan fungsi hash menggunakan operasi modulus terhadap NIM mahasiswa. Oleh karena itu, setiap data ditempatkan pada indeks tertentu di dalam hash table.

Selanjutnya, sistem melakukan proses pencarian data menggunakan fungsi `search()` dengan NIM `231011`. Karena data ditemukan pada hash table, sistem menampilkan 
informasi berupa NIM dan nilai mahasiswa, yaitu nilai `85`. Hal ini menunjukkan bahwa proses pencarian data menggunakan hash map dapat dilakukan dengan cepat karena
sistem langsung menuju indeks yang sesuai berdasarkan hasil fungsi hash.

Pada bagian berikutnya, sistem menjalankan fungsi `remove_key()` untuk menghapus data mahasiswa dengan NIM `231011`. Setelah data dihapus, tampilan hash table 
berubah pada indeks `2` menjadi `DELETED`. Kondisi tersebut menunjukkan bahwa data telah dihapus, tetapi slot tidak dikosongkan sepenuhnya. Status `DELETED` 
digunakan agar proses pencarian data lain yang menggunakan metode linear probing tetap dapat berjalan dengan benar dan tidak mengganggu jalur pencarian pada hash 
table.

Secara keseluruhan, output program menunjukkan bahwa sistem berhasil menjalankan proses penambahan data, pencarian data, dan penghapusan data menggunakan metode 
open addressing dengan teknik linear probing. Selain itu, output juga memperlihatkan bagaimana kondisi setiap slot pada hash table dapat berubah sesuai dengan 
operasi yang dilakukan oleh sistem.

# e. Link Youtube 
https://youtu.be/EPVxLxAqq1o?si=LkUl1-TIhhHKo9ZH
