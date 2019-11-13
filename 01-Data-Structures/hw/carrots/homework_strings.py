"""

Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*


*В папке files вы найдете файл rna_codon_table.txt -
в нем содержится таблица переводов кодонов РНК в аминокислоту,
составляющую часть полипептидной цепи белка.


Вход: файл dna.fasta с n-количеством генов

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

 ** Если вы умеете в matplotlib/seaborn или еще что,
 welcome за дополнительными баллами за
 гистограммы по нуклеотидной статистике.
 (Не забудьте подписать оси)

P.S. За незакрытый файловый дескриптор - караем штрафным дезе.

"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import re


def nucleotid_count(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")


def translate_from_dna_to_rna(string):
    s = string.replace("T", "U")
    return s


""""Сделано две функции перевода рнк в аминокислоты, тк по правилам
перевод заканчивается вместе со стоп кодоном, однако у нас
это не было специально указано, поэтому сделана также функция,
которая просто не учитывает стоп кодоны, но продолжает перевод
последовательности(translate_rna_to_protein_full)"""


def translate_rna_to_protein_full(s, d):
    result = ''
    for i in range(0, len(s)-2, 3):
        if d[s[i:i+3]] != 'Stop':
            result += d[s[i:i+3]]
    return result


def translate_rna_to_protein(s, d):
    result = ''
    for i in range(0, len(s)-2, 3):
        if d[s[i:i+3]] == 'Stop':
            return result
        result += d[s[i:i+3]]
    return result


"""" 1.1. Построение статистики по входящим в последовательность
ДНК нуклеотидам для каждого гена
(например: [A - 46, C - 66, G - 23, T - 34]) """


with open("dna.fasta.txt") as file:
    dna = file.read().split('\n')

d = {}
for line in dna:
    if line.startswith(">"):
        name = line
        d[name] = ""
    else:
        d[name] += line

for key, value in d.items():
    d[key] = dict(zip(['A', 'C', 'G', 'T'], nucleotid_count(value)))

f = open('1.1.Статистика генов.txt', 'tw', encoding='utf-8')
for key, value in d.items():
    f.write(key + '\n')
    for i, j in d[key].items():
        f.write('{}: {}'.format(i, j))
        f.write('\n')
f.close()


"""" 1.2. Перевод последовательности ДНК в РНК """

with open("dna.fasta.txt") as file:
    s = file.read()

s1 = translate_from_dna_to_rna(s).split('\n')
d_rna = {}
for line in s1:
    if line.startswith(">"):
        name = line
        d_rna[name] = ""
    else:
        d_rna[name] += line


f = open('1.2.Перевод последовательности ДНК в РНК.txt', 'tw', encoding='utf-8')
for key, value in d_rna.items():
    f.write(key + '\n')
    for i in range(0, len(d_rna[key]), 75):
        f.write(d_rna[key][i:i+75] + '\n')
f.close()


"""" 1.3. Перевод последовательности РНК в протеин """

with open("rna_codon_table.txt") as file:
    codons = file.read()
text = re.sub(r'\s+', ' ', codons)
text = text.split(' ')

d_codons = {text[i-1]: text[i] for i in range(1, len(text), 2)}

for key, value in d_rna.items():
    d_rna[key] = translate_rna_to_protein(value, d_codons)

f = open('1.3.РНК в протеин со стоп кодоном.txt', 'tw', encoding='utf-8')
for key, value in d_rna.items():
    f.write(key + '\n')
    for i in range(0, len(d_rna[key]), 75):
        f.write(d_rna[key][i:i+75] + '\n')
f.close()

