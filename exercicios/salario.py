salaryFunc = input('Digite o salário do funcionário: ')
salaryFunc = float(salaryFunc)
if salaryFunc > 1250:
    increase = 0.10
    print(f"O aumento foi de {increase * salaryFunc}")
    salaryFunc = salaryFunc * 1.1
    print(f"O salário do funcionário é {salaryFunc}")
else:
    increase = 0.15 * salaryFunc
    # :.2f, formatação de float com 2 casas decimais
    print(f"O aumento foi de {increase:.2f}")
    salaryFunc = salaryFunc * 1.15
    print(f"O salário do funcionário é {salaryFunc}")