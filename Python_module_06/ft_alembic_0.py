#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_alembic_0.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/17 06:03:23 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/19 00:07:17 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import elements

if __name__ == "__main__":
    print("=== Alembic 0 ===")
    print("Using: 'import ...' structure to access elements.py")
    result = elements.create_fire()
    if result:
        print(f"Testing {elements.create_fire.__name__}: {result}\n")