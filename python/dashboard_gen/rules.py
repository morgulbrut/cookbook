#!/usr/bin/python3

import json


class rule:

    def __init__(self, name, short="", text="") -> None:
        self.name = name
        self.short = short
        self.text = text

    def __repr__(self) -> str:
        return f"\n{self.name.upper()}: {self.text}"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


# Weapon rules
R_ELECTRICAL = rule("Electrical",
                    "Mishkin: Rechargable.",
                    "May be recharged according to Mishkin Dynamo rules.")
R_CREW_FIRED = rule("Crew fired",
                    "360-degree Arc of Fire.",
                    "360-degree Arc of Fire.")
R_125MM_CANNON = rule("125mm Cannon",
                      "Firing: Take 2 Hazard.",
                      "When fired, the active vehicle immediately gains 2 Hazard Tokens if it is not a Tank.")
R_ARC_LIGHTNING_PROJECTOR = rule("Arc Lightning Projetor",
                                 "When damaging a target, attack another target whithin Short and 360-degree of the current target.",
                                 "After damaging a target, this vehicle must immediately attack another target within Short range and 360-degree Arc of Fire of the current target (including this vehicle). This chain-reaction continues until the weapon fails to damage a target, or there are no further viable targets. This vehicle can target friendly vehicles with the Arc Lightning Projector. This vehicle cannot target the same vehicle twice in a single Attack Step with the Arc Lightning Projector.")
R_BFG = rule("BFG",
             "Medium straight back, reduce to Gear 1, 3 Hazard tokens.",
             "When this weapon is fired, the vehicle makes an immediately forced move medium straight backwards, reduced to Gear 1 and gains 3 Hazard Tokens. Front mounted only.")
R_DEATH_RAY = rule("Death Ray",
                   "5 or more Hits: remove target from game.",
                   "If this weapon scores five or more un-cancelled hits on the target during a single attack, instead of causing damage, the target car is immediately removed from play.")
R_GRABBER_ARM = rule("Grabber Arm",
                     "Same weight or lighter: Move the target to anywhere in shortrange of its position, rotate it in any direction, Collision Window.",
                     "If this vehicle attacks a target vehicle of the same weight class or lighter with the Grabber Arm and scores one or more un-cancelled hits, the controller of the active vehicle may place the target vehicle anywhere within Short range of the target vehicle’s original position. The target vehicle may be pivoted to face any direction. This movement causes a Collision Window.")
R_GRAV_GUN = rule("Grav Gun",
                  "Until next activition: target is either one class heavier or lighter.",
                  "If this weapon scores one or more un-cancelled hits on the target, instead of causing damage the attacking vehicle’s controller must choose one of the following: until the end of the target’s next activation the target counts as one weight class heavier or until the end of the target’s next activation the target counts as one weight class lighter.")
R_HARPOON = rule("Harpoon",
                 "1. Hit: Orient the target facing toward or away the attacker, whicheve is the smaller, Collision Window. Other Hits: move the lighter vehicle Short Straight towards the heavier one"
                 "This weapon’s hits do not cause damage. Instead, the first un-cancelled hit on the target spins the target vehicle on the spot to either face directly away from or directly towards the attacking vehicle, whichever requires the smallest degree of rotation, as the harpoon catches and the chain goes taut. This triggers a Collision Window.The second and subsequent un-cancelled hits on the target then each cause the target to make a forced Short Straight move towards the attacker, as the harpoon reels the target in .If the target is a heavier weight class than the attacker, it is the attacking vehicle that is spun and moved towards the target vehicle instead.")
R_KINETIC_SUPER_BOOSTER = rule("Kinetic Super Booster",
                               "Every hit shift targets gear up, without Hazard Tokens.", "The Kinetic Super Booster is a bizarre electrical weapon that transfers a jolt of kinetic energy to the target. The target of a Super Booster attack suffers no damage, but instead immediately increases its current Gear by one for every successful hit, without gaining Hazard Tokens. The Super Booster may not increase a vehicle’s current Gear beyond its max Gear.")
R_MAGNETIC_JAMMER = rule("Magnetic Jammer",
                         "Target can´t discard any ammo during its next activition.",
                         "The target vehicle may not discard ammo tokens during its next activation.")
R_THUMPER = rule("Thumper",
                 "Every other vehicle within 360-degree medium range makes a flip check against gear +2, max 6.",
                 "This weapon does not need to declare a facing when purchased. The Thumper is a powerful sonic device that emits a shock wave that hurls nearby vehicles into the air. When this vehicle declares an attack with the Thumper, every other vehicle(friend or foe) within Medium range of this vehicle in a 360-degree Arc of Fire immediately makes a Flip check, in which they count their current Gear as 2 higher, up to a maximum of 6.")
