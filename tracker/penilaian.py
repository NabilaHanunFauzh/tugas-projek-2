"""Modul Penilaian: menghitung nilai akhir mahasiswa"""

class Penilaian:
    """Menyimpan komponen nilai dan menghitung nilai akhir berbobot."""
    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self._quiz = 0.0
        self._tugas = 0.0
        self._uts = 0.0
        self._uas = 0.0
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def _validate(self, v):
        v = float(v)
        if v < 0 or v > 100:
            raise ValueError("nilai harus 0-100")
        return v

    @property
    def quiz(self): return self._quiz
    @quiz.setter
    def quiz(self, v): self._quiz = self._validate(v)

    @property
    def tugas(self): return self._tugas
    @tugas.setter
    def tugas(self, v): self._tugas = self._validate(v)

    @property
    def uts(self): return self._uts
    @uts.setter
    def uts(self, v): self._uts = self._validate(v)

    @property
    def uas(self): return self._uas
    @uas.setter
    def uas(self, v): self._uas = self._validate(v)

    def nilai_akhir(self):
        skor = (
            self.quiz * 0.15 +
            self.tugas * 0.25 +
            self.uts * 0.25 +
            self.uas * 0.35
        )
        return round(skor, 2)
