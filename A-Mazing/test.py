#!/usr/bin/env python3

import mlx

player_x = 400
player_y = 300
SPEED = 10

m = mlx.Mlx()

mlx_ptr = m.mlx_init()
win_ptr = m.mlx_new_window(mlx_ptr, 800, 600, "Mini Engine")


# =========================
# RENDER (SAFE MODE)
# =========================
def render():
    # petit carré
    for y in range(player_y, player_y + 50):
        for x in range(player_x, player_x + 50):
            m.mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0x00FF00)


# =========================
# INPUT
# =========================
def key_hook(keycode, param):
    global player_x, player_y

    if keycode == 65307:
        m.mlx_loop_exit(mlx_ptr)

    elif keycode == 65361:
        player_x -= SPEED
    elif keycode == 65363:
        player_x += SPEED
    elif keycode == 65362:
        player_y -= SPEED
    elif keycode == 65364:
        player_y += SPEED

    render()


# =========================
# EVENTS
# =========================
m.mlx_key_hook(win_ptr, key_hook, 0)

# fermeture fenêtre (à corriger ensuite)
def close_window(param):
    m.mlx_loop_exit(mlx_ptr)

m.mlx_hook(win_ptr, 17, 0, close_window, 0)


# =========================
# START
# =========================
render()
m.mlx_loop(mlx_ptr)