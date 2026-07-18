# ########################################################################### #
#   shebang: 0                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/18 11:10:18 by mpinto-l            #+#    #+#            #
#   Updated: 2026/07/18 11:36:45 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_garden_intro(name: str, height: int, age: int):
    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Heigth: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro('Rose', 25, 30)
