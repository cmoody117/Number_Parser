# -*- coding: utf-8 -*-
"""
"""
import os
import re
import codecs
import math


def import_file(dir, file): 
    full_path = dir + file
    try:
        os.path.exists(full_path)
    except:
        print("Error: file path %s is invalid" % (full_path))
    try:
        full_path.endswith('.txt')
    except:
        print("Error: not a txt file. Please try again")
    txt_file= codecs.open(dir + file,'r',encoding='utf8')
    txt_string = txt_file.read()
    txt_file.close()
    return txt_string

#Parser: Splits text inputs by line, and checks for numbers within them. If any numbers are invalid, the whole line will be returned invalid.
def parser(txt_string): 
    txt_string_by_line = re.split("\n", txt_string)
    number_string_list =[]
    for line in txt_string_by_line:
        numbers_in_line = re.findall("[^\s]*[0-9][0-9\.\,]*",line)
        for position, number in enumerate(numbers_in_line):
            if number[-1] in ['.',',']:
                numbers_in_line[position] = number[:-1]
        for position, number in enumerate(numbers_in_line):
            if re.search("[^0-9]",number):
                numbers_in_line = ['number invalid']
        if numbers_in_line == []:
                numbers_in_line = ['no numbers']
        number_string_list.append(numbers_in_line)
    return number_string_list


def number_converter(number_string_list):
    words_from_numbers = []
    for by_line in number_string_list:
        words_from_numbers_by_line = []
        for txt_string_cleaned in by_line:
            words_from_numbers_by_line.append(integer_converter(txt_string_cleaned))
        words_from_numbers.append(words_from_numbers_by_line)
    return words_from_numbers


def integer_converter(txt_string_cleaned):
    # import pdb;pdb.set_trace()
    try:
        int(txt_string_cleaned)
    except:
        return txt_string_cleaned    
    words_uncleaned = recursive_conv(txt_string_cleaned)
    words_cleaned = clean(words_uncleaned, txt_string_cleaned)
    return words_cleaned
    

 
def recursive_conv(txt_string_cleaned):
    try:
        int(txt_string_cleaned)
    except:
        print("Error: conv input are not numbers. Check if is invalid number or otherwise coming through.")
    if len(txt_string_cleaned)%3 !=0:
        remainder = len(txt_string_cleaned)%3
    else:
        remainder = 3
    power_1000 = math.floor((len(txt_string_cleaned)-1)/3)
    if int(txt_string_cleaned) < 1000:
        return hundreds_handler(txt_string_cleaned[-3:])
    else:
        return hundreds_handler(str(int(txt_string_cleaned[:remainder]))) + ' ' + dict_large[power_1000] + ', ' + recursive_conv(txt_string_cleaned[remainder:])


def clean(words_uncleaned, txt_string_cleaned):
    if int(txt_string_cleaned[len(txt_string_cleaned)-2:]) < 100:
        words_uncleaned = ''.join(words_uncleaned.rsplit(',',1))
    words_uncleaned = re.sub("  +", " ",words_uncleaned)
    return words_uncleaned.strip()


def hundreds_handler(digits):

    if len(digits) == 3:    
        if int(digits[1:3]) >=10 and int(digits[1:3]) <=19:
            return dict_100[digits[0]] + ' and '+ dict_teen[digits[1:3]]
        elif digits[2] == '0' and digits[1] == '0':
            return dict_100[digits[0]]
        elif digits[2] == '0' or digits[1] =='0':
            return dict_100[digits[0]] + ' and ' + dict_10[digits[1]] + dict_digit[digits[2]]
        else:
            return dict_100[digits[0]] + ' and '+ dict_10[digits[1]] + '-' + dict_digit[digits[2]]

    elif len(digits) == 2:
        if int(digits) >=10 and int(digits) <19:
            return dict_teen[digits[0:2]]
        else:
            return dict_10[digits[0]] + '-' + dict_digit[digits[1]]

    else:
        return dict_digit[digits]


dict_large = {0: '', 1:'thousand',2:'million', 3: 'billion', 4: 'trillion', 5: 'quintillion'}
dict_100 = {'0': '', '1': 'one hundred','2': 'two hundred', '3': 'three hundred','4': 'four hundred','5': 'five hundred','6':'six hundred', '7':'seven hundred','8':'eight hundred','9':'nine hundred'}  
dict_teen = {'10': 'ten', '11': 'eleven','12': 'twelve', '13': 'thirteen','14': 'fourteen','15': 'fifteen','16':'sixteen', '17':'seventeen','18':'eighteen','19':'nineteen'}  
dict_10 = {'0': '', '2': 'twenty', '3': 'thirty','4': 'fourty','5': 'fifty','6':'sixty', '7':'seventy','8':'eighty','9':'ninety'}  
dict_digit = {'0': '', '1': 'one','2': 'two', '3': 'three','4': 'four','5': 'five','6':'six', '7':'seven','8':'eight','9':'nine'}  
dict_decim = {'0': 'zero', '1': 'one','2': 'two', '3': 'three','4': 'four','5': 'five','6':'six', '7':'seven','8':'eight','9':'nine'}
directory = input("Hello, please state your file location")
file = input("And file name? ") 

txt_file_input = import_file(directory, file)
numbers_parsed = parser(txt_file_input)

print(number_converter(numbers_parsed))
