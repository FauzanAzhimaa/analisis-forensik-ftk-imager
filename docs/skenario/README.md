# Variasi Skenario

[← Daftar isi](../README.md)

Setiap orang sebaiknya memakai skenario yang berbeda. Kombinasi **tema**, **file system**, **media**, dan **tindakan** membuat temuan dan laporan tiap orang berbeda, walaupun langkah FTK Imager-nya sama.

## Daftar Skenario

| Kode | Tema | Media | File system | Teknik utama | Tingkat |
|---|---|---|---|---|---|
| [S01](S01-kebocoran-dokumen-keuangan.md) | Kebocoran dokumen keuangan | Flash disk > 32 GB | exFAT | File terhapus, ekstensi palsu | Dasar |
| [S02](S02-pencurian-desain-produk.md) | Pencurian desain produk | Flash disk ≤ 32 GB | FAT32 | Entri `E5`, folder terhapus, nama panjang (LFN) | Dasar |
| [S03](S03-plagiarisme-skripsi.md) | Plagiarisme draf skripsi | Flash disk | NTFS | Record MFT terhapus, atribut hidden, Alternate Data Stream | Menengah |
| [S04](S04-foto-bukti-kecelakaan.md) | Foto bukti kecelakaan | SD/microSD | FAT32 | EXIF foto HP, struktur DCIM, file tertimpa | Menengah |
| [S05](S05-penipuan-jual-beli-online.md) | Penipuan jual beli online | microSD | exFAT | Screenshot chat, arsip ZIP, ekstensi palsu `.dat` | Dasar |
| [S06](S06-folder-tersembunyi.md) | Dokumen di folder tersembunyi | Flash disk ≤ 32 GB | FAT32 | Atribut hidden/system, ekstensi ganda, hapus folder bertingkat | Dasar |
| [S07](S07-quick-format.md) | Menghapus jejak dengan Quick Format | Flash disk ≤ 32 GB | NTFS → FAT32 | Sisa data setelah Quick Format | Menengah |
| [S08](S08-data-pelanggan-resident-mft.md) | Data pelanggan bocor | Flash disk | NTFS | File resident di MFT, slack space | Menengah |
| [S09](S09-dua-partisi.md) | Partisi tersembunyi | Flash disk ≥ 8 GB | FAT32 + NTFS | Dua entri tabel partisi, partisi terhapus | Lanjut |
| [S10](S10-flash-disk-gpt.md) | Media berskema GPT | Flash disk | GPT + NTFS | Protective MBR `EE`, header `EFI PART` | Lanjut |

**Dasar** cocok untuk yang baru pertama kali. **Menengah** menambah analisis struktur file system. **Lanjut** memakai Disk Management atau DiskPart; ikuti peringatannya dengan teliti.

## Cara Membuat Skenariomu Unik

Selain memilih kode skenario yang berbeda, ubah juga detail berikut:

1. **Nama kasus dan nama tokoh fiktif.** Contoh: CV Sinar Data Mandiri → PT Batik Nusantara Kreatif.
2. **Isi file.** Ketik sendiri di Word/Excel; foto dengan HP sendiri.
3. **Jumlah dan jenis file.** Misalnya 8 file dengan 3 terhapus, atau 12 file dengan 5 terhapus.
4. **Struktur folder.** Contoh: `Dokumen/2026/Oktober`, `Arsip`, `Foto/Gudang`.
5. **Ukuran cluster.** Pada dialog Format, pilih *Allocation unit size* selain default (misalnya 32 KB atau 64 KB), lalu bandingkan slack space di laporan.
6. **Media.** Flash disk, SD card, atau microSD dengan card reader.

## Struktur Setiap Halaman Skenario

Setiap file skenario berisi:

- **Cerita kasus** untuk bagian pendahuluan.
- **Persiapan media**: file system, ukuran, dan pengaturan format.
- **File yang dibuat** beserta jenis dan signature-nya.
- **Tindakan skenario** dalam urutan yang harus dilakukan.
- **Temuan yang diharapkan** untuk mencocokkan hasil analisis.
- **Fokus analisis** yang dikaitkan dengan materi Modul 03, Modul 04, dan Ignite.
- **Masalah yang mungkin muncul** dan solusinya.

Setelah memilih skenario, kerjakan [panduan langkah 03](../panduan/03-persiapan-media.md) sampai [12](../panduan/12-mengembalikan-sistem.md) seperti biasa.
