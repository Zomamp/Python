#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 20:25:45 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/07 07:34:02 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import random


def gen_player_achievements() -> None:
    player_achievements = {
        "First Steps",
        "First Battle Won",
        "Beginner Explorer",
        "10 Enemies Defeated",
        "100 Coins Collected",
        "First Level Completed",
        "Boss Defeated",
        "No Life Lost",
        "Master of Survival",
    }
    players = ["Alice", "Bob", "Kunimitsu", "Miranda"]
    player_data_save = {}

    for player in players:
        player_data_save[player] = set(
            random.sample(list(player_achievements), k=6)
            )
        print(f"Player {player}: {player_data_save[player]}")
    print("")

    print(f"All distinct achievements: {player_achievements}")
    print("")

    for player in players:
        current1 = player_data_save[player]
    others1 = set.union(*(player_data_save[p] for p in players if p != player))
    common1 = current1 & others1
    print(f"Common achievement: {common1}")
    print("")

    for player in players:
        current = player_data_save[player]
        others = set.union(
            *(player_data_save[p] for p in players if p != player)
            )
        common = current - others
        print(f"Only {player} has : {common}")
    print("")

    for player in players:
        current2 = player_data_save[player]
        others2 = player_achievements - current2
        print(f"{player} is missing: {others2}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    gen_player_achievements()
