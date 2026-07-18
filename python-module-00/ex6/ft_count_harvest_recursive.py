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

def ft_harvest_helper(days, current_day):
    if current_day > days:
        print("Harvest time!")
        return
    print(f"Day {current_day}")
    ft_harvest_helper(days, current_day + 1)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_harvest_helper(days, 1)
