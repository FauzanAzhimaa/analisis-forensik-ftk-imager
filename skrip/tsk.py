"""Menampilkan tabel partisi dan semua file (aktif dan terhapus) beserta lokasinya.
Pemakaian: python3 tsk.py BUKTI01.E01
"""
import sys

import pytsk3

from _ewf import buka_e01, offset_partisi

_, img = buka_e01(sys.argv[1])
try:
    for p in pytsk3.Volume_Info(img):
        print("partisi", p.addr, p.desc.decode(errors="replace"), "mulai", p.start, "panjang", p.len)
except IOError:
    print("tidak ada tabel partisi")

off = offset_partisi(img)
fs = pytsk3.FS_Info(img, offset=off)
print("offset partisi (byte):", off, "| ukuran blok:", fs.info.block_size)


def jelajah(direktori, path):
    for e in direktori:
        nama = e.info.name.name.decode("utf8", "replace")
        if nama in (".", ".."):
            continue
        m = e.info.meta
        status = "AKTIF" if e.info.name.flags & pytsk3.TSK_FS_NAME_FLAG_ALLOC else "TERHAPUS"
        runs = []
        try:
            for atr in e:
                for r in atr:
                    runs.append((r.addr, r.len))
        except Exception as ex:
            runs = str(ex)
        print(f"{path}/{nama}\t{status}\tinode={m.addr if m else '-'}\tukuran={m.size if m else '-'}\tlokasi={runs}")
        if m and m.type == pytsk3.TSK_FS_META_TYPE_DIR and status == "AKTIF":
            jelajah(e.as_directory(), f"{path}/{nama}")


jelajah(fs.open_dir("/"), "")
