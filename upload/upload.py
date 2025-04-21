import json
import time
import string

from mwcleric import AuthCredentials
from mwcleric import WikiggClient

# Nice to haves:
# 1. Better template building code that isn't so cobbled together
# 2. A way to update non destructively: https://github.com/RheingoldRiver/sorcerer-update/blob/master/update.py


################################################################################
################################################################################

# Set true if you want to update item infobox pages
doItemInfoboxes = True
# Set true if you want to update item images
doItemImages = False
# Set to true if you want to update item category pages
doItemCategories = False

# Set true to do a testing printout
doTestingPrint = False

################################################################################
################################################################################

Template_Item = """
{{{{DISPLAYTITLE:{title}}}}}

{{{{Item infobox
|title={title}
|image={image}
|Type={type}
|Description={description}
|Source={source}

|Class={wep_class}
|Damage={wep_damage}
|Rate={wep_rate}
|Projectiles={wep_projectiles}
|Scaling={wep_scaling}

|Heal={con_heal}
|Mana={con_mana}
|Effect={con_effect}

|ModifierString={mods}
}}}}

Warning: This page is automatically generated. Any changes made here may be overwritten.

{demo_gif}

[[Category:Item]]
"""


Template_AllItems="""
Warning: This page is automatically generated. Any changes made here may be overwritten.

{| class="wikitable"
|+ A table of items
|-
! ID !! Image !! Name !! Description
"""

