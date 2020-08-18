# -*- coding: utf-8 -*-
 
import sqlite3 as lite
import sys
 
con = lite.connect('Blueprint.db')

# cur.execute("INSERT INTO weaponsBlueprint VALUES()")
# for using sqlite3 in console use '.mode column' and then use '.headers on'

with con:
 
    cur = con.cursor()    
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