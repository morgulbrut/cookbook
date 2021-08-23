
#!/usr/bin/python3

import json
import rules
import string


class vehicle:

    def __init__(self, v_type="Car", weight="Middleweight", hull=10, handling=3, max_gear=5, crew=2, slots=2, rules=[], cost=12) -> None:
        self.v_type = v_type
        self.weight = weight
        self.hull = hull
        self.handling = handling
        self.max_gear = max_gear
        self.crew = crew
        self.slots = slots
        self.rules = rules
        self.cost = cost
        self.weapons = []
        self.upgrades = []
        self.sponsor = ""
        self.name = ""

    def __repr__(self) -> str:
        return f"Name: {self.name},\nType: {self.v_type}\nWeight:{self.weight} \nHull: {self.hull}, \nHandling {self.handling} \nMax Gear {self.max_gear}, \nCrew {self.crew} \nSlots {self.slots}, \nRules: {self.rules} \nCost: {self.cost}\nWeapons: {self.weapons}, \nUpgrades: {self.upgrades}"

    def set_name(self, name):
        self.name = name

    def attach_weapon(self, weapon, direction="Front"):
        if weapon.slots <= self.slots:
            weapon.direction = direction
            if direction.lower() == "turret":
                weapon.cost *= 3
            if rules.R_CREW_FIRED in weapon.rules:
                weapon.direction = "Crew Fired"
            if rules.R_BFG in weapon.rules:
                weapon.directionn = "Front"
            self.weapons.append(weapon)
            self.cost += weapon.cost
            self.slots -= weapon.slots
            self.rules.extend(weapon.rules)

    def attach_upgrade(self, upgrade):
        if upgrade.slots <= self.slots:
            self.upgrades.append(upgrade)
            self.cost += upgrade.cost
            self.slots -= upgrade.slots
            if upgrade.name == "Armour Plating":
                self.hull += 2
            if upgrade.name == "Extra Crewmember":
                self.crew += 1
            if upgrade.name == "Tank Tracks":
                self.max_gear -= 1
                self.handling += 1
            self.rules.extend(upgrade.rules)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def make_dashboard(self, output_file, template="dashboard.svg"):
        with open(template) as t:
            template = string.Template(t.read())

        final_output = template.substitute(
            name=self.name,
            v_type=self.v_type,
            weight=self.weight,
            crew=self.crew,
            handling=self.handling,
            max_gear=self.max_gear,
            hull=self.hull,
            cost=self.cost,
            addons=self.list_addons())

        with open(output_file, "w") as output:
            output.write(final_output)

    def list_addons(self) -> str:
        addons = "\n".join(
            [f"- {w.direction} {w.name}: {w.dice}" for w in self.weapons])
        addons += "\n"
        addons += "\n".join([f"- {u.name}" for u in self.upgrades])
        return addons


BUGGY = vehicle(v_type="Buggy", weight="Lightweight", hull=6, handling=4,
                max_gear=6, crew=2, slots=2, rules=[rules.R_ROLL_CAGE], cost=6)

CAR = vehicle(v_type="Car", weight="Middleweight", hull=10,
              handling=3, max_gear=5, crew=2, slots=2, cost=12)
PERFOMANCE_CAR = vehicle("Performance Car", "Middleweight", hull=8, handling=4,
                         max_gear=6, crew=1, slots=2, rules=[rules.R_SLIP_AWAY], cost=15)
TRUCK = vehicle(v_type="Truck", weight="Middleweight", hull=12,
                handling=2, max_gear=4, crew=3, slots=3, cost=15)
HEAVY_TRUCK = vehicle(v_type="Heavy Truck", weight="Heavyweight",
                      hull=14, handling=2, max_gear=3, crew=4, slots=5, cost=25)
BUS = vehicle(v_type="Bus", weight="Heavyweight", hull=16,
              handling=2, max_gear=3, crew=8, slots=3, cost=30)
DRAG_RACER = vehicle(v_type="Drag Racer", weight="Lightweight", hull=4, handling=4,
                     max_gear=6, crew=1, slots=2, rules=[rules.R_JET_ENGINE], cost=5)
BIKE = vehicle(v_type="Bike", weight="Lightweight", hull=4, handling=5, max_gear=6,
               crew=1, slots=1, rules=[rules.R_FULL_THROTTLE, rules.R_PIVOT], cost=5)
BIKE_WITH_SIDECAR = vehicle(v_type="Bike with Sidecar", weight="Lightweight", hull=14,
                            handling=5, max_gear=6, crew=2, slots=2, rules=[rules.R_FULL_THROTTLE, rules.R_PIVOT], cost=8)
ICE_CREAM_TRUCK = vehicle(v_type="Ice Cream Truck", weight="Middleweight", hull=10,
                          handling=2, max_gear=4, crew=2, slots=2, rules=[rules.R_INFURIATING_JINGLE], cost=8)
GYROCOPTER = vehicle(v_type="Gyrocopter", weight="Middleweight", hull=4,
                     handling=4, max_gear=6, crew=1, slots=0, rules=[rules.R_AIRWOLF, rules.R_AIRBORNE], cost=10)
AMBULANCE = vehicle(v_type="Ambulance", weight="Middleweight", hull=12,
                    handling=2, max_gear=5, crew=3, slots=3, rules=[rules.R_UPPERS, rules.R_DOWNERS], cost=20)
MONSTER_TRUCK = vehicle(v_type="Monster Truck", weight="Heavyweight", hull=10,
                        handling=3, max_gear=4, crew=2, slots=2, rules=[rules.R_ALL_TERRAIN, rules.R_UP_AND_OVER], cost=25)
HELICOPTER = vehicle(v_type="Helicopter", weight="Heavyweight", hull=8, handling=3,
                     max_gear=4, crew=3, slots=4, rules=[rules.R_AIRWOLF, rules.R_AIRBORNE, rules.R_RESTRICTED], cost=30)
TANK = vehicle(v_type="Tank", weight="Heavyweight", hull=20,
               handling=4, max_gear=3, crew=3, slots=4, rules=[rules.R_PIVOT, rules.R_ALL_TERRAIN, rules.R_UP_AND_OVER,  rules.R_TURRET, rules.R_RESTRICTED], cost=40)
WAR_RIG = vehicle(v_type="War Rig", weight="Heavyweight", hull=26,
                  handling=2, max_gear=4, crew=5, slots=5, rules=[rules.R_WAR_RIG], cost=40)
