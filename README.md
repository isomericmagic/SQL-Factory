# SQL Factory
This is a prototype of a script I made at Nativo to perform bulk updates to the database.

The script reads a csv file and then uses the information in that file to generate multiple SQL statements.

The SQL statement itself is just a simple example (and I realize I could have just used one statement along with an IN() in the WHERE clause), but in practice most of the SQL statements support engineers run need to be individual SQL statements, so having something like this becomes useful when a large number of items need to be updated.
