## a. Judul Program 
Pencarian Nomor Antrian Klinik 

## b. Deskripsi Singkat 
Program ini digunakan untuk mencari nomor antrian pasien di klinik dengan lebih cepat dan teratur. Pengguna dapat memasukkan data berupa nomor antrian beserta nama pasien, kemudian program akan menampilkan daftar tersebut. Selanjutnya, pengguna dapat mencari nomor antrian tertentu dan program akan menampilkan hasilnya jika data ditemukan. Dengan adanya program ini, proses pencarian menjadi lebih praktis dibandingkan harus memeriksa data satu per satu secara manual.

Pada  proses pencarian atau searching, program ini menggunakan metode pencarian Binary Search. Metode ini bekerja pada data yang sudah diurutkan dengan cara membagi data menjadi dua bagian, lalu membandingkan nilai tengah dengan data yang dicari. Jika nilai yang dicari lebih besar maka pencarian dilanjutkan ke bagian kanan. Sedangkan jika lebih kecil akan dilanjutkan ke bagian kiri. Proses ini dilakukan berulang hingga data ditemukan atau tidak ditemukan, sehingga pencarian menjadi lebih efisien dibandingkan metode pencarian biasa.

## c. Source Code 
<img width="810" height="882" alt="image" src="https://github.com/user-attachments/assets/04bb8841-ee3c-4f8e-9eff-53d2dd572b32" />
<img width="864" height="602" alt="image" src="https://github.com/user-attachments/assets/1572b887-fe3f-4db9-9e69-c7d1d008ef88" />

1. *(baris 1)* def binary_search(arr, n, target):
* Baris ini mendefinisikan fungsi binary_search yang digunakan untuk mencari nomor antrian berdasarkan nilai yang dicari.

2. *(baris 2)* l = 0
* Baris ini berfungsi mengatur batas kiri pencarian yang dimulai dari indeks pertama data.

3. *(baris 3)* r = n - 1
* Lalu, pada baris ini mengatur batas kanan pencarian yang merupakan indeks terakhir dari data.

4. *(baris 4)* pos = -1
* Berfungsi membuat variabel pos dengan nilai awal -1 sebagai penanda bahwa data belum ditemukan.

5. *(baris 5)* while l <= r:
* Baris ini merupakan perulangan yang akan berjalan selama batas kiri belum melewati batas kanan.

6. *(baris 6)* m = l + (r - l) // 2
* Baris ini menghitung posisi tengah dari data untuk menentukan elemen yang akan diperiksa.

7. *(baris 7)* print(f"Median: {m}, nomor antrian: {arr[m]}")
* Baris ini berfungsi menampilkan indeks tengah dan nilai nomor antrian yang sedang dicek.

8. *(baris 8)* if arr[m] == target:
* Dilakukan pengecekan apakah nilai tengah sama dengan nilai yang dicari.

9. *(baris 9)* pos = m
* Jika nilai tengah sama, posisi data disimpan ke dalam variabel pos.

10. *(baris 10)* break
* Proses pencarian dihentikan karena data sudah ditemukan.

11. *(baris 11)* elif arr[m] < target:
* Jika nilai tengah lebih kecil dari target, berarti pencarian harus dilanjutkan.

12. *(baris 12)* print("Mencari di kanan")
* Ditampilkan informasi bahwa pencarian berpindah ke bagian kanan.

13. *(baris 13)* l = m + 1
* Batas kiri akan digeser ke posisi setelah tengah.

14. *(baris 14)* else:
* Kondisi ini dijalankan jika nilai tengah lebih besar dari target.

15. *(baris 15)* print("Mencari di kiri")
* Ditampilkan bahwa pencarian dilakukan ke bagian kiri.

16. *(baris 16)* r = m - 1
* Batas kanan akan digeser ke posisi sebelum tengah.

17. *(baris 17)* return pos
* Hasil pencarian dikembalikan yaitu berupa posisi data maupun -1 jika tidak ditemukan.

