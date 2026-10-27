"""Fungsi bantu: membuka file E01 dan mencari partisi pertama."""
import pyewf
import pytsk3


class EwfImg(pytsk3.Img_Info):
    def __init__(self, handle):
        self._h = handle
        super().__init__(url="", type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def read(self, offset, size):
        self._h.seek(offset)
        return self._h.read(size)

    def get_size(self):
        return self._h.get_media_size()


def buka_e01(path):
    """Mengembalikan (handle pyewf, objek Img_Info). Menerima segmen .E01 pertama."""
    segmen = pyewf.glob(path)
    h = pyewf.handle()
    h.open(segmen)
    return h, EwfImg(h)


def offset_partisi(img):
    """Byte offset partisi data pertama. Kalau tidak ada tabel partisi, 0."""
    try:
        vol = pytsk3.Volume_Info(img)
    except IOError:
        return 0
    for p in vol:
        desc = p.desc.decode(errors="replace")
        if p.len > 0 and "Unallocated" not in desc and "Table" not in desc and "Meta" not in desc:
            return p.start * vol.info.block_size
    return 0
