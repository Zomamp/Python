#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_1.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 00:16:20 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/19 04:09:22 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.transmutation as transmutation

if __name__ == "__main__":
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    result = transmutation.lead_to_gold()
    if result:
        print(f"Testing {transmutation.lead_to_gold.__name__}: {result}")