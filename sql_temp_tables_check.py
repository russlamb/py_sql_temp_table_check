"""
This module contains functions to assist in generating SQL.
If calling from the command line, it accepts an file path to a file containing SQL to parse.

Usage:
    python find_sql_temp_tables <file_path>

This example will return SQL to drop all temp tables in <file_path> if they exist
"""

import re

def find_temp_tables(sql):
    """
    accepts a sql string and returns a list of strings containing the names of temp tables from the sql string
    """
    lines = sql.split("\n")
    pattern = r"^.*into\s+#.*$"
    r = re.compile(pattern, re.MULTILINE)

    tables=[]
    for match in r.findall(sql):
        table_start = match.find("#")
        
        tables.append(match[table_start:])

    return tables

def print_temp_table_check(tables):
    """accepts a list of table names and generates SQL that drops temp tables if they exist"""
    temp_table_check = "IF OBJECT_ID('tempdb..#x') IS NOT NULL DROP TABLE #x"

    for i in range(0,len(tables)):
        table = tables[i]
        check = temp_table_check.replace("#x",table)
        print(check)
        
if __name__ == "__main__":
    import sys
    if len(sys.argv)>1:
        file_path = sys.argv[1]
        with open(file_path,'r') as myfile:
            data=myfile.read()

        print(print_temp_table_check(find_temp_tables(data)))
    else:
        help(sys.modules[__name__])
    
    
    
    
