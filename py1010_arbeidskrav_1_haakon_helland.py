# # Arbeidskrav 1 PY1010
# ## Haakon Helland
# ### 2024 11 08

##############################################################################

# Beregner trafikkforsikringsavgift for både bensin- og elbil

TD = 8.38 # [Avgfit kr/dag]

D = 365 # [Antall dager i et år, justeres til 366 hvis skuddår]

TATOT = TD*D # [Trafikkforsikringsavgift per år]

# Faste utgifter per år

FTOTE = 5000 # [Forsikring elbil kr/år]

FTOTB = 7500 # [Forsikring bensinbil kr/år]

# Drivstofforbruk

KM = 16000 # [Antall KM man kjører pr. år]

DFE = 0.2 # [Drivstofforbruk Elbil kwh/km]

LK = 2.00  # [Ladekostnad Elbil 2.00 kr/kwh]

DFB = 1.00 # [Drivstofforbruk bensinbil kr/km]

DTOTE = KM*DFE*LK # [Drivstofforbruk totalt Elbil kr]

DTOTB = KM*DFB # [Drivstofforbruk totalt Bensinbil kr]

# Bomavgift

BE = 0.1 # [Bomavgift elbil kr/km]

BB = 0.3 # [Bomavgift bensinbil kr/km]

BTOTE = KM*BE # [Bomavgift totalt elbil kr]

BTOTB = KM*BB # [Bomavgift totalt bensinbil kr]

# Beregning av totale utgiter

UTOTE = TATOT + FTOTE + DTOTE + BTOTE # [Totalt utgifter elbil kr/år]

UTOTB = TATOT + FTOTB + DTOTB + BTOTB # [Totalt utgifter bensinbil kr/år]

DIFF = UTOTE - UTOTB # [Differanse i utgift mellom elbil og bensinbil per år]

# Print

print("Kostander elbil og bensinbil", KM, "km per år:")

print("Kostnader per år elbil =", round(UTOTE), "kr")

print("Kostnader per år bensinbil =", round(UTOTB))

print("Årlig differanse i kostander =", round(DIFF))