18. *(baris 20)* def main():
* Fungsi utama dibuat untuk mengatur jalannya program secara keseluruhan.

19. *(baris 21)* try:
* Blok percobaan yang digunakan untuk mengantisipasi adanya kesalahan input.

20. *(baris 22)* n = int(input("Masukkan jumlah pasien: "))
* Pengguna diminta memasukkan jumlah pasien dalam bentuk angka.

21. *(baris 23)* except ValueError:
* Jika input bukan angka maka kondisi ini akan dijalankan.

22. *(baris 24)* print("Input tidak valid!")
* Pesan kesalahan ditampilkan agar pengguna mengetahui input tidak sesuai.

23. *(baris 25)* return
* Program dihentikan karena terjadi kesalahan dalam input.

24. *(baris 27)* arr = []
* List kosong disiapkan untuk menyimpan nomor antrian.

25. *(baris 28)* pasien = []
* List kosong lain disiapkan untuk menyimpan nama pasien.

26. *(baris 30)* print("Masukkan data nomor antrian dan nama pasien (urut menaik):")
* Instruksi diberikan agar pengguna memasukkan data nomor antrian dan nama pasien secara berurutan dari rendah ke tinggi.

27. *(baris 31)* for i in range(n):
* Perulangan dilakukan sebanyak jumlah pasien yang diinput.

28. *(baris 32)* while True:
* Perulangan tambahan digunakan agar input tetap diminta sampai benar.

29. *(baris 33)* try:
* Blok percobaan yang digunakan untuk menghindari kesalahan saat input.

30. *(baris 34)* nomor = int(input(f"Nomor antrian ke-{i+1}: "))
* Nomor antrian diminta atau dimasukan oleh pengguna dalam bentuk angka.

31. *(baris 35)* nama = input("Nama pasien: ")
* Nama pasien diinput oleh pengguna.

32. *(baris 36)* arr.append(nomor)
* Nomor antrian disimpan ke dalam list arr.

33. *(baris 37)* pasien.append(nama)
* Nama pasien disimpan ke dalam list pasien.

34. *(baris 38)* break
Perulangan akan dihentikan jika input sudah benar.

35. *(baris 39)* except ValueError:
* Kondisi ini digunakan untuk menangani kesalahan jika nomor yang diinput bukan angka.

36. *(baris 40)* print("Input tidak valid, silakan masukkan angka!")
* Pesan kesalahan akan ditampilkan kepada pengguna.

37. *(baris 42)* print("\nData Antrian:")
* Judul data antrian ditampilkan sebelum daftar ditunjukkan.

38. *(baris 43)* for i in range(n):
* Perulangan dilakukan untuk menampilkan seluruh data.

39. *(baris 44)* print(f"{arr[i]} ({pasien[i]})")
* Nomor antrian dan nama pasien ditampilkan dengan format menggunakan kurung.

40. *(baris 46)* while True:
* Perulangan digunakan untuk memastikan input pencarian valid.

41. *(baris 47)*  try:
* Blok percobaan kembali digunakan untuk menghindari kesalahan input.

42. *(baris 48)* target = int(input("\nMasukkan nomor antrian yang ingin dicari: "))
* Nomor antrian yang ingin dicari dimasukkan oleh pengguna.

43. *(baris 49)* break
* Perulangan dihentikan jika input sudah benar.

44. *(baris 50)* except ValueError:
* Kondisi ini akan dijalankan jika input tidak sesuai.

45. *(baris 51)* print("Input tidak valid, silakan masukkan angka!")
* Pesan kesalahan tersebut akan ditampilkan.

46. *(baris 53)* pos = binary_search(arr, n, target)
* Fungsi binary search dipanggil untuk mencari data sesuai input.

47. *(baris 55)* if pos != -1:
* Dilakukan pengecekan apakah data ditemukan atau tidak.

48. *(baris 56)* print(f"\nNomor antrian ditemukan: {target} ({pasien[pos]})")
* Jika ditemukan, nomor antrian dan nama pasien ditampilkan.

