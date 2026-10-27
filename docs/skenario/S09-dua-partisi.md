# S09 – Partisi Tersembunyi (Dua Partisi, Satu Dihapus)

[← Daftar skenario](README.md)

**Tingkat lanjut.** Skenario ini memakai Disk Management. Salah memilih disk bisa menghapus data laptop. Ikuti setiap pengecekan dengan teliti.

## Cerita Kasus

Pelaku fiktif membagi flash disk menjadi dua partisi. Partisi pertama berisi file biasa, partisi kedua berisi dokumen sensitif. Sebelum menyerahkan flash disk, pelaku menghapus partisi kedua sehingga Windows hanya menampilkan satu drive.

## Persiapan Media

1. Format penuh flash disk (FAT32 atau NTFS) supaya bersih.
2. Buka **Disk Management**: `Win + X` → *Disk Management*.
3. **Cari disk flash disk** berdasarkan ukuran dan label *Removable*. Catat nomornya (misalnya *Disk 1*). **Jangan menyentuh Disk 0** (biasanya SSD/HDD laptop).
4. Klik kanan volume flash disk → *Delete Volume* → Yes. Area berubah menjadi *Unallocated*.
5. Klik kanan area *Unallocated* → *New Simple Volume*:
   - Ukuran: `2048` MB, drive letter bebas, file system **FAT32**, label `PART1`, **jangan centang** *Perform a quick format*.
6. Klik kanan sisa *Unallocated* → *New Simple Volume*:
   - Ukuran: sisa, file system **NTFS**, label `PART2`, **jangan centang** quick format.

Windows 10 versi 1703 ke atas mendukung beberapa partisi pada media removable.

## File yang Dibuat

| Partisi | Isi |
|---|---|
| `PART1` (FAT32) | 3–4 file biasa: jadwal, foto, catatan |
| `PART2` (NTFS) | 3–4 dokumen "sensitif" fiktif: kontrak, daftar gaji fiktif, rencana proyek |

## Tindakan (Berurutan)

1. Salin file ke kedua partisi, lalu hitung hash referensi untuk kedua drive.
2. Screenshot Disk Management yang menampilkan dua partisi.
3. Di Disk Management, klik kanan `PART2` → **Delete Volume** → Yes. Disk Management sekarang menampilkan *Unallocated* di area itu.
4. Screenshot Disk Management lagi.
5. Catat jam, lalu lanjut ke write blocker dan akuisisi (*Physical Drive*).

## Temuan yang Diharapkan

| Temuan | Penjelasan |
|---|---|
| Tabel partisi MBR hanya berisi **satu** entri | Entri kedua (offset `0x1CE`) sudah dinolkan saat partisi dihapus |
| `Unpartitioned Space` berukuran besar | Area bekas `PART2` |
| Di awal area bekas `PART2` masih ada boot sector berisi `NTFS    ` | Delete Volume biasanya hanya menghapus entri tabel partisi |
| Dokumen PART2 dapat ditemukan dengan alat kedua | Autopsy atau The Sleuth Kit dapat diarahkan ke offset sektor partisi lama |

Hitung sektor awal `PART2` dari data partisi pertama: LBA awal PART1 + jumlah sektor PART1 (+ celah perataan, biasanya kelipatan 2048 sektor). Klik `Unpartitioned Space` → `[unallocated space]` di FTK, cari potongan yang diawali `EB 52 90 4E 54 46 53` (`ëR.NTFS`).

Dengan skrip Python, partisi lama bisa dibaca langsung dengan mengubah offset di `tsk.py` (`pytsk3.FS_Info(img, offset=<sektor awal> * 512)`).

## Fokus Analisis

- **Modul 03:** disk partitions (primary/extended), struktur MBR dan empat entri partisi, BPB NTFS.
- **Modul 04:** alasan memilih *Physical Drive* daripada *Logical Drive*: logical drive tidak akan menangkap partisi yang sudah dihapus.

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| *New Simple Volume* tidak tersedia untuk partisi kedua | Windows lama (< 1703) tidak mendukung multi-partisi di media removable. Perbarui Windows atau pakai skenario lain. |
| Boot sector PART2 tidak ditemukan | Partisi dibuat dengan quick format sebelum full format, atau terhapus dengan alat lain. Catat hasil apa adanya. |
| Salah menghapus volume | Hentikan semua aktivitas di disk itu. Kalau yang terhapus volume laptop, minta bantuan teknisi; jangan menulis apa pun ke disk tersebut. |
