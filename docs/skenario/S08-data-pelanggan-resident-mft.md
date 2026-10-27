# S08 – Data Pelanggan Bocor (NTFS, File Resident di MFT)

[← Daftar skenario](README.md)

## Cerita Kasus

Toko online fiktif kehilangan data pelanggan. Flash disk milik admin berisi ekspor data pelanggan dan beberapa catatan kecil berisi kode akses. Catatan kecil itu sudah dihapus.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk ukuran berapa saja |
| File system | **NTFS** |
| Allocation unit size | Default 4 KB, atau 64 KB untuk melihat slack space besar |
| Format | Penuh |

## Konsep: File Resident

Di NTFS, setiap file punya record di `$MFT` berukuran 1024 byte. Kalau file kecil (kira-kira di bawah 700 byte), isinya disimpan **di dalam record MFT itu sendiri** (*resident*) dan tidak memakai cluster terpisah. File yang lebih besar disimpan di cluster (*non-resident*).

## File yang Dibuat

| Path | Ukuran | Jenis |
|---|---|---|
| `Ekspor\pelanggan_oktober.csv` | Beberapa KB (isi 50+ baris data fiktif) | CSV dari Excel |
| `Ekspor\pelanggan_oktober.xlsx` | | Excel |
| `Catatan\kode_akses.txt` | **< 300 byte** | Notepad, 2–3 baris teks fiktif (akan dihapus) |
| `Catatan\todo.txt` | < 300 byte | Notepad |
| `Catatan\panduan_admin.txt` | > 5 KB | Notepad, tempel teks panjang |

## Tindakan (Berurutan)

1. Salin semua file, lalu hitung hash referensi.
2. `Shift + Delete` file `Catatan\kode_akses.txt` dan `Ekspor\pelanggan_oktober.csv`.
3. Catat jam.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| `kode_akses.txt` terhapus, isinya masih terbaca | Data resident tersimpan di record MFT |
| File resident tidak punya *Start Cluster* yang wajar | Isinya ada di dalam `$MFT` |
| `skrip/tsk.py` menampilkan `lokasi=[]` untuk file resident | Tidak ada run cluster |
| Record MFT file terhapus: flag offset `0x16` = `00` | Lihat [panduan 08 bagian H](../panduan/08-analisis.md#h-file-terhapus) |
| Slack space pada file non-resident | `ukuran cluster − (ukuran file mod ukuran cluster)` |

## Fokus Analisis

- **Modul 03:** NTFS dan `$MFT` ("contains a record for every file"), `$Bitmap`, sparse file, ukuran cluster.
- **Bandingkan** dua cara penyimpanan file (resident dan non-resident) dalam satu tabel di laporan.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| File kecil tetap non-resident | Ukurannya terlalu besar atau nama file panjang memakan ruang record. Buat file < 200 byte dengan nama pendek. |
| Sulit menemukan record MFT di hex | Gunakan Autopsy (tab *File Metadata* menampilkan atribut `$DATA` dan status resident). |
