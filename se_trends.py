from flask import Flask, jsonify, render_template, request
import sqlite3 as lite

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', value = [], countries = [], keyword = '', keyword2='',query='', co_appearing_tag_list =[])

@app.route('/search', methods=['GET', 'POST'])
def search():
    con = lite.connect('bigdata.db')

    keywords = request.form['text'].split(' ')
    if request.form['text']=='':
        return render_template('index.html', value = [], countries = [], keyword = '', keyword2='',query='', co_appearing_tag_list =[])
        
    keyword = keywords[0]
    keyword2 = ''
    if len(keywords)>1:
        keyword2 = keywords[1]
        

    
    with con:
        cur = con.cursor()
        sqlQuery = 'SELECT strftime("%Y-%m", CreationDate),COUNT(strftime("%Y-%m", CreationDate)) FROM SO WHERE Tags LIKE ? GROUP BY strftime("%Y-%m", CreationDate)'
        cur.execute(sqlQuery,('%<'+keyword+'>%',))
        tag_count_list_1 = cur.fetchall()

    with con:
        cur = con.cursor()
        sqlQuery = 'SELECT strftime("%Y-%m", CreationDate),COUNT(strftime("%Y-%m", CreationDate)) FROM SO WHERE Tags LIKE ? GROUP BY strftime("%Y-%m", CreationDate)'
        cur.execute(sqlQuery,('%<'+keyword2+'>%',))
        tag_count_list_2 = cur.fetchall()

    if keyword2=='':
        tag_count_list = tag_count_list_1
    else:
        tag_dict = {}
        for tag in tag_count_list_1:
            tag_dict[tag[0]] = (tag[1],0)
        for tag in tag_count_list_2:
            if tag[0] in tag_dict:
                tag_dict[tag[0]] = (tag_dict[tag[0]][0],tag[1])
            else:
                tag_dict[tag[0]] = (0,tag[1])
        tag_count_list = []
        for key,value in tag_dict.iteritems():
            tag_count_list.append((key,value[0],value[1]))
        tag_count_list.sort()

    with con:
        cur = con.cursor()
        sqlQuery = 'SELECT Location, COUNT(Location) FROM SO AS s JOIN USERS AS u ON s.UserID=u.UserID WHERE s.Tags LIKE ? GROUP BY Location'
        cur.execute(sqlQuery,('%<'+keyword+'>%',))
        country_list = cur.fetchall()


    with con:
        cur = con.cursor()
        sqlQuery = 'SELECT Tags, COUNT(Tags) FROM SO WHERE Tags LIKE ? GROUP BY Tags'
        cur.execute(sqlQuery,('%<'+keyword+'>%',))
        co_appearing_tags = cur.fetchall()
        co_appearing_dict = {}
    for tup in co_appearing_tags:
        tags = tup[0].replace('<','').split('>')[:-1]
        posts = tup[1]
        for tag in tags:
            if tag==keyword:
                continue 
            if tag in co_appearing_dict:
                co_appearing_dict[tag] += posts
            else:
                co_appearing_dict[tag] = posts

    co_appearing_tag_list = []
    for key, value in co_appearing_dict.iteritems():
        co_appearing_tag_list.append((key,value))

    return render_template('index.html', value = tag_count_list, countries = country_list, co_appearing_tag_list = sorted(co_appearing_tag_list, key=lambda pair : pair[1],reverse=True)[:30], keyword = keyword, keyword2 = keyword2, query=request.form['text'])




if __name__ == "__main__":
    app.run(debug=True)