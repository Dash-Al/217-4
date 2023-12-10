# Условие: Использовать словарь, содержащий следующие ключи: фамилия, имя; знак Зодиака; дата рождения (список из трёх чисел).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по датам рождения;
# вывод на экран информацию о людях, родившихся под знаком, название которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение.
# Оформив каждую команду в виде отдельной функции.
# Дополнительно реализовать сохранение и чтение данных из файла формата JSON.
# Дополнительно реализовать интерфейс командной строки (CLI).

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import os.path
import sys
from datetime import date
def main():
    # Создание парсера аргументов командной строки
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Имя файла для сохранения/загрузки данных")
    args = parser.parse_args()

def add_person(people):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    zodiac = input("Введите знак Зодиака: ")
    birth_date = [int(x) for x in input("Введите дату рождения (через пробел): ").split()]
    person = {
        "фамилия": last_name,
        "имя": first_name,
        "знак Зодиака": zodiac,
        "дата рождения": birth_date
    }
    people.append(person)
    people.sort(key=lambda x: x["дата рождения"])
def search_by_zodiac(people):
    zodiac = input("Введите знак Зодиака для поиска: ")
    found = False
    for person in people:
        if person["знак Зодиака"] == zodiac:
            print("Фамилия:", person["фамилия"])
            print("Имя:", person["имя"])
            print("Знак Зодиака:", person["знак Зодиака"])
            print("Дата рождения:", "/".join(str(x) for x in person["дата рождения"]))
            print()
            found = True
    if not found:
        print("Люди с указанным знаком Зодиака не найдены.")
def save_to_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)
def load_from_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data
def main():
    people = []
    filename = "data.json"
    while True:
        print("1. Добавить человека")
        print("2. Поиск по знаку Зодиака")
        print("3. Сохранить данные в файл")
        print("4. Загрузить данные из файла")
        print("5. Выйти")
        choice = input("Выберите действие: ")
        if choice == "1":
            add_person(people)
        elif choice == "2":
            search_by_zodiac(people)
        elif choice == "3":
            save_to_file(filename, people)
            print("Данные сохранены в файл:", filename)
        elif choice == "4":
            people = load_from_file(filename)
            print("Данные загружены из файла:", filename)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор.")
if __name__ == "__main__":
    main()
