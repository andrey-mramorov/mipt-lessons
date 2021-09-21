#!/usr/bin/env python
# coding: utf-8

with open('text1.txt', 'w') as file:
    file.writelines([' если б море было водкой  \n', '   я бы был подводной лодкой\n', '\n', 'Когда воду наливают в бутылку, она становится бутылкой.\n Когда воду наливают в чайник, она становится чайников. \nВода может течь, а может крушить. \nБудь водой, друг мой.'])
    
with open('text1.txt', 'r') as file:
    lines = [line.strip() for line in file]
    print('\n'.join(lines))


