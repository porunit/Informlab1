import re

# Задание 1

print("Задание 1\nВариант 535, смайлик: [<{/")

testString1 = "[<{/"
testString2 = "[<{/5[<{67/-[<{/"
testString3 = "_=34-3=4=\/;';34[<{//';-[<{/dfdf"
testString4 = "AAAAAAaaabfdbdfkfd[<{/dsgdsg[<{/53475sdf7[<{/8sdf98fds98[<{/kj"
testString5 = "[<{/[<{/[<{/"

testArray = [testString1, testString2, testString3, testString4, testString5]

lineCounter = 1
for i in testArray:
    match = re.findall('\[<\{/', i)
    print("Количество смайликов в " + str(lineCounter) + " строке: " + str(len(match)))
    lineCounter += 1
print("\n")

# Задание 2
print("Задание 2\nВариант 5")

secondTestString1 = "Кривошеее существо гуляет по парку"
secondTestString2 = "Я обожаю ходить в мид за пуджа, скооперировавшись преждевременно с союзником, конечно"
secondTestString3 = "аист арбуз Даниил нннии рекаа"
secondTestString4 = "Анатолий выложил пост с расписанием доп. занятий по информатике, но везде перепутал время"
secondTestString5 = "В последних версиях Пайтон появилась возможность использовать так называемые форматированные " \
                    "строковые литералы." \
                    " В отличие от обычных строковых литералов перед f-строками ставится буква f."


def exersice3(array, j):
    print(f"Тестовая строка {j}: ", end="")
    for i in range(len(array)):
        match = re.findall(r'[ауоыэяюёие]{2}', array[i])
        if len(match) > 0 and i + 1 < len(array):
            match2 = re.findall(r'[бвгджзйклмнпрстфхцчшщ]', array[i + 1])
            if len(match2) <= 3:
                print(array[i], end="; ")
    print()


testArray2 = [secondTestString1, secondTestString2, secondTestString3, secondTestString4, secondTestString5]
j = 1
for i in testArray2:
    array = i.split(" ")
    exersice3(array, j)
    j += 1
print("\n")

# Задание 3
print("Задание 3\nВариант 4")

thirdTestString1 = "КоРмА КоРкА КоРчмА корма ккрраа"
thirdTestString2 = "rhvfк корма кнрыа кормаакормааппап"
thirdTestString3 = "аываыва"
thirdTestString4 = "выав"
thirdTestString5 = "кзрга"

testArray3 = [thirdTestString1, thirdTestString2, thirdTestString3, thirdTestString4, thirdTestString5]
j = 1
def exersise3(string,j,answerarray):
    match = re.findall(r"(?:К|к)[^КРАкра](?:Р|р)[^КРАкра](?:А|а)",string)
    answerarray+=match

for i in testArray3:
    print(f"Тестовая строка {j}: ", end="")
    answerArray = []
    array = i.split(" ")
    for h in array:
        exersise3(h,j,answerArray)
    print(*answerArray)
    j+=1