"""Menguraikan entri direktori exFAT (85/C0/C1 aktif, 05/40/41 terhapus).
Pemakaian: python3 dirdump.py BUKTI01.E01 [nomor_cluster ...]
Tanpa nomor cluster, skrip menguraikan root directory.
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
bps = 1 << bs[0x6C]
spc = 1 << bs[0x6D]
clusters = [int(c) for c in sys.argv[2:]] or [root]
for c in clusters:
    sektor = heap + (c - 2) * spc
    h.seek(base + sektor * bps)
    d = h.read(spc * bps)
    print(f"== cluster {c} (sektor volume {sektor})")
    for i in range(0, len(d), 32):
        e = d[i:i + 32]
        t = e[0]
        if t == 0:
            break
        aktif = "aktif" if t & 0x80 else "TERHAPUS"
        kode = t & 0x7F
        if kode == 0x05:
            print(f"{i:05x} {t:02x} File            {aktif}")
        elif kode == 0x40:
            print(f"{i:05x} {t:02x} Stream Extension {aktif} cluster_awal={struct.unpack_from('<I', e, 20)[0]} ukuran={struct.unpack_from('<Q', e, 24)[0]}")
        elif kode == 0x41:
            print(f"{i:05x} {t:02x} File Name        {aktif} '{e[2:32].decode('utf-16le', 'replace').rstrip(chr(0))}'")
        elif t == 0x81:
            print(f"{i:05x} {t:02x} Allocation Bitmap")
        elif t == 0x82:
            print(f"{i:05x} {t:02x} Up-case Table")
        elif kode == 0x03:
            print(f"{i:05x} {t:02x} Volume Label     {'berlabel' if t & 0x80 else 'tidak berlabel'}")
        else:
            print(f"{i:05x} {t:02x} entri lain       {aktif}")
