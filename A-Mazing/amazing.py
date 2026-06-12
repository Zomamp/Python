#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   amazing.py                                           :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/11 02:11:21 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/11 02:21:45 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #



from mlx import Mlx

def on_mouse(button, x, y, data):
    print(f"Clic bouton {button} en {x},{y}")

def on_key(keycode, data):
    print(f"Touche pressée : {keycode}")

def on_close(data):
    m.mlx_loop_exit(mlx_ptr)

# 1. Initialisation
m = Mlx()
mlx_ptr = m.mlx_init()

# 2. Créer une fenêtre 400×300
win_ptr = m.mlx_new_window(mlx_ptr, 400, 300, "Ma fenêtre")

# 3. Afficher du texte (couleur 0xAARRGGBB)
m.mlx_string_put(mlx_ptr, win_ptr, 20, 20, 0xFFFFF, "TEST DE STRHDKJHDH DS")

# 4. Brancher les événements
m.mlx_mouse_hook(win_ptr, on_mouse, None)
m.mlx_key_hook(win_ptr, on_key, None)
m.mlx_hook(win_ptr, 33, 0, on_close, None)  # bouton X

# 5. Démarrer la boucle (bloquant)
m.mlx_loop(mlx_ptr)