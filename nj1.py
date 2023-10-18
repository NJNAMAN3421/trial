print("hello NJ")
import pandas as pd
transactions=pd.read_csv("422ceab9-b775-4f4a-8a04-066006bf204b_83d04ac6-cb74-4a96-a06a-e0d5442aa126_transactions.csv")
orders=pd.read_csv("419f8355-6271-44cc-a20b-fea8bd241428_83d04ac6-cb74-4a96-a06a-e0d5442aa126_orders.csv")
customers=pd.read_csv("156c0733-d225-4b76-a984-3ed5e19eb16d_83d04ac6-cb74-4a96-a06a-e0d5442aa126_customers.csv")
#merging the datasets
merged_data = pd.merge(orders, transactions, on='order_id', how='inner')

# Filtering orders with high-value transactions (sales amount > 150)
high_value_orders = merged_data[merged_data['sales'] > 150]

# Getting the list of order IDs with high-value transactions
high_value_order_ids = high_value_orders['order_id'].unique()

# Displaying the list of order IDs
print("List of order IDs with high-value transactions:")
print(high_value_order_ids)


