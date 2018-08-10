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
print data1

# Query to the most popular authors in db
cursor.execute("SELECT authors.name, count(log.path) as views "
               "FROM articles, authors, log "
               "WHERE articles.author = authors.id and articles.slug = "
               "right(log.path, -9) "
               "GROUP BY authors.name order by views desc")

# Get all the reseults of the query and print them out
data2 = cursor.fetchall()
print data2

# Query to select the days more than 1% (129.08) of errors occured
cursor.execute("SELECT to_char(time, 'yyyy-mm-dd') as date, count(*) "
               "FROM log where status like '404%' GROUP BY date "
               "HAVING count(*) > 129.08")

# Get all the reseults of the query and print them out
data3 = cursor.fetchall()
print data3

# Close the connection to the nws database
db.close()
