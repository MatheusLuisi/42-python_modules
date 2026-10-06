#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   dark_validator.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 12:37:44 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 13:26:25 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    normalized = ingredients.lower()
    allowed = dark_spell_allowed_ingredients()
    status = (
        "VALID"
        if any(item in normalized for item in allowed)
        else "INVALID"
    )
    return f"{ingredients} - {status}"
