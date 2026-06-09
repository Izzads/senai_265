def se(condicao, valor_se_verdadeiro,valor_se_falso):

    return valor_se_verdadeiro if condicao else valor_se_falso

alunos = [
          ("João", 40),
          ("Maria", 60),
          ("José", 94),
          ("pedro", 70),
          ("Ricardo", 91),
          ("Bruno", 56),
          ("Bruna", 54),
          ("Silas", 51),
          ("Patrícia", 36),
          ("Tatiana", 82),
          ("Rosiane", 80),
          ("Rebeca", 62),
          ("Carlos", 65),
          ("Marcos", 73),
          ("Adriana", 91),
          ("Adriano", 32)
]       
                   
print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-" * 38)

for nome, nota in alunos:
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADO"))

    print(f"{nome:15}{nota:>6}{situacao:^12}")

print("- * 38")

print("\n --- Boletim ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos: 
    situacao = se(nota >= 70, "APROVADO", se(nota >= 50, "RECUPERAÇÃO", "REPROVADOS"))

    if situacao == "APROVADO":
        aprovados +=1
    elif situacao == "RECUPERAÇÃO":
        recuperacao +=1
    else:
        reprovados +=1

# Exibe o resultado
print(f"Total de APROVADOS: {aprovados}")
print(f"Total de RECUPERAÇÂO:{recuperacao}")
print(f"Total de REPROVADOS:{reprovados}")