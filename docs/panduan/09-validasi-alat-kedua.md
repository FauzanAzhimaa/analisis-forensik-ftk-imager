# 09 – Validasi dengan Alat Kedua

[← Sebelumnya](08-analisis.md) · [Daftar isi](../README.md) · [Berikutnya: Fitur FTK lain →](10-fitur-ftk-lain.md)

Modul 04 Step 7 menganjurkan pemakaian lebih dari satu alat, karena satu alat bisa saja salah. Pada contoh praktik, FTK Imager 8.3.0.27 gagal mengekspor tiga dari empat file terhapus pada exFAT, sedangkan alat kedua memulihkan keempatnya dengan hash yang identik.

Pilih salah satu cara berikut.

---

## Cara 1: Autopsy (GUI, paling mudah)

Autopsy adalah antarmuka grafis untuk The Sleuth Kit dan dibahas di Modul 03 (*File System Analysis Using Autopsy*).

### Instalasi

1. Buka situs resmi `https://www.autopsy.com` atau `https://www.sleuthkit.org/autopsy/`, lalu unduh installer Windows 64-bit (`.msi`).
2. Jalankan installer → Next sampai selesai. Ukurannya sekitar 1 GB.

### Membuka image

1. Jalankan Autopsy → **New Case**.
2. Isi *Case Name* (misalnya `FD-2026-001`) dan *Base Directory* (misalnya `D:\Forensik\Autopsy`) → Next.
3. Isi *Case Number* dan *Examiner* → Finish.
4. Di jendela *Add Data Source*: pilih **Generate new host name** → Next → **Disk Image or VM File** → Next.
5. Path: pilih `D:\Forensik\BUKTI01.E01`. Time zone: **(GMT+7:00) Asia/Jakarta** → Next.
6. Pada *Configure Ingest*, cukup aktifkan:
   - **Hash Lookup** (menghitung MD5 setiap file, walaupun tanpa database hash)
   - **File Type Identification**
   - **Extension Mismatch Detector**
   - **Picture Analyzer** (membaca EXIF foto)

   lalu Next → Finish. Tunggu ingest selesai (progress bar di kanan bawah).

### Yang diperiksa

| Lokasi di Autopsy | Yang dicari |
|---|---|
| *Data Sources* → image → partisi → folder | Daftar file aktif dan terhapus (ikon silang merah) |
| *File Views* → *Deleted Files* → *File System* | Semua file terhapus |
| *Analysis Results* → *Extension Mismatch Detected* | File seperti `catatan_belanja.txt` yang ternyata JPEG |
| Tab *File Metadata* di panel bawah | MD5, ukuran, alamat sektor/cluster |
| Tab *Hex* | Isi file dalam hex |

### Mengekstrak dan mencocokkan

1. Klik kanan file terhapus → **Extract File(s)** → simpan ke `D:\Forensik\Autopsy-Ekspor`.
2. Hitung hash hasil ekstraksi dengan PowerShell:
   ```powershell
   Get-ChildItem D:\Forensik\Autopsy-Ekspor -Recurse -File | Get-FileHash -Algorithm MD5 | Format-Table -AutoSize
   ```
3. Bandingkan dengan `hash_referensi.csv`, lalu screenshot untuk laporan.

---

## Cara 2: Skrip Python (libewf + The Sleuth Kit) lewat WSL

Skrip di folder [`skrip`](../../skrip) dipakai saat panduan ini disusun. Paling mudah dijalankan di WSL (Ubuntu di Windows).

### Persiapan

1. Pasang WSL kalau belum ada. Buka PowerShell sebagai Administrator:
   ```powershell
   wsl --install -d Ubuntu
   ```
   Restart laptop, lalu buka **Ubuntu** dari Start Menu dan buat username/password.
2. Di terminal Ubuntu:
   ```bash
   sudo apt update
   sudo apt install -y python3-venv git
   python3 -m venv ~/forensik
   source ~/forensik/bin/activate
   pip install libewf-python pytsk3
   git clone https://github.com/FauzanAzhimaa/analisis-forensik-ftk-imager.git
   cd analisis-forensik-ftk-imager/skrip
   ```

Drive Windows dapat diakses dari WSL lewat `/mnt/<huruf drive>`. Contoh: `D:\Forensik\BUKTI01.E01` menjadi `/mnt/d/Forensik/BUKTI01.E01`.

### Menjalankan

| Perintah | Hasil |
|---|---|
| `python3 ewfhash.py /mnt/d/Forensik/BUKTI01.E01` | Ukuran, MD5, dan SHA-1 media. Harus sama dengan log FTK. Untuk 64 GB butuh ±6 menit. |
| `python3 tsk.py /mnt/d/Forensik/BUKTI01.E01` | Tabel partisi dan semua file beserta status dan lokasinya |
| `python3 recover.py /mnt/d/Forensik/BUKTI01.E01 /mnt/d/Forensik/TSK-Ekspor` | Mengekstrak semua file (termasuk terhapus) dan menampilkan MD5 |
| `python3 dirdump.py /mnt/d/Forensik/BUKTI01.E01 4 9 14` | Mengurai entri direktori exFAT di cluster tertentu (khusus exFAT) |
| `python3 bitmap.py /mnt/d/Forensik/BUKTI01.E01 30` | Status alokasi 30 cluster pertama (khusus exFAT) |

Simpan hasil ke file teks supaya bisa dimasukkan ke laporan, misalnya:

```bash
python3 recover.py /mnt/d/Forensik/BUKTI01.E01 /mnt/d/Forensik/TSK-Ekspor > /mnt/d/Forensik/hasil_pemulihan.txt
```

---

## Cara Menyimpulkan

| Kondisi | Arti |
|---|---|
| Hash media (`ewfhash.py`) sama dengan log FTK | Image valid, terbukti dengan alat kedua |
| File terhapus terpulihkan dan MD5 sama dengan referensi | Data belum tertimpa; pemulihan berhasil |
| FTK gagal, alat kedua berhasil | Keterbatasan FTK; bahas di laporan sebagai alasan validasi dengan alat kedua |
| Kedua alat gagal dan isi cluster sudah berbeda | Data sudah tertimpa |

## Jika Ada Masalah

| Masalah | Penyebab | Solusi |
|---|---|---|
| `wsl --install` gagal | Virtualisasi belum aktif di BIOS | Aktifkan *Intel VT-x / AMD SVM* di BIOS, atau pakai Cara 1 (Autopsy). |
| `pip install` error *externally-managed-environment* | Ubuntu baru melarang pip di Python sistem | Pakai virtual environment seperti di langkah persiapan (`python3 -m venv` lalu `source`). |
| `ModuleNotFoundError: No module named 'pyewf'` | Virtual environment belum aktif | Jalankan `source ~/forensik/bin/activate`. |
| `No such file or directory: /mnt/d/...` | Huruf drive atau path salah | Cek dengan `ls /mnt/d/Forensik`. Huruf drive memakai huruf kecil. |
| `Partisi pertama bukan exFAT.` saat menjalankan `dirdump.py`/`bitmap.py` | Kedua skrip itu khusus exFAT | Untuk FAT32/NTFS, pakai `tsk.py` dan `recover.py` saja. |
| Autopsy lama saat ingest | Media besar atau banyak modul aktif | Nonaktifkan modul yang tidak diperlukan, terutama *Keyword Search*. |
