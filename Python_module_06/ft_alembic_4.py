#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_4.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 06:25:43 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 23:14:33 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import alchemy

if __name__ == "__main__":
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    result1 = alchemy.create_air()
    if result1:
        print(f"Testing {alchemy.create_air.__name__}: {result1}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        print("Testing the hidden create_earth: Traceback (most recent call last):")
        alchemy.create_earth()
    except AttributeError as e:
        print(e)