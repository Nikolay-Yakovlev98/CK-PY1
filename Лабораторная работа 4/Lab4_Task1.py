def get_count_char(str_):
    str_ = str_.lower()
    slovar = {}
    for bukva in str_:
        if bukva.isalpha():
            slovar[bukva] = str_.count(bukva)
    return slovar

def dictionary (dict_):
    dict2 = dict_
    summa = sum(dict2.values())
    for letter in dict2:
        dict2[letter] = (dict2[letter] * 100) / summa


    return dict2



main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
