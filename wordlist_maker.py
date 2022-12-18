import importlib

# Kütüphaneleri yükleme işlemlerini gerçekleştir
try:
    import tkinter as tk
except ImportError:
    importlib.import_module("tkinter")

try:
    import itertools
except ImportError:
    importlib.import_module("itertools")

# Geri kalan kod parçacığı
window = tk.Tk()
window.title("wordlist maker")

entry = tk.Entry(window)
entry.pack()


def generate_combinations():
    words = entry.get().split()
    combinations = itertools.combinations(words, 2)
    with open("combinations.txt", "w") as f:
        for combination in combinations:
            f.write(" ".join(combination) + "\n")
    print("Kombinasyonlar dosyaya yazıldı.")


button = tk.Button(window, text="make wordlist", command=generate_combinations)
button.pack()
window.mainloop()
