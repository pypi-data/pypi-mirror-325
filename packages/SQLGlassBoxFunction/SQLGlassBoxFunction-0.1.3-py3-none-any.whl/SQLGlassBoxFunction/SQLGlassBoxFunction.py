import re
import os
from collections import OrderedDict
try:
    from pyspark.sql import SparkSession
except ImportError:
    SparkSession = None

class SQLUtil:
    def __init__(self):
        self.color_map = OrderedDict([
            ('comment', '\033[36m'),     # Cyan
            ('string', '\033[32m'),      # Green
            ('number', '\033[34m'),      # Blue
            ('function', '\033[33m'),    # Yellow
            ('keyword', '\033[35m'),     # Magenta
            ('reset', '\033[0m'),
        ])
        
        self.patterns = [
            (r'(--.*?$|/\*.*?\*/)', 'comment', re.DOTALL|re.MULTILINE|re.IGNORECASE),
            (r"('(?:''|[^'])*'|\"(?:\"\"|[^\"])*\")", 'string', 0),
            (r'\b(\d+\.?\d*|\.\d+)\b', 'number', 0),
            (r'\b(SELECT|FROM|WHERE|JOIN|ON|GROUP BY|HAVING|ORDER BY|LIMIT|'
             r'INSERT INTO|VALUES|UPDATE|SET|DELETE|CREATE TABLE|DROP TABLE|'
             r'CREATE|OR|REPLACE|TEMP|TEMPORARY|VIEW|AS|'
             r'ALTER TABLE|ADD|CONSTRAINT|PRIMARY KEY|FOREIGN KEY|REFERENCES|'
             r'UNIQUE|INDEX|NOT NULL|AND|OR|NOT|IN|IS NULL|IS NOT NULL|TRUE|FALSE|'
             r'INT|VARCHAR|CHAR|DATE|TIME|TIMESTAMP|BOOL)\b', 'keyword', re.IGNORECASE),
            (r'\b(COUNT|SUM|AVG|MAX|MIN|ABS|UPPER|LOWER|TRIM|SUBSTR|CONCAT)\b', 
             'function', re.IGNORECASE),
        ]

    def highlight(self, sql):
        """
        Highlights SQL syntax based on predefined patterns and colors.
        Args:
            sql (str): The SQL query string to be highlighted.
        Returns:
            str: The SQL query string with syntax highlighted using ANSI color codes.
        """
        combined = []
        
        # Compile all patterns with their flags
        for pattern, color, flags in self.patterns:
            combined.append(f'(?P<{color}>{pattern})')
            
        master_pattern = re.compile('|'.join(combined), re.DOTALL|re.MULTILINE | re.IGNORECASE)
        
        def replace(match):
            for name, color in self.color_map.items():
                if match.group(name):
                    return f'{color}{match.group()}{self.color_map["reset"]}'
            return match.group()
            
        return master_pattern.sub(replace, sql)
                
    def append_to_file(self, query) -> None:
        """
        Appends a given SQL query to a log file.
        This method writes the provided SQL query to a log file specified by the
        environment variable 'SQL_QUERY_LOG_FILE'. If the environment variable is
        not set, it defaults to 'default_sql_log.txt'. The method ensures that the
        query is appended to the file and prints a message indicating the absolute
        path of the log file.
        Args:
            query (str): The SQL query to be logged.
        """
        file_path = os.getenv('SQL_GBF_QUERY_LOG_FILE', 'default_sql_log.txt')
        
        # Ensure the directory exists
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        
        # Create the file if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                pass
        
        with open(file_path, 'a') as file:
            file.write(query + '\n')
        print(f'{self.color_map["comment"]}SQL Log File location: {os.path.abspath(file_path)}{self.color_map["reset"]}')


def sql(query, dry_run=False, write_to_log_file=True):
    """
    Executes or simulates the execution of an SQL query, with options to log the query.
    Parameters:
    query (str): The SQL query to be executed or highlighted.
    dry_run (bool, optional): If True, the query is only highlighted and not executed. Defaults to False.
    write_to_log_file (bool, optional): If True, the query is logged to a file. Defaults to True.
    Environment Variables:
    SQL_DRY_RUN (str): If set to 'True', '1', or 't', the query is only highlighted and not executed.
    SQL_WRITE_TO_LOG_FILE (str): If set to 'True', '1', or 't', the query is logged to a file.
    Returns:
    None
    """
    dry_run_env = os.getenv('SQL_GBF_DRY_RUN', 'False').lower() in ('true', '1', 't')
    write_to_log_env = os.getenv('SQL_GBF_WRITE_TO_LOG_FILE', 'True').lower() in ('true', '1', 't')
    
    sql_util = SQLUtil()
    print(sql_util.highlight(query))
    if write_to_log_file and write_to_log_env:
        sql_util.append_to_file(query)
    
    # Execute the query using Spark SQL
    if not dry_run and not dry_run_env:
        if SparkSession is None:
            raise ImportError("pyspark module is not available. Please install it to execute SQL queries.")

        sc = None
        if 'spark' not in globals():
            sc = SparkSession.builder \
                .appName("SQLHighlighter") \
                .getOrCreate()
        else:
            sc = spark
        sc.sql(query)
        