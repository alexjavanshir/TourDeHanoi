from tkinter import Tk, Button, Label, Frame, StringVar
from time import sleep
 
 
def hanoi(n, tour_un, tour_deux, tour_trois, root):
 
    if n == 1:
        tour_trois.append(tour_un.pop())
        root.update()
 
    else:
        hanoi(n - 1, tour_un, tour_trois, tour_deux, root)
        tour_trois.append(tour_un.pop())
        root.update()
        hanoi(n - 1, tour_deux, tour_un, tour_trois, root)
 
 
class TowersRepr(Tk):
 
 
    def __init__(self, tower1, tower2, tower3):
 
        Tk.__init__(self)
 
        self.tower1 = tower1
        self.tower2 = tower2
        self.tower3 = tower3
 
        self.play_next_move = False
 
        self.display = StringVar(self)
        Label(self, textvariable=self.display).pack()
 
        Button(self, text="go !", command=self.do_play_next_move).pack()
 
    def update_repr_towers(self):
 
        txt = "\n".join(" ".join(map(str, tower)) for tower in (self.tower1, self.tower2, self.tower3))
        self.display.set(txt)
 
    def do_play_next_move(self):
 
        self.play_next_move = True
 
    def update(self):
 
        self.play_next_move = False
        self.update_repr_towers()
 
        # on attend que l'utilisateur appuie sur le boutton pour reprendre
        while not self.play_next_move:
            sleep(0.01)
            Tk.update(self) # régulièrement l'application se remet à jour
 
        # l'utilisateur a appuyé sur le boutton, on repasse la main au code appelant
        # (la fonction hanoi)
 
 
taille = int(input('Quel est le rayon de la plus grande rondelle ?\n Donner un \
nombre/chiffre entier... : '))
l1 = [i for i in range(1, taille + 1)]
l1.reverse()
l2 = []
l3 = []
 
root = TowersRepr(l1, l2, l3)
 
root.update()
 
hanoi(taille, l1, l2, l3, root)