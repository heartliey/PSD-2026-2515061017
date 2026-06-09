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

Pada sistem ini, `class SlotState` digunakan untuk memberikan penanda kondisi pada setiap slot di dalam hash table. Terdapat tiga kondisi yang digunakan, yaitu 
`EMPTY`, `OCCUPIED`, dan `DELETED`. Kondisi `EMPTY` menunjukkan bahwa slot masih kosong dan belum pernah digunakan. Kondisi `OCCUPIED` menunjukkan bahwa slot
sudah berisi data mahasiswa. Sementara itu, kondisi `DELETED` digunakan untuk menandai bahwa data pada slot tersebut telah dihapus, namun slot tetap dipertahankan
agar proses pencarian data pada metode open addressing tetap berjalan dengan baik dan tidak merusak jalur pencarian data lainnya.

Selanjutnya, `class Entry` digunakan sebagai tempat penyimpanan data pada setiap slot hash table. Pada bagian ini terdapat atribut `nim`, `nilai`, dan `state`. 
Variabel `nim` digunakan untuk menyimpan nomor induk mahasiswa, variabel `nilai` digunakan untuk menyimpan nilai mahasiswa, sedangkan `state` digunakan untuk 
menyimpan kondisi slot berdasarkan `SlotState`. Pada saat objek `Entry` dibuat, seluruh data akan bernilai kosong dan status awal slot berada pada kondisi `EMPTY`.

Bagian utama sistem terdapat pada `class HashMapOpenAddressing`. Kelas ini digunakan untuk mengatur seluruh proses pengolahan data pada hash map menggunakan 
metode open addressing dengan teknik linear probing. Pada fungsi `__init__(self, size=10)`, sistem akan menentukan ukuran hash table melalui variabel `SIZE`. 
Selain itu, sistem juga membuat tabel kosong menggunakan:

```python id="g2m8vp"
self.table = [Entry() for _ in range(self.SIZE)]
```

Kode tersebut digunakan untuk membuat sejumlah slot kosong sesuai ukuran hash table yang telah ditentukan.

Fungsi `hash_function(self, key)` digunakan untuk menentukan posisi awal penyimpanan data pada hash table. Fungsi ini menggunakan operasi modulus berikut : 

```python id="p7v4rt"
return key % self.SIZE
```

Operasi tersebut bertujuan untuk menghasilkan indeks penyimpanan data berdasarkan nilai NIM mahasiswa. Dengan cara ini, data dapat disimpan secara lebih terstruktur dan
proses pencarian dapat dilakukan dengan lebih cepat.

Fungsi `insert(self, nim, nilai)` digunakan untuk menambahkan data mahasiswa ke dalam hash table. Pertama, sistem akan mencari indeks awal menggunakan fungsi hash berikut : 

```python id="u3k9ns"
idx = self.hash_function(nim)
```

Setelah itu, sistem akan memeriksa kondisi slot pada indeks tersebut. Jika slot masih kosong, maka data langsung disimpan. Namun, apabila slot sudah terisi dan 
\terjadi collision, sistem akan menggunakan metode linear probing untuk mencari slot kosong berikut diantaranya : 

```python id="x6q2ld"
i = (idx + step) % self.SIZE
```

Proses ini dilakukan secara berulang hingga ditemukan slot kosong. Setelah slot ditemukan, data mahasiswa disimpan dan dapat dilihat seperti berikut : 

```python id="m5r8tc"
self.table[i].nim = nim
self.table[i].nilai = nilai
self.table[i].state = SlotState.OCCUPIED
```

Kode tersebut digunakan untuk memasukkan NIM, nilai mahasiswa, dan mengubah status slot menjadi `OCCUPIED`.

Fungsi `search(self, nim)` digunakan untuk mencari data mahasiswa berdasarkan NIM. Sistem akan mencari indeks awal menggunakan fungsi hash, kemudian melakukan 
pemeriksaan pada setiap slot. Jika ditemukan slot dengan kondisi `EMPTY`, maka pencarian dihentikan karena data dianggap tidak tersedia. Namun, apabila slot 
berisi data dan NIM sesuai dengan data yang dicari, maka data tersebut akan dikembalikan sebagai hasil pencarian.

Fungsi `remove_key(self, nim)` digunakan untuk menghapus data mahasiswa dari hash table. Pada fungsi ini, sistem terlebih dahulu mencari data menggunakan 
fungsi `search()`. Jika data ditemukan, maka status slot akan diubah menjadi `DELETED` yaitu : 

```python id="b8t1qy"
data.state = SlotState.DELETED
```

Penggunaan status `DELETED` bertujuan agar slot tetap dapat dikenali dalam proses pencarian data lainnya dan tidak mengganggu proses linear probing.

Fungsi `display(self)` digunakan untuk menampilkan seluruh isi hash table. Sistem akan menampilkan kondisi setiap slot satu per satu. Jika slot kosong, sistem akan 
menampilkan tulisan `EMPTY`. Jika slot telah dihapus, sistem akan menampilkan `DELETED`. Sedangkan apabila slot berisi data mahasiswa, maka sistem akan menampilkan
NIM dan nilai mahasiswa yang tersimpan pada slot tersebut.

Pada bagian `main()`, sistem menjalankan seluruh fungsi utama yang terdapat pada hash map. Sistem akan membuat objek hash map terlebih dahulu, kemudian menambahkan
beberapa data mahasiswa menggunakan fungsi `insert()`. Setelah itu, sistem melakukan pencarian data menggunakan fungsi `search()`, menghapus data menggunakan 
fungsi `remove_key()`, dan menampilkan seluruh isi hash table menggunakan fungsi `display()`. Bagian ini menjadi pusat eksekusi sistem karena seluruh proses 
dijalankan melalui fungsi `main()`.

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
