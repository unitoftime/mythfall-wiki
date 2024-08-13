{% import "macros.tera" as macros %}

![Weapons](../../images/items/weapons.png)
# Weapons

## Contents
The list of contents present within this article:
- 1[General information](#general-information)
- 2[Weapon types](#weapon-types)
	- 2.1[Swords](#swords)
	- 2.2[Bows](#bows)
	- 2.3[Crossbows](#crossbows)
	- 2.4[Throwables](#throwables)
	- 2.5[Staves](#staves)
	- 2.6[Hammers](#hammers)

## General information
Weapons in Mythfall come in many different shapes and forms of attack, but with one objective - to help you with defeating your enemies.

## Weapon types

### Swords
Most weapons that fall into this category posses the following features:
- A rather high damage in comparison to other types of weapons on the same level.
- Have strength scaling of 1.0X or more.
- Shoot two projectiles: one that dissipates after travelling very short distance and one that travels quite far - except for those with "dagger" in their name, as they only posses the long distance one.
- The said projectiles are broad, making them easier to hit with.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Sword") }}

### Bows
Most weapons that fall into this category posses the following features:
- Shoot out multiple projectiles every attack.
- The shot projectiles are spread out in a predefined arc and follow a straight line.
- Have small base damage per projectile.
- Have low strength scaling, 0.5X being the default.
- The said projectiles are narrow, making them harder to hit with.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Bow") }}

### Crossbows
Most weapons that fall into this category posses the following features:
- Shoot out multiple projectiles every attack.
- In case there are multiple projectiles, they are fired one after the other in a straight line.
- The said projectiles are narrow, making them harder to hit with.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Crossbow") }}

### Throwables
Most weapons that fall into this category posses the following features:
- Have a very high attack rate of 3.3.
- Have a very short attack range.
- Shoot out a single projectile in a straight line.
- The said projectiles are small, making them harder to hit with.
- Have strength scaling of 1X.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Throwable") }}

### Staves
Most weapons that fall into this category posses the following features:
- Have an attack rate of 2.0.
- Shoot out a a projectile in a straight line, which later explodes after either:
	- Hitting an enemy;
	- Reaching the position the cursor was in when the projectile was fired;
	- Reached its maximum range;
- The created explosion pierces;
- Do not scale with strength (have strength scaling of 0X).
- Have a chance to apply some kind of effect to any enemy hit by the explosion.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Staff") }}

### Hammers
Most weapons that fall into this category posses the following features:
- A very hight damage in comparison to other weapons of similar tier.
- Create circular explosions that pierce and damage enemies instead of normal projectiles.
- Have very high strength scaling.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Hammer") }}
