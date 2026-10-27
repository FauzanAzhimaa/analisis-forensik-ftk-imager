# 10 – Fitur FTK Imager Lainnya

[← Sebelumnya](09-validasi-alat-kedua.md) · [Daftar isi](../README.md) · [Berikutnya: Menyusun laporan →](11-menyusun-laporan.md)

Materi Ignite membahas fitur FTK Imager di luar pembuatan image. Bagian ini menunjukkan fitur yang relevan untuk media penyimpanan dan alasan fitur lain tidak dipakai.

## A. Image Mounting

Fitur ini memasang file E01 sebagai drive read-only, sehingga isinya bisa dijelajahi dengan File Explorer tanpa mengubah image.

1. **File → Image Mounting…**
2. Image File: klik **…** → pilih `D:\Forensik\BUKTI01.E01`.
3. Atur:

   | Pilihan | Isi |
   |---|---|
   | Mount Type | **Physical & Logical** |
   | Drive Letter | Next Available |
   | Mount Method | **Block Device / Read Only** |

4. Klik **Mount**. Daftar *Mapped Image List* menampilkan `PhysicalDriveN` (disk utuh) dan huruf drive untuk partisinya. Screenshot.

   ![Image Mounting](../gambar/image_mounting.png)

5. Buka huruf drive itu di File Explorer, lalu screenshot. Coba buat folder baru di sana; Windows harus menolak karena mount-nya read-only.
6. Kembali ke jendela Image Mounting → pilih baris **PhysicalDriveN** → **Unmount**. Kalau baris partisi masih ada, pilih dan Unmount juga. Klik Close.

## B. Detect EFS Encryption

1. Klik node image di Evidence Tree.
2. **File → Detect EFS Encryption**. Screenshot hasilnya.

   ![Detect EFS](../gambar/detect_efs.png)

| Hasil | Arti |
|---|---|
| *No EFS encryption detected* | Tidak ada file EFS. Untuk FAT32/exFAT selalu begini, karena EFS adalah fitur NTFS (Modul 03: EFS diperkenalkan pada NTFS 3.0). |
| Daftar file terenkripsi | Ada file EFS di volume NTFS. Hanya bisa dibuat di Windows edisi Pro/Enterprise/Education. |

## C. Fitur yang Tidak Dipakai dan Alasannya

| Fitur (materi Ignite) | Alasan tidak dipakai |
|---|---|
| Capture Memory | Untuk live acquisition (RAM komputer yang menyala). Bukti tugas ini adalah media lepasan. |
| Obtain Protected Files | Mengambil file registry dan kata sandi dari sistem Windows yang berjalan, bukan dari flash disk. |
| Custom Content Image + AD Encryption | Mengemas sebagian file bukti dalam format AD1 terenkripsi. Opsional; pemeriksaan sudah memiliki image utuh dan hash list. |
| Decrypt AD1 Image | Hanya diperlukan kalau ada image AD1 terenkripsi. |

Fitur Custom Content Image boleh dicoba sebagai tambahan: klik kanan file di File List → *Add to Custom Content Image (AD1)* → di panel *Custom Content Sources* klik **Create Image** → isi informasi bukti → centang *Use AD Encryption* → Finish → isi password. Hasilnya bisa dibuka lagi lewat *Add Evidence Item* (FTK meminta password) atau *File → Decrypt AD1 Image*.

## Jika Ada Masalah

| Masalah | Penyebab | Solusi |
|---|---|---|
| Tombol Mount tidak aktif | Path image kosong atau salah | Pilih ulang file `.E01` dengan tombol **…** |
| Drive hasil mount tidak muncul di This PC | Explorer belum menyegarkan tampilan | Tekan F5 di This PC atau buka langsung huruf drive dari daftar Mapped. |
| Unmount tidak bisa | Drive masih dibuka di File Explorer | Tutup jendela Explorer yang membuka drive itu, lalu Unmount lagi. |
| Menu Detect EFS Encryption abu-abu | Belum ada evidence yang dipilih | Klik node image di Evidence Tree terlebih dahulu. |