R_WALL_OF_AMPLIFIERS = rule("Wall of Amplifier.",
                            "Every vehicle within 360-degree medium range gets a hit, that can be evaded, for each un-cancelled hit: discard or add one Hazard Token on target"
                            "This weapon does not require a target. When fired, this weapon automatically causes one hit to every vehicle within Medium range and within a 360-degree Arc of Fire. These hits do not cause damage and may be Evaded. For each un-cancelled hit on a vehicle, choose one: either discard 1 Hazard Token from the vehicle or add 1 Hazard Token to the vehicle.")
R_WRECK_LOBBER = rule("Wreck Lobber",
                      "See special rules.",
                      "See special rules.")
R_WRECKING_BALL = rule("Wrecking Ball",
                       "T-Bone every vehicle and destructible object within 360-degree short range.",
                       "When fired, this vehicle must immediately engage in a T-Bone Collision with every vehicle and Destructible obstacle within Short range of it, in a 360-degree Arc of Fire, in an order chosen by this vehicle’s controller.")
R_AMMO_1 = rule("Ammo 1",
                "",
                "weapon or upgrade with this special rule begins the game with (x) number of Ammo Tokens on its dashboard for that weapon or upgrade, where (x) is the value listed.Before making an attack with this weapon or using this upgrade, this vehicle must discard an Ammo Token from this weapon or upgrade. If the vehicle cannot discard an Ammo Token, this weapon or upgrade may not be used.")
R_AMMO_3 = rule("Ammo 3",
                "",
                "weapon or upgrade with this special rule begins the game with (x) number of Ammo Tokens on its dashboard for that weapon or upgrade, where (x) is the value listed.Before making an attack with this weapon or using this upgrade, this vehicle must discard an Ammo Token from this weapon or upgrade. If the vehicle cannot discard an Ammo Token, this weapon or upgrade may not be used.")
R_AMMO_5 = rule("Ammo 5",
                "",
                "weapon or upgrade with this special rule begins the game with (x) number of Ammo Tokens on its dashboard for that weapon or upgrade, where (x) is the value listed.Before making an attack with this weapon or using this upgrade, this vehicle must discard an Ammo Token from this weapon or upgrade. If the vehicle cannot discard an Ammo Token, this weapon or upgrade may not be used.")
R_BLAST = rule("Blast",
               "Every un-cancelled hit: target adds 1 Hazard.",
               "For every un-cancelled hit caused by a weapon or effect with the Blast rule, the target immediately gains 1 Hazard Token.")
R_BLITZ = rule("Blitz",
               "Can attack up to either crew or ammo, whatever is smaller.",
               "This vehicle counts as being armed with a number of copies of this weapon equal to this weapon’s remaining Ammo Tokens, where each copy counts as having a single Ammo Token. This means that during its Attack Step, this vehicle may attack with this weapon any number of times, as long as it doesn’t attack more times that is has Ammo Tokens, and doesn’t attack more times than its Crew Value.")
R_FIRE = rule("Fire",
              "If the target suffers at least one damage its on fire until it has 0 Hazard: looses 1 hull every activation, Smash Attacks have Fire.",
              "If a vehicle suffers at least one damage from a weapon or effect with the Fire special rule, it gains the On-Fire rule in addition to suffering damage. A vehicle cannot gain the On-Fire rule a second time.On Fire: At the start of this vehicle’s activation, it loses 1 Hull Point. This vehicle’s Smash Attacks count as having the Fire special rule. If this vehicle ever has zero Hazard Tokens, the fire goes out and this vehicle loses the On-Fire rule.")
R_INDIRECT = rule("Indirect",
                  "Ignore Terrain and cover.",
                  "When making a shooting attack with a weapon with this special rule, the vehicle may ignore Terrain and Cover during that attack.")
R_SPLASH = rule("Splash",
                "Attack all (including friendly) vehicles beneath the template.",
                "When a weapon with the Splash rule is used to attack, the weapon must target, and attack, every vehicle beneath the shooting template, including friendly vehicles. Each target must suffer a separate attack from the weapon.")
R_ZERO_CREW = rule("Zero crew",
                   "Switch down one gear, only choose templates which are hazadous.",
                   "Some game effect can reduce a vehicle’s Crew Value. When a vehicle with zero Crew is selected to activate, it first automatically changes down one Gear to a minimum of Gear 1. During its Movement Step, only movement templates that are hazardous in the vehicle’s current Gear count as permitted. This means in Gear Phases 1 and 2, the player controlling a vehicle will be forced to select movement templates that are not permitted.")
