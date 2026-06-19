#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_3.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 06:24:45 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 22:29:03 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air

if __name__ == "__main__": 
    print("=== Alembic 3 ===")
    result = create_air()
    print("Accessing alchemy/elements.py using 'from ... import ...' structure")
    if result:
        print(f"Testing {create_air.__name__}: {result}\n")