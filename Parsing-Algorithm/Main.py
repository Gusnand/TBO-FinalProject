import CYK as tabelFilling
import CNF as chom

def Main():
    print("CONVERSION CFG to CNF")
    print("===========================")
    init_gramar = get_gramar()
    while True:
        print("\nCek String")
        print("Masukkan String : (ketik 0 atau 'exit' untuk keluar program.)")
        kata = input("=> ")

        if kata == "0" or kata == "exit":
            break;
        else:
            tabelFilling.CYK(kata, init_gramar)

def get_gramar():
    init_gramar = {
        "V": ["S", "X", "Y"],
        "T": ["a", "b", "c"],
        "SoP": [
            {"head": "S", "body": ["a", "X", "b", "X"]},
            {"head": "X", "body": ["a", "Y"]},
            {"head": "X", "body": ["b", "Y"]},
            {"head": "X", "body": []},
            {"head": "Y", "body": ["X"]},
            {"head": "Y", "body": ["c"]}
        ],
        "Start": "S"
    }
    chomsky = chom.CNF(init_gramar, True)
    init_gramar = chomsky.send_to_var()
    return init_gramar

Main()