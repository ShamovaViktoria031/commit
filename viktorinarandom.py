import random
print("Привет, вы попали на викторину, проверяющую знание иностранных слов")
def help():
    print("Правила: вам будет показано слово на иностранном языке. От вас требуется написать перевод слова на руссом языке с маленькой буквы") 

a=input("Введите имя")
b=input("Если необходимо узнать правила викторины, напишите 1. Если правила известны заранее - 2.")
if b=='1':
    help()
c=["frog","das eichhörnchen", "košeľu", "tercüman", "niu", "tata", "כֶּסֶף"]
c_1 = ["лягушка", "белка", "рубашка", "переводчик", "кокос", "папа", "деньги"]
t=0
p=len(c)
for i in range (p):
    k=random.randint(0,(len(c)))
    print(c[k]) 
    v=input("Введите перевод слова")
    if v==c_1[k]:
        print("Bернo")
        t=t+1
        c.remove(c[k])
        c_1.remove(c_1[k])
    else:
      print(f'Неверно. Правильный ответ: {c_1[k]}')
      c.remove(c[k])
      c_1.remove(c_1[k])
print(f'{a}, Bы успешно прошли викторину. Спасибо за участие. Ваш результат {t} из {p}.')