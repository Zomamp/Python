#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_0.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 00:16:17 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/19 01:36:53 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import alchemy.transmutation.recipes as transmute

if __name__ == "__main__":
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    result = transmute.lead_to_gold()
    if result:
        print(f"Testing {transmute.lead_to_gold.__name__}: {result}")