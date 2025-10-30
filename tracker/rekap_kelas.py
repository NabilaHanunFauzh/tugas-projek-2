from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """Kelas untuk mengelola data mahasiswa dan penilaian."""

    def __init__(self):
        # Menyimpan data mahasiswa dan nilai dalam dictionary
        self.data = {}

    def tambah_mahasiswa(self, nim, nama):
        """Menambahkan mahasiswa baru ke dalam rekap."""
        if nim not in self.data:
            self.data[nim] = {
                "mhs": Mahasiswa(nim, nama),
                "nilai": Penilaian()
            }
        else:
            print("Mahasiswa sudah ada dalam data.")

    def set_hadir(self, nim, persen):
        """Mengatur persentase kehadiran mahasiswa."""
        if nim in self.data:
            try:
                self.data[nim]["mhs"].hadir_persen = persen
            except ValueError as e:
                print("Error:", e)
        else:
            print("NIM tidak ditemukan dalam data.")

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        """Mengatur nilai quiz, tugas, uts, dan uas mahasiswa."""
        if nim in self.data:
            try:
                self.data[nim]["nilai"] = Penilaian(quiz, tugas, uts, uas)
            except ValueError as e:
                print("Error:", e)
        else:
            print("NIM tidak ditemukan dalam data.")

    def predikat(self, nilai_akhir):
        """Mengubah nilai akhir menjadi predikat huruf."""
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >= 70:
            return "B"
        elif nilai_akhir >= 60:
            return "C"
        elif nilai_akhir >= 50:
            return "D"
        else:
            return "E"

    def rekap(self):
        """Menghasilkan list berisi ringkasan data mahasiswa."""
        hasil = []
        for nim, item in self.data.items():
            mhs = item["mhs"]
            nilai = item["nilai"]
            akhir = nilai.nilai_akhir()
            hasil.append({
                "nim": mhs.nim,
                "nama": mhs.nama,
                "hadir": mhs.hadir_persen,
                "nilai_akhir": round(akhir, 2),
                "predikat": self.predikat(akhir)
            })
        return hasil
