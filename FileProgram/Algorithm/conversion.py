from Algorithm.setOfRule import *

# array with table filling triangle
def arrayTableFill(n : int) -> list:
  daftar1 = [ ]
  # segitiga yg dibuat adalah segitiga menurun
  for i in range(n, 0, -1):
    daftar2 = [ ]
    for j in range(i):
      daftar2.append("")
    daftar1.append(daftar2)
  return daftar1

# fungsi untuk konkatenasi 2 string
def konkatenasiStr(string1 : str, string2 : str) -> str:
  string3 = ""
  for i in string1:
    for j in string2:
      string3 = string3 + (i + j)
  return string3

# fungsi untuk mencari nilai unik dalam string
def stringUnik(string1 : str) -> str:
  string3 = ""
  for i in string1:
    # jika tidak ada dalam string3, maka nilai unik bisa ditambahkan
    if i not in string3:
        string3 = string3 + i
  return string3

# fungsi untuk mengubah string ke dalam notasi kalimat (contoh : SPO)
def konversi(string1 : str, daftar1 : list) -> str:
  string2 = ""
  for i in range(len(daftar1[:])):
    for j in daftar1[i][1:]:
      # jika elemen pada daftar1 ada pada string, dengan kata lain
      # jika notasi terdapat dalam aturan, maka bisa diganti menjadi contoh : SPO
      if j in string1:
        string2 = string2 + daftar1[i][0]
  return stringUnik(string2)

# fungsi ini digunakan untuk menginisiasi triangle table filling
def inisiasiTableFill(daftar1 : list, daftar2 : list, arrayTableFill : list):
  for i in range(0, len(daftar1)):
    for j in range(len(daftar2)):
      # ada perubahan string ke notasi kalimat (contoh : noun)
      # jika elemen pada daftar2 ada pada daftar1, maka dapat diubah
      for k in daftar2[j][1:]:
        if k in daftar1[i]:
          arrayTableFill[i][0] = daftar2[j][0]
  return arrayTableFill

# fungsi untuk menambah string dalam segitiga tabel feeling
def kalkulasi(y : int, x : int, daftar1 : list):
  # pada fungsi ini, koordinat x dan y dikurangi 1 agar sesuai indeks
  x -= 1
  y -= 1
  i = 0
  j = y + 1
  k = x - 1
  while(i < x):
    # operasi yang dilakukan dalam loop adalah
    # arrayTableFill[i][j] = arrayTableFill[i][i] + arrayTableFill[i + 1][j - 1]
    daftar1[y][x] = daftar1[y][i] + daftar1[j][k]
    i += 1
    j += 1
    k -= 1

# fungsi untuk memproses arrayTableFill yang sudah diinisiasi dengan fungsi inisiasiTableFill
def process1(daftar1 : list, x : int):
  tempX = x
  for i in range(1, x+1):
    for j in range(1, tempX+1):
      # pertama, dilakukan fungsi kalkulasi untuk menambah string pada
      # indeks arrayTableFill yang ditentukan berdasarkan 2 loop bersarang di atas
      kalkulasi(j, i, daftar1)
    tempX -= 1
  tempX = x
  for i in range(0, x):
    for j in range(1, tempX):
      # setelah penambahan string, dilakukan konversi untuk mengubah
      # string ke aturan-aturan grammar
      temp = daftar1[i][j]
      temp = konversi(temp, pembagian_Rules)
      daftar1[i][j] = temp
    tempX -= 1

# fungsi untuk proses kedua untuk proses tabelQ
def process2(daftar1 : list, x : int):
  tempX = x
  for i in range(0, x):
    for j in range(1, tempX):
      temp = daftar1[i][j]
      # konversi lagi sekali dilakukan untuk menentukan nilai "K"
      # yang dimana K tersebut merupakan string yang menandakan kalimat baku
      temp = konversi(temp, rules_kalimat)
      daftar1[i][j] = temp
    tempX -= 1
  # untuk melihat hasil, digunakan print
  for i in range(0, x):
    print(daftar1[i][:])
