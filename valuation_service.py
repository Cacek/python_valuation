import pandas as pd

'''Create dataframes from files'''
df_data = pd.read_csv('data.csv')
df_currencies = pd.read_csv('currencies.csv')
df_matching = pd.read_csv('matching.csv')

'''List all dataframes'''
print(df_data, '\n')
print(df_currencies, '\n')
print(df_matching, '\n')

'''Create new column [total_price]'''
df_data["total_price"] = df_data["price"] * df_data["quantity"]
print(df_data, '\n')

'''JOIN data and currencies dataframes'''
df_data = pd.merge(df_data, df_currencies, on='currency')
print(df_data, '\n')

'''Create new column [total_value[PLN]]'''
df_data["total_value[PLN]"] = df_data["total_price"] * df_data["ratio"]
print(df_data, '\n')

'''JOIN data and matching dataframes'''
df_data = pd.merge(df_data, df_matching, on='matching_id')
print(df_data, '\n')

'''Create sub dataframes with particular matching ids'''
df_filtered_id_1 = df_data[df_data.matching_id == 1].sort_values(by=['total_price'], ascending=False)
print(df_filtered_id_1, '\n')
df_filtered_id_2 = df_data[df_data.matching_id == 2].sort_values(by=['total_price'], ascending=False)
print(df_filtered_id_2, '\n')
df_filtered_id_3 = df_data[df_data.matching_id == 3].sort_values(by=['total_price'], ascending=False)
print(df_filtered_id_3, '\n')

'''Count ignored_products'''
ignored_products_count_id_1 = df_filtered_id_1.shape[0] - df_filtered_id_1['top_priced_count'].values[0]
ignored_products_count_id_2 = df_filtered_id_2.shape[0] - df_filtered_id_2['top_priced_count'].values[0]
ignored_products_count_id_3 = df_filtered_id_3.shape[0] - df_filtered_id_3['top_priced_count'].values[0]

df_top_priced_count_id_1 = (df_filtered_id_1.head(df_filtered_id_1['top_priced_count'].values[0]))
df_top_priced_count_id_2 = (df_filtered_id_2.head(df_filtered_id_2['top_priced_count'].values[0]))
df_top_priced_count_id_3 = (df_filtered_id_3.head(df_filtered_id_3['top_priced_count'].values[0]))


'''Concat sub dataframes into one big'''
df_filtered_all_ids = pd.concat([df_top_priced_count_id_1, df_top_priced_count_id_2, df_top_priced_count_id_3])
print(df_filtered_all_ids, '\n')

'''Sorting'''
df_to_csv = df_filtered_all_ids.sort_values(by=['id'])
print(df_to_csv)

'''Export dataframe to csv'''
df_to_csv.to_csv('top_products.csv', index=False)
