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

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")


ft_water_reminder()
