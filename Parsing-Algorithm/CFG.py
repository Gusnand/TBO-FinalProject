# Class yang merepresentasikan CFG
class CFG:
    def __check_ambiguous_symbols(self):
        # Method untuk memeriksa apakah simbol digunakan secara sesuai dengan aturan CNF atau tidak
        # aturan menggunakan 1 variabel atau 2 terminal dan tidak boleh menggabungkan variabel dan terminal
        ambiguous = set()
        ambiguous.intersection(self.variables, self.terminals)
        if len(ambiguous) > 0:
            bad_simbol = ambiguous.pop()
            pesan_error  = ("Simbol ambigu " + bad_simbol + ". Pastikan menggunakan simbol yang benar pada init grammar")
            raise Exception(pesan_error)

    def __init__(self, init_grammar):
        # membuat objek CFG dan interpretasi dari tupple
        self.init_gramar = init_grammar
        self.variables   = set(self.init_gramar["V"])
        self.terminals   = set(self.init_gramar["T"])
        self.productions = {}
        self.start       = self.init_gramar["Start"]
        self.__read_grammar()
        self.__check_ambiguous_symbols()

    def __read_grammar(self):
        get_productions  = self.init_gramar["SoP"]
            
        # Ini adalah simbol-simbol yang dapat muncul dalam produksi
        valid_symbols = set().union(self.variables, self.terminals)
        for entry in get_productions:
            key = entry["head"]
            val = entry["body"]
            # Pastikan semua simbol yang digunakan dalam produksi adalah simbol yang valid
            if (all( symbol in valid_symbols for symbol in val)):
                val = tuple(entry["body"])
            else:
                pesan_error = ("The production " + key + " => " + str(val) + " mengandung simbol-simbol yang bukan bagian dari" + " variabel atau terminal")
                raise Exception(pesan_error)
            
            # Buat daftar kosong untuk produksi saat pertama kali menemukan kunci
            if key not in self.productions:
                self.productions[key] = set()
            self.productions[key].add(val)