# 11 – Menyusun Laporan

[← Sebelumnya](10-fitur-ftk-lain.md) · [Daftar isi](../README.md) · [Berikutnya: Mengembalikan pengaturan →](12-mengembalikan-sistem.md)

## Ketentuan Tugas

- Bentuk **PDF**, **maksimal 10 halaman**.
- **Tanpa halaman sampul.** Cukup judul, nama, NIM, dan tanggal di bagian atas halaman pertama.
- Komprehensif: proses **akuisisi**, **analisis**, dan **kesimpulan hasil temuan**.
- Berdasarkan tiga materi yang diunggah dosen.

Tulis dengan bahasamu sendiri berdasarkan data dari media milikmu. Angka contoh di panduan ini hanya ilustrasi, jangan dipakai di laporanmu.

## Kerangka yang Disarankan

| Bagian | Isi | Halaman |
|---|---|---|
| Identitas | Judul, nama, NIM, tanggal | – |
| 1. Pendahuluan | Latar belakang, tujuan, ruang lingkup dan skenario | 0,5 |
| 2. Dasar Teori | Akuisisi live/dead, order of volatility, jenis dan format akuisisi, struktur disk dan file system, validasi hash | 1–1,5 |
| 3. Metodologi | Tabel alat dan bahan; tabel 8 langkah metodologi Modul 04 dan penerapannya | 1 |
| 4. Proses Akuisisi | Persiapan media, skenario, write blocker dan ujinya, wizard Create Disk Image | 2 |
| 5. Verifikasi | Hasil Verify, log, salinan kedua dan Get-FileHash | 0,5–1 |
| 6. Analisis dan Temuan | MBR, boot sector, CHS, daftar file, slack, file terhapus, unallocated, signature, ekspor, validasi alat kedua, fitur lain, kronologi | 3–3,5 |
| 7. Kesimpulan | Jawaban atas tujuan, temuan utama, keterbatasan | 0,5 |
| Daftar Pustaka | Tiga materi kuliah dan sumber pendukung | 0,3 |

## Isi yang Diambil dari Setiap Materi

| Materi | Konsep yang wajib muncul |
|---|---|
| **Modul 03** | Sektor, cluster, slack space, struktur MBR (446 + 64 + 2 byte), GPT, BPB, FAT/NTFS, perhitungan CHS, NAND flash dan controller, EFS (NTFS), The Sleuth Kit/Autopsy |
| **Modul 04** | Live vs dead acquisition, order of volatility (RFC 3227), rules of thumb, logical/sparse/bit-stream, format Raw/E01/AFF/AFF4, 8 langkah metodologi, standar sanitasi, write blocker hardware vs software, plan for contingency (dua salinan, dua alat), validasi hash dan Get-FileHash |
| **Ignite** | Create Disk Image, Physical vs Logical Drive, format image, Evidence Item Information, Verify, Add Evidence Item, Image Mounting, Detect EFS, Export Files, fitur lain yang tidak dipakai dan alasannya |

## Tabel dan Gambar yang Disarankan

**Tabel:** format image, alat dan bahan, metodologi Modul 04, isi media dan hash referensi, ringkasan akuisisi dan verifikasi, interpretasi MBR dan boot sector, hasil pemulihan file terhapus, signature file, kronologi.

**Gambar (crop seperlunya):** format media, registry dan uji tulis, wizard akuisisi, verify results dan Get-FileHash, hex sektor 0 dan boot sector, daftar file, entri direktori/record terhapus, signature mismatch, export results, image mounting dan detect EFS.

## Tips Menulis

1. **Setiap angka harus berasal dari data milikmu**: log FTK, screenshot, atau hasil PowerShell. Jangan memakai angka contoh dari panduan ini.
2. **Parafrase materi.** Jangan menyalin kalimat dari slide atau dari internet. Cantumkan nomor sumber, misalnya [1], [2].
3. **Jelaskan arti setiap temuan**, bukan hanya menampilkan screenshot. Contoh: "byte `07` di offset `0x1C2` adalah tipe partisi NTFS/exFAT".
4. **Tulis keterbatasan dengan jujur**: kasus simulasi, write blocker software, alat yang gagal.
5. **Gunakan tabel untuk data, paragraf untuk penjelasan.**
6. Kalau memakai bantuan AI atau orang lain, ikuti aturan kampus tentang pengungkapannya.

## Membuat PDF dari Word

1. Atur kertas A4, margin sekitar 2 cm, huruf 11 pt.
2. Tulis laporan, masukkan tabel dan gambar. Supaya tabel tidak terpotong antarhalaman: klik kanan tabel → *Table Properties* → *Row* → hapus centang *Allow row to break across pages*; untuk judul tabel, gunakan *Paragraph* → *Line and Page Breaks* → centang *Keep with next*.
3. Cek jumlah halaman di status bar Word (maksimal 10).
4. *File → Save As → PDF*.
5. Buka PDF dan periksa setiap halaman: gambar terbaca, tidak ada halaman kosong, tidak ada data pribadi di screenshot.

## Daftar Periksa Sebelum Dikumpulkan

- [ ] Tanpa sampul; identitas di halaman 1
- [ ] Maksimal 10 halaman
- [ ] Ada bagian akuisisi, analisis, dan kesimpulan
- [ ] Ketiga materi dirujuk dan tercantum di daftar pustaka
- [ ] Hash MD5/SHA-1 dari log tercantum dan berstatus Match
- [ ] Bukti write blocker (registry + uji tulis)
- [ ] Analisis MBR dan boot sector dengan penjelasan offset
- [ ] File terhapus ditemukan, dipulihkan, dan hash-nya dicocokkan
- [ ] Analisis signature
- [ ] Kesimpulan menjawab semua tujuan
- [ ] Screenshot bebas data pribadi
- [ ] Semua angka sesuai data milikmu sendiri
