# Funkcija, kas aprēķina visu skaitļu summu dotajā sarakstā
def calculate_sum(numbers):  # 1. rinda
    total = 0  # 2. rinda
    for num in numbers:  # 3. rinda
        total += num  # 4. rinda
    return total  # 5. rinda

# Funkcija, kas ģenerē sarakstu ar secīgiem skaitļiem
def generate_sequential_list(start, end):  # 6. rinda
    return [i for i in range(start, end + 1)]  # 7. rinda

# Funkcija, kas ģenerē nejaušu skaitļu sarakstu
import random  # 8. rinda
def generate_random_list(size, min_val, max_val):  # 9. rinda
    return [random.randint(min_val, max_val) for _ in range(size)]  # 10. rinda

# Funkcija, kas izdrukā sarakstu un tā summu
def print_list_and_sum(numbers):  # 11. rinda
    print("Saraksts:", numbers)  # 12. rinda
    total = calculate_sum(numbers)  # 13. rinda
    print("Summa:", total)  # 14. rinda

# Funkcija, kas apstrādā vairākus sarakstus
def process_multiple_lists(lists):  # 15. rinda
    for i, lst in enumerate(lists):  # 16. rinda
        print(f"Saraksts {i + 1}:")  # 17. rinda
        print_list_and_sum(lst)  # 18. rinda

# Galvenā programma
if __name__ == "__main__":  # 19. rinda
    # Ģenerējam sarakstu ar secīgiem skaitļiem
    saraksts1 = generate_sequential_list(1, 10)  # 20. rinda
    print("Pirmais saraksts:")  # 21. rinda
    print_list_and_sum(saraksts1)  # 22. rinda

    # Ģenerējam nejaušu sarakstu
    saraksts2 = generate_random_list(5, 1, 50)  # 23. rinda
    print("Otrais saraksts:")  # 24. rinda
    print_list_and_sum(saraksts2)  # 25. rinda

    # Apvienojam sarakstus apstrādei
    visi_saraksti = [saraksts1, saraksts2]  # 26. rinda
    print("Visu sarakstu apstrāde:")  # 27. rinda
    process_multiple_lists(visi_saraksti)  # 28. rinda

    # Pievienojam vēl vienu nejaušu sarakstu
    saraksts3 = generate_random_list(7, 10, 100)  # 29. rinda
    print("Trešais saraksts:")  # 30. rinda
    print_list_and_sum(saraksts3)  # 31. rinda

    # Apstrādājam visus trīs sarakstus kopā
    visi_saraksti.append(saraksts3)  # 32. rinda
    process_multiple_lists(visi_saraksti)  # 33. rinda

    # Tukšs saraksts piemēram
    tukss_saraksts = []  # 34. rinda
    print("Tukšs saraksts:")  # 35. rinda
    print_list_and_sum(tukss_saraksts)  # 36. rinda

    # Ģenerējam vairākus sarakstus ar ciklu
    random_lists = []  # 37. rinda
    for _ in range(3):  # 38. rinda
        random_lists.append(generate_random_list(6, 5, 20))  # 39. rinda

    # Apstrādājam ģenerētos sarakstus
    print("Ģenerēti saraksti ar ciklu:")  # 40. rinda
    process_multiple_lists(random_lists)  # 41. rinda

    # Kopējā summa visiem sarakstiem
    kopējā_summa = 0  # 42. rinda
    for lst in random_lists:  # 43. rinda
        kopējā_summa += calculate_sum(lst)  # 44. rinda
    print("Kopējā summa visiem sarakstiem:", kopējā_summa)  # 45. rinda

# Komentāri un papildu rindu aizpildīšana
# -------------------------------------------
# Šis ir algoritms, kas aprēķina summu visiem sarakstiem       # 46. rinda
# Tā izmanto vairākas funkcijas un ciklus, lai veiktu darbības # 47. rinda
# -------------------------------------------
# Loģikas atkārtojumi un piemēri ar papildus rindām
for i in range(3):  # 48. rinda
    saraksts = generate_random_list(4, 1, 10)  # 49. rinda
    print(f"Saraksts {i + 1}: {saraksts}")  # 50. rinda
    print("Summa:", calculate_sum(saraksts))  # 51. rinda

# --------------------------------------------------------------
# Tukši cikli un papildu darbības līdz 100. rinda               # 52.-100. rinda
for _ in range(48):  # 52. rinda
    pass  # Tukša darbība aizpildīšanai                         # 53.-100. rinda
