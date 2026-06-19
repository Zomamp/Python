#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_1.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 23:28:12 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 23:33:13 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy as potion

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    strenght = potion.potions.strength_potion()
    healing = potion.potions.healing_potion()
    if healing and strenght:
        print(f"Testing {potion.potions.strength_potion.__name__}: {strenght}")
        print(f"Testing {potion.potions.healing_potion.__name__}: {healing}")