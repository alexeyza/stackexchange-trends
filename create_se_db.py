import xml.etree.ElementTree as ET
from xml.etree.ElementTree import iterparse
import sqlite3 as lite

def main():
    limited_tags = ['jquery','javascript','python']
    con = lite.connect('bigdata.db')
##    tree = ET.parse('Posts.xml')
##    root = tree.getroot()

    # get an iterable
    context = iterparse('Posts.xml', events=("start", "end"))
    # turn it into an iterator
    context = iter(context)
    # get the root element
    event, root = context.next()

    with con:
        # Commented sections below create a separate table for tags
        #tags_dict = {}
        cur = con.cursor()    
        cur.execute("CREATE TABLE SO(Id INTEGER PRIMARY KEY ASC, Tags TEXT, CreationDate TEXT, UserID INTEGER)")
        #cur.execute("CREATE TABLE TAGS(Id INTEGER PRIMARY KEY ASC, Tag TEXT)")
        #tag_id = 0
        for event, child in context:
            if event == "end" and 'Title' in child.attrib and 'OwnerUserId' in child.attrib and (limited_tags[0] in child.attrib['Tags'] or limited_tags[1] in child.attrib['Tags'] or limited_tags[2] in child.attrib['Tags']):
                sqlQuery = "INSERT INTO SO VALUES(?,?,?,?)"
                cur.execute(sqlQuery,(child.attrib['Id'],child.attrib['Tags'],child.attrib['CreationDate'],child.attrib['OwnerUserId']))
                # tags = child.attrib['Tags'].replace('<','').split('>')[:-1]
                # for tag in tags:
                #     if not tag in tags_dict:
                #         tags_dict[tag] = tag_id
                #         tag_id+=1
                root.clear()
 
        # sqlQuery = "INSERT INTO TAGS VALUES(?,?)"
        # for tag in tags_dict:
        #     cur.execute(sqlQuery,(tags_dict[tag],tag))

    # get an iterable
    context = iterparse('Users.xml', events=("start", "end"))
    # turn it into an iterator
    context = iter(context)
    # get the root element
    event, root = context.next()

    with con:
        cur = con.cursor()    
        cur.execute("CREATE TABLE USERS(UserID INTEGER PRIMARY KEY ASC, Location TEXT)")

        for event, child in context:
            if event == "end" and 'Location' in child.attrib:
                sqlQuery = "INSERT INTO USERS VALUES(?,?)"
                cur.execute(sqlQuery,(child.attrib['Id'],child.attrib['Location']))
                root.clear()

if __name__ == '__main__':
    main()