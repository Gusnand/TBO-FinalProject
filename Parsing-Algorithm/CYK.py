import os

class CYK():
    # Menampilkan triangular table
    def __viewTabel(self):
        for i in range(1, len(self.kata) + 1):
            for j in range(i, len(self.kata) + 1):
                print(i, end=",")
                print(j, end=" = ")
                print(self.arrTabel[i][j], end=" ")
            print(end="\n")
        print()

    # Mendapatkan variabel dan menggabungkanya menjadi 1 tuple
    def __getVariabel(self, sum, lim, i, j, k, l):
        Wi = set()
        # Memasukkan semua key dari transition dan menconcatenate
        for m in self.arrTabel[i][k]:
            for n in self.arrTabel[l][j]:
                gabung = [m, n]
                Wi.add(tuple(gabung))
        Y = set()
        for o in Wi:
            for key, value in self.init_grammar["SoP"].items():
                for m in value:
                    if tuple(o) == tuple(m):
                        Y.add(key)
        return Y

    # Mengatur perulangan sesuai rumus compare n pairs
    def __formulaCal(self, sum, lim, i, j):
        l = i
        Y = set()
        for k in range(i, j):
            l += 1
            # Menggabungkan production rule yang dituju 
            Y = Y.union(self.__getVariabel(sum, lim, i, j, k, l))
        self.arrTabel[i][j] = Y
        self.__viewTabel()
        return self.arrTabel

    # Fungsi untuk perulangan baris sepanjang lim untuk membentuk seperti segitiga
    def __repeatCal(self, sum, lim):
        for i in range(1, lim):
            j = i + sum
            self.arrTabel = self.__formulaCal(sum, lim, i, j)
        return self.arrTabel

    # Fungsi untuk mengatur kalkulasi top row
    def __multiCal(self, sum, lim):
        # Base case mengembalikan arrTabel yang sudah diisi
        if sum >= len(self.kata) or lim < 1:
            return self.arrTabel
        # Memanggil fungsi repeatCal untuk perulangan per baris
        self.arrTabel = self.__repeatCal(sum, lim)
        # Menjalankan secara rekursif untuk perulangan triangle tabel
        sum += 1
        lim -= 1
        return self.__multiCal(sum, lim)

    # Fungsi untuk iterasi pertama, mengkalkulasi bottom row
    def __firstCal(self):
        num = 0
        # Perulangan sebanyak jumlah karakter
        for k in self.kata:
            num += 1
            Wi = set()
            # Perulangan sebanyak production
            for key, value in self.init_grammar["SoP"].items():
                for m in value:
                    if set(m).issubset({k}):
                        Wi.add(key)
            # Memasukkan key-key yang didapat ke dalam tabel yang sesuai
            self.arrTabel[num][num] = Wi
        print("\n\n================ Table Filling =================\n")
        self.__viewTabel()
        return self.arrTabel
    
    # Fungsi yang akan dipanggil dalam class CYK, 
    # untuk mengatur assignment arrTabel dan pemanggilan fungsi
    def __init__(self, kata, init_grammar):
        self.kata = kata
        self.init_grammar = init_grammar
        self.arrTabel = [[' ' for x in range(len(kata)+1)] for y in range(len(kata)+1)]
        self.arrTabel = self.__firstCal()
        self.arrTabel = self.__multiCal(1, len(kata))

        self.__checkResult()

    # Mengecek hasil cell Xi,j terakhir untuk mendapatkan string valid/tidak
    def __checkResult(self):
        if len(self.arrTabel[1][len(self.kata)]) == 0:
            print("String Tidak Valid")
        else:
            print("String Valid")
        os.system("pause")