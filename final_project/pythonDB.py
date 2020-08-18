# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('WeaponsINFO.db')

# cur.execute("INSERT INTO weaponsData VALUES()")
# for using sqlite3 in console use '.mode column' and then use '.headers on'

with con:
 
    cur = con.cursor()    
    cur.execute("CREATE TABLE weaponsData(Name TEXT, Weapon_Type TEXT, Damage INT, Critical_Chance INT, Critical_Damage INT, Status_Chance INT, Projectile_Type TEXT, Fire_rate INT, Madazine_Size INT, Reload_Time INT, Mastery_Rank INT, Disposition INT)")
    cur.execute("INSERT INTO weaponsData VALUES('Amprex', 'Rifle', 22, 32, 2.2, 22, 'Discharge', 12.0, 100, 2.6, 10, 2)")
    cur.execute("INSERT INTO weaponsData VALUES('Boar', 'Shotgun', 176.0, 10, 1.5, 20, 'Hit-Scan', 4.17, 20, 2.7, 2, 5)")
    cur.execute("INSERT INTO weaponsData VALUES('Boltor', 'Rifle', 25.0, 10, 1.8, 14, 'Projectile', 8.75, 60, 2.6, 2, 2)")
    cur.execute("INSERT INTO weaponsData VALUES('Hek', 'Shotgun', 525.0, 10, 2.0, 25, 'Hit-Scan', 2.17, 4, 2.0, 4, 2)")
    cur.execute("INSERT INTO weaponsData VALUES('Lenz', 'Lenz', 720, 50, 2.0, 5, 'Projectile', 1.0, 1, 0.6, 8, 3)")
    cur.execute("INSERT INTO weaponsData VALUES('Rubico', 'Sniper-Rifle', 180.0, 30, 3.0, 12, 'Hit-Scan', 2.67, 5, 2.4, 6, 3)")
    cur.execute("INSERT INTO weaponsData VALUES('Tigris', 'Shotgun', 1050.0, 10, 2.0, 28, 'Hit-Scan', 2.0, 2, 1.8, 7, 1)")
    cur.execute("INSERT INTO weaponsData VALUES('Zarr', 'Launcher', 25, 17, 2.5, 29, 'Projectile', 1.67, 3, 2.3, 7, 3)")


    cur.execute("CREATE TABLE weaponsBlueprint(Name TEXT, Blueprint_Costs INT, Credits_Cost INT, Platinum_Cost INT, Time_to_Build INT)")
    #                                               Name    BPCost  Credit  Plat    time
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Amprex', 50000, 25000, 225, 24)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Boar', 0, 15000, 225, 12)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Boltor', 15000, 25000, 150, 24)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Hek', 25000, 25000, 225, 24)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Lenz', 50000, 25000, 235, 24)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Rubico', 20000, 20000, 225, 12)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Tigris', 40000, 25000, 150, 24)")
    cur.execute("INSERT INTO weaponsBlueprint VALUES('Zarr', 30000, 30000, 225, 24)")


    cur.execute("CREATE TABLE weaponsResource(Name TEXT, Resource_first TEXT, Quantity_First INT, Resource_Second TEXT, Quantity_Second INT, Resource_Third TEXT, Quantity_Third INT, Resource_Fourth TEXT, Quantity_Fourth INT)")

    cur.execute("INSERT INTO weaponsResource VALUES('Amprex', 'Fieldron', 8, 'Plastids', 600, 'Ferrite', 9000, 'Argon Crystal', 3)")
    cur.execute("INSERT INTO weaponsResource VALUES('Boar', 'Morphics', 6, 'Alloy Plate', 900, 'Salvage', 750, 'Plastids', 900)")
    cur.execute("INSERT INTO weaponsResource VALUES('Boltor', 'Neurodes', 2, 'Alloy Plate', 100, 'Salvage', 900, 'Polymer Bundle', 600)")
    cur.execute("INSERT INTO weaponsResource VALUES('Hek', 'Neurodes', 5, 'Circuits', 900, 'Salvage', 1200, 'Rubedo', 1100)")
    cur.execute("INSERT INTO weaponsResource VALUES('Lenz', 'Fieldron', 10, 'Alloy Plate', 8200, 'Cryotic', 2400, 'Nitain Extract', 3)")
    cur.execute("INSERT INTO weaponsResource VALUES('Rubico', 'Salvage', 3800, 'Polymer Bundle', 1300, 'Rubedo', 900, 'Argon Crystal', 2)")
    cur.execute("INSERT INTO weaponsResource VALUES('Tigris', 'Orokin Cell', 3, 'Circuits', 900, 'Salvage', 1200, 'Rubedo', 1200)")
    cur.execute("INSERT INTO weaponsResource VALUES('Zarr', 'Kuva', 1800, 'Alloy Plate', 2400, 'Salvage', 5500, 'Drakgoon', 1)")
    