R_GAS_GRENADES = rule("Gas Grenades",
                      "Hits reduce the Crew by one until the end of the Gear Phase.",
                      "If this weapon scores one or more un-cancelled hits on the target, instead of causing damage, reduce the target’s Crew Value by 1 for each un-cancelled hit, to a minimum of 0, until the end of the Gear Phase.")
R_STEEL_NETS = rule("Steel Nets",
                    "Hits add hazard tokens with blast.",
                    "This weapon’s hits do not cause damage. Hits will add Hazard Tokens as a result of the Blast special rule as normal.")
R_SHOTGUN = rule("Shotgun",
                 "Target in Short Range: 3D6, Medium Range: 2D6, Long Range: 1D6.",
                 "Target in Short Range: 3D6, Medium Range: 2D6, Long Range: 1D6.")
R_CALTROP_DROPPER = rule("Caltorp Dropper",
                         "Treacherous Terrain, first vehicle gets attacket with 2D6"
                         "The dropped weapon template for this dropped weapon counts as a treacherous surface. The first vehicle affected by this weapon is attacked with a 2D6 attack, then remove the Caltrops template from play.")
R_GLUE_DROPPER = rule("Glue Dropper",
                      "Treacherous Terrain, every vehicle switch down 2 gears.",
                      "The dropped weapon template for the Glue Dropper counts as a treacherous surface. Any vehicle affected by this weapon must reduce its current Gear by 2 at the end of their Movement Step. A single vehicle may not be affected by this weapon two activations in a row.")
R_MINE_DROPPER = ("Mine Dropper",
                  "First vehicle get attacked with 4D6 with blast",
                  "The first vehicle affected by this weapon is attacked with a 4D6 attack with Blast, then remove the Mine’s template from play.")
R_NAPALM_DROPPER = rule("Napalm Dropper",
                        "First vehicle get attacked with 4D6 with fire",
                        "The first vehicle affected by this weapon is attacked with a 4D6 attack with Fire, then remove the Napalm template from play.")
R_OIL_SLICK_DROPPER = rule("Oil Slick Dropper",
                           "Treacherous Terrain",
                           "The dropped weapon template for the Oil Slick Dropper counts as a treacherous surface.")
R_RC_CAR_BOMBS = rule("RC Car Bombs",
                      "RC car: Short range, Gear 3, 1 hull, 1 crew, handling 0. Can shoot short range. If the car gets wrecked it explodes as middleweight with 4D6,",
                      "Bombs are taped to remote-controlled cars, which are dropped from a vehicle and then piloted to impact.When attacking with this dropped weapon, place a RC Car (use a tiny car miniature, no larger than 20mm square) so that it is within Short range of the attacking vehicle, and facing in any direction. This placement triggers a Collision Window.The RC Car counts as a lightweight vehicle in current Gear 3 with 1 Hull Point, 1 Crew and 0 Handling. This tiny car can make shooting attacks but cannot change Gear. Although controlled by the player that dropped it, the RC Car does not count as part of the player’s team, and so cannot be used for the purposes of scenario rules, Audience Votes, or perks.The RC Car is involved in a Collision, it suffers one damage before the Collision is resolved. When the RC Car would be Wrecked, it instead explodes. When the RC Car explodes, it rolls 4D6 attack dice, as if it were a middleweight vehicle.If the RC Car wipes out, it suffers one damage before the Wipeout is resolved.")
R_SENTRY_GUN = rule(
    "Sentry Gun",
    "Place within short range, leightweight, destructible obstacle. 2D6 attack against anyone in medium range. No friendly fire.",
    "When attacking with this dropped weapon, place a Sentry Gun so that it is within Short range of the attacking vehicle.The Sentry Gun remains in play as a lightweight destructible obstacle. They may be targeted with shooting attacks and have 2 Hull Points.This Sentry Gun automatically makes a 2D6 shooting attack against any vehicle that ends their Movement Step within Medium range of the Sentry Gun in a 360-degree Arc of Fire. The target may Evade as normal. This Sentry Gun will never target vehicles from the team of the vehicle that dropped it. Although controlled by the player that dropped it, the Sentry Gun does not count as part of the player’s team, and so cannot be used for the purposes of scenario rules, Audience Votes, or perks.")
