from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    # for row in rows:
    #     print(row)
    return rows

# ## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """


# ]

prompt = [
    """
    You are an expert in translating English questions into SQL queries!
    The SQL database contains a table named NATION, representing information about nations.
    The NATION table has the following columns: N_NATIONKEY, N_NAME, N_REGIONKEY, and N_COMMENT.

    Example 1 - Retrieve a list of all nations in the dataset.
    Example 2 - Identify nations in Region X and list their details.
    Example 3 - Count the total number of nations in the dataset.   
    Example 4 - Retrieve detailed information about a specific nation.
    Example 5 - Search for nations with comments containing specific keywords.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM NATION;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM NATION WHERE N_REGIONKEY = X; -- Replace X with the desired region key.

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM NATION;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM NATION WHERE N_NATIONKEY = Y; -- Replace Y with the desired nation key.

    For Example 5, the SQL command will be something like this:
    SELECT * FROM NATION WHERE LOWER(N_COMMENT) LIKE '%keyword%'; -- Replace 'keyword' with the desired keyword.

    

    You are an expert in translating English questions into SQL queries!
    The SQL database contains a table named CUSTOMER, representing information about customers.
    The table includes columns such as C_CUSTKEY, C_NAME, C_ADDRESS, C_NATIONKEY, C_PHONE, 
    C_ACCTBAL, C_MKTSEGMENT, and C_COMMENT.

    Example 1 - Retrieve a sample of customer records:
    - Write an SQL query to retrieve a sample of customer records from the CUSTOMER table.

    Example 2 - Identify customers in a specific market segment:
    - Write an SQL query to identify customers in a particular market segment (C_MKTSEGMENT).
      Provide details of these customers.

    Example 3 - Count the total number of customers:
    - Write an SQL query to count the total number of customers in the CUSTOMER table.

    Example 4 - Retrieve detailed information about a specific customer:
    - Write an SQL query to retrieve detailed information about a specific customer using their key (C_CUSTKEY).

    Example 5 - Search for customers with comments containing specific keywords:
    - Write an SQL query to search for customers whose comments (C_COMMENT) contain specific keywords.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM CUSTOMER;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM CUSTOMER WHERE C_MKTSEGMENT = 'YourSegment'; -- Replace 'YourSegment' with the desired market segment.

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM CUSTOMER;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM CUSTOMER WHERE C_CUSTKEY = 'YourCustKey'; -- Replace 'YourCustKey' with the desired customer key.

    For Example 5, the SQL command will be something like this:
    SELECT * FROM CUSTOMER WHERE LOWER(C_COMMENT) LIKE '%keyword%'; -- Replace 'keyword' with the desired keyword.

    

    Explore the ORDERS table in the TPC-H dataset, which contains information about orders. 
    The table includes columns such as O_ORDERKEY, O_CUSTKEY, O_ORDERSTATUS, O_TOTALPRICE, O_ORDERDATE, and O_SHIPPRIORITY.
    Example 1 - Retrieve a sample of orders:
    - Write an SQL query to retrieve a sample of orders from the ORDERS table.

    Example 2 - Identify orders with a specific order status:
    - Write an SQL query to select orders from the ORDERS table based on a specific order status.
    Replace 'YourStatus' with the desired order status.

    Example 3 - Count the total number of orders:
    - Write an SQL query to count the total number of orders in the ORDERS table.

    Example 4 - Retrieve detailed information about a specific order:
    - Write an SQL query to retrieve detailed information about a specific order using its key (O_ORDERKEY).
    Replace 'YourOrderKey' with the desired order key.

    Example 5 - Search for orders with a total price above a certain threshold:
    - Write an SQL query to search for orders in the ORDERS table with a total price above a specific threshold.
    Replace 'YourThreshold' with the desired threshold.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM ORDERS;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM ORDERS WHERE O_ORDERSTATUS = 'YourStatus';

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM ORDERS;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM ORDERS WHERE O_ORDERKEY = YourOrderKey;

    For Example 5, the SQL command will be something like this:
    SELECT * FROM ORDERS WHERE O_TOTALPRICE > YourThreshold;


    Explore the PART table in the TPC-H dataset, which contains information about parts. 
The table includes columns such as P_PARTKEY, P_NAME, P_MFGR, P_BRAND, P_TYPE, and P_SIZE.

Example 1 - Retrieve a sample of parts:
- Write an SQL query to retrieve a sample of parts from the PART table.

Example 2 - Identify parts with a specific type:
- Write an SQL query to select parts from the PART table based on a specific type.
  Replace 'YourType' with the desired part type.

Example 3 - Count the total number of parts:
- Write an SQL query to count the total number of parts in the PART table.

Example 4 - Retrieve detailed information about a specific part:
- Write an SQL query to retrieve detailed information about a specific part using its key (P_PARTKEY).
  Replace 'YourPartKey' with the desired part key.

Example 5 - Search for parts with a specific brand:
- Write an SQL query to search for parts in the PART table with a specific brand.
  Replace 'YourBrand' with the desired part brand.

For Example 1, the SQL command will be something like this:
SELECT * FROM PART;

For Example 2, the SQL command will be something like this:
SELECT * FROM PART WHERE P_TYPE = 'YourType';

For Example 3, the SQL command will be something like this:
SELECT COUNT(*) FROM PART;

For Example 4, the SQL command will be something like this:
SELECT * FROM PART WHERE P_PARTKEY = YourPartKey;

For Example 5, the SQL command will be something like this:
SELECT * FROM PART WHERE P_BRAND = 'YourBrand';


    The SQL database contains a table named PARTSUPP, representing part-supplier relationships.
    The PARTSUPP table has the following columns: PS_PARTKEY, PS_SUPPKEY, PS_AVAILQTY, PS_SUPPLYCOST, and PS_COMMENT.

    Example 1 - Retrieve a sample of part-supplier records.
    Example 2 - Identify part-supplier relationships in Region X and list their details.
    Example 3 - Count the total number of part-supplier relationships in the dataset.
    Example 4 - Retrieve detailed information about a specific part-supplier relationship.
    Example 5 - Search for part-supplier relationships with comments containing specific keywords.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM PARTSUPP;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM PARTSUPP WHERE PS_REGIONKEY = X; -- Replace X with the desired region key.

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM PARTSUPP;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM PARTSUPP WHERE PS_PARTKEY = Y; -- Replace Y with the desired part key.

    For Example 5, the SQL command will be something like this:
    SELECT * FROM PARTSUPP WHERE LOWER(PS_COMMENT) LIKE '%keyword%'; -- Replace 'keyword' with the desired keyword.



    The SQL database contains a table named REGION, representing information about geographic regions.
    The REGION table has the following columns: RegionKey, RegionName, and Comment.

    Example 1 - Retrieve a list of all regions.
    Example 2 - Identify regions with specific attributes.
    Example 3 - Count the total number of regions in the dataset.
    Example 4 - Retrieve detailed information about a specific region.
    Example 5 - Search for regions with comments containing specific keywords.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM REGION;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM REGION WHERE R_ATTRIBUTE = 'YourAttribute'; -- Replace 'YourAttribute' with the desired attribute.

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM REGION;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM REGION WHERE RegionKey = Z; -- Replace Z with the desired region key.

    For Example 5, the SQL command will be something like this:
    SELECT * FROM REGION WHERE LOWER(Comment) LIKE '%keyword%'; -- Replace 'keyword' with the desired keyword.



    The SQL database contains a table named SUPPLIER, representing information about suppliers.
    The SUPPLIER table has the following columns: S_SUPPKEY, S_NAME, S_ADDRESS, S_NATIONKEY, S_PHONE, S_ACCTBAL, and S_COMMENT.

    Example 1 - Retrieve a sample of supplier records.
    Example 2 - Identify suppliers with specific attributes.
    Example 3 - Count the total number of suppliers in the dataset.
    Example 4 - Retrieve detailed information about a specific supplier.
    Example 5 - Search for suppliers with comments containing specific keywords.

    For Example 1, the SQL command will be something like this:
    SELECT * FROM SUPPLIER;

    For Example 2, the SQL command will be something like this:
    SELECT * FROM SUPPLIER WHERE S_ATTRIBUTE = 'YourAttribute'; -- Replace 'YourAttribute' with the desired attribute.

    For Example 3, the SQL command will be something like this:
    SELECT COUNT(*) FROM SUPPLIER;

    For Example 4, the SQL command will be something like this:
    SELECT * FROM SUPPLIER WHERE S_SUPPKEY = W; -- Replace W with the desired supplier key.

    For Example 5, the SQL command will be something like this:
    SELECT * FROM SUPPLIER WHERE LOWER(S_COMMENT) LIKE '%keyword%'; -- Replace 'keyword' with the desired keyword.

    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"tpch.db")
    st.subheader("Our Response is")
    for row in response:
        # print(row)
        st.header(row)
