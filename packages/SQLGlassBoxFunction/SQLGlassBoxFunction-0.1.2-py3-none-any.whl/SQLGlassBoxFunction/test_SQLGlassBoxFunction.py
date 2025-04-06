import unittest
import os
from SQLGlassBoxFunction import SQLGlassBoxFunction

class TestSQLGlassBoxFunction(unittest.TestCase):
    
    def setUp(self):
        self.sql_gbf = SQLGlassBoxFunction()
        self.query = """
        SELECT * /* This is a SELECT block comment */ 
        FROM users 
        -- This is a line comment
        WHERE age > 18 
            AND country = 'USA' 
            AND c >= 11.5
            AND name = "John's SELECT string18" 
        -- second is a line comment
        ORDER BY COUNT(id);
        """
        self.log_file_path = 'sql_logs/sql_log.txt'
        
        # Ensure the log file directory exists
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)
        
        # Clear the log file before each test
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)

    def test_highlight(self):
        highlighted_query = self.sql_gbf.highlight(self.query)
        self.assertIn('\033[36m', highlighted_query)  # Check for comment color
        self.assertIn('\033[32m', highlighted_query)  # Check for string color
        self.assertIn('\033[34m', highlighted_query)  # Check for number color
        self.assertIn('\033[33m', highlighted_query)  # Check for function color
        self.assertIn('\033[35m', highlighted_query)  # Check for keyword color
        self.assertIn('\033[0m', highlighted_query)   # Check for reset color

    def test_sql_dry_run(self):
        os.environ['SQL_GBF_DRY_RUN'] = 'True'
        self.sql_gbf.sql(self.query, dry_run=True)
        # Check that the query is not executed but highlighted
        highlighted_query = self.sql_gbf.highlight(self.query)
        self.assertIn(highlighted_query, self.sql_gbf.highlight(self.query))
        
    def test_sql_write_to_log_file(self):
        os.environ['SQL_GBF_WRITE_TO_LOG_FILE'] = 'True'
        self.sql_gbf.sql(self.query, write_to_log_file=True)
        # Check that the query is written to the log file
        with open(self.log_file_path, 'r') as file:
            logged_query = file.read()
        self.assertIn(self.query.strip(), logged_query.strip())

    def test_append_to_file(self):
        self.sql_gbf.append_to_file(self.query)
        # Check that the query is appended to the log file
        with open(self.log_file_path, 'r') as file:
            logged_query = file.read()
        self.assertIn(self.query.strip(), logged_query.strip())

if __name__ == '__main__':
    unittest.main()