R_SMOKE_DROPPER = rule("Smoke Dropper",
                       "Target os distracted and gains 1 Hazard.",
                       "This dropped weapon template counts as an obstruction for the purposes of determining Cover. Whilst a vehicle is in contact with this dropped weapon template, that vehicle counts as distracted. If any part of a vehicle’s movement template or Final Position touches this dropped weapon template, the vehicle gains 1 Hazard Token at the end of its Movement Step.")

# Update rules
R_ARMOUR_PLATING = rule("Armour Plating.",
                        "+2 Hull Points.",
                        "+2 Hull Points.")
R_ROLL_CAGE = rule("Roll Cage.",
                   "Ignores the 2 hits from flipping.",
                   "Ignores the 2 hits from flipping.")
R_EXPERIMENTAL_NUCLEAR_ENGINE = rule("Experimental Nuclear Engine.",
                                     "+2 Max Gear, Long Straight neither Hazardous nor Trival and always allowed. If a flipcheck fails, explode as heavyweight."
                                     "This upgrade may not be purchased for lightweight vehicles. A vehicle may only purchase this upgrade once. Add 2 to this vehicle’s max Gear, (up to a maximum of 6). This vehicle considers the Long Straight movement to be permitted in any Gear. The Long Straight is not considered either Hazardous or Trivial in any Gear. If this vehicle ever fails a Flip check, it is immediately Wrecked and automatically Explodes. When this vehicle Explodes, it counts as Heavyweight.")
R_EXPERIMENTAL_TELEPORTER = rule("Experimental Teleporter.",
                                 "Prior to Movement Step: Roll a Skid Die, Hazard: Next player places vehicle within Long Range, Other: place vehicle within Medium Range, keep its facing, add 3 Hazard."
                                 "A vehicle may only purchase this upgrade once. At the start of this vehicle’s activation this vehicle may choose to activate the Experimental Teleporter prior to (and in addition to) its normal Movement Step. When the Experimental Teleporter is activated, this vehicle gains 3 Hazard Tokens, and then rolls a single Skid Die. If the Skid Dice result is any result other than a Hazard, place this vehicle anywhere within Medium range of its current position, not touching an obstruction or terrain, without altering the vehicle’s facing. This does not cause a Collision. This vehicle then begins its normal Movement Step from this new location. If the Skid Dice result is a Hazard, the player to the left of the controller of the vehicle places this vehicle anywhere within Long range of its current position, not touching an obstruction or terrain, without altering its facing. This does not cause a Collision.")
R_EXTRA_CREWMEMBER = rule("Extra Crewmember.",
                          "Each Extra Crewmember purchased increases the vehicles Crew Value by 1.",
                          "Each Extra Crewmember purchased increases the vehicles Crew Value by 1. Maximum twice the normal crew.")
R_IMPROVISED_SLUDGE_THROWER = rule("Improvised Sludge Thrower.",
                                   "Dropped template within 360-degree Medium Range"
                                   "This vehicle may place the Burst templates for its dropped weapons anywhere that is at least partially within Medium range and 360-degree Arc of Fire of this vehicle.")
R_NITRO_BOOSTER = rule("Nitro Booster.",
                       "May move Long Straight and gain 1 Hazard until it has 5.",
                       "Once per activation, at the start of a Movement Step, this vehicle may declare that it is using a Nitro Booster. If it does, this vehicle makes an immediate forced, Long Straight move forward, and then gains Hazard Tokens until it has 5 Hazard Tokens.")
R_TANK_TRACKS = rule("Tank Tracks.",
                     "Handling +1, Max Gear -1.",
                     "Handling +1, Max Gear -1.")


R_RAM = rule("Ram.",
             "Add 2 attack dice to Smash Attak, don't add Hazard in Collisions.",
             "When involved in a Collision on the declared facing, this vehicle may add 2 attack dice to its Smash Attack, and this vehicle does not gain any Hazard Tokens as a result of the Collision.")
R_EXPLODING_RAM = rule("Exploding Ram.",
                       "First Collision: Smash atttack with +6 attack dice. Looses 1 Hull for each 1 or 2 rolled."
                       "The first time this vehicle is involved in a Collision on the declared facing in a game, this vehicle must declare a Smash Attack (even if the Collision is a Tailgate). During this Smash Attack this vehicle gains +6 attack dice. If any 1s or 2s are rolled on this vehicle’s attack dice during this Smash Attack, this vehicle immediately loses one hull point for each 1 or 2 rolled.")


