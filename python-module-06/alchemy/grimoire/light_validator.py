#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   light_validator.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: mpinto-l <mpinto-l@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/10/06 11:47:07 by mpinto-l            #+#    #+#            #
#   Updated: 2026/10/06 13:26:31 by mpinto-l           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    normalized = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    status = (
        "VALID"
        if any(item in normalized for item in allowed)
        else "INVALID"
    )
    return f"{ingredients} - {status}"
