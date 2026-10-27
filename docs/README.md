# Panduan Praktik Analisis Forensik Media Penyimpanan dengan FTK Imager

Panduan ini menjelaskan cara mengerjakan tugas *Analisis Media Penyimpanan* dari awal sampai laporan selesai. Setiap langkah ditulis berdasarkan praktik nyata, termasuk error yang muncul dan cara mengatasinya.

Tugasnya: membuat laporan analisis forensik flash disk atau memory card (SD/microSD) dengan FTK Imager, dalam bentuk PDF maksimal 10 halaman tanpa sampul, yang mencakup proses akuisisi, analisis, dan kesimpulan temuan. Materi rujukan:

1. EC-Council DFE Module 03 – *Understanding Hard Disks and File Systems*
2. EC-Council DFE Module 04 – *Data Acquisition and Duplication*
3. Ignite Technologies – *Digital Forensic: FTK Imager*

## Penting: Jangan Menyalin Hasil Orang Lain

Setiap orang wajib memakai flash disk sendiri, membuat skenario sendiri, dan menulis laporan sendiri. Nilai hash, serial number, jumlah sektor, cluster, dan timestamp pasti berbeda di setiap media. Kalau dua laporan memuat angka yang sama, dosen langsung tahu salah satunya menyalin.

Pilih satu skenario dari [daftar variasi skenario](skenario/README.md), lalu ubah detailnya sesuai keinginanmu. Angka dan screenshot di panduan ini hanya ilustrasi, bukan hasil untuk disalin.

## Urutan Pengerjaan

Ingin membaca semuanya dalam satu halaman? Buka **[PANDUAN-LENGKAP.md](PANDUAN-LENGKAP.md)**.

| No | Tahap | Perkiraan waktu | Dokumen |
|---|---|---|---|
| 1 | Menyiapkan alat dan bahan | 10 menit | [01-alat-dan-bahan.md](panduan/01-alat-dan-bahan.md) |
| 2 | Mengunduh dan menginstal FTK Imager | 15 menit | [02-unduh-instal-ftk-imager.md](panduan/02-unduh-instal-ftk-imager.md) |
| 3 | Menyiapkan media (format penuh) | 15–90 menit | [03-persiapan-media.md](panduan/03-persiapan-media.md) |
| 4 | Membuat skenario bukti | 20 menit | [04-membuat-skenario.md](panduan/04-membuat-skenario.md) |
| 5 | Mengaktifkan write blocker | 10 menit | [05-write-blocker.md](panduan/05-write-blocker.md) |
| 6 | Akuisisi image E01 | 5–60 menit | [06-akuisisi.md](panduan/06-akuisisi.md) |
| 7 | Verifikasi hash dan salinan kedua | 10 menit | [07-verifikasi.md](panduan/07-verifikasi.md) |
| 8 | Analisis image | 45 menit | [08-analisis.md](panduan/08-analisis.md) |
| 9 | Validasi dengan alat kedua | 30 menit | [09-validasi-alat-kedua.md](panduan/09-validasi-alat-kedua.md) |
| 10 | Fitur FTK Imager lain | 10 menit | [10-fitur-ftk-lain.md](panduan/10-fitur-ftk-lain.md) |
| 11 | Menyusun laporan | 2–4 jam | [11-menyusun-laporan.md](panduan/11-menyusun-laporan.md) |
| 12 | Mengembalikan pengaturan laptop | 5 menit | [12-mengembalikan-sistem.md](panduan/12-mengembalikan-sistem.md) |

Kalau menemui masalah, buka [troubleshooting.md](troubleshooting.md). Semua error yang muncul selama praktik tercatat di sana beserta penyebab dan solusinya.

## Kebiasaan yang Wajib Dilakukan Selama Praktik

1. **Ambil screenshot di setiap langkah** dengan `Win + PrtSc`. Windows menyimpannya otomatis di `Pictures\Screenshots`. Kalau OneDrive aktif, lokasinya `OneDrive\Pictures\Screenshots`.
2. **Catat jam setiap tindakan** di Notepad (contoh: `17.05 hapus 4 file`). Catatan ini menjadi tabel kronologi di laporan.
3. **Jangan menyimpan apa pun ke media bukti** setelah skenario selesai dibuat.
4. **Jangan menampilkan data pribadi** di screenshot, misalnya nama folder pribadi, chat, atau email. Potong (crop) screenshot sebelum dimasukkan ke laporan.
