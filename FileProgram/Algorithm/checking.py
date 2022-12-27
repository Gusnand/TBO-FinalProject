from Algorithm.conversion import *
from Algorithm.separator import *
# fungsi untuk mengecek nilai K pada arrayTableFill[0][akhir]
def cek_baku(daftar1 : list) -> int:
  if "K" in daftar1[0][-1]:
    return 1
  elif "K" not in daftar1[0][-1]:
    return 0

# fungsi untuk memproses kalimat dari awal
def cek_kalimat(strinx):
  # string dipecah dahulu
  strinx = strinx.split(" ") 
  # lalu buat segitiga tabel sesuai banyak kata pada string
  ar = arrayTableFill(len(strinx))
  # membuat var test untuk mengganti kata menjadi notasi kalimat (contoh : Noun, Verb)
  test = inisiasiTableFill(strinx, data, ar)
  # pemrosesan grammar tahap 1
  process1(test, len(strinx))
  # pemrosesan grammar tahap 2
  process2(test, len(strinx))
  # meminta nilai return dari fungsi cek_baku (nilai 1 atau 0)
  return cek_baku(test)