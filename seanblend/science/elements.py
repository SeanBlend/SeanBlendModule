class Element:
    def data(self):
        return f"Name: {self.name}\nChemical Symbol: {self.chemical_symbol}\nAtomic Mass: {self.atomic_mass}\nAtomic Number: {self.atomic_number}\nSeries: {self.series}"

    def __repr__(self):
        return f"{self.name.lower()} element object"


class Hydrogen(Element):
    name = "Hydrogen"
    chemical_symbol = "H"
    atomic_mass = 1.0079
    atomic_number = 1
    series = "Reactive Metals (Natrual)"

class Helium(Element):
    name = "Helium"
    chemical_symbol = "He"
    atomic_mass = 4.0026
    atomic_number = 2
    series = "Mainly Non-metals (Natrual)"

class Lithium(Element):
    name = "Lithium"
    chemical_symbol = "Li"
    atomic_mass = 6.941
    atomic_number = 3
    series = "Reactive Metals (Natrual)"

class Beryllium(Element):
    name = "Beryllium"
    chemical_symbol = "Be"
    atomic_mass = 9.0122
    atomic_number = 4
    series = "Reactive Metals (Natrual)"

class Boron(Element):
    name = "Boron"
    chemical_symbol = "B"
    atomic_mass = 10.811
    atomic_number = 5
    series = "Mainly Non-metals (Natrual)"

class Carbon(Element):
    name = "Carbon"
    chemical_symbol = "C"
    atomic_mass = 12.011
    atomic_number = 6
    series = "Mainly Non-metals (Natrual)"

class Nitrogen(Element):
    name = "Nitrogen"
    chemical_symbol = "N"
    atomic_mass = 14.007
    atomic_number = 7
    series = "Mainly Non-metals (Natrual)"

class Oxygen(Element):
    name = "Oxygen"
    chemical_symbol = "O"
    atomic_mass = 15.999
    atomic_number = 8
    series = "Mainly Non-metals (Natrual)"

class Fluorine(Element):
    name = "Fluorine"
    chemical_symbol = "F"
    atomic_mass = 18.998
    atomic_number = 9
    series = "Mainly Non-metals (Natrual)"

class Neon(Element):
    name = "Neon"
    chemical_symbol = "Ne"
    atomic_mass = 20.180
    atomic_number = 10
    series = "Mainly Non-metals (Natrual)"

class Sodium(Element):
    name = "Sodium"
    chemical_symbol = "Na"
    atomic_mass = 22.990
    atomic_number = 11
    series = "Reactive Metals (Natrual)"

class Magnesium(Element):
    name = "Magnesium"
    chemical_symbol = "Mg"
    atomic_mass = 24.305
    atomic_number = 12
    series = "Reactive Metals (Natrual)"

class Aluminum(Element):
    name = "Aluminum"
    chemical_symbol = "Al"
    atomic_mass = 26.982
    atomic_number = 13
    series = "Mainly Non-metals (Natrual)"

class Silicon(Element):
    name = "Silicon"
    chemical_symbol = "Si"
    atomic_mass = 28.086
    atomic_number = 14
    series = "Mainly Non-metals (Natrual)"

class Phosphorus(Element):
    name = "Phosphorus"
    chemical_symbol = "P"
    atomic_mass = 30.974
    atomic_number = 15
    series = "Mainly Non-metals (Natrural)"

class Sulfur(Element):
    name = "Sulfur"
    chemical_symbol = "S"
    atomic_mass = 32.065
    atomic_number = 16
    series = "Mainly Non-metals (Natural)"

class Chlorine(Element):
    name = "Chlorine"
    chemical_symbol = "Cl"
    atomic_mass = 35.453
    atomic_number = 17
    series = "Mainly Non-metals (Natural)"

class Argon(Element):
    name = "Argon"
    chemical_symbol = "Ar"
    atomic_mass = 39.948
    atomic_number = 18
    series = "Mainly Non-metals (Natural)"

class Potassium(Element):
    name = "Potassium"
    chemical_symbol = "K"
    atomic_mass = 39.098
    atomic_number = 19
    series = "Reactive Metals (Natural)"

