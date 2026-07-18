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

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets avaible")
    if unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    if unit == "area":
        print(f"{seed_type} seeds: {quantity} square meters")
