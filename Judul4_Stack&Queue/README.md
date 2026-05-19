## a. Judul Program 
Nomor Antrean Kantin 

## b. Deskripsi Singkat 
Program ini digunakan untuk mengatur nomor antrean kantin agar proses pelayanan dapat berjalan dengan lebih tertib dan teratur. Nomor antrean yang masuk akan disimpan berdasarkan urutan kedatangan sehingga pelanggan yang datang lebih dahulu akan dilayani terlebih dahulu. Program ini memiliki beberapa fungsi seperti menambahkan nomor antrean, menghapus antrean yang sudah selesai dilayani, melihat nomor antrean paling depan, serta menampilkan seluruh data antrean yang tersedia.

Struktur data yang diterapkan pada program ini adalah Queue dengan metode Linked List. Queue bekerja menggunakan konsep FIFO (First In First Out) yaitu data yang pertama masuk akan diproses lebih dahulu dibandingkan data yang masuk setelahnya. Penggunaan Linked List membantu proses pengelolaan data antrean menjadi lebih fleksibel karena data dapat ditambah maupun dihapus tanpa harus menentukan kapasitas data sejak awal.

## c. Source Code 
<img width="680" height="892" alt="image" src="https://github.com/user-attachments/assets/03be54f7-14cb-4313-a2f1-c0c8c8b701e4" />
<img width="666" height="843" alt="image" src="https://github.com/user-attachments/assets/5795a2de-6a0f-4791-877d-54b2d28fd587" />
<img width="688" height="792" alt="image" src="https://github.com/user-attachments/assets/2c296eca-7ae8-448a-93a6-4b07bf51c054" />

1. *(baris 1)* class Node:
* Baris 1 digunakan untuk membuat class Node sebagai dasar pembentukan Linked List.

2. *(baris2)* 2 def __init__(self, data):
* Baris 2 digunakan untuk membuat constructor pada class Node.

3. *(baris 3)* self.data = data
* Baris 3 digunakan untuk menyimpan data ke dalam node.

4. *(baris 4)* self.next = None
* Baris 4 digunakan untuk menghubungkan node ke node berikutnya dan diberi nilai awal None.

5. *(baris 7)* class QueueLinkedList:
* Baris 7 digunakan untuk membuat class Queue dengan metode Linked List.

 6. *(baris 8)* def __init__(self):
* Baris 8 digunakan untuk membuat constructor pada class queue.

7. *(baris 9)* self.front_ptr = None
* Baris 9 digunakan untuk membuat pointer depan antrean.

8. *(baris 10)* self.rear_ptr = None
* Baris 10 digunakan untuk membuat pointer belakang antrean.

9. *(baris 12)* def is_empty(self):
* Baris 12 digunakan untuk membuat method pengecekan queue kosong.

10. *(baris 13)* return self.front_ptr is None
* Baris 13 digunakan untuk mengembalikan nilai True jika queue kosong.

11. *(baris 15)* def enqueue(self, x):
* Baris 15 digunakan untuk membuat method penambahan data antrean.

12. *(baris 16)* new_node = Node(x)
* Baris 16 digunakan untuk membuat node baru dari input pengguna.

13. *(baris 18)* if self.is_empty():
* Baris 18 digunakan untuk mengecek apakah antrean kosong.

14. *(baris 19)* self.front_ptr = new_node
* Baris 19 digunakan untuk menjadikan node baru sebagai antrean depan.

15. *(baris 20)* self.rear_ptr = new_node
* Baris 20 digunakan untuk menjadikan node baru sebagai antrean belakang.

16. *(baris 21)* else:
* Baris 21 dijalankan jika antrean tidak kosong.

17. *(baris 22)* self.rear_ptr.next = new_node
* Baris 22 digunakan untuk menghubungkan node terakhir dengan node baru.

18. *(baris 23)* self.rear_ptr = new_node
* Baris 23 digunakan untuk memindahkan pointer belakang ke node baru.

19. *(baris 25)* print(f"Nomor antrean {x} berhasil ditambahkan")
* Baris 25 digunakan untuk menampilkan pesan bahwa data berhasil ditambahkan.

20. *(baris 27)* def dequeue(self):
* Baris 27 digunakan untuk membuat method penghapusan antrean depan.

21. *(baris 28)* if self.is_empty():
* Baris 28 digunakan untuk mengecek apakah antrean kosong.

22. *(baris 29)* print("Antrean kantin kosong")
* Baris 29 digunakan untuk menampilkan pesan antrean kosong.

23. *(baris 30)* return
* Baris 30 digunakan untuk menghentikan proses jika antrean kosong.

