## В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
## Не учитывать знаки препинания и регистр символов.
## За основу возьмите любую статью из википедии или из документации к языку.

text = "Убийство Калинки Бамберски — преступление, совершённое в июле 1982 года в Линдау, Федеративная Республика Германии."\
    "Француженка Калинка Бамберски (фр. Kalinka Bamberski) умерла в возрасте 14 лет в доме своего отчима Дитера Кромбаха. "\
    "В связи с подозрительными результатами вскрытия, отец девушки Андре Бамберски начал оказывать давление на власти Германии"\
    "с целью расследования причастности Кромбаха к смерти дочери.После того, как суд Германии прекратил судопроизводство,"\
    "в 1995 году суд Франции заочно осудил Кромбаха и признал виновным в непреднамеренном убийстве. В связи с отказом "\
    "немецкого правительства экстрадировать Кромбаха, в 2009 году Бамберски участвовал в его похищении и вывозе из Германии"\
    "во Францию. Там Кромбах предстал перед судом, и в 2011 году был признан виновным в умышленном нанесении телесных повреждений,"\
    "повлекших непреднамеренную смерть. Кромбах был приговорён к 15 годам лишения свободы; в феврале 2020 года он был освобождён"\
    "из тюрьмы по состоянию здоровья, а 12 сентября того же года умер в доме престарелых в Винзене. В свою очередь, французский"\
    "суд приговорил Бамберски к одному году условного лишения свободы за похищение Кромбаха."

my_dict = {}
text_list = text.lower().split()
text_list_new = [''.join(filter(str.isalpha, a)) for a in text_list]

while '' in text_list_new:
    text_list_new.remove('')

for word in text_list_new:
    my_dict.setdefault(word, text_list_new.count(word))

num_words = 1

while num_words <= 10:
    num_words += 1
    max_key = max(my_dict, key=my_dict.get)
    print(f'{max_key:>5}  =  {my_dict[max_key]}')
    my_dict.pop(max_key)