## a. Judul Program
Pengurutan Prioritas Pengiriman Paket dari Deadline dan Jarak 

## b. Deskripsi Singkat
Program ini dibuat untuk mengatur dan mengurutkan data pengiriman paket berdasarkan dua kriteria, yaitu deadline pengiriman dan jarak tujuan. Data yang dimasukkan berupa nama paket, jumlah hari deadline, dan jarak dalam kilometer. Tujuan dari program ini adalah untuk menentukan prioritas pengiriman agar paket yang lebih cepat harus dikirim terlebih dahulu.

Proses pengurutan dilakukan menggunakan metode insertion sort. Data akan dibandingkan berdasarkan deadline terlebih dahulu, kemudian jika deadline sama maka akan dilihat jaraknya. Hasil akhir dari program ini menampilkan urutan paket dari prioritas tertinggi sampai terendah sehingga lebih mudah dalam menentukan urutan pengiriman.

## c. Source Code 
<img width="899" height="887" alt="image" src="https://github.com/user-attachments/assets/40771734-996e-4e1d-bc76-aea8eaab7b68" />
<img width="858" height="676" alt="image" src="https://github.com/user-attachments/assets/679b7a84-9278-4737-ac3b-092889bda327" />

1. (baris 1) def insertion_sort(deadline, jarak, nama, n):
* Fungsi insertion_sort digunakan untuk mengurutkan data paket menggunakan metode Insertion Sort. Pengurutan dilakukan berdasarkan deadline tercepat terlebih dahulu. Jika terdapat deadline yang sama, maka paket akan diurutkan lagi berdasarkan jarak yang paling dekat. Fungsi ini menerima parameter berupa list deadline, jarak, nama paket, dan jumlah data.

2. (baris 2) for i in range(1, n):
  * Perulangan ini digunakan untuk menjalankan proses sorting dari data kedua sampai data terakhir. Pada metode Insertion Sort, data pertama dianggap sudah berada pada posisi yang benar sehingga pengecekan dimulai dari indeks ke-1.

3. (baris 3-5) temp_deadline = deadline[i], temp_jarak = jarak[i], temp_nama = nama[i]
  * Bagian ini berfungsi untuk menyimpan sementara data yang sedang dibandingkan. Penyimpanan sementara diperlukan agar data tidak hilang ketika proses penggeseran elemen dilakukan selama sorting.

4. (baris 6) j = i - 1
  * Variabel j digunakan untuk mengecek dan membandingkan data sebelumnya dengan data yang sedang diproses.

5. (baris 8-9) while j >= 0 and (deadline[j] > temp_deadline or (deadline[j] == temp_deadline and jarak[j] > temp_jarak)):
  * Perulangan while digunakan untuk membandingkan data saat ini dengan data sebelumnya. Jika deadline sebelumnya lebih besar, maka data akan digeser ke kanan. Jika deadline sama, maka perbandingan dilakukan berdasarkan jarak. Paket dengan jarak lebih dekat akan diprioritaskan berada di depan.

6. (baris 10-12) deadline[j + 1] = deadline[j], jarak[j + 1] = jarak[j], nama[j + 1] = nama[j]
  * Kode ini digunakan untuk menggeser data ke kanan agar tersedia tempat untuk memasukkan data yang sedang diurutkan ke posisi yang sesuai.

7. baris (13) j -= 1
  * Baris ini digunakan untuk memundurkan posisi pengecekan ke data sebelumnya agar proses perbandingan terus berjalan sampai posisi yang tepat ditemukan.

8. (baris 15-17) deadline[j + 1] = temp_deadline, jarak[j + 1] = temp_jarak, nama[j + 1] = temp_nama
  * Setelah posisi yang benar ditemukan, data sementara yang sebelumnya disimpan akan dimasukkan ke posisi tersebut sehingga urutan data menjadi lebih rapi.

9. (baris 20) def main():
  * Fungsi main merupakan fungsi utama yang menjalankan seluruh program. Di dalam fungsi ini terdapat proses input data, penyimpanan data, pemanggilan fungsi sorting, hingga menampilkan hasil akhir.

10. (baris 22) n = int(input("Masukkan jumlah paket: "))
  * Kode ini digunakan untuk meminta pengguna memasukkan jumlah paket yang ingin diinput. Nilai yang dimasukkan kemudian diubah menjadi tipe data integer.

11. (baris 23) except ValueError:
  * Bagian ini berfungsi untuk menangani kesalahan input apabila pengguna memasukkan data selain angka. Program akan menampilkan pesan bahwa input tidak valid sehingga program tidak langsung error.

