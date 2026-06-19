#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_distillation_0.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 23:21:59 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 23:25:16 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import potions

if __name__ == "__main__":
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    healing = potions.healing_potion()
    strenght = potions.strength_potion()
    if healing and strenght:
        print(f"Testing {potions.strength_potion.__name__}: {strenght}")
        print(f"Testing {potions.healing_potion.__name__}: {healing}")