class Calcium(Element):
    name = "Calcium"
    chemical_symbol = "Ca"
    atomic_mass = 40.078
    atomic_number = 20
    series = "Reactive Metals (Natural)"

class Scandium(Element):
    name = "Scandium"
    chemical_symbol = "Sc"
    atomic_mass = 44.956
    atomic_number = 21
    series = "Transition Metals (Natural)"

class Titanium(Element):
    name = "Titanium"
    chemical_symbol = "Ti"
    atomic_mass = 47.867
    atomic_number = 22
    series = "Transition Metals (Natural)"

class Vanadium(Element):
    name = "Vanadium"
    chemical_symbol = "V"
    atomic_mass = 50.942
    atomic_number = 23
    series = "Transition Metals (Natural)"

class Chronium(Element):
    name = "Chronium"
    chemical_symbol = "Cr"
    atomic_mass = 51.996
    atomic_number = 24
    series = "Transition Metals (Natural)"

class Maganese(Element):
    name = "Maganese"
    chemical_symbol = "Mn"
    atomic_mass = 54.938
    atomic_number = 25
    series = "Transition Metals (Natural)"

class Iron(Element):
    name = "Iron"
    chemical_symbol = "Fe"
    atomic_mass = 55.845
    atomic_number = 26
    series = "Transition Metals (Natural)"

class Cobalt(Element):
    name = "Cobalt"
    chemical_symbol = "Co"
    atomic_mass = 58.933
    atomic_number = 27
    series = "Transition Metals (Natural)"

class Nickel(Element):
    name = "Nickel"
    chemical_symbol = "Ni"
    atomic_mass = 58.693
    atomic_number = 28
    series = "Transition Metals (Natural)"

class Copper(Element):
    name = "Copper"
    chemical_symbol = "Cu"
    atomic_mass = 63.546
    atomic_number = 29
    series = "Transition Metals (Natural)"

class Zinc(Element):
    name = "Zinc"
    chemical_symbol = "Zn"
    atomic_mass = 65.39
    atomic_number = 30
    series = "Transition Metals (Natural)"

class Gallium(Element):
    name = "Gallium"
    chemical_symbol = "Ga"
    atomic_mass = 69.723
    atomic_number = 31
    series = "Mainly Non-metals (Natural)"

class Germanium(Element):
    name = "Germanium"
    chemical_symbol = "Ge"
    atomic_mass = 72.64
    atomic_number = 32
    series = "Mainly Non-metals (Natural)"

class Arsenic(Element):
    name = "Arsenic"
    chemical_symbol = "As"
    atomic_mass = 74.922
    atomic_number = 33
    series = "Mainly Non-metals (Natural)"

class Selenium(Element):
    name = "Selenium"
    chemical_symbol = "Se"
    atomic_mass = 78.96
    atomic_number = 34
    series = "Mainly Non-metals (Natural)"

class Bromine(Element):
    name = "Bromine"
    chemical_symbol = "Br"
    atomic_mass = 79.904
    atomic_number = 35
    series = "Mainly Non-metals (Natrual)"

class Krypton(Element):
    name = "Krypton"
    chemical_symbol = "Kr"
    atomic_mass = 83.80
    atomic_number = 36
    series = "Mainly Non-metals (Natural)"

class Rubidium(Element):
    name = "Rubidium"
    chemical_symbol = "Rb"
    atomic_mass = 85.468
    atomic_number = 37
    series = "Reactive Metals (Natural)"

class Strontium(Element):
    name = "Strontium"
    chemical_symbol = "Sr"
    atomic_mass = 87.62
    atomic_number = 38
    series = "Reactive Metals (Natural)"

class Yttrium(Element):
    name = "Yttrium"
    chemical_symbol = "Y"
    atomic_mass = 88.906
    atomic_number = 39
    series = "Transition Metals (Natural)"

class Zirconium(Element):
    name = "Zirconium"
    chemical_symbol = "Zr"
    atomic_mass = 91.224
    atomic_number = 40
    series = "Transition Metals (Natural)"

class Niobium(Element):
    name = "Niobium"
    chemical_symbol = "Nb"
    atomic_mass = 92.906
    atomic_number = 41
    series = "Transition Metals (Natural)"

