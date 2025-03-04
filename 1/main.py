import json
from datetime import datetime


def dosyaokuma():
    try:
        with open("notdefteri.json","r",encoding="utf-8") as file:
             data= json.load(file)
             if isinstance(data, list):
                 return data
             else:
               return []
    except(FileNotFoundError, json.JSONDecodeError):
        return[]

def doysayazma(notes):
    with open("notdefteri.json","w",encoding="utf-8") as file:
        return json.dump(notes,file,ensure_ascii=False, indent=4)



def sırala():
    notes=dosyaokuma()
    for note in notes:
        if "tarih" not in note:  # Eğer tarih yoksa, tarihi ekle
            note["tarih"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notes.sort(key=lambda x:x["tarih"],reverse=True)

def not_al():
    notlar=input("Notunuzu yazabilirsiniz:")
    note ={
        "metin":notlar,
        "tarih":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    notes=dosyaokuma()
    notes.append(note)
    doysayazma(notes)


def menu():
    while True:

        secenek=int(input("dosyaya yazmak için 1'yi\n dosyaya yazdıklarınızı zamana göre sıralamak için 2'yi\n çıkış için 3'ü"))
        if secenek==1:
            not_al()

        if secenek==2:
            sırala()

        if secenek==3:
            break


menu()