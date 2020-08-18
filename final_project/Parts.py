# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('Parts.db')

# https://warframe.fandom.com/wiki/Module:Weapons/data
# cur.execute("INSERT INTO weaponsBlueprint VALUES()")
# for using sqlite3 in console use '.mode column' and then use '.headers on'

with con:
 
    cur = con.cursor()    
    cur.execute("CREATE TABLE weaponsBlueprint(Name TEXT, Resource_first TEXT, Quantity_First INT, Resource_Second TEXT, Quantity_Second INT, Resource_Third TEXT, Quantity_Third INT, Resource_Fourth TEXT, Quantity_Fourth INT)")

    cur.execute("INSERT INTO weaponsBlueprint VALUES('Amprex', 'Fieldron', 8, 'Plastids', 600, 'Ferrite', 9000, 'Argon Crystal', 3)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Boar', 'Morphics', 6, 'Alloy Plate', 900, 'Salvage', 750, 'Plastids', 900)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Boltor', 'Neurodes', 2, 'Alloy Plate', 100, 'Salvage', 900, 'Polymer Bundle', 600)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Hek', 'Neurodes', 5, 'Circuits', 900, 'Salvage', 1200, 'Rubedo', 1100)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Lenz', 'Fieldron', 10, 'Alloy Plate', 8200, 'Cryotic', 2400, 'Nitain Extract', 3)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Rubico', 'Salvage', 3800, 'Polymer Bundle', 1300, 'Rubedo', 900, 'Argon Crystal', 2)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Tigris', 'Orokin Cell', 3, 'Circuits', 900, 'Salvage', 1200, 'Rubedo', 1200)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Zarr', 'Kuva', 1800, 'Alloy Plate', 2400, 'Salvage', 5500, 'Drakgoon', 1)")
    