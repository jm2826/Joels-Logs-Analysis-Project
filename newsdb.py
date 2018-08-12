#!/usr/bin/env python

# Database code for the DB Forum.
import psycopg2

# Connect to news database
db = psycopg2.connect("dbname=news")

# Declare cursor to allow me to query database
cursor = db.cursor()

# Query to select 3 most popular articles in db
cursor.execute("SELECT articles.title, count(log.path) as views "
               "FROM log right join articles on "
               "articles.slug = right(log.path, -9) "
               "GROUP BY articles.title order by views desc limit 3")

# Get all the reseults of the query and print them out
data1 = cursor.fetchall()

# Iterate through query
for results in data1:
    print '"'+results[0]+'" - '+str(results[1])+ ' views'

# Query to the most popular authors in db
cursor.execute("SELECT authors.name, count(log.path) as views "
               "FROM articles, authors, log "
               "WHERE articles.author = authors.id and articles.slug = "
               "right(log.path, -9) "
               "GROUP BY authors.name order by views desc")

# Get all the reseults of the query and print them out
data2 = cursor.fetchall()

# Iterate through query
for results in data2:
    print results[0]+' - '+str(results[1])+ ' views'

# Query to select the days more than 1% (129.08) of errors occured
cursor.execute("SELECT num.date, ((cast(num.count as float) / "
               "cast(dem.count as float))*100) as percent FROM "
               "num JOIN dem on num.date = dem.date WHERE"
               " ((cast(num.count as float) / cast(dem.count as float))"
               "*100) > 1")

# Get all the reseults of the query and print them out
data3 = cursor.fetchall()
# Iterate through query
for results in data3:
    print results[0]+' - ' + str(results[1]) +'% errors'

# Close the connection to the news database
db.close()
