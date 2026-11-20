# -*- coding: utf-8 -*-
"""Chess Tournament Swiss Pairing Engine"""
def compute_buchholz(player_id, rounds_results, all_players):
    opponents = [r["opponent_id"] for r in rounds_results.get(player_id, [])]
    buchholz = sum(all_players.get(opp_id, {}).get("points", 0) for opp_id in opponents)
    return buchholz
