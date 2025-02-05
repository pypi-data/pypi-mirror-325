# GestUniDt
It is a very basic personal project to quickly store and fetch different types of data into csv files

## Installation

```bash
pip install GestUniDt

```
## Usage

```python


# Import the library
from GestUniDt import Gud 

# Initialize the main class
g = Gud()

# Use the .new('file_name') method to create a new file
# Use the .idCol() method to add an auto-incrementing id column
# Use the .timeCol() method to add a column that will show the time when a row is added
# Use the .textCol() method to add a simple text column
# Use the .dataCol() to add different types of data who'll be serialized
# You can use multiple textCols and dataCols
g.new('log.csv').idCol().timeCol().textCol('source').textCol('type').dataCol('content')

# Use the .load('file_name') to load an existing file
g.load('log.csv')

# Use the .add() method to add a row
# You can use a list with textCols and dataCols values in order
# You can add multiple lists to add multiple rows
g.add(['Main Function', 'Info', 'Starting the program...'], ['Config Function', 'Error', 'File Config Not Found.'])

# You can also use one or multiple dictionaries as parameter to add rows
g.add({'type': 'log', 'content': 'Another log message.'})

# You can add lists in dataCols
g.add(['numbers', [1, 2, 3, 4]])

# You can add dictionaries in dataCols
g.add(['objects', {'name': 'chair', 'code': 'ab123cd'}])


# Use the .get() method to make query-like data fetching
# Use the .where(col, condition) method to filter the rows
# Use the .cols([cols_list]) to get only selected columns
# Use the .last(n) and the .first(n) methods to get the last or the first n columns
# Use the .values() method to get the result as a list
# Without any other method the .get() method will return the entire content
# Without the .values() method the result will be returned as a dataframe
# You can use multiple .where() methods to add more conditions
# the .where() method accepts "=", "!=", ">", "<", ">=", "<=" conditions


res = g.get().where('type', '= log').cols(['type', 'content']).values()
res = g.get().where('id', '> 2').cols(['id', 'type', 'content']).last(2).values()
res = g.get().where('id', '> 2').where('type', '= log').cols(['id', 'type', 'content']).last(2).values()


# Use the .del_() method to delete one or multiple rows with .where() method filtering.
deleted_count = g.del_().where('type', '= log').execute()

# Use the .count() method to get the actual number of rows
current_count = g.count()

# Use the .clear() method to delete every row
g.clear()

# Use the .deleteCsvFile() method to delete the file.
g.deleteCsvFile()

```

## Development status

**GestUniDt** is a work-in-progress personal project. Suggestions, feature requests, and constructive feedback are highly welcome. Feel free to open an issue or submit a pull request.