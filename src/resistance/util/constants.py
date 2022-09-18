# changing these values should be fine -- customize names of things
GOOD_TEAM = "the RESISTANCE"            # or e.g. "Loyal Servants of Arthur"
EVIL_TEAM = "the SPIES"                 # or e.g. "Minions of Mordred"
GOOD_TEAM_MEMBER = f"a member of {GOOD_TEAM}"
GOOD_TEAM_MEMBER_PL = f"members of {GOOD_TEAM}"
EVIL_TEAM_MEMBER = "a SPY"
EVIL_TEAM_MEMBER_PL = "SPIES"

MERLIN = "Commander"                    # in the code I'm mostly using the Avalon names for special roles
PERCIVAL = "Body Guard"                 # because I'm more used to them, but for the default names in output
ASSASSIN = "Assassin"                   # values, I'm using the Resistance-themed names bc they're straightforward
MORGANA = "False Commander"
MORDRED = "Deep Cover"
OBERON = "Blind Spy"
MORDRED_ASSASSIN = "Deep Cover Assassin"    # for some setups to have Mordred, they must also be the Assassin (shooter)


# changing these values could break something
MIN_PLAYERS = 5
MAX_PLAYERS = 10
TEAM_SIZE_BY_PLAYERS_MISSION = {    # TEAM_SIZE_BY_PLAYERS_MISSION[7][2] => 7 player game, mission 2: has 3 players
    5: {
        1: 2, 2: 3, 3: 2, 4: 3, 5: 3
    },
    6: {
        1: 2, 2: 3, 3: 4, 4: 3, 5: 4
    },
    7: {
        1: 2, 2: 3, 3: 3, 4: 4, 5: 4
    },
    8: {
        1: 3, 2: 4, 3: 4, 4: 5, 5: 5
    },
    9: {
        1: 3, 2: 4, 3: 4, 4: 5, 5: 5
    },
    10: {
        1: 3, 2: 4, 3: 4, 4: 5, 5: 5
    }
}
