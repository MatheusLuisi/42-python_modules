# ****************************************************************************#
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plot_area.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: mpinto-l <mpinto-l@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/14 09:41:41 by mpinto-l          #+#    #+#             #
#    Updated: 2026/07/14 09:54:20 by mpinto-l         ###   ########.fr       #
#                                                                             #
# ****************************************************************************#

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    x = length * width
    print(f"Plot area: {x}")
