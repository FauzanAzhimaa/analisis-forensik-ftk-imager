# S01 – Kebocoran Dokumen Keuangan (exFAT)

[← Daftar skenario](README.md)

Skenario ini dipakai pada contoh praktik di panduan. Kalau memilihnya, **wajib** mengganti nama kasus, nama file, isi file, dan jumlah file.

## Cerita Kasus

Seorang staf administrasi perusahaan fiktif diduga membawa pulang dokumen anggaran dan daftar kontak internal menggunakan flash disk pribadi. Sebelum flash disk diamankan, staf tersebut menghapus beberapa file dan menyamarkan satu foto sebagai catatan belanja.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk > 32 GB (exFAT adalah default untuk ukuran ini) |
| File system | exFAT |
| Allocation unit size | Default (contoh: 128 KB untuk 57 GB) |
| Format | Penuh (Quick Format tidak dicentang) |

## File yang Dibuat

| Path | Jenis | Dibuat dengan |
|---|---|---|
| `README.txt` | Teks | Notepad |
| `Dokumen\rencana_anggaran.docx` | Word | Word |
| `Dokumen\notulen_rapat.pdf` | PDF | Word → Save as PDF |
| `Dokumen\laporan_audit.pdf` | PDF | Word → Save as PDF |
| `Dokumen\daftar_kontak.xlsx` | Excel | Excel |
| `Foto\foto_gudang_01.jpg` | JPEG | Kamera HP |
| `Foto\foto_gudang_02.jpg` | JPEG | Kamera HP |
| `Foto\denah_kantor.png` | PNG | Paint |
| `catatan_rahasia.txt` | Teks | Notepad |
| `foto_bukti.jpg` | JPEG | Kamera HP (akan disamarkan) |

## Tindakan (Berurutan)

1. Salin semua file ke media. Catat jam.
2. Hitung hash referensi ([panduan 04, bagian D](../panduan/04-membuat-skenario.md#d-mencatat-hash-referensi-sebelum-penghapusan)).
3. `Shift + Delete`: `catatan_rahasia.txt`, `Dokumen\laporan_audit.pdf`, `Dokumen\daftar_kontak.xlsx`, `Foto\foto_gudang_02.jpg`.
4. Ganti nama `foto_bukti.jpg` menjadi `catatan_belanja.txt`.
5. Catat jam tiap tindakan, lalu lanjut ke write blocker.

## Temuan yang Diharapkan

| Temuan | Lokasi di FTK Imager |
|---|---|
| MBR dengan satu partisi tipe `07` | Sektor 0, offset `0x1BE` |
| Boot sector berlabel `EXFAT` | Partition 1, offset 3 |
| Empat file bertanda silang merah | File List folder masing-masing |
| Entri `85/C0/C1` (aktif) dan `05/40/41` (terhapus) | Data direktori (lihat [panduan 08, bagian H](../panduan/08-analisis.md#h-file-terhapus)) |
| `catatan_belanja.txt` diawali `FF D8 FF` | Mode HEX |
| Slack space tiap file | Baris `.FileSlack` |

## Fokus Analisis

- **Modul 03:** cluster dan slack space (cluster exFAT besar → slack besar), struktur MBR, perhitungan CHS.
- **Modul 04:** metodologi 8 langkah, format E01, validasi hash, plan for contingency (low disk space, salinan kedua).
- **Ignite:** Create Disk Image, Add Evidence Item, Export Files, Image Mounting, Detect EFS.

## Masalah yang Mungkin Muncul

- Beberapa file terhapus tampil kosong dan terekspor 0 byte di FTK Imager 8.3.0.27 → [troubleshooting no. 14](../troubleshooting.md#14-file-terhapus-exfat-kosong-atau-terekspor-0-byte). Validasi dengan alat kedua.
