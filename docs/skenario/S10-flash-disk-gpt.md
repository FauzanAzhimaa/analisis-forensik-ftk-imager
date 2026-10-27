# S10 – Media Berskema GPT

[← Daftar skenario](README.md)

**Tingkat lanjut.** Skenario ini memakai `diskpart`. Perintah `clean` menghapus **seluruh** isi disk yang dipilih. Salah nomor disk berarti data laptop hilang.

## Cerita Kasus

Flash disk milik staf IT fiktif diformat dengan skema GPT, berbeda dari flash disk pada umumnya yang memakai MBR. Pemeriksa harus mengenali skema partisi sebelum menganalisis isinya.

## Persiapan Media dengan DiskPart

1. Buka **Command Prompt sebagai Administrator**.
2. Jalankan:
   ```
   diskpart
   list disk
   ```
3. **Cocokkan ukuran** dengan flash disk. Catat nomornya. Disk laptop biasanya *Disk 0*.
4. Lanjutkan (ganti `1` dengan nomor flash disk):
   ```
   select disk 1
   detail disk
   ```
   Pastikan `detail disk` menampilkan merek flash disk dan *Type: USB*. Kalau ragu, ketik `exit` dan jangan lanjutkan.
5. Lanjutkan:
   ```
   clean
   convert gpt
   create partition primary
   format fs=ntfs label=BUKTIGPT
   assign
   list partition
   exit
   ```
   `format` tanpa `quick` adalah format penuh dan bisa lama. Screenshot hasil `list partition`.

## File yang Dibuat

Bebas, 6–10 file campuran (Word, PDF, foto, teks) dengan tema rencana pengadaan perangkat IT fiktif. Hapus 2–3 file dan samarkan satu ekstensi seperti skenario lain.

## Temuan yang Diharapkan

| Lokasi | Isi | Arti |
|---|---|---|
| Sektor 0, offset `0x1C2` | `EE` | Protective MBR: disk memakai GPT |
| Sektor 0, offset `0x1FE` | `55 AA` | Signature |
| Sektor 1 (offset `0x200` pada node image) | Teks `EFI PART` | Header GPT |
| Header GPT offset `0x48` (8 byte) | Biasanya `2` | LBA awal tabel entri partisi |
| Sektor 2, setiap entri 128 byte | Offset +0 GUID tipe partisi, +32 LBA awal, +40 LBA akhir, +56 nama partisi (UTF-16) | Entri partisi |
| GUID tipe `A2 A0 D0 EB E5 B9 33 44 87 C0 68 B6 B7 26 99 C7` | Microsoft Basic Data | Partisi data Windows |
| Sektor terakhir disk | Salinan header GPT | Backup GPT (Modul 03: *primary and backup partition tables*) |

Kemungkinan juga ada partisi **Microsoft Reserved (MSR)** kecil sebelum partisi data. Catat kalau muncul.

## Fokus Analisis

- **Modul 03:** UEFI dan GPT (LBA 0 protective MBR, LBA 1 header, LBA 2–33 entri, header cadangan di akhir disk), GUID, kelebihan GPT (128 partisi, LBA 64-bit).
- **Modul 03:** artefak GPT (hidden data di celah antarpartisi dan area tak terpartisi di akhir disk).

## Masalah yang Mungkin Muncul

| Masalah | Solusi |
|---|---|
| `convert gpt` gagal | Ketik `clean` sekali lagi pada disk yang benar, lalu ulangi. |
| `clean` gagal karena *access denied* | Write blocker masih aktif. Set `WriteProtect = 0`, cabut-colok, ulangi. |
| Flash disk tidak muncul di Explorer setelah `exit` | Lupa `assign`. Masuk diskpart lagi, `select disk 1`, `select partition 1` (atau 2 kalau ada MSR), `assign`. |
| Ingin kembali ke MBR | `select disk N` → `clean` → `convert mbr` → buat partisi dan format lagi. |
