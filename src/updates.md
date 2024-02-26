# Updates
The game regularily receives updates that improve the game, fix bugs and add more content.

⚠️ This list is not exhaustive

## 24/FEB/2024
```
When you walk through room barriers you will now be pushed in the direction of the barrier. Kind of like a door closing behind you. This is to prevent ppl from standing on the barriers
Mobs now have a chance to drop mana in the nearby area when they die (automatically will add mana to your mana bar)
Mobs now have a chance to drop small mana potions when they die
Added 4 ability types (explosion, lifesteal, barrier, heal) and the new librarian NPC/Shop for combining ability pages into an ability book.
a. Low level bosses typically drop Page 1 of an ability, Alivarg will drop page 2 of the book. And usually a harder dungeon boss will drop page 3 of the book. Books will likely be used to craft other, stronger books in the future.
b. Pages and books can both go into your ability slot. And consume mana on activation. "Spacebar" is default keybind
```

## 22/FEB/2024
```
Fix golden scarab vision so he doesnt see you through walls
Make elder scarab battle a bit easier and more fun
Dungeons now seal in 2 minutes rather than 5 minutes
In temple of anubis, mummies will now drop HP pots
Lots of item changes (I might forget a few): Jester hat, leaf blade, stick, ring of iron
Lots of new items: Chitin weapona and chestplate, spectral sword (Ectoplasm), New Best in slot sword (Trinity Sword), Also Added "Heavy Swords" which scale 2x and 3x with your strength level

Bugs
Ring of obsidian sprite is broken
Scarab Sword should have +5 crit and not +5 guard
```

## 13/FEB/2024
```
Mythfall The Dating Sim?
Can you pull a smooch off a princess? I know it's still the day before, but today's deployment has something very special! The first every Mythfall event: Valentines Day! Artwork done by UnitOfSis, so it's even extra special!

Other Updates
New minibosses will spawn at sphere creation town in various biomes. Right now there's only 3 new ones: (beach biome, Mountain biome, and Desert biome). Their drop table isn't completely filled out yet, but they do drop items. My plan right now is to incrementally add new content as frequent as I can, but what that means is that sometimes it'll not yet have all of the things that I'm wanting for it to eventually have. The other alternative is that I do longer release cycles and add more "finished" content to the game. I think for now we'll try the quick approach. But sometime in the future we might change over.
Disabled profanity Filter - it was just catching too many normal words and not enough swear words
Changed mobs in mountain to use the 2 damage projectile (previously they did 2 damage, but used the 1 damage projectile.
Changed demons to use the 2 damage projectile
Rewrote my dialogue system to support branching dialogues (literally only for the valentines day event)
```

## 12/FEB/2024
```
Fixed onkill lag troubles - Kills should register ~250ms faster. Lmk if it is still unbearable
Fix bug where first hit would take damage and then look like it immediately healed
Move back to webrtc
```

## 09/FEB/2024
```
Added smooth HP bars rather than chunky ones. (minor redeploy: Decreased them from 1s to 1/2s)
Extended the entity timeout time (which helps the symptom of  long disconnects, but doesn't fix the root cause for why those disconnects are happening)
Improve proxy performance by maybe 20% percent, with the magic of code generation
Improved some of the backend metrics so that I can analyze problems a bit better
I think I fixed the problem where sometimes dungeon doors wouldn't open
I hopefully decreased the chance that barriers end up in hallways
```

## 08/FEB/2024
```
On a trial basis: switched networking to use websockets. For those interested it uses about 10% less CPU on the server and 80% less goroutines.
```

## 07/FEB/2024
```
NPC interaction fixed. Used to loop back to start
Added better printouts for various RPC failures
Fixed deadlock which was in the TCP framing layer. Which was causing server to crash under high load
Fixed proxy/server reconnect issue where if they disconnect they never try to reconnect
```

## 06/FEB/2024
```
Improved how the recall gets triggered. So hopefully there will be less times where the client gets stuck not able to recall
Fixed windows build which broke a while ago
For the disconnect/reconnect bug that TC found. I added a fix to detect, but instead of handling it I'm just going to track metrics and printout a log statement for it. Then if I'm satisfied that it works.
```

## 05/FEB/2024
```
Lots of backend improvements that make my life easier + some better metric tracking to find performance bottlenecks
Moved some services off of the game server to hopefully reduce some pressure during peak times
Chat now persists between dungeons
Drop table rates are now corrected
Spawn point shouldnt be blocked now

Outstanding bugs. Will work on fixing these next:
Sometimes recall doesn't complete
Sometimes dungeon doors don't open after all of the monsters are killed
```

## 02/FEB/2024
```
More quickly resolve the case where two people get loot from the same bag (eventually it'll resolve now)
Draw teleporter icons behind player icons on mm
honor bar now fills up and has tooltips
Dungeon hallways should line up a bit better, so you should get less cases of those weird barrier-filled hallways
```

## 01/FEB/2024
```
Now you'll gain Honor on death based on how much XP you have when you die. Honor will eventually be a currency that you can make purchases with. Every 1k exp converts to 1 honor
Added the Hall of heroes which will track the top 8 deaths, how much honor they got and the items they had
Shooting through barriers bugfix
```

## 30/JAN/2023
```
Lotta bug fixes (shooting through walls, mobs seeing outside of their room, Alivarg boss crystals not spawning projectiles on death, Sometimes bosses not dropping items)
Hopefully fixed: sometimes dungeon doors not opening
Stat crystals should work now
Shop scrolling should now work properly! (browsers were tracking 120 ticks per scroll rather than 1 (which is what GLFW does)
```