# Vehicle rules
R_SLIP_AWAY = rule("Slip Away.",
                   "When targeted with a tailgate or T-bone smash attack and declares Evade as reaction perform a free activation.",
                   "When targeted with a tailgate or T-bone smash attack and declares Evade as reaction perform a free activation.")
R_UPPERS = rule("Uppers.",
                "In a collision where both evade: switch one Gear up ((gaining a Hazard Token as normal).",
                "When involved in a Collision in which both vehicles declare an Evade, both vehicles must declare a single change Gear up immediately after the Collision is resolved (gaining a Hazard Token as normal).")
R_DOWNERS = rule("Downers.",
                 "Smash Attack: Looses 2 Hazard, reduce targets Crew Value by 1 until end of Gear Phase."
                 "When involved in a Collision during its activation in which it declares a Smash Attack, the target vehicle does not gain any Hazard Tokens from the Collision and instead discards 2 Hazard Tokens. Then reduce the target vehicle’s Crew Value by 1 until the end of the Gear Phase.")
R_FULL_THROTTLE = rule("Full Throttle.",
                       "The Long Straight movement template to be permitted in any Gear. The Long Straight is not Hazardous nor Trivial in any Gear.",
                       "The Long Straight movement template to be permitted in any Gear. The Long Straight is not Hazardous nor Trivial in any Gear.")
R_PIVOT = rule("Pivot.",
               "If in Gear 1: Rotate to any direction you want."
               "At the start of this vehicle's activation, if this vehicle's current Gear is 1, this vehicle may make a pivot about its centre to face any direction. This pivot cannot cause a Collision and cannot leave this vehicle touching an obstruction.")
R_JET_ENGINE = rule("Jet Engine.",
                    "Move Long Straight and gain 1 Hazard, Explode when Wrecked",
                    "A jet engine counts as having a Nitro Booster with infinite ammo tokens. This means this vehicle automatically Explodes when it is Wrecked. A vehicle with a jet engine must use Nitro Booster every time it activates.")
R_AIRBORNE = rule("Airborne.",
                  "Ignore non-tall obstacles, droped weapons and terrain exept for Cover or Attacking others. Cannot be in Collisions.",
                  "Ignores non-tall obstructions, dropped weapons, and terrain at all times, except when checking for Cover, and when targeting other vehicles in its Attack Step. Other vehicles ignore this vehicle at all times, except that other vehicles may target this vehicle during their Attack Steps. This vehicle cannot be involved in Collisions.")
R_AIRWOLF = rule("Airwolf.",
                 "At the start of this vehicle’s activation, this vehicle may gain 2 Hazard Tokens to make a single pivot about its centre point, up to 90 degrees.",
                 "At the start of this vehicle’s activation, this vehicle may gain 2 Hazard Tokens to make a single pivot about its centre point, up to 90 degrees.")
R_BOMBS_AWAY = rule("Bombs Away.",
                    "Dropped Weapons don't use suild slots, attack with any number of dropped weapons.",
                    "When purchasing weapons for this vehicle, this vehicle may count dropped weapons as requiring 0 build slots. This vehicle may attack with any number of dropped weapons in a single Attack Step.")
R_INFURIATING_JINGLE = rule("Infuriating Jingle.",
                            "If attacked with a Smash Attack, the attacker gain no Hazard Tokens.",
                            "Vehicles that target this vehicle with a Smash Attack during a Collision gain no Hazard Tokens during step 6 of the Collision resolution.")
R_ALL_TERRAIN = rule("All Terrain.",
                     "Ignore terrain penalties.",
                     "This vehicle may ignore the penalties for rough and treacherous surfaces.")
R_UP_AND_OVER = rule("Up And Over.",
                     "During Movement, after a Collision with a something lighter without Up and Over, ignore the ostruction for the rest of the movement step."
                     "During this vehicle’s Movement Step, after resolving a Collision with an obstruction of a lower weight class, this vehicle may declare that it is going “Up and Over”. If it does, it may ignore the obstruction for the remainder of its Movement Step, as it drives right over the top of it. This vehicle cannot use this ability to ignore another vehicle with the Up and Over special rule.")
R_TURRET = rule("Turret.",
                "This vehicle may count one weapon as turret-mounted without paying for the upgrade."
                "This vehicle may count one weapon as turret-mounted without paying for the upgrade.")
R_WAR_RIG = rule("War Rig.",
                 "See the War Rig section for details.",
                 "The War Rig has multiple special rules. See the War Rig section for details.")
R_RESTRICTED = rule("Restricted.",
                    "Only for sponsored teams.",
                    "If you are playing with Sponsor rules, Helicopters and Tanks cannot be purchased as standard.")
