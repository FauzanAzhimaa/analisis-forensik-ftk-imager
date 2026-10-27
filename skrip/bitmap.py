"""Menampilkan status alokasi cluster exFAT dari allocation bitmap.
Pemakaian: python3 bitmap.py BUKTI01.E01 [jumlah_cluster]
"""
import struct
import sys

from _ewf import buka_e01, offset_partisi

h, img = buka_e01(sys.argv[1])
base = offset_partisi(img)
h.seek(base)
bs = h.read(512)
if bs[3:11] != b"EXFAT   ":
    sys.exit("Partisi pertama bukan exFAT.")
heap = struct.unpack_from("<I", bs, 0x58)[0]
root = struct.unpack_from("<I", bs, 0x60)[0]
bps, spc = 1 << bs[0x6C], 1 << bs[0x6D]
h.seek(base + (heap + (root - 2) * spc) * bps)
d = h.read(spc * bps)
bitmap_cluster = None
for i in range(0, len(d), 32):
    if d[i] == 0x81:
        bitmap_cluster = struct.unpack_from("<I", d, i + 20)[0]
        break
h.seek(base + (heap + (bitmap_cluster - 2) * spc) * bps)
n = int(sys.argv[2]) if len(sys.argv) > 2 else 40
b = h.read(n // 8 + 1)
print(f"allocation bitmap di cluster {bitmap_cluster}; bit pertama = cluster 2")
for i in range(n):
    print(f"cluster {i + 2}: {'terpakai' if (b[i // 8] >> (i % 8)) & 1 else 'kosong'}")
