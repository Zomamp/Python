#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: zo-rakot <zo-rakot@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/06 20:24:59 by zo-rakot            #+#    #+#            #
#   Updated: 2026/06/06 20:25:00 by zo-rakot           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys


def scoring() -> None:
    args = sys.argv[1:]
    score = []
    for x in args:
        try:
            score += [int(x)]
        except ValueError:
            print(f"Invalid parameter '{x}'")

    if len(score) == 0:
        print(
            "No scores provided."
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
            )
        return

    Average = sum(score) / len(score)
    Range = max(score) - min(score)
    print(f"Scores processed: {score}")
    print(f"Total players: {len(score)}")
    print(f"Total score: {sum(score)}")
    print(f"Average score: {Average}")
    print(f"High score: {max(score)}")
    print(f"Low score: {min(score)}")
    print(f"Score range: {Range}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scoring()
