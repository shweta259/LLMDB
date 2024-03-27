1. Create a virtual env
conda create -p venv python==3.10 -y

2. Activate the venv created in earlier step
conda activate /Users/shweta/Documents/DR/GenAI/Gemini/venv

3. Install all the required libraries in requirements.txt
pip install -r requirements.txt

4. Run application
streamlit run sql.py

---------------------------------------------------------------------------------------------------------------------

Database cmds::

Connect to the db :
.open tpch.db

DROP TABLE IF EXISTS ORDERS;

CREATE TABLE ORDERS (
    O_ORDERKEY INTEGER PRIMARY KEY,
    O_CUSTKEY INTEGER NOT NULL,
    O_ORDERSTATUS CHAR(1) NOT NULL,
    O_TOTALPRICE DECIMAL(15, 2) NOT NULL,
    O_ORDERDATE DATE NOT NULL,
    O_ORDERPRIORITY CHAR(15) NOT NULL,
    O_CLERK CHAR(15) NOT NULL,
    O_SHIPPRIORITY INTEGER NOT NULL,
    O_COMMENT VARCHAR(79) NOT NULL
);

.separator '|'

.import /Users/shweta/Downloads/TPC-HV3.0.1/dbgen/orders.tbl ORDERS;
