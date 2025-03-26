print(" Girl's information")
print("NAME    | AGE | HIEGHT | SCORE")
print("---------------------------------")

girls_names = ["Evelyn", "Jessica", "Somto", "Edith", "Liza","Madonna", "Waje", "Tola", "Aisha", "Latifa"]
girls_ages = [17, 16, 17, 18, 16, 18, 17, 20, 19, 17]
girls_height = [5.5, 6.0, 5.4, 5.9, 5.6, 5.5, 6.1, 6.0, 5.7, 5.5]
girls_scores = [80, 85, 70, 60, 76, 66, 87, 95, 50, 49]

for i in range(len(girls_names)):
    print(f"{girls_names[i]:<8} | {girls_ages[i]:<3} | {girls_height[i]:<6} | {girls_scores[i]:<5}")

print("\nBoy's information")
print("NAME    | AGE | HIEGHT | SCORE")
print("---------------------------------")

boys_names = ["Chinedu", "Liam", "Wale", "Gbenga", "Abiola", "Kola", "Kunle", "George", "Thomas", "Wesley"]
boys_ages = [19, 16, 18, 17, 20, 19, 16, 18, 17, 19]
boys_height = [5.7, 5.9, 5.9, 5.8, 6.1, 5.9, 5.5, 6.1, 5.4, 5.8]
boys_scores = [74, 87, 75, 68, 66, 78, 87, 98, 54, 60]

for i in range(len(boys_names)):
    print(f"{boys_names[i]:<8} | {boys_ages[i]:<3} | {boys_height[i]:<6} | {boys_scores[i]:<5}")