24. *(baris 32)* temp = self.front_ptr
* Baris 32 digunakan untuk menyimpan data antrean paling depan sementara.

25. *(baris 33)* print(f"Nomor antrean {temp.data} selesai dilayani")
* Baris 33 digunakan untuk menampilkan antrean yang selesai dilayani.

26. *(baris 35)* self.front_ptr = self.front_ptr.next
* Baris 35 digunakan untuk memindahkan pointer depan ke node berikutnya.

27. *(baris 37)* if self.front_ptr is None:
* Baris 37 digunakan untuk mengecek apakah antrean sudah kosong.

28. *(baris 38)* self.rear_ptr = None
* Baris 38 digunakan untuk mengosongkan pointer belakang jika antrean habis.

29. *(baris 40)* def peek(self):
* Baris 40 digunakan untuk membuat method melihat antrean depan.

30. *(baris 41)* if self.is_empty():
* Baris 41 digunakan untuk mengecek apakah antrean kosong.

31. *(baris 42)* print("Antrean kantin kosong")
* Baris 42 digunakan untuk menampilkan pesan antrean kosong.

31. *(baris 43)* return
* Baris 43 digunakan untuk menghentikan proses jika antrean kosong.

32. *(baris 45)* print(f"Antrean paling depan: {self.front_ptr.data}")
* Baris 45 digunakan untuk menampilkan data antrean paling depan.

33. *(baris 47)* def display(self):
* Baris 47 digunakan untuk membuat method menampilkan seluruh antrean.

34. *(baris 48)* if self.is_empty():
* Baris 48 digunakan untuk mengecek apakah antrean kosong.

35. *(baris 49)* print("Antrean kantin kosong")
* Baris 49 digunakan untuk menampilkan pesan antrean kosong.

36. *(baris 50)* return
* Baris 50 digunakan untuk menghentikan proses jika antrean kosong.

37. *(baris 52)* print("Isi antrean kantin:", end=" ")
* Baris 52 digunakan untuk menampilkan judul antrean.

38. *(baris 54)* current = self.front_ptr
* Baris 54 digunakan untuk menyimpan posisi awal antrean.

39. *(baris 56)* while current is not None:
* Baris 56 digunakan untuk melakukan perulangan selama data masih ada.

40. *(baris 57)* print(current.data, end=" ")
* Baris 57 digunakan untuk menampilkan data antrean.

41. *(baris 58)* current = current.next
* Baris 58 digunakan untuk berpindah ke node berikutnya.

42. *(baris 60)* print()
* Baris 60 digunakan untuk membuat baris baru setelah antrean selesai ditampilkan.

43. *(baris 63)* def main():
* Baris 63 digunakan untuk membuat fungsi utama program.

44. *(baris 64)* queue = QueueLinkedList()
* Baris 64 digunakan untuk membuat objek queue.

45. *(baris 65)* pilih = 0
* Baris 65 digunakan untuk memberi nilai awal pada variabel pilihan menu.

46. *(baris 67)* while pilih != 5:
* Baris 67 digunakan untuk menjalankan program selama pengguna belum memilih keluar.

47. *(baris 68)* print("\nSISTEM ANTREAN KANTIN")
* Baris 68 digunakan untuk menampilkan judul program.

48. *(baris 69)* print("1. Tambah Antrean")
* Baris 69 digunakan untuk menampilkan menu tambah antrean.

49. *(baris 70)* print("2. Layani Antrean")
* Baris 70 digunakan untuk menampilkan menu melayani antrean.

50. *(baris 71)* print("3. Lihat Antrean Depan")
* Baris 71 digunakan untuk menampilkan menu melihat antrean depan.

51. *(baris 72)* print("4. Tampilkan Antrean")
* Baris 72 digunakan untuk menampilkan menu melihat seluruh antrean.

52. *(baris 73)* print("5. Keluar")
* Baris 73 digunakan untuk menampilkan menu keluar program.

53. *(baris 75)* try:
* Baris 75 digunakan untuk menangani kemungkinan error input.

54. *(baris 76)* pilih = int(input("Pilih menu: "))
* Baris 76 digunakan untuk menerima input menu dari pengguna.

55. *(baris 77)* except ValueError:
* Baris 77 digunakan untuk menangkap error jika input bukan angka.

56. *(baris 78)* print("Input tidak valid!")
* Baris 78 digunakan untuk menampilkan pesan kesalahan input.

57. *(baris 79)* continue
* Baris 79 digunakan untuk mengulangi program ke menu utama.

58. *(baris 81)*  if pilih == 1:
* Baris 81 digunakan untuk mengecek apakah pengguna memilih menu tambah antrean.

