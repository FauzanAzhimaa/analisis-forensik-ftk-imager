# 01 – Alat dan Bahan

[← Daftar isi](../README.md) · [Berikutnya: Unduh dan instal FTK Imager →](02-unduh-instal-ftk-imager.md)

## Daftar Kebutuhan

| Kebutuhan | Keterangan |
|---|---|
| Laptop/PC Windows 10 atau 11 | Berfungsi sebagai *forensic workstation*. FTK Imager 8.3 hanya tersedia untuk Windows. |
| Akun Windows dengan hak Administrator | Wajib untuk menginstal FTK Imager, mengubah registry, dan membaca physical drive. |
| Media bukti | Flash disk atau SD/microSD. Ukuran 2–16 GB paling praktis. Ukuran 64 GB tetap bisa dipakai, tetapi prosesnya lebih lama. |
| Card reader | Hanya jika memakai SD/microSD dan laptop tidak punya slot kartu. |
| Ruang kosong di laptop | Minimal 2 GB untuk image E01 dari media yang sudah diformat penuh. Lihat penjelasan di bawah. |
| Koneksi internet | Untuk mengunduh FTK Imager (±230 MB). |
| Email kampus (`.ac.id`) | Formulir unduhan Exterro menolak email pribadi seperti Gmail. |

## Cara Mengecek Ruang Kosong

1. Buka **File Explorer** → **This PC**.
2. Lihat angka *free of* di bawah setiap drive (C:, D:, dan seterusnya).
3. Pilih drive dengan ruang kosong paling besar sebagai tujuan image. Jangan memilih drive media bukti.

### Berapa ruang yang dibutuhkan?

FTK Imager menyalin **seluruh sektor** media, termasuk sektor kosong. Ukuran file image bergantung pada isi sektor kosong itu:

| Kondisi media | Perkiraan ukuran E01 |
|---|---|
| Diformat **penuh** (sektor kosong berisi nol) | Kecil. Media 57 GB pada contoh praktik hanya menghasilkan E01 107 MB. |
| Diformat **Quick Format** atau tidak diformat | Bisa hampir sama dengan kapasitas media, karena data lama tidak dapat dikompresi. |

Karena itu, lakukan format penuh di [03-persiapan-media.md](03-persiapan-media.md).

## Cara Mengecek Media Bukti

1. Colokkan flash disk atau kartu.
2. Buka **This PC**, lalu catat **huruf drive** (misalnya `E:`) dan kapasitasnya.
3. Catat **merek dan kapasitas** yang tertulis di fisik media (misalnya SanDisk Cruzer Blade 64 GB).
4. Foto fisik media dari depan dan belakang dengan HP. Foto ini bisa masuk ke bagian alat dan bahan di laporan.

## Jika Ada Masalah

| Masalah | Penyebab | Solusi |
|---|---|---|
| Flash disk tidak muncul di This PC | Port USB bermasalah atau driver belum terpasang | Coba port USB lain, lalu buka *Disk Management* (`Win + X` → Disk Management) dan lihat apakah disk muncul tanpa huruf drive. |
| Kapasitas terbaca lebih kecil dari label (misalnya 64 GB terbaca 57,3 GB) | Produsen memakai 1 GB = 10⁹ byte, Windows memakai 1 GiB = 2³⁰ byte, dan sebagian kecil kapasitas dipakai controller | Normal. Jelaskan di laporan (lihat bagian CHS di [08-analisis.md](08-analisis.md)). |
| Laptop tidak punya akun Administrator | Laptop kampus atau kantor | Pinjam laptop pribadi, atau minta bantuan asisten lab. |
