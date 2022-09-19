mes = '''Janeiro Fevereiro Março Abril Maio Junho Julho Agosto Setembro Outubro Novembro Dezembro'''.split()
d,m,a = input('dd/mm/aaaa: ').split('/')


print(f'{d} de {mes[int(m)-1]} de {a}')
