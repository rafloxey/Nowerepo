class Auto:
    def __init__(self, waga):
        self.waga = waga
    
    def jedz(self):
        print("Jadę !")
        
class AutoSpalinowe(Auto):
    def __init__(self, ilość_cylindrów, waga):
        self.ilość_cylindrów = ilość_cylindrów
        super().__init__(waga)
    def sprawdz_olej(self):
        return("Olej jest ok!")
    
class Polonez(AutoSpalinowe):
    def __init__(self, model, ilość_cylindrów, waga):
        self.model = model
        super().__init__(ilość_cylindrów, waga)
    def jazda_bokiem(self):
        print("Jadę bokiem!")
        
    
        
    
auto_spalinowe = Polonez("Wścieknięty", 8, 1500)
print(auto_spalinowe.sprawdz_olej())
print(auto_spalinowe.model)
        
        
        