59. *(baris 82)* try:
* Baris 82 digunakan untuk menangani error input angka.

60. *(baris 83)* nomor = int(input("Masukkan nomor antrean: "))
* Baris 83 digunakan untuk menerima input nomor antrean.

61. *(baris 84)* queue.enqueue(nomor)
* Baris 84 digunakan untuk menambahkan data ke antrean.

62. *(baris 85)* except ValueError:
* Baris 85 digunakan untuk menangkap kesalahan input.

63. *(baris 86)* print("Input harus angka!")
* Baris 86 digunakan untuk menampilkan pesan jika input bukan angka.

64. *(baris 88)* elif pilih == 2:
* Baris 88 digunakan untuk mengecek menu dequeue.

65. *(baris 89)* queue.dequeue()
* Baris 89 digunakan untuk menghapus antrean depan.

66. *(baris 91)* elif pilih == 3:
* Baris 91 digunakan untuk mengecek menu peek.

67. *(baris 92)* queue.peek()
* Baris 92 digunakan untuk melihat antrean paling depan.

68. *(baris 94)* elif pilih == 4:
* Baris 94 digunakan untuk mengecek menu display.

69. *(baris 95)* queue.display()
* Baris 95 digunakan untuk menampilkan seluruh antrean.

70. *(baris 97)* elif pilih == 5:
* Baris 97 digunakan untuk mengecek menu keluar.

71. *(baris 98)* print("Program selesai.")
* Baris 98 digunakan untuk menampilkan pesan program selesai.

72. *(baris 100)* else:
* Baris 100 digunakan jika pilihan menu tidak tersedia.

73. *(baris 101)* print("Pilihan tidak valid!")
* Baris 101 digunakan untuk menampilkan pesan kesalahan menu.

74. *(baris 104)* if __name__ == "__main__":
* Baris 104 digunakan untuk menjalankan program utama.

75. *(baris 105)* main()
* Baris 105 digunakan untuk memanggil fungsi main().

## d. Output Program 
<img width="412" height="852" alt="image" src="https://github.com/user-attachments/assets/91c44cfd-8ce2-4018-9522-fa492df22411" />
<img width="407" height="773" alt="image" src="https://github.com/user-attachments/assets/a7dbf699-00a8-4889-a4b7-cba8245fe675" />

1. SISTEM ANTREAN KANTIN
* Menampilkan judul program antrean kantin.

2. 1. Tambah Antrean, 2. Layani Antrean, 3. Lihat Antrean Depan, 4. Tampilkan Antrean, 5. Keluar
* Menampilkan daftar menu yang bisa dipilih pengguna.

3. Pilih menu: 1
* User memilih menu 1 untuk menambah antrean.

4. Masukkan nomor antrean: 2
* User memasukkan nomor antrean 2.

5. Nomor antrean 2 berhasil ditambahkan
* Program berhasil menambahkan nomor 2 ke dalam antrean.

6. Pilih menu: 1
*  User kembali memilih menu tambah antrean.
  
7. Masukkan nomor antrean: 4
* User memasukkan nomor antrean 4.

8. Nomor antrean 4 berhasil ditambahkan
* Nomor 4 berhasil masuk ke antrean.

9. Pilih menu: 1
* User memilih tambah antrean lagi.

10. Masukkan nomor antrean: 6
* User memasukkan nomor antrean 6.

11. Nomor antrean 6 berhasil ditambahkan
* Nomor 6 berhasil ditambahkan ke antrean.

12. Pilih menu: 4
* User memilih menu untuk menampilkan seluruh isi antrean.

13. Isi antrean kantin: 2 4 6
* Program menampilkan semua antrean yang ada, yaitu 2, 4, dan 6 sesuai urutan masuk.

14. Pilih menu: 2
* User memilih menu layani antrean.

15. Nomor antrean 2 selesai dilayani
* Program mengambil antrean paling depan yaitu nomor 2 lalu menghapusnya dari antrean karena sudah dilayani.

16. Pilih menu: 4
* User kembali memilih tampilkan antrean.

17. Isi antrean kantin: 4 6
* Isi antrean sekarang tinggal 4 dan 6 karena nomor 2 sudah dilayani.

18. Pilih menu: 3
* User memilih melihat antrean paling depan.

19. Antrean paling depan: 4
* Program menampilkan nomor antrean yang berada di posisi terdepan, yaitu 4.

20. Pilih menu: 5
* User memilih keluar dari program.

21. Program selesai.
* Program berhenti dijalankan.

## e. Link YouTube
https://youtu.be/9pp3rQwoZao?si=bDZzHUEc-duelHqT

































