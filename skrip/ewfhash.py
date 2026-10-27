"""Menghitung ukuran, MD5, dan SHA-1 media yang direkonstruksi dari file E01.
Pemakaian: python3 ewfhash.py BUKTI01.E01
"""
import hashlib
import sys

from _ewf import buka_e01

h, _ = buka_e01(sys.argv[1])
md5, sha1 = hashlib.md5(), hashlib.sha1()
total, off = h.get_media_size(), 0
while off < total:
    blok = h.read(min(64 * 1024 * 1024, total - off))
    md5.update(blok)
    sha1.update(blok)
    off += len(blok)
    print(f"\r{off * 100 // total}%", end="", file=sys.stderr)
print(file=sys.stderr)
print("Ukuran media :", total, "byte")
print("MD5          :", md5.hexdigest())
print("SHA1         :", sha1.hexdigest())
