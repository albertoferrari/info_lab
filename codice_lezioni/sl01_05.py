''' 
 dati di input: capitale iniziale, tasso d'interesse, durata investimento (anni)
 calcola il capitale dopo ogni anno
'''

capitale = float(input("capitale "))
tasso = float(input("tasso % "))
anni = int(input("anni "))

for anno in range(1, anni+1):
    capitale = capitale + capitale * tasso / 100
    print("anno: ",anno,"capitale: ",capitale)
