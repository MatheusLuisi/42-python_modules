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

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")


ft_plant_age()
