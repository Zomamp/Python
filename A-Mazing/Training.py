#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   Training.py                                          :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/12 00:44:30 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/12 00:56:41 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def labyrinthe_test() -> dict:
    path = {
        "nord" : True,
        "sud" : True,
        "est" : True,
        "ouest" : True
        }
    print(f"nord : {path['nord']}")
    path["sud"] = False
    print(f"sud : {path['sud']}")

    for key, value in path.items():
        print(f"{key} -> {value}")

labyrinthe_test()