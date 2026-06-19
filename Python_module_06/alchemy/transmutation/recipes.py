#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   recipes.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 00:20:29 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/19 02:24:01 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import elements
from ..elements import create_air
from ..potions import strength_potion

def lead_to_gold() -> str:
    return(f"Recipe transmuting Lead to Gold: brew ’{create_air()}’ and ’{strength_potion()}’ mixed with ’[{elements.create_fire()}]’")