12. (baris 27-29) nama = [], deadline = [], jarak = []
  * Kode ini digunakan untuk membuat list kosong yang nantinya dipakai menyimpan data nama paket, deadline, dan jarak.

13. (baris 32) for i in range(n):
  * Perulangan ini digunakan untuk melakukan input data paket sebanyak jumlah paket yang telah dimasukkan sebelumnya.

14. (baris 35) nama.append(input("Nama paket: "))
  * Bagian ini digunakan untuk menerima input nama paket dari pengguna lalu menyimpannya ke dalam list nama.

15. (baris 37) while True:
  * Perulangan while True digunakan agar program terus meminta input sampai pengguna memasukkan data yang benar.

16. (baris 39-40) d = int(input("Deadline (hari): ")), deadline.append(d)
  * Kode ini digunakan untuk menerima input deadline paket dalam satuan hari lalu menyimpannya ke dalam list deadline.

17. (baris 47-48) j = int(input("Jarak (km): ")), jarak.append(j)
  * Bagian ini digunakan untuk menerima input jarak pengiriman paket dalam kilometer kemudian menyimpannya ke list jarak.

18. (baris 53) print("\nData sebelum diurutkan:")
  * Kode ini digunakan untuk menampilkan judul data sebelum dilakukan proses sorting.

19. (baris 55) print(nama[i], "dalam", deadline[i], "hari dengan jarak", jarak[i], "km")
  * Bagian ini digunakan untuk menampilkan seluruh data paket satu per satu beserta deadline dan jaraknya.

20. (baris 57) insertion_sort(deadline, jarak, nama, n)
  * Kode ini digunakan untuk memanggil fungsi insertion_sort agar data paket dapat diurutkan sesuai aturan yang telah dibuat.

21. (baris 59) print("\nData setelah diurutkan (Insertion Sort):")
  * Bagian ini digunakan untuk menampilkan hasil data setelah proses pengurutan selesai dilakukan.

22. (baris 64) if __name__ == "__main__":
  * Kode ini digunakan agar fungsi main() hanya dijalankan ketika file Python dieksekusi secara langsung, bukan ketika file dijadikan module atau di-import ke program lain.

23. (baris 65) main()
  * Baris terakhir ini digunakan untuk memanggil fungsi main() sehingga seluruh program dapat dijalankan.

## d. Output Program 
<img width="557" height="310" alt="image" src="https://github.com/user-attachments/assets/24f983b2-92f7-40b6-bac5-eb1e9275692f" />

1. Baris pertama menampilkan “Deadline (hari): 1” yang berarti program menerima atau menggunakan nilai deadline sebesar 1 hari sebagai batas waktu.
2. Baris kedua menampilkan “Jarak (km): 10” yang menunjukkan bahwa nilai jarak yang digunakan atau dijadikan acuan adalah 10 km.
3. Baris ketiga menampilkan “Data sebelum diurutkan:” yang menandakan bahwa data yang akan ditampilkan berikutnya masih dalam kondisi awal, belum melalui proses pengurutan.
4. Baris keempat menjelaskan data pertama yaitu Rina dengan waktu 2 hari dan jarak 9 km, sesuai dengan urutan input awal.
5. Baris kelima menjelaskan data kedua yaitu Rahma dengan waktu 2 hari dan jarak 5 km, juga masih mengikuti urutan awal.
6. Baris keenam menjelaskan data ketiga yaitu Keisha dengan waktu 1 hari dan jarak 10 km, melengkapi data sebelum diurutkan.
7. Baris ketujuh menampilkan “Data setelah diurutkan (Insertion Sort):”, menandakan bahwa data berikutnya sudah melalui proses pengurutan menggunakan metode insertion sort.
8. Baris kedelapan menunjukkan Keisha berada di posisi pertama karena memiliki waktu paling kecil yaitu 1 hari, sehingga diprioritaskan dalam hasil sorting.
9. Baris kesembilan menunjukkan Rahma berada di posisi kedua karena meskipun waktunya sama dengan Rina yaitu 2 hari, jaraknya lebih dekat yaitu 5 km.
10. Baris kesepuluh menunjukkan Rina berada di posisi terakhir karena memiliki waktu yang sama dengan Rahma tetapi jaraknya lebih jauh yaitu 9 km.

## e. Link YouTube 
https://youtu.be/oz86FHpp7io?si=IxjYCsSLzKst3D6Y