49. *(baris 57)* else:
* Kondisi ini dijalankan jika data tidak ditemukan.

50. *(baris 58)* print("\nNomor antrian tidak ditemukan")
* Pesan bahwa data tidak ditemukan

51. *(baris 61)* if __name__ == "__main__":
* Bagian ini memastikan program dijalankan sebagai program utama.

52. *(baris 62)* main()
* Fungsi main() dipanggil untuk menjalankan seluruh program.

## d. Output Program 
<img width="552" height="447" alt="image" src="https://github.com/user-attachments/assets/c0cf3257-0d43-44ff-aedd-0adfbb495435" />

1. *(baris 1)* Masukkan jumlah pasien: 3
* Pada bagian ini pengguna diminta untuk memasukkan jumlah data pasien yang akan diolah oleh program. Angka 3 menunjukkan bahwa akan ada tiga data pasien yang dimasukkan ke dalam sistem.

2. *(baris 2)* Masukkan data nomor antrian dan nama pasien (urut menaik):
* Program memberikan instruksi kepada pengguna untuk memasukkan data nomor antrian beserta nama pasien. Ditegaskan bahwa nomor antrian harus dimasukkan secara urut menaik karena metode binary search membutuhkan data yang sudah terurut.

3. *(baris 3-4)* Nomor antrian ke-1: 8 dan Nama pasien: Isa
* Pengguna memasukkan data pasien pertama yaitu nomor antrian 8 dengan nama Isa. Data ini kemudian disimpan ke dalam list nomor antrian dan list nama pasien.

4. *(baris 5-6)* Nomor antrian ke-2: 15 dan Nama pasien: Cas
* Selanjutnya dimasukkan data pasien kedua dengan nomor antrian 15 dan nama Cas, yang juga disimpan ke dalam struktur data yang sama.

5. *(baris 7-8)* Nomor antrian ke-3: 24 dan Nama pasien: Seo
* Data pasien ketiga dimasukkan dengan nomor antrian 24 dan nama Seo, melengkapi seluruh data sesuai jumlah yang telah ditentukan sebelumnya.

6. *(baris 9)* Data Antrian:
* Program menampilkan judul sebagai penanda bahwa seluruh data yang telah dimasukkan akan ditampilkan kembali kepada pengguna.

7. *(baris 10-12)* 8 (Isa), 15 (Cas), dan 24 (Seo)
* Seluruh data antrian ditampilkan dalam format nomor antrian diikuti nama pasien dalam tanda kurung. Hal ini memudahkan pengguna untuk melihat kembali data yang sudah tersimpan sebelum melakukan pencarian.

8. *(baris 13)* Masukkan nomor antrian yang ingin dicari: 24
* Pengguna diminta memasukkan nomor antrian yang ingin dicari dalam data. Pada contoh ini, pengguna memilih mencari nomor 24.

9. *(baris 14)* Median: 1, nomor antrian: 15
* Program mulai melakukan proses binary search dengan mengambil nilai tengah dari data. Indeks tengah berada pada posisi 1 dengan nilai nomor antrian 15, yang kemudian dibandingkan dengan nilai yang dicari.

10. *(baris 15)* Mencari di kanan
* Karena nilai 15 lebih kecil dari 24 maka pencarian dilanjutkan ke bagian kanan dari data, yaitu bagian yang memiliki nilai lebih besar.

11. *(baris 16)* Median: 2, nomor antrian: 24
* Program kembali menentukan nilai tengah pada bagian kanan yaitu indeks 2 dengan nilai 24, lalu membandingkannya dengan target.

12. *(baris 17)* Nomor antrian ditemukan: 24 (Seo)
* Nilai yang dicari berhasil ditemukan. Program kemudian menampilkan nomor antrian 24 beserta nama pasien Seo, sehingga pengguna mengetahui hasil pencarian dengan jelas.

## e. Link YouTube
https://youtu.be/wfpfli6eUa4?si=zWvXkVa37RlgWPGR
