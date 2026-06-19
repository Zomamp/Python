#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_1.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 06:09:50 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 22:29:15 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from elements import create_water

if __name__ == "__main__":
    print("=== Alembic 1 ===")
    result = create_water()
    print("Using: 'from ... import ...' structure to access elements.py")
    if result:
        print(f"Testing {create_water.__name__}: {result}\n")