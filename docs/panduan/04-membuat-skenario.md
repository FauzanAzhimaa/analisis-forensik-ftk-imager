# 04 – Membuat Skenario Bukti

[← Sebelumnya](03-persiapan-media.md) · [Daftar isi](../README.md) · [Berikutnya: Write blocker →](05-write-blocker.md)

Media kosong tidak menghasilkan temuan yang bisa dianalisis. Karena itu, isi media dengan file skenario, lalu lakukan beberapa tindakan yang meninggalkan jejak forensik: menghapus file, menyamarkan ekstensi, dan sebagainya. Pilih skenario dari [daftar variasi skenario](../skenario/README.md).

## A. Menyiapkan File

Buat file dengan aplikasi yang ada di laptopmu sendiri supaya isinya unik:

| Jenis | Cara membuat | Signature (byte awal) |
|---|---|---|
| `.docx` | Microsoft Word → ketik isi fiktif → Save | `50 4B 03 04` (ZIP) |
| `.xlsx` | Microsoft Excel → isi tabel fiktif → Save | `50 4B 03 04` (ZIP) |
| `.pdf` | Word → *File → Save As → PDF* | `25 50 44 46` (`%PDF`) |
| `.jpg` | Foto dari kamera HP (pindahkan ke laptop) | `FF D8 FF` |
| `.png` | Screenshot atau Paint → Save as PNG | `89 50 4E 47` |
| `.txt` | Notepad | Tidak ada signature khusus (teks biasa) |

Pakai **nama orang dan perusahaan fiktif**. Jangan memakai data pribadi asli siapa pun.

Foto dari kamera HP lebih baik daripada gambar dari internet atau gambar buatan AI. Foto HP membawa metadata EXIF (merek HP, waktu pengambilan) yang bisa dianalisis, sedangkan gambar buatan AI biasanya membawa metadata C2PA yang mencatat aplikasi pembuatnya.

## B. Menyiapkan Folder Kerja di Laptop

Buat folder kerja di drive laptop (bukan di media bukti), misalnya `D:\Forensik`. Semua hasil (image, log, hash, ekspor) disimpan di sini.

## C. Menyalin File ke Media

1. Buat struktur folder di media, misalnya `E:\Dokumen` dan `E:\Foto`.
2. Salin file skenario ke media lewat File Explorer.
3. Catat jam penyalinan.

## D. Mencatat Hash Referensi (Sebelum Penghapusan)

Hash referensi dipakai untuk membuktikan bahwa file hasil pemulihan identik dengan file asli. Buka **PowerShell** (tidak perlu Administrator), lalu jalankan:

```powershell
Get-ChildItem E:\ -Recurse -File -Force -ErrorAction SilentlyContinue |
  Where-Object { $_.FullName -notlike "*System Volume Information*" } |
  ForEach-Object {
    [PSCustomObject]@{
      Path   = $_.FullName
      Ukuran = $_.Length
      MD5    = (Get-FileHash $_.FullName -Algorithm MD5).Hash
      SHA1   = (Get-FileHash $_.FullName -Algorithm SHA1).Hash
    }
  } | Export-Csv D:\Forensik\hash_referensi.csv -NoTypeInformation
```

Ganti `E:\` dengan huruf drive media bukti. Parameter `-Force` membuat file hidden ikut tercatat. File `hash_referensi.csv` tersimpan di `D:\Forensik`, **bukan** di media bukti. Buka file itu dengan Excel untuk memastikan isinya lengkap, lalu screenshot.

## E. Melakukan Tindakan Skenario

Lakukan tindakan sesuai skenario yang kamu pilih. Contoh tindakan dan cara melakukannya:

| Tindakan | Cara | Jejak yang bisa dianalisis |
|---|---|---|
| Menghapus permanen | Pilih file → `Shift + Delete` → Yes | File bertanda silang merah di FTK Imager |
| Menyamarkan ekstensi | Aktifkan *View → Show → File name extensions* di Explorer, lalu ganti nama `foto.jpg` menjadi `catatan.txt` | Signature `FF D8 FF` tidak sesuai ekstensi `.txt` |
| Menyembunyikan file | Klik kanan → Properties → centang *Hidden* | Atribut hidden di properties FTK Imager |
| Menghapus folder beserta isinya | Pilih folder → `Shift + Delete` | Folder dan isinya terhapus |
| Menimpa file terhapus | Hapus file A, lalu salin file besar B | Sebagian data A hilang karena cluster ditimpa |

Media lepasan (flash disk, SD card) tidak memiliki Recycle Bin, jadi `Delete` biasa pun langsung menghapus permanen. Tetap gunakan `Shift + Delete` supaya konsisten.

Catat jam setiap tindakan. Contoh catatan:

```
17.00  salin 10 file ke E:
17.02  hitung hash referensi → D:\Forensik\hash_referensi.csv
17.05  Shift+Delete: catatan_rahasia.txt, laporan_akhir_audit.pdf, ...
17.06  ganti nama foto_bukti.jpg → catatan_belanja.txt
```

## F. Hasil yang Benar

- File yang dihapus tidak terlihat lagi di File Explorer.
- `hash_referensi.csv` memuat semua file, termasuk yang sudah dihapus.
- Catatan waktu lengkap.

Setelah tahap ini, **jangan menulis apa pun lagi ke media**. Langsung lanjut ke write blocker.

## Jika Ada Masalah

| Masalah | Penyebab | Solusi |
|---|---|---|
| Ekstensi file tidak terlihat saat ganti nama | Windows menyembunyikan ekstensi | Explorer → *View* → *Show* → centang *File name extensions*. |
| Muncul peringatan *"If you change a file name extension, the file might become unusable"* | Peringatan normal Windows | Klik **Yes**. |
| PowerShell: *"Access to the path ... System Volume Information is denied"* | Folder sistem yang dibuat Windows | Normal. Perintah di atas sudah menyaringnya dengan `-ErrorAction SilentlyContinue` dan `Where-Object`. |
| PowerShell: *"running scripts is disabled on this system"* | Perintah dijalankan sebagai file `.ps1` | Tempel perintah langsung ke jendela PowerShell, bukan sebagai file skrip. |
| Lupa mencatat hash sebelum menghapus | - | Hash file terhapus tetap bisa dihitung dari file aslinya yang masih ada di laptop, asalkan file itu belum diubah. Kalau tidak ada, format ulang media dan ulangi tahap ini. |
