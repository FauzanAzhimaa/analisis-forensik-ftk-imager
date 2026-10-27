# S02 – Pencurian Desain Produk (FAT32)

[← Daftar skenario](README.md)

## Cerita Kasus

Seorang desainer di usaha konveksi fiktif diduga menyalin desain kaos dan daftar harga ke flash disk untuk dijual ke pesaing. Ia menghapus satu folder berisi desain final dan beberapa file harga sebelum flash disk diperiksa.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk 4–32 GB |
| File system | **FAT32** |
| Allocation unit size | Default, atau pilih 16 KB/32 KB supaya berbeda dari teman |
| Format | Penuh |

## File yang Dibuat

| Path | Jenis | Catatan |
|---|---|---|
| `Desain\Draf\kaos_motif_batik_v1.png` | PNG | Buat di Paint atau aplikasi desain |
| `Desain\Draf\kaos_motif_batik_v2.png` | PNG | |
| `Desain\Final\kaos_final_produksi.png` | PNG | Folder `Final` akan dihapus seluruhnya |
| `Desain\Final\spesifikasi_sablon.docx` | Word | |
| `Harga\daftar_harga_grosir_2026.xlsx` | Excel | |
| `Harga\penawaran_ke_toko_lain.pdf` | PDF | |
| `catatan.txt` | Teks | |

Gunakan **nama file panjang** (lebih dari 8 karakter). FAT32 menyimpannya di entri *Long File Name* (LFN) tambahan.

## Tindakan (Berurutan)

1. Salin semua file, lalu hitung hash referensi.
2. `Shift + Delete` folder `Desain\Final` (beserta isinya).
3. `Shift + Delete` file `Harga\penawaran_ke_toko_lain.pdf`.
4. Catat jam.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| MBR, tipe partisi `0C` (FAT32 LBA) atau `0B` | Sektor 0, offset `0x1C2` |
| Boot sector berisi `MSDOS5.0` (offset 3) dan `FAT32` (offset `0x52`) | Partition 1 |
| BPB FAT32: bytes/sector (`0x0B`), sectors/cluster (`0x0D`), reserved sectors (`0x0E`), jumlah FAT (`0x10`), sectors/FAT (`0x24`), root cluster (`0x2C`) | Tabel BPB Modul 03 |
| Folder `Final` dan isinya bertanda silang merah | File List |
| Byte pertama entri direktori terhapus = `E5` | Data direktori folder induk |
| Nama panjang tetap terbaca dari entri LFN, nama pendek 8.3 kehilangan karakter pertama | File List / hex direktori |

## Fokus Analisis

- **Modul 03:** BPB FAT32 (tabelnya ada di modul), struktur FAT (cluster chain), perbedaan cluster FAT12/16/32.
- **Hitung lokasi area data:** reserved sectors + (jumlah FAT × sectors per FAT). Bandingkan dengan sektor awal file pertama.
- **Modul 04 dan Ignite:** sama seperti skenario lain.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| Opsi FAT32 tidak ada | Media > 32 GB. Pakai media lebih kecil. |
| Isi file di folder terhapus tidak bisa dibaca | Rantai cluster di FAT sudah dinolkan. FTK membaca file secara berurutan mulai dari cluster awal; file yang terfragmentasi bisa tidak utuh. Validasi dengan alat kedua dan catat hasilnya. |