class Molybdenum(Element):
    name = "Molybdenum"
    chemical_symbol = "Mo"
    atomic_mass = 95.94
    atomic_number = 42
    series = "Transition Metals (Natural)"

class Technetium(Element):
    name = "Technetium"
    chemical_symbol = "Tc"
    atomic_mass = 96
    atomic_number = 43
    series = "Transition Metals (Natural)"

class Ruthenium(Element):
    name = "Ruthenium"
    chemical_symbol = "Ru"
    atomic_mass = 101.07
    atomic_number = 44
    series = "Transition Metals (Natural)"

class Rhodium(Element):
    name = "Rhodium"
    chemical_symbol = "Rh"
    atomic_mass = 102.91
    atomic_number = 45
    series = "Transition Metals (Natural)"

class Palladium(Element):
    name = "Palladium"
    chemical_symbol = "Pd"
    atomic_mass = 106.42
    atomic_number = 46
    series = "Transition Metals (Natural)"

class Silver(Element):
    name = "Silver"
    chemical_symbol = "Ag"
    atomic_mass = 107.87
    atomic_number = 47
    series = "Transition Metals (Natural)"

class Cadmium(Element):
    name = "Cadmium"
    chemical_symbol = "Cd"
    atomic_mass = 15.999
    atomic_number = 48
    series = "Transition Metals (Natural)"

class Indium(Element):
    name = "Indium"
    chemical_symbol = "In"
    atomic_mass = 114.82
    atomic_number = 49
    series = "Mainly Non-metals (Natural)"

class Tin(Element):
    name = "Tin"
    chemical_symbol = "Sn"
    atomic_mass = 118.71
    atomic_number = 50
    series = "Mainly Non-metals (Natural)"

class Antimony(Element):
    name = "Antimony"
    chemical_symbol = "Sb"
    atomic_mass = 121.76
    atomic_number = 51
    series = "Mainly Non-metals (Natural)"

class Tellurium(Element):
    name = "Tellurium"
    chemical_symbol = "Te"
    atomic_mass = 127.60
    atomic_number = 52
    series = "Mainly Non-metals (Natural)"

class Iodine(Element):
    name = "Iodine"
    chemical_symbol = "I"
    atomic_mass = 126.90
    atomic_number = 53
    series = "Mainly Non-metals (Natural)"

class Xenon(Element):
    name = "Xenon"
    chemical_symbol = "Xe"
    atomic_mass = 131.29
    atomic_number = 54
    series = "Mainly Non-metals (Natural)"

class Caesium(Element):
    name = "Caesium"
    chemical_symbol = "Cs"
    atomic_mass = 132.91
    atomic_number = 55
    series = "Reactive Metals (Natural)"

class Barium(Element):
    name = "Barium"
    chemical_symbol = "Ba"
    atomic_mass = 137.33
    atomic_number = 56
    series = "Reactive Metals (Natural)"

class Lathanium(Element):
    name = "Lathanium"
    chemical_symbol = "La"
    atomic_mass = 138.91
    atomic_number = 57
    series = "Rare Earth Metals (Natural)"

class Cerium(Element):
    name = "Cerium"
    chemical_symbol = "Ce"
    atomic_mass = 140.12
    atomic_number = 58
    series = "Rare Earth Metals (Natural)"

class Praseodymium(Element):
    name = "Praseodymium"
    chemical_symbol = "Pr"
    atomic_mass = 140.91
    atomic_number = 59
    series = "Rare Earth Metals (Natural)"

class Neodymium(Element):
    name = "Neodymium"
    chemical_symbol = "Nd"
    atomic_mass = 144.24
    atomic_number = 60
    series = "Rare Earth Metals (Natural)"

class Promethium(Element):
    name = "Promethium"
    chemical_symbol = "Pm"
    atomic_mass = 145
    atomic_number = 61
    series = "Rare Earth Metals (Natural)"

class Samarium(Element):
    name = "Samarium"
    chemical_symbol = "Sm"
    atomic_mass = 150.36
    atomic_number = 62
    series = "Rare Earth Metals (Natural)"

