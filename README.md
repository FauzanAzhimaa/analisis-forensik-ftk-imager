# Panduan Analisis Forensik Media Penyimpanan dengan FTK Imager

Panduan langkah demi langkah untuk tugas *Analisis Media Penyimpanan*: membuat laporan analisis forensik flash disk atau memory card memakai Exterro FTK Imager, dari mengunduh aplikasi sampai PDF laporan siap dikumpulkan. Setiap langkah dilengkapi tabel *Jika Ada Masalah*.

**Mulai dari sini → [Panduan Lengkap (satu halaman)](docs/PANDUAN-LENGKAP.md)**

| Langkah | Isi |
|---|---|
| [01 – Alat dan bahan](docs/panduan/01-alat-dan-bahan.md) | Kebutuhan laptop, media, ruang disk |
| [02 – Unduh dan instal FTK Imager](docs/panduan/02-unduh-instal-ftk-imager.md) | Formulir Exterro, ekstrak, instal |
| [03 – Persiapan media](docs/panduan/03-persiapan-media.md) | Format penuh, memilih FAT32/exFAT/NTFS |
| [04 – Membuat skenario](docs/panduan/04-membuat-skenario.md) | Membuat file, hash referensi, menghapus file |
| [05 – Write blocker](docs/panduan/05-write-blocker.md) | Registry `WriteProtect`, uji tulis |
| [06 – Akuisisi](docs/panduan/06-akuisisi.md) | Wizard Create Disk Image sampai E01 jadi |
| [07 – Verifikasi](docs/panduan/07-verifikasi.md) | Verify Results, log, Get-FileHash, salinan kedua |
| [08 – Analisis](docs/panduan/08-analisis.md) | MBR, boot sector, CHS, file terhapus, unallocated, signature, ekspor |
| [09 – Validasi alat kedua](docs/panduan/09-validasi-alat-kedua.md) | Autopsy atau skrip Python (WSL) |
| [10 – Fitur FTK lain](docs/panduan/10-fitur-ftk-lain.md) | Image Mounting, Detect EFS |
| [11 – Menyusun laporan](docs/panduan/11-menyusun-laporan.md) | Kerangka 10 halaman, isi tiap materi, daftar periksa |
| [12 – Mengembalikan pengaturan](docs/panduan/12-mengembalikan-sistem.md) | Mematikan write blocker (eject saja tidak cukup) |
| [Troubleshooting](docs/troubleshooting.md) | 50 masalah dan solusinya |
| [Variasi skenario S01–S10](docs/skenario/README.md) | Sepuluh studi kasus berbeda supaya hasil tiap orang tidak sama |

## Sebelum Mulai

- Pakai media, skenario, data, dan tulisan milikmu sendiri. Hash, serial number, jumlah sektor, dan timestamp pasti berbeda di setiap media.
- Angka dan screenshot di panduan ini hanya ilustrasi. Jangan memasukkannya ke laporanmu.
- Pilih salah satu [skenario S01–S10](docs/skenario/README.md) supaya studi kasus tiap orang berbeda.

## Struktur Repositori

```
docs/
  PANDUAN-LENGKAP.md   panduan 01–12 dalam satu halaman
  README.md            daftar isi panduan
  panduan/             panduan langkah 01–12
  skenario/            variasi skenario S01–S10
  troubleshooting.md   masalah dan solusinya
  gambar/              screenshot ilustrasi untuk panduan
skrip/                 skrip Python validasi dengan alat kedua (libewf, The Sleuth Kit)
```

## Skrip Validasi

Skrip di folder `skrip/` membaca file E01 hasil akuisisimu untuk membandingkan hasil FTK Imager dengan alat kedua. Butuh Python 3, `libewf-python`, dan `pytsk3`. Cara memasang dan menjalankannya di WSL ada di [panduan 09](docs/panduan/09-validasi-alat-kedua.md#cara-2-skrip-python-libewf--the-sleuth-kit-lewat-wsl).

| Skrip | Fungsi |
|---|---|
| `ewfhash.py` | Ukuran, MD5, dan SHA-1 media yang direkonstruksi dari E01 |
| `tsk.py` | Tabel partisi dan daftar semua file beserta status dan lokasinya |
| `recover.py` | Mengekstrak semua file, termasuk yang terhapus, lalu menghitung MD5 |
| `dirdump.py` | Mengurai entri direktori exFAT pada cluster tertentu |
| `bitmap.py` | Status alokasi cluster dari allocation bitmap exFAT |

## Sumber Utama

1. EC-Council, *Digital Forensics Essentials v1*, Module 03: Understanding Hard Disks and File Systems.
2. EC-Council, *Digital Forensics Essentials v1*, Module 04: Data Acquisition and Duplication.
3. Ignite Technologies, *Digital Forensic: FTK Imager*, hackingarticles.in.
4. Microsoft, [exFAT File System Specification](https://learn.microsoft.com/windows/win32/fileio/exfat-specification).

Seluruh nama orang dan perusahaan di dalam skenario bersifat fiktif.
