class Bacteria:
    
    def __init__(self, shape, is_gram_negative, flagella, antibiotic_resistance, is_anaerobic, x, y, is_patogenic=True):
        self.shape = shape
        self.is_gram_negative = is_gram_negative
        self.flagella = flagella
        self.antibiotic_resistance = antibiotic_resistance
        self.is_anaerobic = is_anaerobic
        self.x = x
        self.y = y
        self.is_patogenic = is_patogenic
 
 
# Create 3 instances
e_coli = Bacteria("bacillus", True, True, False, True, 20, 49, True)
s_typhi = Bacteria("bacillus", True, True, True, True, 120, 3)
s_sonnei = Bacteria("bacillus", True, False, True, True, 30, 13, True)
s_aureus = Bacteria("coccus", False, False, True, True, 22, 10, False)
k_pneumoniae = Bacteria("bacillus", True, False, False, True, 39, 40, False)