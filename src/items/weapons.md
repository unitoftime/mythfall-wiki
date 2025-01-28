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
	- 2.4[Cannons](#Cannons)
	- 2.5[Throwables](#throwables)
	- 2.6[Staves](#staves)
	- 2.7[Hammers](#hammers)

## General information
Weapons in Mythfall come in many different shapes and forms of attack, but with one objective - to help you with defeating your enemies.

## Weapon types

### Swords
Most weapons that fall into this category posses the following features:
- A rather high damage in comparison to other types of weapons on the same level.
- Have strength scaling of 1.0X or more.
- Shoot two projectiles: one that dissipates after travelling very short distance, but pierces, and one that travels the full distance of the weapon's range - except for those with "dagger" in their name, as they only posses the long distance one.
- The said projectiles are broad, making them easier to hit with.
- Their damage scaling is based on Strength.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Sword") }}

### Greatswords
Most weapons that fall into this category posses the following features:
- Are similar to sword in terms of both their outlook and projectiles.
- Have a slow attack rate of 1.
- Have incrediblu high strength scaling.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Greatsword") }}

### Bows
Most weapons that fall into this category posses the following features:
- Shoot outa volley of multiple projectiles every attack.
- The shot projectiles are spread out in a predefined arc and follow a straight line.
- The said projectiles are narrow, making them harder to hit with.
- Their damage scaling is based on Dexterity.
- Have small base damage per projectile.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Bow") }}

### Crossbows
Most weapons that fall into this category posses the following features:
- Shoot out multiple projectiles every attack.
- In case there are multiple projectiles, they are fired one next to the other in a straight line.
- The said projectiles are narrow, making them harder to hit with.
- Have the chance to apply the fractured status effect upon hit.
- Their damage scaling is based on Dexterity.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Crossbow") }}

### Cannons
Most weapons that fall into this category posses the following features:
- Have attack rate that ranges from 4 to 2.5.
- Fire a projectile that, depending on the weapon's subtype:
	- In case of a connon, is slightly inaccurate, travels in an arc, similarly to the projectiles thrown by blightcap, slow, and explodes, dealing AOE damage upon reaching its destination;
	- In case of a pistol, has a very short range and travels in a straight line.
	- In case of a rifle, has a very long range and travels in a straight line.
- Their damage scaling is based on either Strength, Dexterity or Willpower, on the case by case basis.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Cannon") }}

### Throwables
Most weapons that fall into this category posses the following features:
- Have a very high attack rate of 3.3.
- Have a very short attack range.
- Shoot out a single projectile in a straight line.
- The said projectiles are small, making them harder to hit with.
- Their damage scaling is based on Dexterity.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Throwable") }}

### Staves
Most weapons that fall into this category posses the following features:
- Have an attack rate, ranging from 2.0 to 4.0.
- Shoot out a a projectile in a straight line, which either:
	- Takes on a form of an orb that explodes, dealing AOE damage, upon either hitting an enemy, reaching the position the cursor was in when the projectile was fired or reaching its maximum range;
	- Takes on a form of an orb that deals damage upon impact and shoots out in all directions a set amount of smaller orbs also deal damage, upon either hitting an enemy, reaching the position the cursor was in when the projectile was fired or reaching its maximum range; the formed projectiles do not replicate.
	- Takes on a form of an energy beam that pierces and has the length equal to the weapon's range.
- Their damage scaling is based on Willpower.
- Have a chance to apply some kind of effect to any enemy hit by the explosion.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Staff") }}

### Hammers
Most weapons that fall into this category posses the following features:
- A very hight damage in comparison to other weapons of similar tier.
- Create a set amount of wide, piercing projectiles in a circular pattern that fly outwards.
- Have high strength scaling.

{{ macros::resourceTable(type="Weapon", hideModifiers=false, weaponType = "Hammer") }}
