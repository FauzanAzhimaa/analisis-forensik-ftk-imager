# 12 – Mengembalikan Pengaturan Laptop

[← Sebelumnya](11-menyusun-laporan.md) · [Daftar isi](../README.md)

Lakukan langkah ini **setelah** semua screenshot dan data yang dibutuhkan sudah terkumpul.

## A. Menonaktifkan Write Blocker

Selama `WriteProtect = 1`, **semua** flash disk dan media USB di laptop tidak bisa ditulisi.

> **Eject tidak mematikan write blocker.** *Eject* (klik kanan drive di File Explorer → *Eject*) atau *Safely Remove Hardware* hanya melepas flash disk dengan aman. Nilai `WriteProtect` tersimpan di Registry laptop, bukan di flash disk. Nilainya tetap `1` walaupun flash disk sudah di-eject, dicabut, atau laptop di-restart. Selama nilainya belum diubah, flash disk apa pun yang dicolok ke laptop itu tetap read-only.
>
> Flash disk yang sudah di-eject tidak rusak dan tidak perlu diapa-apakan. Cukup jalankan langkah di bawah.

1. `Win + R` → `regedit` → Enter → Yes.
2. Buka `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies`.
3. Klik dua kali `WriteProtect` → ubah Value data menjadi `0` → OK. Tutup Registry Editor.
4. Colokkan flash disk. Kalau flash disk masih tercolok sejak tadi, eject dulu, cabut, tunggu 5 detik, lalu colokkan lagi. Windows baru membaca nilai `WriteProtect` yang baru saat media dicolok.
5. Uji dengan menyimpan file teks ke flash disk. Sekarang harus berhasil. Hapus lagi file uji itu kalau tidak diperlukan.

Nilai `WriteProtect` juga boleh dihapus (klik kanan → Delete). Hasilnya sama dengan nilai `0`.

## B. Membersihkan FTK Imager

1. Pastikan tidak ada image yang masih ter-mount (*File → Image Mounting* → daftar Mapped harus kosong).
2. *File → Remove All Evidence Items*.
3. Tutup FTK Imager.

## C. Menyimpan Hasil

Simpan isi folder `D:\Forensik` sampai nilai tugas keluar: image E01, log `.txt`, directory listing `.csv`, `hash_list.csv`, `hash_referensi.csv`, folder ekspor, dan semua screenshot. Kalau dosen meminta bukti tambahan, semuanya masih tersedia.

## D. Memakai Flash Disk Lagi

Flash disk masih berisi file skenario. Kalau ingin dipakai lagi, format ulang (Quick Format sudah cukup kalau isinya hanya file skenario).

## Jika Ada Masalah

| Masalah | Penyebab | Solusi |
|---|---|---|
| Sudah eject flash disk, tetapi saat dicolok lagi tetap tidak bisa menyimpan file | Eject tidak mengubah Registry; `WriteProtect` masih `1` | Jalankan langkah 1–5 di atas. |
| Flash disk masih read-only setelah `WriteProtect = 0` | Belum dicolok ulang | Cabut, tunggu 5 detik, colokkan lagi. Kalau masih, restart laptop. |
| Masih read-only setelah restart | Ada kebijakan lain (misalnya `Deny_Write` di `RemovableStorageDevices`) atau saklar lock SD card | Cek `HKLM\SOFTWARE\Policies\Microsoft\Windows\RemovableStorageDevices` dan saklar lock pada kartu. |
