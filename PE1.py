selected_numbers = []
for number in range(1,1000):
	if number % 3 == 0 or number % 5 == 0: 
		selected_numbers.append(number)

summa = sum(selected_numbers)

print("Summa summárum " + str(summa))
