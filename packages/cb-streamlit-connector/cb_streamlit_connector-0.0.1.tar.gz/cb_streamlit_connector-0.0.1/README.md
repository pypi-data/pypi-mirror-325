# Couchbase Connector for Streamlit

## 1. Introduction
This project provides a seamless integration between Streamlit and Couchbase, allowing developers to interact with Couchbase databases effortlessly. It enables users to fetch, insert, update, and delete data within Streamlit applications without needing to switch between different SDKs, enhancing the overall development experience.

## 2. Prerequisites
### System Requirements
- Couchbase Capella account ([Docs](https://docs.couchbase.com/cloud/get-started/intro.html))
- An operational cluster created in a project
- Configured cluster access permissions and allowed IP addresses ([Docs](https://docs.couchbase.com/cloud/get-started/connect.html#prerequisites))
- Connection string obtained from Couchbase Capella

### Installing Dependencies
To install the required dependencies, run:
```sh
pip install couchbase streamlit
```

## 3. Usage Guide

### Initializing the Connector
You can set up the Couchbase connection using either of the following methods:

#### **Option 1: Using `secrets.toml` (Recommended)**
For better security and convenience, store your credentials in a `.streamlit/secrets.toml` file at the root of your project. Learn more about [Streamlit Secrets Management](https://docs.streamlit.io/develop/concepts/connections/secrets-management):

```toml
[connections.couchbase]
CONNSTR = "<CONNECTION_STRING>"
USERNAME = "<CLUSTER_ACCESS_USERNAME>"
PASSWORD = "<CLUSTER_ACCESS_PASSWORD>"
BUCKET_NAME = "<BUCKET_NAME>"
SCOPE_NAME = "<SCOPE_NAME>"
COLLECTION_NAME = "<COLLECTION_NAME>"
```

Then, initialize the connection in your Streamlit application:

```python
import streamlit as st
from cb_streamlit_connector.connector import CouchbaseConnector

connection = st.connection(
    "couchbase",
    type=CouchbaseConnector
)
st.help(connection)
```

#### **Option 2: Passing Credentials Directly (Alternative)**
Alternatively, you can pass the connection details as keyword arguments:

```python
import streamlit as st
from cb_streamlit_connector.connector import CouchbaseConnector

connection = st.connection(
    "couchbase",
    type=CouchbaseConnector,
    CONNSTR="<CONNECTION_STRING>",
    USERNAME="<USERNAME>",
    PASSWORD="<PASSWORD>",
    BUCKET_NAME="<BUCKET_NAME>",
    SCOPE_NAME="<SCOPE_NAME>",
    COLLECTION_NAME="<COLLECTION_NAME>"
)
st.help(connection)
```

### Performing CRUD Operations

#### **Insert a Document**
```python
connection.insert_document("222", {"key": "value"})
st.write(connection.get_document("222"))
```

#### **Fetch a Document**
```python
st.write(connection.get_document("111"))
```

#### **Replace a Document**
```python
connection.replace_document("222", {"new_key": "new_value"})
st.write(connection.get_document("222"))
```

#### **Delete a Document**
```python
connection.remove_document("222")
st.write("Document 222 deleted")
```

#### **Run a Query**
```python
result = connection.query("SELECT * FROM `travel-sample`.`inventory`.`airline` LIMIT 5;")
st.write(result)
```
