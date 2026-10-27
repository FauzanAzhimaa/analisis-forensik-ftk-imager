"""Mengekstrak semua file (termasuk yang terhapus) dan menghitung MD5-nya.
Pemakaian: python3 recover.py BUKTI01.E01 folder_hasil
"""
import hashlib
import os
import sys

import pytsk3

from _ewf import buka_e01, offset_partisi

_, img = buka_e01(sys.argv[1])
fs = pytsk3.FS_Info(img, offset=offset_partisi(img))
out = sys.argv[2]
os.makedirs(out, exist_ok=True)


def ekstrak(direktori, path):
    for e in direktori:
        nama = e.info.name.name.decode("utf8", "replace")
        if nama in (".", "..") or nama.startswith("$") or e.info.meta is None:
            continue
        m = e.info.meta
        status = "AKTIF" if e.info.name.flags & pytsk3.TSK_FS_NAME_FLAG_ALLOC else "TERHAPUS"
        if m.type == pytsk3.TSK_FS_META_TYPE_DIR:
            if status == "AKTIF":
                ekstrak(e.as_directory(), f"{path}/{nama}")
            continue
        data = e.read_random(0, m.size) if m.size else b""
        tujuan = os.path.join(out, (path.strip("/").replace("/", "__") + "__" if path else "") + nama)
        with open(tujuan, "wb") as f:
            f.write(data)
        print(f"{status}\t{path}/{nama}\t{m.size}\t{len(data)}\t{hashlib.md5(data).hexdigest()}\t{data[:4].hex()}")


print("status\tpath\tukuran_metadata\tbyte_terbaca\tmd5\tbyte_awal")
ekstrak(fs.open_dir("/"), "")
