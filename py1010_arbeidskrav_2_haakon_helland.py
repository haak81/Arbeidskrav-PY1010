# # Arbeidskrav 2 PY1010
# ## Haakon Helland
# ### 2025 01 

##############################################################################

#Oppgave 1

alder = int(input('Hvilket år er du født? ') ) #Skriver inn hvilket år man er født (gitt kode)

alder = 2024 - alder # Beregner alder i 2024

print('I løpet av 2024 fyller du', alder, 'år') 

#Oppgave 2

antall_elever = int(input('Skriv inn antall elever: ' )) #Skriver inn antall elver i klassen (Gitt kode)

antall_pizzaer = antall_elever*1/4 #Beregner hvor mange pizzaer man trenger hvis hver elev spiser 1/4 pizza

import numpy as np

print('Det må handles inn', int(np.ceil(antall_pizzaer)), 'pizzaer') #Antall pizzaer man må handle inn rundet opp til nærmeste integer

#Oppgave 3

import numpy as np 

v_grad = float(input('Skriv inn gradtallet: ' )) # Skriver inn grader (gitt kode)

v_rad = v_grad*np.pi/180 #Formel for å regne om fra grader til radianer

print(v_grad, 'grader', '=', round(v_rad, 2), 'radianer') # Runder av svaret til to desimaler

#Oppgave 4

#a

data = {                                   #Gitt dictionary med land, hovedstad og antall innbyggere i hovedstaden
        'Norge': ['Oslo', 0.634],
        'England': ['London', 8.982],
        'Frankrike': ['Paris', 2.161],
        'Italia': ['Roma', 2.873]
        } 

#b

land = str(input('Skriv inn landet: '))  #Her skriver man inn landet man vil ha informasjon om

print( (data[land][0]),'er hovedstaden i', land, 'og det er', (data[land][1]), 'mill. innbyggere i', (data[land][0])  )

#c

nytt_land = str(input('Skriv inn et nytt land '))  #Her skal man skrive inn et nytt land

ny_hovedstad = str(input('Skriv inn hovedstaden i {} '.format(nytt_land)))   #Her skriver man inn hovedstaden til landet

nytt_innbyggertall = float(input('Skriv innbyggertallet i {}, oppgis som x.xxx mill. '.format(ny_hovedstad)))  #Her skal man skrive inn innbyggertallet

data[nytt_land] = [ny_hovedstad, nytt_innbyggertall]  # Legger til nytt land i dictionary land

data #Skriver hele dictionaryen til skjerm

#Oppgave 5

def fun_areal_og_omkrets(a, b):
    """Beregner arealet og ytre okrets av en figur som er satt sammen av 
    en rettvinklet trekant og en halvsirkel.
    
    a er diameter til sirkelen og lengden av trekantens katet, inn-argument
    b er lengden av trekantens andre katet, inn-argument
    r er radius (diamter/2)
    hyp er hypotenusen til den rettvinklede trekanten
    o_sirk er sirkelens omkrets
    o_fig er fikgurens omkrets: katet + halve sirkelens omkrets + hypotenus
    a_tre er trekantens areal
    a_sirk er sirkelens areal
    a_fig er figurens areal: trekantens areal + areal av halve sirkelen
    
    """
    import numpy as np
    r=(a/2)
    hyp = np.sqrt((a**2) + (b**2 ))
    o_sirk = 2*np.pi*r
    o_fig = b + (o_sirk/2) + hyp
    a_tre = (a*b)/2
    a_sirk = np.pi*(r**2)
    a_fig = a_tre + (a_sirk/2)
    return (a_fig, o_fig)

katet1_diameter = 2.0
katet2 = 4.0

(areal, omkrets) = fun_areal_og_omkrets(katet1_diameter, katet2)
print('Figurens areal er', round(areal, 2)) #runder av til 2 desimaler
print('Figurens omkrest er', round(omkrets, 2)) #runder av til 2 desimaler

#Oppgave 6

import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 200) # x = array med 200 punkter jevnt fordelt (hint i oppgaven)

y = (-x**2) - 5 #Funksjonen som skal plottes

plt.plot(x, y) #Selve plottet

    
    

























