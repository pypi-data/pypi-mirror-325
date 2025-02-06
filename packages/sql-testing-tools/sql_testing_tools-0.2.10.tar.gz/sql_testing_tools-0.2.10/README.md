A library that normalizes simple SQL queries and compares them first by equality of the normalized string and then using the cosette API. 

#### [Beta in Development!]
 [![Build and Test](https://github.com/ValentinHerrmann/sql_testing_tools/actions/workflows/python-build.yml/badge.svg)](https://github.com/ValentinHerrmann/sql_testing_tools/actions/workflows/python-build.yml)
 [![Build and Test](https://github.com/ValentinHerrmann/sql_testing_tools/actions/workflows/python-unittests.yml/badge.svg)](https://github.com/ValentinHerrmann/sql_testing_tools/actions/workflows/python-unittests.yml)

- Submit bug reports and features requests at: https://github.com/ValentinHerrmann/sql_testing_tools
- PyPi-Package available at: https://pypi.org/project/sql-testing-tools/ 


## Getting started

### Imports
``` python
# ensure to always use the latest version of sql_testing_tools
import os
os.system('pip install -U sql_testing_tools')

# import sql_testing_tools
import sql_testing_tools.BaseAccess as Ba
import sql_testing_tools.Helper as He

# import unittest and create TestClass
import unittest 
class TestClass(unittest.TestCase):
    # Ba.setDBName(...)
    # ...
```

### Choosing a database

On top level of your test class, set the SQLite database you want to use. 

**Option 1:** Use the predefined ones from [dbiu_databases](https://github.com/ValentinHerrmann/dbiu_databases) which are based on [datenbanken-im-unterricht.de](https://www.datenbanken-im-unterricht.de/catalog.php)

``` python
    # with DB name (preferred)
    # --> only available if current dbiu_databases version has been imported to sql_testing_tools
    Ba.setDBName("dbiu.bayern")

    # or with dbiu_databases version number
    # --> available as soon as a dbiu_databases version has been published on PyPi
    Ba.setDBName(2) 
```

Currently supported to use with DB name are: 
1. `dbiu.bahn`: https://www.dbiu.de/bahn
2. `dbiu.bayern`: https://www.dbiu.de/bayern
3. `dbiu.bundestag`: https://www.datenbanken-im-unterricht.de/downloads/bundestag.zip
4. `dbiu.bundestag_einfach`: https://www.dbiu.de/bundestagsmitglieder
5. `dbiu.film_fernsehen`: https://www.dbiu.de/filmundfernsehen
6. `dbiu.haushaltsausstattung`: https://www.dbiu.de/haushaltsausstattung
7. `dbiu.straftaten`: https://www.datenbanken-im-unterricht.de/downloads/kriminalstatistik-erweitert.zip
8. `dbiu.straftaten_einfach`: https://www.dbiu.de/kriminalstatistik
9. `dbiu.kunstsammlung`: https://www.dbiu.de/kunstsammlung
10. `dbiu.ladepunkte`: https://www.dbiu.de/ladepunkte
11. `dbiu.laenderspiele`: https://www.dbiu.de/laenderspiele
12. `dbiu.lebensmittel`: https://www.dbiu.de/lebensmittel
13. `dbiu.schulstatistik`: https://www.dbiu.de/schulstatistik
14. `dbiu.studierende`: https://www.dbiu.de/studierende
15. `dbiu.unfallstatistik`: https://www.dbiu.de/unfallstatistik
16. `dbiu.videospiele_einfach`: https://www.dbiu.de/videospiele
17. `dbiu.videospiele`: https://www.dbiu.de/videospiele2
18. `dbiu.wetterdaten`: https://www.dbiu.de/wetterdaten

**Option 2:** Use your own SQLite database with relative path starting at the working dir of your test repository.
``` python
    Ba.setDBName("databases/bayern.db")
```

### Available testing features

The following methods are available for use in test methods:


**Run the query to find out if syntax/database errors occur.**
``` python
try:
    Ba.runAndGetStringTable_fromFile("sqlfile.sql")
except Exception as e:
    # the execution failed (usually due to syntax or database errors)
    self.fail(e)
```



**Set sql files to be compared (optional).**
The sql strings will  be normalized and used or all following methods (to improve performance) until new files are specified. All check...() functions call setup(...) as first step. If one argument is `""` or `None` the corresponding file is not changed. Therefore calling the check...() functions without arguments does not change the sql files that are compared.
``` python
# Raises an Exception if one of the files is empty. 
setup("sqlfile.sql","solution.sql")
```

**Compared single parts of a sql query**
Call without arguments to keep the last normalized sql strings (and improve performance) and with one or two sql file paths to load and normalize new queries. 
Each check was successfull if `""` is returned. Returns a German error message if not. 
Each method compares the normalized string between the start keyword and the next keyword or ;
``` python

res = He.checkColumns() # starts at "SELECT"
res = He.checkTables() # starts at "FROM"
res = He.checkCondition() # starts at "WHERE"
res = He.checkOrder() # starts at "ORDER BY"
res = He.checkGroup() # starts at "GROUP BY"
```

In special cases where you'd like to start and stop at individual keywords for comparison use this directly:
``` python
# Can not be called with new sql files. If needed call setup(...) before.
res = checkKeywords("startKeyword",["end","keywords"]) 
```

Compares equality of the full normalized sql strings and if not equal uses the Cosette API (cosette.cs.washington.edu) for comparison. A file `cosette_apikey.txt` with only the apikey in it on root level of the test repository is required to use this feature. If not existant, only the string comparison is performed. *Warning: Cosette is currently not maintained!*

``` python
res = checkEquality()
```









### Changelog

##### V 0.2.10
- fixed part checks if keywords are in wrong order

##### V 0.2.9
- added NOT support
- improved Parentheses handling

##### V 0.2.8
- ignore case in '=' string comparison and convert to LIKE (if no '%', '_' in String)

##### V 0.2.7
- Normalize String unequality: ...<>..., ...!=..., ...NOT LIKE... --> NOT...LIKE...

##### V 0.2.6
- Fixed bug in checkKeywords: if keyword was present in one query and not in the other, the comparison was not performed correctly.

##### V 0.2.5
- Added support for [dbiu.de](https://www.datenbanken-im-unterricht.de/catalog.php) databases 1-18 (loaded via [dbiu_databases](https://github.com/ValentinHerrmann/dbiu_databases)) with option to still load DBs from local repo.
- Improved docs

##### V 0.2.4
- Added more check methods for single parts of queries: checkColumns, checkTables, checkCondition, checkOrder, checkGroup, checkKeywords

##### V 0.2.3
- fix: ASC/DESC in ORDER BY (also with multiple columns and order directions), no direction treated as ASC
- Verified that ; and whitespaces, linebreaks at end of query are ignored

##### V 0.2.2 
- Support LIKE
- Support '<=' and '>=' (geq and leq)

##### V 0.2.1
- Support LIMIT
  
##### V 0.1.9 + 0.2.0
- Support ORDER BY

##### V 0.1.8
- Fixed linebreak problems: Linebreaks are now converted into whitespaces before parsing where tokens

##### V 0.1.6 + V 0.1.7
- Fixed import error to ensure imports working in different environments

##### V 0.1.4 + V 0.1.5
- Chained conditions (with AND,OR and Paranthesises) in WHERE statement
- Aggregate Functions

##### V 0.1.3
- SELECT: columns with our without table prefix
- FROM: one or more table from DB; no queries as tables!
- WHERE: single conditions; no Paranthesises!
- GROUP BY one or more columns

