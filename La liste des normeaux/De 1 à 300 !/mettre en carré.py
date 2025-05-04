import tkinter as tk
from tkinter import messagebox
from PIL import Image
import os

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Transformateur de PNG en Carré")
fenetre.geometry("400x300")

def process_all_png():
    # Récupérer et vérifier la taille du carré entrée par l’utilisateur
    try:
        size = int(entry_size.get())
    except Exception:
        messagebox.showerror("Erreur", "Veuillez spécifier une taille valide.")
        return

    # Obtenir la liste de tous les fichiers PNG dans le répertoire courant
    current_dir = os.path.dirname(os.path.abspath(__file__))
    png_files = [f for f in os.listdir(current_dir) if f.lower().endswith('.png')]
    
    if not png_files:
        messagebox.showinfo("Information", "Aucun fichier PNG n'a été trouvé dans le dossier courant.")
        return

    # Créer un dossier de sortie pour conserver les images transformées
    output_dir = os.path.join(current_dir, "squares")
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    processed_count = 0
    # Parcourir chaque fichier PNG et créer une version centrée et sans rognage
    for filename in png_files:
        try:
            img = Image.open(filename)
            # Redimensionner l’image proportionnellement pour qu’elle tienne dans le carré
            img.thumbnail((size, size))
            # Créer un fond transparent carré
            img_square = Image.new("RGBA", (size, size), (255, 255, 255, 0))
            # Calculer l’offset pour centrer l’image dans le carré
            offset_x = (size - img.width) // 2
            offset_y = (size - img.height) // 2
            img_square.paste(img, (offset_x, offset_y))
            # Définir le nom du fichier de sortie en ajoutant un suffixe "_square"
            base = os.path.splitext(filename)[0]
            output_filename = f"{base}_square.png"
            output_path = os.path.join(output_dir, output_filename)
            img_square.save(output_path)
            processed_count += 1
        except Exception as e:
            print(f"Erreur lors du traitement de {filename} : {e}")

    messagebox.showinfo("Succès", f"{processed_count} fichiers ont été traités et enregistrés dans le dossier:\n{output_dir}")

# Création des widgets dans l’interface
label_intro = tk.Label(fenetre, text="Transformer vos PNG en carrés centrés et intacts")
label_intro.pack(pady=10)

label_size = tk.Label(fenetre, text="Entrer la taille du carré :")
label_size.pack(pady=5)

entry_size = tk.Entry(fenetre)
entry_size.pack(pady=5)
entry_size.insert(0, "1000")  # Valeur par défaut

button_process = tk.Button(fenetre, text="Traiter tous les fichiers PNG", command=process_all_png)
button_process.pack(pady=20)

# Lancement de la boucle principale de l'application
fenetre.mainloop()
