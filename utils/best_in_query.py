
def best_in_query(df, query, key):
    # Your code goes here
    result = df.query(query).sort_values(by=key, ascending=False)
    return result[["Name","Type_Full"]].head(5)

