## a. Judul Program
Sistem Barang Hilang

## b. Deskripsi Singkat
Program ini dibuat untuk memudahkan pengguna dalam mencatat dan mengelola barang yang hilang. Melalui program ini, pengguna bisa menambahkan barang ke dalam daftar, melihat daftar barang yang sudah dicatat, serta menghapus barang dari daftar ketika barang tersebut sudah ditemukan. Program dijalankan menggunakan menu sederhana sehingga pengguna bisa memilih fitur yang diinginkan dengan mudah.

Struktur data yang digunakan adalah list satu dimensi pada Python. List tersebut berfungsi untuk menyimpan data barang dalam bentuk teks (string). Proses yang dilakukan dalam program ini meliputi penambahan data, penampilan data, dan penghapusan data dengan memanfaatkan fungsi dasar pada list seperti append() dan pop().

## c. Source Code 
<img width="671" height="884" alt="image" src="https://github.com/user-attachments/assets/2da28876-c190-428c-9d23-36fc7903b745" />
<img width="866" height="574" alt="image" src="https://github.com/user-attachments/assets/10a737ed-e46c-4282-8ce8-d0f381338eca" />  

1. Fungsi menu()  
- Digunakan untuk menampilkan pilihan menu ke user yang berisi 4 pilihan yaitu :
- Tampilkan daftar barang
- Tambah barang
- Hapus barang
- Keluar
  
2. Fungsi main()
- Merupakan fungsi utama yang menjalankan seluruh alur program dan memiliki variabel :
- barang (list untuk menyimpan data barang hilang)

3. Perulangan while True
- Digunakan agar program terus berjalan dan akan berhenti jika user memilih menu keluar

4. Menu 1 (Tampilkan daftar barang)
- Mengecek apakah list barang kosong
- Jika kosong akan menampilkan pesan “Belum ada barang”
- Jika tidak kosong akan menampilkan semua barang
- Menggunakan enumerate() untuk memberi nomor urut

5. Menu 2 (Tambah barang)
- User diminta memasukkan nama barang
- Data disimpan ke dalam list menggunakan append()
- strip() digunakan untuk menghapus spasi berlebih
- Menampilkan pesan bahwa barang berhasil ditambahkan

6. Menu 3 (Hapus barang)
- Mengecek apakah list kosong
- Jika tidak kosong akan menampilkan daftar barang
- User memasukkan nomor barang yang ingin dihapus
- Menggunakan pop() untuk menghapus data dari list
- Jika nomor tidak sesuai akan tampil pesan error
- Jika input bukan angka akan ditangani dengan try-except

7. Menu 4 (Keluar)
- Menampilkan pesan “Program selesai”
- Menghentikan perulangan dengan break

8. Pemanggilan main()
- Pemanggilan main() di akhir program berfungsi untuk menjalankan fungsi utama yang telah dibuat

## d. Output Program 
<img width="381" height="878" alt="image" src="https://github.com/user-attachments/assets/310e3ef7-fd7b-4ea9-8fd5-c8b96f6fea92" />
<img width="432" height="834" alt="image" src="https://github.com/user-attachments/assets/623dc0d4-9079-4fea-837d-9daebcaff4cf" />
<img width="322" height="410" alt="image" src="https://github.com/user-attachments/assets/2edf02f9-977f-4e21-82b3-3e220984b684" />

1. Menampilkan daftar awal
- Saat pertama memilih menu 1, program menampilkan pesan “Belum ada barang” karena data masih kosong

2. Menambahkan barang pertama
- user memilih menu 2 dan memasukkan topi
- Program menyimpan data dan menampilkan pesan bahwa barang berhasil ditambahkan

3. Menambahkan barang kedua
- User kembali memilih menu 2 dan memasukkan pena
- Data bertambah, sekarang terdapat dua barang dalam daftar

4. Menampilkan daftar barang
- Saat memilih menu 1, program menampilkan: topi, pena yang artinya data berhasil tersimpan dan ditampilkan dengan nomor urut

5. Percobaan hapus dengan input salah
- User memilih menu 3 lalu memasukkan nomor 3
- Program menolak karena nomor tersebut tidak ada, dan menampilkan “Nomor tidak valid”
  
6. Input menu tidak valid
- User memasukkan huruf c
- Program menampilkan “Pilihan tidak valid” sebagai bentuk validasi input
  
7. Menghapus barang dengan benar
- User memilih menu 3 dan memasukkan nomor 2
- Barang pena berhasil dihapus dari daftar
  
8. Menampilkan daftar setelah penghapusan
- Saat memilih menu 1, program menampilkan hanya topi, artinya data sudah terupdate dengan benar
  
9. Keluar dari program
- User memilih menu 4
- Program menampilkan “Program selesai” dan berhenti berjalan.

## e. Link YouTube 
https://youtu.be/E7UjK65RYcA?si=_wwWXEfJjeNgx_8H
