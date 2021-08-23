#!/usr/bin/python3

import vehicles
import weapons
import upgrades
import dashboard_pdf


team = []

flammenwerfer = vehicles.HEAVY_TRUCK
flammenwerfer.set_name("[FlammenwerfeR]")
flammenwerfer.attach_weapon(weapons.FLAMETHROWER, "Turrent")
flammenwerfer.attach_weapon(weapons.RAM)
flammenwerfer.attach_weapon(weapons.BLUNDERBUSS)
flammenwerfer.attach_upgrade(weapons.MOLOTOV_COCKTAILS)
flammenwerfer.attach_upgrade(upgrades.ARMOUR_PLATING)
flammenwerfer.attach_upgrade(upgrades.ARMOUR_PLATING)
team.append(flammenwerfer)

blitz = vehicles.BUGGY
blitz.set_name("[BlitZ]")
blitz.attach_weapon(weapons.SHOTGUN)
blitz.attach_weapon(weapons.GRENADES)
blitz.attach_weapon(weapons.MACHINE_GUN)
blitz.attach_upgrade(upgrades.NITRO_BOOSTER)
team.append(blitz)


smasher = vehicles.CAR
smasher.set_name("[SmasheR]")
smasher.attach_weapon(weapons.HANDGUN)
smasher.attach_upgrade(upgrades.TANK_TRACKS)
smasher.attach_weapon(weapons.MINIGUN, "Turrent")
team.append(smasher)


def gen_svg():
    dash = dashboard_pdf.dashboard(
        v, ["Railway To Hells", "Road Rage", "Agency FB"], ['orange', 'magenta'])
    dash.titleblock(50, 60)
    dash.upgradeblock(30, 180)
    dash.ruleblock(30, 400)
    dash.hullblock(700, 250, x_spacing=80)
    dash.gearblock(700, 180, x_spacing=80)
    dash.attributesblock(700, 300)

    dash.save_svg(v.name+".svg")


def gen_pdf():
    dash = dashboard_pdf.dashboard(
        v, title_colour='red', subtitle_colour='hotpink')

    # dash.titleblock(30, 380)
    # dash.upgradeblock(50, 330)
    # dash.hullblock(330, 330)
    # dash.gearblock(500, 330)
    # dash.ruleblock(50, 200)
    # dash.save_pdf()

    dash.default_dashboard()
    print(v.name + ".pdf generated.")


for v in team:

    gen_pdf()

    # gen_svg()
