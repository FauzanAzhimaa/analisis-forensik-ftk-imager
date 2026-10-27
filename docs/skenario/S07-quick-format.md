# S07 – Menghapus Jejak dengan Quick Format (NTFS → FAT32)

[← Daftar skenario](README.md)

## Cerita Kasus

Pelaku fiktif mengira semua bukti hilang setelah flash disk di-Quick Format. Pemeriksa ingin membuktikan bahwa Quick Format hanya membuat struktur file system baru, sementara isi file lama masih tertinggal di sektor kosong.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk 4–32 GB (lebih kecil lebih cepat) |
| Tahap 1 | Format **penuh** NTFS |
| Tahap 2 | **Quick Format** FAT32 (setelah file disalin) |

## File yang Dibuat

| Path | Jenis | Kata unik di dalam isi |
|---|---|---|
| `laporan_keuangan_rahasia.pdf` | PDF | `RAHASIA-KEU-2026` |
| `transaksi_oktober.xlsx` | Excel | - |
| `memo_direksi.docx` | Word | - |
| `catatan_pelaku.txt` | Teks | `JEJAK-PELAKU-01` |
| `foto_dokumen.jpg` | JPEG (kamera HP) | - |

Kata unik di file teks dan PDF memudahkan pencarian di unallocated space.

## Tindakan (Berurutan)

1. Format penuh NTFS (Quick Format tidak dicentang).
2. Salin semua file, lalu hitung hash referensi.
3. Format ulang media dengan **FAT32** dan **Quick Format dicentang**. Ini satu-satunya skenario yang sengaja memakai Quick Format.
4. Salin satu file baru yang kecil, misalnya `catatan_baru.txt`.
5. Catat jam setiap tahap.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| Partisi FAT32 hanya berisi `catatan_baru.txt` | Quick Format membuat struktur FAT32 baru |
| `[unallocated space]` berisi signature `%PDF`, `PK`, `FF D8 FF` dan teks `JEJAK-PELAKU-01` | Isi file lama masih ada |
| Mungkin masih ada sisa record MFT NTFS lama yang diawali `FILE0` beserta nama file lama (UTF-16) | Struktur NTFS lama berada di tengah volume dan tidak ditimpa Quick Format |
| File lama tidak muncul sebagai file terhapus | Entri direktori lama milik NTFS, bukan FAT32 |

Cara mencari: klik potongan-potongan di `[unallocated space]`, mode HEX/TEXT, dan perhatikan kolom ASCII. Potongan yang berisi data terlihat berbeda dari potongan yang semuanya `00`.

## Fokus Analisis

- **Modul 04 – sanitasi media:** bandingkan Quick Format, format penuh, dan standar NIST SP 800-88 / DoD 5220.22-M. Skenario ini membuktikan Quick Format bukan sanitasi.
- **Modul 03:** boot sector FAT32 baru vs sisa struktur NTFS.
- **Alat kedua:** pemulihan file tanpa metadata (*file carving*) bisa dicoba dengan Autopsy (modul ingest *PhotoRec Carver*). Bahas hasilnya.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| Ukuran E01 besar | Wajar: data NTFS lama tidak berupa nol. Siapkan ruang ±ukuran data yang pernah ditulis. |
| Tidak menemukan teks unik | Data bisa berada di potongan unallocated mana saja; telusuri potongan yang tidak kosong, atau pakai Autopsy *Keyword Search* dengan kata unik. |
