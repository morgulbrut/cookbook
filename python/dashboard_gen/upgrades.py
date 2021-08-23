#!/usr/bin/python3

import json
import rules


class upgrade:

    def __init__(self, name="Armour Plating", rules=[], slots=0, cost=0) -> None:
        self.name = name
        self.rules = rules
        self.slots = slots
        self.cost = cost

    def __repr__(self) -> str:
        return f"\nName: {self.name} \n\tRules: {self.rules} \n\tSlot {self.slots} \n\tCost {self.cost} "

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


ARMOUR_PLATING = upgrade(name="Armour Plating", rules=[
                         rules.R_ARMOUR_PLATING], slots=1, cost=4)
EXPERIMENTAL_NUCLEAR_ENGINE = upgrade(name="Experimental Nuclear Engine", rules=[
                                      rules.R_ELECTRICAL, rules.R_EXPERIMENTAL_NUCLEAR_ENGINE], cost=5)
EXPERIMENTAL_TELEPORTER = upgrade(name="Experimental Teleporter", rules=[
                                  rules.R_ELECTRICAL, rules.R_EXPERIMENTAL_TELEPORTER], cost=7)
EXTRA_CREWMEMBER = upgrade(name="Extra Crewmember", rules=[
                           rules.R_EXTRA_CREWMEMBER], cost=4)
IMPROVISED_SLUDGE_THROWER = upgrade(name="Improvised Sludge Thrower", rules=[
    rules.R_IMPROVISED_SLUDGE_THROWER], slots=1, cost=2)
NITRO_BOOSTER = upgrade(name="Nitro Booster", rules=[
    rules.R_AMMO_1, rules.R_NITRO_BOOSTER], cost=6)
ROLL_CAGE = upgrade(name="Roll Cage", rules=[
                    rules.R_ROLL_CAGE], slots=1, cost=4)
TANK_TRACKS = upgrade(name="Tank Tracks", rules=[
    rules.R_TANK_TRACKS], slots=1, cost=4)
