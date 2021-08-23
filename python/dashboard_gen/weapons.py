#!/usr/bin/python3

import json
import rules


class weapon:

    def __init__(self, name="Handgun", template="medium", dice="1D6", rules=[], slots=0, cost=0) -> None:
        self.name = name
        self.template = template
        self.dice = dice
        self.rules = rules
        self.slots = slots
        self.cost = cost
        self.direction = ""

    def __repr__(self) -> str:
        return f"\nName: {self.name}\n\tTemplate: {self.template}\n\tDice: {self.dice}\n\tRules: {self.rules}\n\tSlots {self.slots}\n\tCost: {self.cost}\n\tDirection: {self.direction}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# Crew fired
HANDGUN = weapon(name="Handgun", template="Medium",
                 dice="1D6", rules=[rules.R_CREW_FIRED])
BLUNDERBUSS = weapon(name="Blunderbuss", template="Small Burst",
                     dice="2D6", rules=[rules.R_CREW_FIRED, rules.R_SPLASH], cost=2)
GAS_GRENADES = weapon(name="Gas Grenades", template="Medium",
                      dice="(1D6)", rules=[rules.R_CREW_FIRED, rules.R_AMMO_5, rules.R_INDIRECT, rules.R_BLITZ, rules.R_GAS_GRENADES], cost=1)
GRENADES = weapon(name="Grenades", template="Medium",
                  dice="1D6", rules=[rules.R_CREW_FIRED, rules.R_AMMO_5, rules.R_BLAST, rules.R_INDIRECT, rules.R_BLITZ], cost=1)
MAGNUM = weapon(name="Magnum", template="Double",
                dice="1D6", rules=[rules.R_CREW_FIRED, rules.R_BLAST], cost=3)
MOLOTOV_COCKTAILS = weapon(name="Molotov Cocktails", template="Medium",
                           dice="1D6", rules=[rules.R_CREW_FIRED, rules.R_AMMO_5, rules.R_FIRE, rules.R_INDIRECT, rules.R_BLITZ], cost=1)
SHOTGUN = weapon(name="Shotgun", template="Long",
                 dice="*", rules=[rules.R_CREW_FIRED, rules.R_SHOTGUN], cost=4)
STEEL_NETS = weapon(name="Steel Nets", template="Short",
                    dice="(3D6)", rules=[rules.R_CREW_FIRED, rules.R_BLAST, rules.R_STEEL_NETS], cost=2)
SMG = weapon(name="Submachine Gun", template="Medium",
             dice="3D6", rules=[rules.R_CREW_FIRED], cost=5)

# Car mouted
MACHINE_GUN = weapon(name="Machine Gun", template="Double",
                     dice="2D6", slots=1, cost=2)
HEAVY_MACHINE_GUN = weapon(name="Heavy Machine Gun", template="Double",
                           dice="3D6", slots=1, cost=3)
MINIGUN = weapon(name="Minigun", template="Double",
                 dice="4D6", slots=1, cost=5)
CANNON_125MM = weapon(name="125mm Cannon", template="Double",
                      dice="8D6", rules=[rules.R_AMMO_3, rules.R_BLAST, rules.R_125MM_CANNON], slots=3, cost=6)
ARC_LIGHTNING_PROJECTOR = weapon(name="Arc Lightning Projector", template="Double",
                                 dice="6D6", rules=[rules.R_AMMO_1, rules.R_ELECTRICAL, rules.R_ARC_LIGHTNING_PROJECTOR], slots=2, cost=6)
BAZOOKA = weapon(name="Bazooka", template="Double",
                 dice="3D6", rules=[rules.R_AMMO_3, rules.R_BLAST], slots=2, cost=4)
BFG = weapon(name="BFG", template="Double", dice="10D6", rules=[
    rules.R_AMMO_1, rules.R_BFG], slots=3, cost=1)
COMBAT_LASER = weapon(name="Combat Laser", template="Double",
                      dice="3D6", rules=[rules.R_SPLASH], slots=1, cost=5)
DEATH_RAY = weapon(name="Death Ray", template="Double",
                   dice="3D6", rules=[rules.R_AMMO_1, rules.R_ELECTRICAL, rules.R_DEATH_RAY], slots=1, cost=3)
FLAMETHROWER = weapon(name="Flamethrower", template="Large Burst",
                      dice="6D6", rules=[rules.R_AMMO_3, rules.R_SPLASH, rules.R_FIRE, rules.R_INDIRECT], slots=2, cost=4)
