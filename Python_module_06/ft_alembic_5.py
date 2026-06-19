#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_5.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/18 23:14:55 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/18 23:17:16 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from alchemy import create_air

if __name__ == "__main__":
    print("=== Alembic 5 === ")
    print("Accessing the alchemy module using 'from alchemy import ...'")
    result = create_air()
    if result:
        print(f"Testing {create_air.__name__}: {result}")