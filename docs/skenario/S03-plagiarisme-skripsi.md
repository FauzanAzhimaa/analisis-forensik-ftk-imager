# S03 – Plagiarisme Draf Skripsi (NTFS)

[← Daftar skenario](README.md)

## Cerita Kasus

Seorang mahasiswa fiktif diduga menyalin bab skripsi milik kakak tingkat. Di flash disknya ada beberapa versi draf. Versi yang berisi salinan sudah dihapus, dan sumber aslinya disembunyikan di atribut file.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk ukuran berapa saja |
| File system | **NTFS** |
| Allocation unit size | Default (umumnya 4 KB) |
| Format | Penuh |

## File yang Dibuat

| Path | Jenis |
|---|---|
| `Skripsi\BAB1_draf_v1.docx` | Word |
| `Skripsi\BAB1_draf_v2.docx` | Word |
| `Skripsi\BAB2_draf_v1.docx` | Word |
| `Skripsi\BAB2_salinan_kating.docx` | Word (akan dihapus) |
| `Referensi\jurnal_utama.pdf` | PDF |
| `Referensi\catatan_sumber.txt` | Teks (akan diberi atribut hidden) |

## Tindakan (Berurutan)

1. Salin semua file.
2. Tambahkan **Alternate Data Stream (ADS)**, fitur khusus NTFS untuk menyimpan data tersembunyi di dalam file. Di PowerShell (ganti `E:`):
   ```powershell
   Set-Content -Path E:\Skripsi\BAB2_draf_v1.docx -Stream sumber -Value "Disalin dari skripsi kating tahun 2022 (fiktif)"
   Get-Item E:\Skripsi\BAB2_draf_v1.docx -Stream *
   ```
   Perintah kedua harus menampilkan stream `:$DATA` dan `sumber`. Screenshot.
3. Beri atribut hidden: klik kanan `Referensi\catatan_sumber.txt` → Properties → centang **Hidden** → OK.
4. Hitung hash referensi.
5. `Shift + Delete` file `Skripsi\BAB2_salinan_kating.docx`.
6. Catat jam.

## Temuan yang Diharapkan

| Temuan | Lokasi |
|---|---|
| MBR tipe partisi `07` | Sektor 0 |
| Boot sector `NTFS    ` (offset 3), cluster `$MFT` (offset `0x30`) | Partition 1 |
| File sistem NTFS: `$MFT`, `$MFTMirr`, `$LogFile`, `$Bitmap`, dan lainnya | [root] |
| `BAB2_salinan_kating.docx` bertanda silang merah | Folder Skripsi |
| ADS `BAB2_draf_v1.docx:sumber` | File List (FTK menampilkan stream sebagai item tersendiri) |
| `catatan_sumber.txt` dengan atribut hidden | Panel Properties |
| Record MFT diawali `FILE`, flag di offset `0x16` (`01` aktif, `00` terhapus) | Mode HEX pada `$MFT` |

## Fokus Analisis

- **Modul 03:** arsitektur NTFS, tabel file sistem NTFS (`$mft`, `$bitmap`, `$logfile`, dan lainnya), BPB NTFS, EFS.
- **Ignite – Detect EFS Encryption:** pada NTFS hasilnya bermakna. Kalau laptopmu Windows Pro, boleh coba mengenkripsi satu file (klik kanan → Properties → Advanced → *Encrypt contents*) sebelum write blocker aktif, lalu jalankan Detect EFS.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| `Set-Content -Stream` error | Media bukan NTFS. ADS hanya ada di NTFS. |
| Opsi *Encrypt contents* abu-abu | Windows Home tidak mendukung EFS. Lewati, cukup jelaskan di laporan. |
| ADS tidak terlihat di FTK | Periksa dengan alat kedua (Autopsy menampilkan ADS), lalu catat perbedaannya. |
