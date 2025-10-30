from tracker import RekapKelas, build_markdown_report, save_text
import os
from pathlib import Path
import csv

# Fungsi untuk memuat data CSV
def load_csv(path):
    p = Path(path)
    if not p.exists():
        print(f"File {path} tidak ditemukan.")
        return []
    with p.open(encoding='utf-8') as f:
        return list(csv.DictReader(f))

def bootstrap_from_csv(rekap, att_path, grd_path):
    """Muat data mahasiswa, kehadiran, dan nilai dari file CSV ke objek RekapKelas."""
    att = load_csv(att_path)
    grd = load_csv(grd_path)
    if not att or not grd:
        print("Tidak ada data yang dimuat (file kosong atau tidak ditemukan).")
        return

    by_grades = {g.get('nim') or g.get('student_id'): g for g in grd}

    for row in att:
        nim = row.get('nim') or row.get('student_id')
        nama = row.get('nama') or row.get('name') or ''
        try:
            rekap.tambah_mahasiswa(nim, nama)
        except Exception:
            pass

        # Jika kehadiran berbentuk week1, week2, dst.
        weeks = [k for k in row.keys() if k.lower().startswith('week')]
        if weeks:
            total = len(weeks)
            hadir = sum(int(row[w].strip() or 0) for w in weeks)
            persen = round(hadir / total * 100.0, 2)
        else:
            persen = float(row.get('hadir_persen', 0) or 0)

        try:
            rekap.set_hadir(nim, persen)
        except Exception:
            pass

    for nim, g in by_grades.items():
        if nim in rekap.data:
            try:
                rekap.set_penilaian(
                    nim,
                    quiz=float(g.get('quiz', 0) or g.get('kuis', 0) or 0),
                    tugas=float(g.get('tugas', g.get('assignment', 0)) or 0),
                    uts=float(g.get('uts', g.get('mid', 0)) or 0),
                    uas=float(g.get('uas', g.get('final', 0)) or 0),
                )
            except Exception:
                pass

    print("Data berhasil dimuat dari CSV.")


# Program utama
def main():
    os.makedirs("data", exist_ok=True)
    os.makedirs("out", exist_ok=True)
    r = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Muat data dari CSV")
        print("2) Tambah mahasiswa")
        print("3) Ubah presensi")
        print("4) Ubah nilai")
        print("5) Lihat rekap")
        print("6) Simpan laporan Markdown")
        print("7) Keluar")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            bootstrap_from_csv(r, "data/attendance.csv", "data/grades.csv")

        elif pilih == "2":
            nim = input("NIM: ").strip()
            nama = input("Nama: ").strip()
            try:
                hadir = float(input("Persentase hadir (%): ").strip() or 0)
            except ValueError:
                hadir = 0

            try:
                r.tambah_mahasiswa(nim, nama)
                r.set_hadir(nim, hadir)
                print(f"Mahasiswa {nama} ditambahkan dengan kehadiran {hadir}%.")
            except Exception as e:
                print("Error:", e)

        elif pilih == "3":
            nim = input("NIM: ").strip()
            persen = float(input("Persentase hadir (%): ").strip() or 0)
            try:
                r.set_hadir(nim, persen)
                print("Presensi diperbarui.")
            except Exception as e:
                print("Error:", e)

        elif pilih == "4":
            nim = input("NIM: ").strip()
            quiz = float(input("Nilai Quiz: ").strip() or 0)
            tugas = float(input("Nilai Tugas: ").strip() or 0)
            uts = float(input("Nilai UTS: ").strip() or 0)
            uas = float(input("Nilai UAS: ").strip() or 0)
            try:
                r.set_penilaian(nim, quiz=quiz, tugas=tugas, uts=uts, uas=uas)
                print("Nilai diperbarui.")
            except Exception as e:
                print("Error:", e)

        elif pilih == "5":
            print("\n--- Rekap Nilai Mahasiswa ---")
            data = r.rekap()
            if not data:
                print("Belum ada data mahasiswa.")
            else:
                # header tabel
                print(f"{'NIM':<10} {'Nama':<15} {'Hadir (%)':<10} {'Nilai Akhir':<13} {'Predikat':<10}")
                print("-" * 60)

                # isi tabel
                for row in data:
                    print(f"{row['nim']:<10} {row['nama']:<15} {row['hadir']:<10.1f} {row['nilai_akhir']:<13.2f} {row['predikat']:<10}")

        elif pilih == "6":
            data = r.rekap()
            if not data:
                print("Belum ada data untuk disimpan.")
            else:
                report = build_markdown_report(data)
                save_text("out/report.md", report)
                print("Laporan disimpan di out/report.md")

        elif pilih == "7":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
