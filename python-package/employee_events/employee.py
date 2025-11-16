# Import the QueryBase class
#### YOUR CODE HERE
import pandas as pd
import query_base 
# Import dependencies needed for sql execution
# from the `sql_execution` module
#### YOUR CODE HERE
from sql_execution import connect, db_path, QueryMixin, query
# Define a subclass of QueryBase
# called Employee
#### YOUR CODE HERE
class Employee(query_base.QueryBase, QueryMixin):

    # Set the class attribute `name`
    # to the string "employee"
    #### YOUR CODE HERE
    name = "employee"
    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def names(self):

        # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database
        #### YOUR CODE HERE
        conn = connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT full_name, employee_id
            FROM {self.name}
        """)
        return cursor.fetchall()

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
    #### YOUR CODE HERE
    def username(self, id):

        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
        #### YOUR CODE HERE
        conn = connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f"""
            SELECT full_name
            FROM {self.name}
            WHERE employee_id = {id}
        """)
        return cursor.fetchall()

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):
        conn = connect(db_path)
        query = f"""
            SELECT ee.event_date,
                   SUM(ee.positive_events) AS positive_events,
                   SUM(ee.negative_events) AS negative_events
            FROM employee_events ee
            JOIN {self.name} e
                USING(employee_id)
            WHERE e.employee_id = {id}
            GROUP BY ee.event_date
            ORDER BY ee.event_date
        """
        return pd.read_sql_query(query, conn)