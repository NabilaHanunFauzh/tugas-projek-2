class Mahasiswa:
    """Kelas Mahasiswa menyimpan data NIM, nama, dan persentase kehadiran."""

    def __init__(self, nim, nama, hadir_persen=0):
        self.nim = nim
        self.nama = nama
        # jika nilai hadir tidak valid, set otomatis ke 0
        try:
            self.hadir_persen = float(hadir_persen)
        except Exception:
            self.hadir_persen = 0.0

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Persentase hadir harus berupa angka")
        if value < 0 or value > 100:
            raise ValueError("Persentase hadir harus antara 0–100")
        self._hadir_persen = value

    def __repr__(self):
        return f"<Mahasiswa {self.nim} - {self.nama}, hadir {self.hadir_persen}%>"