class Creator:
    summary = 'Creating new pages from data file'

    def __init__(self):
        credentials = AuthCredentials(user_file="creds.json")
        # the following login has been changed to edit gg.wiki.gg rather than sorcererbyriver.wiki.gg
        # gg.wiki.gg is our sandbox wiki that anyone may edit for any reason to test scripts
        # so while you are testing your code, you can leave this as-is and view changes at gg.wiki.gg
        # then change it to your wiki afterwards
        self.site = WikiggClient('mythfall', credentials=credentials)
        with open('wikidata/items.json', 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    def run(self):
        itemPageString = Template_AllItems
        equipTypePageString = {
            "Resource": Template_AllItems,
            "Weapon": Template_AllItems,
            "Ability": Template_AllItems,
            "Hat": Template_AllItems,
            "Armor": Template_AllItems,
            "Ring": Template_AllItems,
            "Consumable": Template_AllItems,
            "Boots": Template_AllItems,
            "Cape": Template_AllItems,
            "Block": Template_AllItems
        }
        weaponTypePageString = {
            "Sword": Template_AllItems,
            "Bow": Template_AllItems,
            "Staff": Template_AllItems,
            "Throwable": Template_AllItems,
            "Hammer": Template_AllItems,
            "Crossbow": Template_AllItems,
            "Cannon": Template_AllItems,
            "Dagger": Template_AllItems,
            "Greatsword": Template_AllItems
        }


        for i, v in enumerate(self.data):
            if v['ID'] == 0: continue; # Skip ItemNone
            if v['Deprecated']: continue; # Skip Deprecated Items

#            if v['ID'] != 83: continue;

            itemId = str(v['ID'])

            # split out into multiple lines for clarity
            item_name = string.capwords(v['Name'])
            page_name = "Item/" + str(v['ID'])

            demoAnimation = ""

            wep = {
                    "Class": "",
                    "Damage": "",
                    "Rate": "",
                    "Projectiles": "",
                    "Scaling": ""
                }

            if v['Weapon'] != None:
                wep = {
                    "Class": v['Weapon']['Class'],
                    "Damage": v['Weapon']['Damage'],
                    "Rate": v['Weapon']['Rate'],
                    "Projectiles": v['Weapon']['Projectiles'],
                    "Scaling": v['Weapon']['StrengthScaling']
                }
                demoAnimation="[[File: item-attack-" + itemId + ".gif|thumb|Animation of the " + item_name + "]]"

            con = {
                    "Heal": "",
                    "Mana": "",
                    "Effect": "",
                }

            if v['Consumable'] != None:
                con = {
                    "Heal": v['Consumable']['Heal'],
                    "Mana": v['Consumable']['Mana'],
                    "Effect": self.build_modstring(v['Consumable']['Modifiers']),
                }

            mods = self.build_modstring(v['Modifiers'])

            page_text = Template_Item.format(
                title=item_name,
                image=v['Image'],
                # General
                type=v['EquipType'],
                description=v['Description'],
                source=v['Source'],

                # Weapon
                wep_class=wep['Class'],
                wep_damage=wep['Damage'],
                wep_rate=wep['Rate'],
                wep_projectiles=wep['Projectiles'],
                wep_scaling=wep['Scaling'],

                # Consumable
                con_heal=con["Heal"],
                con_mana=con["Mana"],
                con_effect=con["Effect"],

                # Modifiers
                mods=mods,

                # Demo Gif
                demo_gif=demoAnimation

#                recipe=v['EquipType']#,
#                builds_into=v['builds_into']
            )

            nameLink = '[['+page_name+"|"+item_name+']]'
            itemPageString = self.addItem(itemPageString, str(v['ID']), v['Image'], nameLink, v['Description'])

            ps = equipTypePageString[v['EquipType']]
            equipTypePageString[v['EquipType']] = self.addItem(ps, str(v['ID']), v['Image'], nameLink, v['Description'])

            wepClass = wep['Class']
            if wepClass != '':
                ps2 = weaponTypePageString[wepClass]
                weaponTypePageString[wepClass] = self.addItem(ps2, str(v['ID']), v['Image'], nameLink, v['Description'])

            if doTestingPrint:
                print("Proposed Update for " + page_name)
                print(page_text)

            if doItemInfoboxes:
                print("Updating " + page_name)
                page = self.site.client.pages[page_name]
                page.save(page_text, summary=self.summary)
                time.sleep(1) # To prevent rate limits

            # Upload Image file
            if doItemImages:
                print("Updating Image " + v['Image'])
                self.upload_img(v['Image'])
                time.sleep(1) # To prevent rate limits


        if doItemCategories:
            print("Updating " + "All Items")
            itemPageString += "|}"
            itemPage = self.site.client.pages["All Items"]
            itemPage.save(itemPageString, summary="List of all items")
            time.sleep(1) # To prevent rate limits

            for k, v in equipTypePageString.items():
                print("Updating " + k)
                v += "|}"
                itemPage = self.site.client.pages[k]
                itemPage.save(v, summary="List of all category items")
                time.sleep(1) # To prevent rate limits

            for k, v in weaponTypePageString.items():
                print("Updating " + k)
                v += "|}"
                itemPage = self.site.client.pages[k]
                itemPage.save(v, summary="List of all category items")
                time.sleep(1) # To prevent rate limits


    def addItem(self, pageString, idString, imgString, nameLinkString, descString):
        imageLink = "[[File:"+imgString+"|class=pixel-image|64px]]"
        pageString += "\n"
        pageString += "|-\n"
        pageString += "| " + idString
        pageString += " || " + imageLink
        pageString += " || " + nameLinkString
        pageString += " || " + descString + "\n"
        return pageString

    def build_modstring(self, modifier):
        mods = ""
        if modifier != None:
            for m in modifier:
                mods += " " + m['Filter']
                for mm in m['Modifiers']:
                    mods += " " + mm
        return mods

    def upload_img(self, srcFilename):
        srcFile = "wikidata/img/" + srcFilename
        dstFile = srcFilename
        try:
            res = self.site.client.upload(file=srcFile, filename=dstFile, description="automatically uploaded", ignore=True)
            print(res)
        except:
            print("exception")


#         for k, v in self.data.items():
#             # split out into multiple lines for clarity
#             page_name = string.capwords(k)
#             page = self.site.client.pages[page_name]
#             page_text = Template_Item.format(
#                 title=page_name,
#                 weight=v['weight'],
#                 image=v['image'],
#                 element=v['element'],
#                 recipe=v['recipe']#,
# #                builds_into=v['builds_into']
#             )

#             # this is the general form for saving a page
#             # the page is a Page object gotten from site.client.pages[page_name]
#             # page_text is the text you want to save
#             # summary is the edit summary to use
#             page.save(page_text, summary=self.summary)

    # @staticmethod
    # def get_recipe_text(info):
    #     if len(info['ingredients']) == 0:
    #         # We could also choose to always return something here, and simply sometimes
    #         # have an empty |Recipe= parameter in the item infobox.
    #         # That would simplify the code a bit and not really cause any problems,
    #         # I just wanted to show a slightly more complex operation that you can simplify
    #         # rather than the other way around
    #         return ''
    #     # when doing string.format, {{ will be condensed down to {
    #     # so there are often a lot of { and } when you put wikitext here
    #     recipe_string = '{{{{RecipePart|item={ing}|quantity={q}}}}}'
    #     ingredients = ''.join(
    #         [recipe_string.format(ing=string.capwords(x['ingredient']), q=x['quantity']) for x in info['ingredients']])
    #     return f'|Recipe={ingredients}\n'

    # def get_builds_into_text(self, item):
    #     for _, other in self.data.items():
    #         for ing in other['ingredients']:
    #             if ing['ingredient'] == item:
    #                 # as this string won't be in any string.format call, there is
    #                 # no need to escape the open & closing braces here
    #                 return '== Builds into ==\n{{BuildsInto}}'
    #     return ''

if __name__ == '__main__':
    Creator().run()
