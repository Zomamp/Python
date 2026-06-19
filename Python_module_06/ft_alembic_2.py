#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_2.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 06:18:31 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 22:29:20 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy.elements as elements

if __name__ == "__main__":
    print("=== Alembic 2 ===")
    result = elements.create_earth()
    print(f"Accessing alchemy/elements.py using 'import ...' structure")
    if result:
        print(f"Testing {elements.create_earth.__name__}: {result}\n")