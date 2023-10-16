# # 4
# # для удобства проверки,пользователь может самостоятельно писать входные данные(пользователь вводит с клавиатуры целые числа)и проверят функцию
# temp = int(input())
#
#
# def temp_cat(temp):
#     # проверка условия для холодной погоды
#     if temp < -20:
#         print(0)
#         # проверка условия для прохладной погоды
#     elif temp in range(-21, -1):
#         print(1)
#         # проверка условия для зябкой погоды
#     elif temp in range(0, 15):
#         print(2)
#         # проверка условия для теплой погоды
#     elif temp in range(14, 26):
#         print(3)
#         # проверка условия для жаркой погоды
#     elif temp > 25:
#         print(4)
#
#
# # присваеваем result итоговое знвчение
# result = temp_cat(temp)
#
#
# # 1
# # создаем функцию в которую передаем сначала список имен,а потом список фамилий
# def list_reorder(ref_list):
#     # присваеваем первой переменной name_list первый список так как это имена ,а переменной surnames_list присваеваем второй список,то есть фамилии
#     names_list = ref_list[0]
#     surnames_list = ref_list[1]
#
#     reordered_list = []
#     # циклом for проходимся по каждой переменной в name и sunname  и склеиваем эти значения через zip
#     for name, surname in zip(names_list, surnames_list):
#         # добавляем в массив reordered_list переменные name, surname
#         reordered_list.append([name, surname])
#     # возврвщвем итоговый массив,он должен выводить имя и фамилию
#     return reordered_list
#
#
# # пример использования функции
# ref_list = [['Анастасия', 'Анастасия'], ['Рудько', 'Иванова']]
# result = list_reorder(ref_list)
# print(result)
# #
# 2
#
#
# def del_rep(num):
#     # cоздаем список с помощью list  verb_nums в котором будут лежать только уникальные значения (set(num))
#     verb_nums = list(set(num))
#     # cортируем этот список с порядке возрастания
#     sorted_nums = sorted(verb_nums)
#     # возвращаем итоговое значение
#     return sorted_nums
#
#
# # для удобства ввода передаем в входные данные список разделенный ,
# num = list(map(int, input().split(',')))
# result = del_rep(num)
# print(result)
#
#
# #
# # 5
# def check_phn(phones):
#     phones_checkes = []
#     for phone in phones:
#         # Удаление разделителей c помощью join, isdigit проверяет наличие цифр оставляя только цифры c помощью filter
#         phone_number = ''.join(filter(str.isdigit, phone))
#
#         # если длинна не такая какая нам нужна,добавляем последнй элемент
#         if len(phone_number) != 11:
#             phones_checkes.append(-1)
#             continue
#
#         # создаем перменную в которой будет проверяться первая цифра
#         seven = '7', '8'
#         if phone_number[0] not in seven:
#             phones_checkes.append(-1)
#             continue
#
#         # складываем конкатинацией в итоговый результат для правильного вывода
#         phones_check = '+7(' + phone_number[1:4] + ')' + phone_number[4:7] + '-' + phone_number[
#                                                                                    7:9] + '-' + phone_number[9:11]
#         phones_checkes.append(phones_check)
#
#     return phones_checkes
#
#
# phones = ['+7(123)456-7890', '8(123)456-7890', '+7 123 456 78901', '123 456 7890']
# result = check_phn(phones)
# print(result)
#
#
#
#
#
# def lin_max(nums, limit):
#
#     max_num = -1
#     for num in nums:
#         #если num меньше limit  и больше max_nums,то переопределяется переменная max_num
#         if num < limit and num > max_num:
#             max_num = num
# # возврат итогового значения
#     return max_num
#
#
# nums =(10, 20, 30, 40, 50, 60, 70, 80, 100)
# limit = int(input())
# result = lin_max(nums, limit)
# print(result)