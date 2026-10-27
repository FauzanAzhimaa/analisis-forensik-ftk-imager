# S05 – Penipuan Jual Beli Online (microSD, exFAT)

[← Daftar skenario](README.md)

## Cerita Kasus

Penjual fiktif di marketplace diduga menipu pembeli dengan bukti transfer palsu. microSD dari HP-nya berisi screenshot percakapan, arsip dokumen, dan gambar bukti transfer yang disamarkan sebagai file data.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | microSD dengan adapter/card reader USB |
| File system | **exFAT** (untuk kartu ≤ 32 GB, pilih exFAT secara manual di dialog Format) |
| Format | Penuh |

## File yang Dibuat

| Path | Jenis | Cara membuat |
|---|---|---|
| `Screenshots\chat_pembeli_01.png` … `03.png` | PNG | Screenshot **percakapan fiktif** yang kamu ketik sendiri di Notepad/Word (jangan memakai chat asli) |
| `Download\katalog_produk.pdf` | PDF | Word → Save as PDF |
| `Download\arsip_pesanan.zip` | ZIP | Pilih beberapa file teks → klik kanan → *Compress to ZIP file* |
| `Download\bukti_transfer.png` | PNG | Gambar bertuliskan "BUKTI TRANSFER (SIMULASI)" di Paint (akan disamarkan) |
| `Android\data\cache.txt` | Teks | Notepad |

**Jangan membuat gambar yang meniru bukti transfer bank asli** (logo bank, nomor rekening asli, desain aplikasi bank). Cukup tulisan "SIMULASI" yang jelas.

## Tindakan (Berurutan)

1. Salin semua file, lalu hitung hash referensi.
2. Ganti nama `Download\bukti_transfer.png` menjadi `Download\cache_0091.dat`.
3. `Shift + Delete` file `Screenshots\chat_pembeli_02.png` dan `Download\katalog_produk.pdf`.
4. Catat jam.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| `cache_0091.dat` diawali `89 50 4E 47` | Signature PNG; ekstensi `.dat` menyamarkannya |
| `arsip_pesanan.zip` diawali `50 4B 03 04` dan memuat nama file di dalamnya (terbaca di kolom ASCII) | Struktur ZIP menyimpan nama file anggota arsip |
| Dua file terhapus | File List |
| Entri direktori exFAT `05/40/41` | Lihat panduan 08 bagian H |

## Fokus Analisis

- **Signature analysis:** bedakan ZIP asli, DOCX/XLSX (juga ZIP), dan file yang disamarkan.
- **Modul 03:** exFAT, slack space. Bandingkan cluster default microSD dengan flash disk teman.
- **Ignite:** Image Mounting untuk membuka `arsip_pesanan.zip` dari image tanpa menyentuh media asli.

## Masalah yang Mungkin Muncul

- Sama dengan S01: perhatikan [troubleshooting no. 14](../troubleshooting.md#14-file-terhapus-exfat-kosong-atau-terekspor-0-byte) untuk file terhapus exFAT.
