import sys
sys.path.append("C:\Python311\Lib\site-packages\streamlit")
import streamlit as strlit

# Set of Rules
rules_kalimat = [["K", "SPO"],
          ["K", "SPOKet"],
          ["K", "SPOpel"],
          ["K", "SPKet"],
          ["K", "SP"],
          ["K", "SPpel"],
          ["K", "SPOpelKet"],
          ["K", "SPpelKet"]]
pembagian_Rules = [["S", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "PropNounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "NumNoun", "NumPAdv"],
         ["P", "Verb", "VerbAdj", "AdjAdj", "VerbVerb", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "PropNounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "NumNoun"],
         ["O", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun", "PropNounNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun"],
         ["pel", "AdvVerb", "AdvAdj", "AdjAdj", "AdvAdj", "Adj", "PrepPrep", "PrepAdj", "PrepPronoun", "PrepPropNoun", "PrepNoun", "PrepVerb", "PrepNum", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun", "PropNounNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "Verb", "VerbAdj", "AdjAdj", "VerbVerb", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "PropNounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "NumNoun"],
         ["Ket", "PrepPronoun", "PrepPropNoun", "PrepNoun", "PrepAdj",  "PrepVerb", "PrepNum", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumNoun", "PropNounNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "Verb", "VerbAdj", "AdjAdj", "VerbVerb", "Noun", "Pronoun", "PropNoun", "NounAdj", "PronounNoun", "PropNounNoun", "NounAdv", "NounPronoun", "NounPropNoun", "NumP", "Num", "NounNumP", "NounNum", "NumPNoun", "NounNoun", "NumNoun"]]

num = "Num | tiga puluh dua | seratus dua puluh | tiga | sebelas | tiga puluh | lima ratus | dua | sembilan | empat | satu | sembilan belas ribu tiga ratus enam puluh | lima | empat puluh lima | dua puluh | lima belas | sepuluh | berempat | berdua | bertiga | berlima | bersembilan | berenam | bertujuh | bersepuluh | bersebelas | berdelapan | empat belas | tiga belas | dua puluh | lima belas | berdua-lima | berenam belas | banyak | berbagai | pelbagai | sedikit | semua | seluruh | segala | segenap | berpuluh-puluh | beratus-ratus | beribu-ribu | berjuta-juta | belasan | puluhan | ratusan | ribuan | beberapa | sebagian | separuh | segelintir | ketiga | kedua | kesembilan | kesebelas | keempat belas | kedua-puluh-lima | kelima belas | kedua puluh satu | pertama | keenam | ketiga belas | keenam belas | ketujuh belas | kedelapan belas | kesembilan belas | kedua puluh | dua | lima | tiga | delapan | enam | tujuh | bertujuh | bersepuluh | kedua | ketiga | keempat | kelima | kesepuluh | keseratus | kedelapan | seorang | ribuan | lima | seekor | tiga | ratusan | tujuh ratus | juta | banyak | 11 | 3  | 25 | kedua | 5 | seikat | setangkai | sepasang | 10 | dua puluh | separuh | 15 | 2 | 1 | 7 | setengah | 8 | bertahun-tahun | 27 | delapan | selusin | beberapa | berhari-hari | semua | sebagian | berbulan – bulan | setiap | seluruh | kedua | semangkok"
adv = "Adv | sedang | sudah | baru | saja | sangat | telah | akan | selalu | selamanya | sering | harus | sekali | masih | lagi | hanya | makin | begitu | nya | dapat | sempat | ingin"
adj = "Adj | aktif | sungguh | pusing | khawatir | baik | syok | megah | pintar | kompak | akrab | baru | kembar | segar | bagus | pintar | berat | mahal | bagus | keren | cantik | lebar | sama | tua | kecil | keras | besar | menarik | terkenal | bahagia | handal | pemarah | pendiam | senang | tangguh | pelupa"
verb = "Verb | membutuhkan | memiliki | memerlukan | membangun | menyebar | memandikan | melihat | berkurban | membaca | memberhentikan | menjual | meminjam | menyewakan | membeli | datang | bermain | membuat | membersihkan | merapikan | terpisahkan | melaksanakan | liburan | bekerja | menghadapi | dilestarikan | diikuti | dibungkam | datang | gotong royong | mengucapkan | bertahan | beribadah | bersama-sama | menjadi | bergotong royong | mengalami | menderita | meninggal | mengungsi | menolak | melanggar | bersembunyi | melanggar | ditendang | menulis | menginjak | turun | kalah | memperoleh | terpilih | menjadi | merayakan | mendapat | merayakan | bertelur | berada | didapatkan | pergi | memerlukan | membeli | mempunyai | menjual | mencari | mempunyai | bermain | membaca | membangun | belajar | memakan | bermain | memanjat | menyembunyikan | membangun | menonton | dijual | mengambil | melempar | mengerjakan | memberikan | membaca | berisi | membersihkan | berdatangan | menanam | bercucuran | menyelesaikan | bermandikan | berpegangan | melontarkan | berjatuhan | berlatih | beranggotakan | pergi | memecahkan | menyulutkan | mendaftar | mencetak | dikumpul | mendapatkan | bertemu | menarik | memadati | menyeruduk | menghampiri | membeli | dibagikan | membantu | menonton | mengangkat | memasuki | mengerjakan | mengendarai | ditulis | menghadiri | bermain | meninggal | ada | membeli | mencuci | menjual | mempunyai | memiliki | mengganti | merenovasi | memakan | menggoreng | memasak | memetik | memelihara | menebang | meminjam | menyembelih | tersisa | membawa | makan | tinggal | diikuti | dianjurkan | minum | tidur | wisata | selama | memuat | berkurban | disaksikan | membuat | menampilkan | muncul | dihapus | terjadi | melakukan | mengoleksi | terasa | memiliki | mendaki | merupakan | terlihat | terdengar | menjadi | bermain | mengajar | makan | minum | terjatuh | hidup | tercinta | mencekam | menjemukan | mengerikan | memalukan | menjijikan | terpukau | terbengkalai | menakutkan | menentramkan | mengubah | berbahaya | menelan | terlantar | diasuh | memerankan | berbahaya | membuat | terkejut | memiliki | memukau | merekam | mengharukan | memalukan | menarik| memikat | memarahi | membunuh | ditangkap | membantu| adalah | membawa | dikalahkan | merasakan | menolak | menyedihkan | menonton | melawan | menghantui | mencekam | membanggakan | mengherankan | beristirahat | tertidur | berlajan |  bisa | membelikan | berdarah | mencekam | menuduh | menawarkan | terkenal | memelihara | berbahaya | mengakui | mendapatkan | menyukai | menakutkan | tercinta | memenangkan | tinggal | mengajak | membuat | menjadi | tidur | menyenangkan | membeli | melemparkan | menyebabkan | memakai | terkenal | terharu | melukai | kehilangan | membanggakan | memikat | mengusir | dapat | terlantar | menceritakan | menggembirakan | berbekas"
noun = "Noun | acara | orang | panitia | bapak | ekor | ayam | penerbit | penyunting | lagu | pertandingan | pemain | cadangan | perusahaan | unit | rumah | benih | ikan | lele | kucing | petani | sawah | benua | musim | kambing | tahun | universitas | hutan | mahasiswa | buah | buku | perpustakaan | kampus | karyawan | ibu | setel | baju | olah-raga | biologi | unit | mikroskop | kamera | es | krim | toko | basket | tugas | sekolah | selokan | jendela | kamar | kursi-kursi | sejoli | sekawan | serangkai | anggota | geng | mall | bersahabat | anggota | taman | bersaudara | sekelas | masalah | adonan | air | aturan | rakyat | rejeki | penjuru | organisasi | terima kasih | tengkorak | tahun | umat | muslim | depan | budak | tragedi | luka | bencana | gempa | tragedi | pengungsi | bantuan | kode | etik | pelajar | tentara | hutan | bakau | oknum | polisi | prosedur | bola | pemain | jawaban | adikku | lapangan | tim | sepak bola | kali | pak | penghargaan | pengabdian | pengabdian | relawan | perusahaan | hari jadi | peringkat | kelas | ulang tahun | masalah | ayam | bupati | anak | keluarga | buku | deret | teluk | pagi | jam | kegiatan | ibu | orang | motor | roda | ayah | buah | semangka | buah | buku | tulis | pensil | bu | unit | sepeda | sapi | setel | baju | sekolah | acara | sofa | pasang | sepatu | kamar | hotel | mangga | rumah | durian | pohon | buaya | anak | bola | lapangan | perpustakaan | serangkai | saudara | sekawan | taman | apel | belakang | kartu | pos | ronda | gazebo | laptop | adik | tetangga |  bersaudara | dalam | kota | tugas | kafe | sahabat | patung | kuda | rumput | kandang | gula | kopi | hal | jawaban | ujian | ibu | penjuru | anggota | tni | pengunjung | tiket | halaman | air | mata | persoalan | keringat | insan | tangan | tas | permen | cerita | korban | perang | petak | umpet | siswa | upacara | bendera | kelompok | rombongan | gelas | suara | penonton | laptop | generasi | edisi | kaset | peserta | pasien | rumah | sakit | pemain | gol | urutan | tas | makalah | kampus | siswa | bantuan | gadis | seseorang | tali | orang | lapangan | banteng | orang-orang | jalan | serdadu | bapak | karcis | eksemplar | buku | acara | bedah | mahasiswa | masyarakat | pasang | mata | pertandingan | wasit | bendera | pinggir | lapangan | pemain | ruangan | tugas | sepeda | listrik | jawaban | papan tulis | rapat umum | pantai | sapi | pensil | buah | apel | ibu | adik | baju | korban | tsunami | ayah | motor | paman | istri | unit | laptop | ban | mobil | rumah | mangga | kakak | kakek | telur | ikat | kangkung | bayam | sawah | kilogram | daging | bunga | mawar | penjual | ayam | ikan | mujair | petak | gorengan  | meja | kerja | potong | puding | kambing | tugas | wasit kedua | kuliah | sisir | pisang | proposal | atas | meja | ponsel | kucing | Mangga | beras | rapat daring | kg | sandal | rumah | konglomerat | manusia | gula | mobil | galon | air | kantor | gedung | pembangunan | tanaman | kebun | jenis | objek | kampungku | jam | sehari | ember | liter | warung | cangkir | kopi | video | juta | penonton | kemarin | dunia | suara | burung | pepohonan | suasana | malam | kedatangan | kepala | sekolah | kelas | serigala | hutan | keadaannya | kecelakaan | tangan-tangan | mimpiku | suara-suara | penonton | turis | pantai | hadirin | seisi | presentasi | kelompok | galaksi | pemain | film | adegan | kejadian | orang | seniman | lukisan-lukisan | belatung | mie | rumah | internet | dosen | nilainya | anjing | pembicara | seminar | keindahan | kualitas | grafisnya | negara | provinsi | hal-hal | hal | keluarga | tempat | kuburan | hawa | gunung | sebagian | film-film | keganasannya | lagu | tindakan | bangsa | masa | penjajahan | dahulu | cara | permainan | pembawa | acara | penampilan | opera | lelucon | pelawak | cerita | isi | berita | pembicaraan | olahraga | wahana | taman | pengunjung | rumahmu | makanan | minuman | selama | rasa | snack | pemandangan | kepemimpinan | gaya | bicara | hewan | kondisi | hasil | pekerjaan | perbuatan | kakak | servis | kelakuan | anak | paman | diri | depan | pertandingan | hukum | riasan | wanita | kecuraman | jalan | pejalan | kaki | kemarin | wajah | motor | kucing | adalah | senyum | tawa | tadi | kehilangan | bom | atom | kesepian | Kejadian | persepsi | masyarakat | wahana | korban | anak | paman | adegan | adik | teman | orang | paras | pengalaman | hal |gadis | perhatian | wanita | hati | bujang | pemalu | pacar | pria | pendendam | remaja | pencuri | polisi | orang | penyayang | kakek | seorang | pejuang | negara | banteng | perusak | kebun | kelapa | sawit | malam | petinju | turnamen | film | bioskop | sekolah | suasana | pantai | olimpiade | matematika | ayah | uang | rumah | pemotong | kayu | desa | pria | penipu | kantor | polisi | pemalas | Prestasi | Pejuang | tenda | kelas | kukang | hewan | hutan | peneliti | laboratorium  | Penyabar | taman | kota | bakso | anjing | Pria | tangan | pejuang | tongkat | pertandingan | penyayang | Pengalaman | parfum | Ibu | Bapak | bunga | mawar | kayu | perusak | hadiah | rumah | kucing | masyarakat | pengalaman | onar | sifat | pemaaf | wanita | pencuri | kue | rumah | konser | burung | bulu | lagu | saat | hakim | pengampun | kasus | kakak | depan | umum | pemberontak | nenek | pelupa | kancil | pembohong"
pronoun = "Pronoun | kami | itu | saya | ini | mereka | kalian | kita | kamu | anda | ia | ku | sesuatu"
propnoun = "PropNoun | Ngurah | Adi | Dimas | Eropa | Udayana | Paragon | Trisna | Aris | PKK | Bali | Monas | Cianjur | Kanjuruhan | Benoa | Adit | Parman | Made | Rudi | Ketut | Klungkung | Putu | Botak | Darma | Dewi | Santi | Winda | Andri | Wendi | Weli | Asti | Wendy | Budi | Tuli | Aris | Surabaya | Amir | Inggris | Amanda | mangrove | Widia | Singaraja | Yanto | Sista | TBO | Anto | Lita | Gunggus | Bhadrika | Salim | Ary | Eka | Saleh | Fredy | Andi | Kadir | Wawin | Surya | Mahayasa | Fika | Okta | Lindung | dede | lohan | Rama | Bella | Nia | Widia | Budi | Alit | Faisal | Gagak | Kuta | Shawn Mendes | Cyberpunk 2077 | Bima Sakti | Biznet | Indonesia | iPhone | Nanggroe Aceh Darussalam | Piranha | Jepang | Hantu | Udin | Akhirudin | Awaludin | Kirudin | Kamarudin | Samsudin | Saipudin | Sarafudin | Bahrudin | Yando | Dila | Arga | Deni | Wena | Arya | Rika"
prep = "Prep | di | dari | dengan | untuk | setelah | karena | ke | akibat | sampai | pada | oleh | kepada | bagi | dalam | secara | supaya | hingga | si"

data = [ ]
data.append(num.split(" | "))
data.append(adv.split(" | "))
data.append(adj.split(" | "))
data.append(verb.split(" | "))
data.append(noun.split(" | "))
data.append(pronoun.split(" | "))
data.append(propnoun.split(" | "))
data.append(prep.split(" | "))
# karena berbentuk string dengan pemisah " | ", maka harus dipisah

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
      # jika notasi terdapat dalam aturan, maka bisa diganti menjadi contoh : SPO
      if j in string1:
        string2 = string2 + daftar1[i][0]
  return stringUnik(string2)

# fungsi ini digunakan untuk menginisiasi triangle table filling
def inisiasiTableFill(daftar1 : list, daftar2 : list, arrayTableFill : list):
  for i in range(0, len(daftar1)):
    for j in range(len(daftar2)):
      # jika elemen pada daftar2 ada pada daftar1, maka dapat diubah
      for k in daftar2[j][1:]:
        if k in daftar1[i]:
          arrayTableFill[i][0] = daftar2[j][0]
  return arrayTableFill

# fungsi untuk menambah string dalam table filling
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

strlit.write("""
# Application of CFG in Syntactic Parsing
Simple Application for Checking *Standard Sentence Pattern* for Fulfill The Final Project of the "Teori Bahasa dan Automata" Subject at Teknik Informatika Udayana University's Lectures.
_____________________________________
Kelompok 1
Kameliya Putri (2108561019)
Yehezkiel Batara Lumbung (21018561048)
Ketut Agus Cahyadi Nanda (2108561079)
I Gede Ngurah Arya Wira Putra (2108561119)
""")

input = strlit.text_input("Input the String that you want to check:")
cek = strlit.button("Check It!")

if cek:
    if cek_kalimat(input) == 1:
        strlit.success("It's Standard Sentence! Congratulations...")
    else:
        strlit.error("Unfortunately, Your String is non-Standard. Try Again!")