class Europium(Element):
    name = "Europium"
    chemical_symbol = "Eu"
    atomic_mass = 151.96
    atomic_number = 63
    series = "Rare Earth Metals (Natural)"

class Gadolinium(Element):
    name = "Gadolinium"
    chemical_symbol = "Gd"
    atomic_mass = 157.25
    atomic_number = 64
    series = "Rare Earth Metals (Natural)"

class Terbium(Element):
    name = "Terbium"
    chemical_symbol = "Tb"
    atomic_mass = 158.93
    atomic_number = 65
    series = "Rare Earth Metals (Natural)"

class Dysprosium(Element):
    name = "Dysprosium"
    chemical_symbol = "Dy"
    atomic_mass = 162.5
    atomic_number = 66
    series = "Rare Earth Metals (Natural)"

class Holmium(Element):
    name = "Holmium"
    chemical_symbol = "Ho"
    atomic_mass = 164.93
    atomic_number = 67
    series = "Rare Earth Metals (Natural)"

class Erbium(Element):
    name = "Erbium"
    chemical_symbol = "Er"
    atomic_mass = 167.26
    atomic_number = 68
    series = "Rare Earth Metals (Natural)"

class Thulium(Element):
    name = "Thulium"
    chemical_sumbol = "Tm"
    atomic_mass = 168.93
    atomic_number = 69
    series = "Rare Earth Metals (Natural)"

class Ytterbium(Element):
    name = "Ytterbium"
    chemical_symbol = "Yb"
    atomic_mass = 173.04
    atomic_number = 70
    series = "Rare Earth Metals (Natural)"

class Lutetium(Element):
    name = "Lutetium"
    chemical_symbol = "Lu"
    atomic_mass = 174.97
    atomic_number = 71
    series = "Rare Earth Metals (Natural)"

class Hafnium(Element):
    name = "Hafnium"
    chemical_symbol = "Hf"
    atomic_mass = 178.49
    atomic_number = 72
    series = "Transition Metals (Natural)"

class Tantalum(Element):
    name = "Tantalum"
    chemical_symbol = "Ta"
    atomic_mass = 180.95
    atomic_number = 73
    series = "Transition Metals (Natural)"

class Tungsten(Element):
    name = "Tungsten"
    chemical_symbol = "W"
    atomic_mass = 183.84
    atomic_number = 74
    series = "Transition Metals (Natural)"

class Rhenium(Element):
    name = "Rhenium"
    chemical_symbol = "Re"
    atomic_mass = 186.21
    atomic_number = 75
    series = "Transition Metals (Natural)"

class Osmium(Element):
    name = "Osmium"
    chemical_symbol = "Os"
    atomic_mass = 190.23
    atomic_number = 76
    series = "Transition Metals (Natural)"

class Irdium(Element):
    name = "Irdium"
    chemical_symbol = "Ir"
    atomic_mass = 192.22
    atomic_number = 77
    series = "Transition Metals (Natural)"

class Platinum(Element):
    name = "Platinum"
    chemical_symbol = "Pt"
    atomic_mass = 195.08
    atomic_number = 78
    series = "Transition Metals (Natural)"

class Gold(Element):
    name = "Gold"
    chemical_symbol = "Au"
    atomic_mass = 196.97
    atomic_number = 79
    series = "Transition Metals (Natural)"

class Mercury(Element):
    name = "Mercury"
    chemical_symbol = "Hg"
    atomic_mass = 15.999
    atomic_number = 80
    series = "Transition Metals (Natural)"

class Thallium(Element):
    name = "Thallium"
    chemical_symbol = "Tl"
    atomic_mass = 204.38
    atomic_number = 81
    series = "Mainly Non-metals (Natural)"

class Lead(Element):
    name = "Lead"
    chemical_symbol = "Pb"
    atomic_mass = 207.2
    atomic_number = 82
    series = "Mainly Non-metals (Natural)"

class Bismuth(Element):
    name = "Bismuth"
    chemical_symbol = "Bi"
    atomic_mass = 208.96
    atomic_number = 83
    series = "Mainly Non-metals (Natural)"