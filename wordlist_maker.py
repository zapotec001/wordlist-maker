import tkinter as tk
import itertools

window = tk.Tk()
window.title("wordlist maker")

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="make wordlist", command=generate_combinations)
button.pack()
def generate_combinations():
    words = entry.get().split()
    combinations = itertools.combinations(words, 2)
    with open("combinations.txt", "w") as f:
        for combination in combinations:
            f.write(" ".join(combination) + "\n")
    print("Kombinasyonlar dosyaya yazıldı.")
window.mainloop()
