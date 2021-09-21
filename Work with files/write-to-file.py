#!/usr/bin/env python
# coding: utf-8

def write_array(array, file_name):
    """записывает строки из array в файл file_name"""
    with open(file_name, 'a') as file:
        file.writelines(array)

with open('text1.txt', 'w') as file:
    file.writelines([' если б море было водкой  \n', '   я бы был подводной лодкой\n', '\n', 'Когда воду наливают в бутылку, она становится бутылкой.\n Когда воду наливают в чайник, она становится чайников. \nВода может течь, а может крушить. \nБудь водой, друг мой.'])
    
with open('text1.txt', 'r') as file:
    lines = file.readlines() # - список строк
    
write_array(lines, 'output.txt')

