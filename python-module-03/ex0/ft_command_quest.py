#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/08/10 14:15:31 by mpinto-l            #+#    #+#            #
#   Updated: 2026/08/11 13:37:35 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


program_name = sys.argv[0]
total_arguments = len(sys.argv)
arguments_received = total_arguments - 1

print('=== Command Quest ===')
print(f'Program name: {program_name}')
print(f'Arguments received: {arguments_received}')
if total_arguments > 1:
    i = 1
    while i < total_arguments:
        print(f'Argument {i}: {sys.argv[i]}')
        i += 1
else:
    print('No arguments provided!')
print(f'Total arguments: {total_arguments}')
