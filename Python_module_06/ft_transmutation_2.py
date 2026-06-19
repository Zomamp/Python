#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_transmutation_2.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/19 00:16:22 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/19 04:03:07 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

if __name__ == "__main__":
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    result = alchemy.lead_to_gold()
    if result:
        print(f"Testing {alchemy.lead_to_gold.__name__}: {result}")