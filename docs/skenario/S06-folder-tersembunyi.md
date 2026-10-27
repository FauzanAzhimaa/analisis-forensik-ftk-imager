# S06 – Dokumen di Folder Tersembunyi (FAT32)

[← Daftar skenario](README.md)

## Cerita Kasus

Seorang karyawan fiktif menyimpan salinan kontrak kerja sama di folder tersembunyi pada flash disk, memberi nama ganda supaya terlihat seperti dokumen biasa, lalu menghapus satu folder bertingkat sebelum flash disk diserahkan.

## Persiapan Media

| Pengaturan | Nilai |
|---|---|
| Media | Flash disk 4–32 GB |
| File system | **FAT32** |
| Allocation unit size | Pilih 8 KB atau 16 KB (bukan default) supaya slack space berbeda |
| Format | Penuh |

## File yang Dibuat

| Path | Jenis | Perlakuan |
|---|---|---|
| `Kantor\jadwal_rapat.docx` | Word | Biasa |
| `Kantor\memo_internal.pdf` | PDF | Biasa |
| `.sistem\kontrak_kerjasama.pdf` | PDF | Folder diberi atribut hidden |
| `.sistem\nilai_kontrak.xlsx.txt` | Excel yang diberi nama ganda | Ekstensi ganda |
| `Arsip\2025\Q4\draf_kontrak_lama.docx` | Word | Folder `Arsip\2025` akan dihapus |
| `Arsip\2025\Q4\lampiran.pdf` | PDF | |

## Tindakan (Berurutan)

1. Salin semua file.
2. Beri atribut hidden dan system pada folder `.sistem` lewat Command Prompt (ganti `E:`):
   ```cmd
   attrib +h +s E:\.sistem
   attrib E:\.sistem
   ```
   Perintah kedua harus menampilkan huruf `S` dan `H`.
3. Pastikan ekstensi terlihat di Explorer, lalu ganti nama `nilai_kontrak.xlsx` menjadi `nilai_kontrak.xlsx.txt`.
4. Hitung hash referensi dengan perintah di [panduan 04 bagian D](../panduan/04-membuat-skenario.md#d-mencatat-hash-referensi-sebelum-penghapusan). Perintah itu memakai `-Force`, sehingga file di folder hidden ikut tercatat. Pastikan `kontrak_kerjasama.pdf` dan `nilai_kontrak.xlsx.txt` ada di CSV.
5. `Shift + Delete` folder `Arsip\2025`.
6. Catat jam.

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| Folder `.sistem` tampil di FTK walaupun hidden di Explorer | FTK membaca entri direktori langsung, atribut tidak menyembunyikan apa pun dari alat forensik |
| Byte atribut entri direktori FAT (offset `0x0B` entri 32 byte): `0x02` hidden, `0x04` system, `0x10` directory, `0x20` archive | Hex direktori induk |
| `nilai_kontrak.xlsx.txt` diawali `50 4B 03 04` | Signature ZIP/Office; ekstensi akhir `.txt` palsu |
| Folder `2025`, `Q4`, dan isinya terhapus | Entri diawali `E5` |
| Slack space dengan cluster 8/16 KB | Bandingkan dengan cluster default |

## Fokus Analisis

- **Modul 03:** struktur entri direktori FAT, atribut file, slack space dan ukuran cluster.
- **Analisis signature:** ekstensi ganda.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| Folder hidden tidak tercatat di hash referensi | Pastikan perintah memakai `-Force` pada `Get-ChildItem`. |
| `attrib` menolak (*Access denied*) | Jalankan Command Prompt biasa, pastikan media belum write-protected. |
