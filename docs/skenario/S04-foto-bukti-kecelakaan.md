# S04 – Foto Bukti Kecelakaan (SD Card, FAT32)

[← Daftar skenario](README.md)

## Cerita Kasus

Seorang saksi fiktif menyerahkan kartu memori dari kamera atau HP yang berisi foto lokasi kecelakaan. Pemilik kendaraan diduga sempat menghapus foto yang memperlihatkan pelat nomornya dan memotret hal lain setelahnya.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | SD card atau microSD 4–32 GB, dibaca lewat card reader |
| File system | **FAT32** |
| Format | Penuh |

Pastikan saklar *lock* pada SD card dalam posisi **tidak terkunci** saat format dan pengisian.

## File yang Dibuat

Tiru struktur folder kamera digital (standar DCIM):

| Path | Isi |
|---|---|
| `DCIM\100MEDIA\IMG_0001.JPG` … `IMG_0006.JPG` | Foto asli dari kamera HP (misalnya foto jalan, kendaraan mainan, rambu) |
| `DCIM\100MEDIA\IMG_0007.JPG` | Foto yang akan dihapus (misalnya foto pelat nomor fiktif yang ditulis di kertas) |
| `MISC\keterangan_saksi.txt` | Teks keterangan fiktif |

Pindahkan foto dari HP ke laptop **tanpa diedit** dan tanpa dikirim lewat aplikasi chat, karena aplikasi chat biasanya menghapus metadata EXIF.

## Tindakan (Berurutan)

1. Salin semua file ke kartu, lalu hitung hash referensi.
2. `Shift + Delete` file `IMG_0007.JPG`.
3. Salin satu foto baru yang **ukurannya lebih besar**, beri nama `IMG_0008.JPG`.
4. Catat jam.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| Header JPEG `FF D8 FF E1` disusul teks `Exif` | Foto kamera menyimpan metadata EXIF di segmen APP1 |
| Merek/model HP dan tanggal pengambilan foto terbaca di kolom ASCII | Metadata EXIF |
| `IMG_0007.JPG` bertanda silang merah | File terhapus |
| Apakah `IMG_0008.JPG` menimpa cluster `IMG_0007.JPG`? | Bandingkan cluster awal kedua file di panel Properties |

Windows biasanya mengalokasikan cluster FAT32 mulai dari petunjuk *next free cluster* di FSInfo, sehingga cluster bekas file terhapus belum tentu langsung dipakai ulang. Ada dua kemungkinan:

| Hasil | Arti untuk laporan |
|---|---|
| Cluster berbeda, `IMG_0007.JPG` terpulihkan utuh (hash cocok) | File terhapus belum tertimpa |
| Cluster sama atau bertumpuk, hash tidak cocok | Data tertimpa sebagian; pemulihan tidak utuh |

Laporkan hasil yang terjadi pada mediamu.

## Fokus Analisis

- **Modul 03:** FAT32, cluster chain, alokasi cluster, file tertimpa vs file terhapus.
- **Modul 04:** jenis data statis (gambar, file terhapus, unallocated space).
- **Analisis metadata:** EXIF sebagai bukti waktu dan perangkat pengambil foto.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| Write blocker tidak berlaku untuk card reader bawaan laptop | Pakai card reader USB eksternal, lalu uji tulis lagi. Geser saklar lock ke posisi terkunci saat akuisisi sebagai perlindungan tambahan. |
| Teks `Exif` tidak muncul | Foto sudah melalui aplikasi yang menghapus metadata. Ambil ulang foto langsung dari galeri HP lewat kabel USB. |
