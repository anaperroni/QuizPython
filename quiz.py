print("Bem vindo(a) ao Quiz da série Friends!")

answer_user = input("Está preparado? Por favor, digite sim ou não ")

if answer_user != "sim":
    quit()

score = 0

print("Qual é o nome da música que Phoebe canta repetidamente no Central Perk? \n (A) Smelly Cat \n (B) Sticky Dog \n (C) Crazy Bird \n (D) Funny Fish")
answer1 = input("Resposta: ")

if answer1 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual é o nome do macaco de estimação de Ross? \n (A) Max \n (B) Milo \n (C) Mark \n (D) Marcel")
answer2 = input("Resposta: ")

if answer2 == "D":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Em que cidade a série Friends é ambientada? \n (A) Chicago \n (B) Los Angeles \n (C) New York \n (D) Boston")
answer3 = input("Resposta: ")

if answer3 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual a frase icônica de Janice? \n (A) How you doing? \n (B) Smelly Cat \n (C) Oh..my..god \n (D) We were on a break!")
answer4 = input("Resposta: ")

if answer4 == "C":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print("Qual é o personagem que tem obsessão por limpeza? \n (A) Monica \n (B) Rachel \n (C) Ross \n (D) Chandler")
answer5 = input("Resposta: ")

if answer5 == "A":
    print("Correto!")
    score = score + 1
else:
    print("Incorreto")

print(f"Quiz encerrado, a sua pontuação é: {score}/5")