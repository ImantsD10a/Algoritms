#Algoritms skaitļu rindas summas saskaitīšanai


# Funkcija, kas aprēķina visu skaitļu summu dotajā sarakstā
def calculate_sum(numbers):  
    total = 0  
    for num in numbers:  
        total += num 
    return total  
# Funkcija, kas ģenerē sarakstu ar secīgiem skaitļiem
def generate_sequential_list(start, end):  
    return [i for i in range(start, end + 1)]  


# Funkcija, kas ģenerē nejaušu skaitļu sarakstu
import random  
def generate_random_list(size, min_val, max_val):  
    return [random.randint(min_val, max_val) for _ in range(size)] 


# Funkcija, kas izdrukā sarakstu un tā summu
def print_list_and_sum(numbers):  
    print("Saraksts:", numbers) 
    total = calculate_sum(numbers)  
    print("Summa:", total) 

# Funkcija, kas apstrādā vairākus sarakstus
def process_multiple_lists(lists):  
    for i, lst in enumerate(lists):  
        print(f"Saraksts {i + 1}:")  
        print_list_and_sum(lst)  

# Galvenā programma
if __name__ == "__main__":  
    # Ģenerējam sarakstu ar secīgiem skaitļiem
    saraksts1 = generate_sequential_list(1, 20)  
    print("Pirmais saraksts:")  
    print_list_and_sum(saraksts1) 


    # Ģenerējam nejaušu sarakstu
    saraksts2 = generate_random_list(5, 1, 50)  
    print("Otrais saraksts:")  
    print_list_and_sum(saraksts2)

 # Apvienojam sarakstus apstrādei
    visi_saraksti = [saraksts1, saraksts2]  
    print("Visu sarakstu apstrāde:")  
    process_multiple_lists(visi_saraksti)   

    
     # Cits nejaušu saraksts
    saraksts3 = generate_random_list(7, 10, 100)  
    print("Trešais saraksts:")  
    print_list_and_sum(saraksts3)  
 
  # Apstrādājam visus trīs sarakstus kopā
    visi_saraksti.append(saraksts3)  
    process_multiple_lists(visi_saraksti)  

    # Tukša saraksta piemērs (ja nav skaitļu)
    tukss_saraksts = []  
    print("Tukšs saraksts:")  
    print_list_and_sum(tukss_saraksts)  

    # Vairāku skaitļu ģenerēšana ar ciklu
    random_lists = []  
    for _ in range(3):  
        random_lists.append(generate_random_list(6, 5, 20))  

 # Apstrādājam ģenerētos sarakstus
    print("Ģenerēti saraksti ar ciklu:")  
    process_multiple_lists(random_lists)  
  
    # Kopējā summa visiem sarakstiem
    kopējā_summa = 0  
    for lst in random_lists:  
        kopējā_summa += calculate_sum(lst)  
    print("Kopējā summa visiem sarakstiem:", kopējā_summa)  


    # Daži komentāri:

    # Dotais algoritms saskaita visus skaitļus sarakstā, neatkarīgi no to secības.

    # To izmanto dažādās funkcijās un saitēs, lai veiktu saskaitīšanu.

    # Apstrāde palīdz saskaitīt kopējo summu visiem sarakstiem.
    
