
def most_connected(df, ftype):
    # Your code goes here
    same_type = df[df["strength"] == ftype] #Compare each line w/ BFFs. the second df* (df*[df...]) gives us back only the true lines.

    counts = same_type["Name_friend1"].value_counts() #How many times each name appears (from biggest to smallest, no need to put "ascending=False" inside the parentheses)

    best_pokemon = counts.index[0] #The names are in the index, so the first one has the most friendships
    return f"{best_pokemon} has most {ftype}"