GRABBER_ARM = weapon(name="Grabber Arm", template="Short",
                     dice="3D6", rules=[rules.R_GRABBER_ARM], slots=1, cost=6)
GRAV_GUN = weapon(name="Grav Gun", template="Double",
                  dice="(3D6)", rules=[rules.R_AMMO_1, rules.R_ELECTRICAL, rules.R_GRAV_GUN], slots=1, cost=2)
HARPOON = weapon(name="Harpoon", template="Double",
                 dice="(5D6)", rules=[rules.R_HARPOON], slots=1, cost=2)
KINETIC_SUPER_BOOSTER = weapon(name="Kinetic Super Booster", template="Double",
                               dice="(6D6)", rules=[rules.R_AMMO_1, rules.R_ELECTRICAL, rules.R_KINETIC_SUPER_BOOSTER], slots=2, cost=6)
MAGNETIC_JAMMER = weapon(name="Magnetic Jammer", template="Double",
                         dice="", rules=[rules.R_ELECTRICAL, rules.R_MAGNETIC_JAMMER], cost=2)
MORTAR = weapon(name="Mortar", template="Double",
                dice="4D6", rules=[rules.R_AMMO_3, rules.R_INDIRECT], slots=1, cost=4)
ROCKETS = weapon(name="Rockets", template="Double",
                 dice="6D6", rules=[rules.R_AMMO_3], slots=2, cost=5)
THUMPER = weapon(name="Thumper", template="Medium",
                 dice="", rules=[rules.R_AMMO_1, rules.R_ELECTRICAL, rules.R_INDIRECT, rules.R_THUMPER], slots=2, cost=4)
WALL_OF_AMPLIFIERS = weapon(name="Wall of Amplifiers", template="Medium",
                            dice="", rules=[rules.R_WALL_OF_AMPLIFIERS], slots=3, cost=4)
WRECK_LOBBER = weapon(name="Wreck Lobber", template="Double/Dropped",
                      dice="", rules=[rules.R_AMMO_3, rules.R_WRECK_LOBBER], slots=4, cost=4)
WRECKING_BALL = weapon(name="Wrecking Ball", template="Short",
                       dice="", rules=[rules.R_WRECKING_BALL], slots=3, cost=2)

# According to the rules they count as upgrade.
RAM = weapon(name="Ram", template="", dice="",
             rules=[rules.R_RAM], slots=1, cost=4)
EXPLODING_RAM = weapon(name="Exploding Ram", template="",
                       dice="", rules=[rules.R_EXPLODING_RAM])

#  Dropped weapons
CALTROP_DROPPER = weapon(name="Caltrop Dropper", template="Dropped, Small", dice="2D6", rules=[
                         rules.R_AMMO_3, rules.R_CALTROP_DROPPER], slots=1, cost=1)
GLUE_DROPPER = weapon(name="Glue Dropper, Small", template="Dropped", dice="",
                      rules=[rules.R_AMMO_3, rules.R_GLUE_DROPPER], slots=1, cost=1)
MINE_DROPPER = weapon(name="Mine Dropper, Small", template="Dropped", dice="4D6",
                      rules=[rules.R_AMMO_3, rules.R_BLAST, rules.R_MINE_DROPPER], slots=1, cost=1)
NAPALM_DROPPER = weapon(name="Napalm Dropper, Small", template="Dropped, Small", dice="4D6", rules=[
                        rules.R_AMMO_3, rules.R_FIRE, rules.R_NAPALM_DROPPER], slots=1, cost=1)
OIL_SLICK_DROPPER = weapon(name="Oil Slick Dropper", template="Dropped, Large", dice="",
                           rules=[rules.R_AMMO_3, rules.R_OIL_SLICK_DROPPER],  cost=2)
RC_CAR_BOMBS = weapon(name="RC Car Bombs", template="Dropped, Large", dice="4D6",
                      rules=[rules.R_AMMO_3, rules.R_RC_CAR_BOMBS],  cost=3)
SENTRY_GUN = weapon(name="Sentry Gun", template="Dropped, Large", dice="2D6",
                    rules=[rules.R_AMMO_3, rules.R_SENTRY_GUN],  cost=2)
R_SMOKE_DROPPER = weapon(name="Smoke Dropper", template="Dropped, Large", dice="",
                         rules=[rules.R_AMMO_3, rules.R_SMOKE_DROPPER], cost=1)
