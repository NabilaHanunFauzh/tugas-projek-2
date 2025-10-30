# Student Performance Tracker

**Student Performance Tracker** merupakan sebuah aplikasi berbasis **Command Line Interface (CLI)** yang dirancang untuk membantu dalam pengelolaan data kehadiran serta nilai mahasiswa.  
Program ini memudahkan pengguna dalam melakukan pencatatan, pembaruan, dan penilaian secara terstruktur, sekaligus menyediakan fitur untuk menyimpan hasil rekap dalam format **Markdown**.

---

## File Laporan
File laporan hasil rekap nilai secara otomatis akan disimpan di:
out/report.md

---

## Menu Utama Aplikasi
Aplikasi ini memiliki beberapa menu utama yang dapat digunakan untuk mengelola data mahasiswa, yaitu:

1. **Muat data dari CSV** – Mengimpor data kehadiran dan nilai mahasiswa dari file CSV.  
2. **Tambah mahasiswa** – Menambahkan data mahasiswa baru ke dalam sistem.  
3. **Ubah presensi** – Mengedit atau memperbarui persentase kehadiran mahasiswa.  
4. **Ubah nilai** – Memasukkan dan memperbarui nilai berdasarkan komponen penilaian.  
5. **Lihat rekap** – Menampilkan rekapitulasi nilai akhir serta status kehadiran seluruh mahasiswa.  
6. **Simpan laporan Markdown** – Membuat laporan rekap nilai dalam format Markdown (`report.md`) untuk dokumentasi.  
7. **Keluar** – Menutup program.

---

## Komponen Penilaian
Dalam proses perhitungan nilai akhir, aplikasi ini menggunakan empat komponen utama dengan bobot tertentu, yaitu:

- **Quiz**
- **Tugas**
- **UTS**
- **UAS**

Keempat komponen tersebut digunakan sebagai dasar perhitungan nilai akhir agar hasil penilaian lebih **objektif**, **akurat**, dan mencerminkan **performa akademik mahasiswa secara menyeluruh**.

---

## Manfaat Aplikasi
Dengan adanya **Student Performance Tracker**, proses pengelolaan data akademik menjadi:

- Lebih **efisien** karena semua data tersimpan dalam satu sistem.
- Lebih **terorganisir** dengan struktur yang mudah diakses.
- Lebih **cepat dan tepat** dalam menyusun laporan hasil penilaian mahasiswa.

---

## Cara Menjalankan Program
1. Pastikan **Python 3.8+** sudah terinstal di perangkat Anda.  
2. Buka terminal dan arahkan ke folder proyek:  
cd student_performance_tracker
3. Jalankan perintah berikut:
python app.py
4. Pilih menu yang diinginkan untuk mulai mengelola data mahasiswa.
5. Setelah selesai, laporan rekap nilai dapat dilihat di:
out/report.md

---

## ✨ Kesimpulan
Dengan adanya **Student Performance Tracker**, pengelolaan data akademik menjadi lebih efisien, terorganisir, dan mudah digunakan.  
Aplikasi ini membantu pengguna dalam menyusun laporan penilaian mahasiswa secara cepat, tepat, dan dapat disimpan secara otomatis dalam format Markdown untuk dokumentasi akademik.