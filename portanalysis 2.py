import csv

# Read the CSV file
with open('rollova.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# Get current holdings
holdings = {}
for row in data:
    if row['Transaction Type'] == '':
        symbol = row['Symbol']
        shares = float(row['Shares'])
        holdings[symbol] = shares

# Analyze and provide recommendations
for symbol, shares in holdings.items():
    if symbol == 'CLSK':
        if shares > 200:
            print(f"You have a large holding of {shares} shares in Cleanspark (CLSK). Consider diversifying your portfolio.")
        else:
            print(f"Your holding of {shares} shares in Cleanspark (CLSK) seems reasonable.")

    elif symbol == 'MLGO':
        if shares > 1000:
            print(f"You have a substantial holding of {shares} shares in Microalgo (MLGO), which is a relatively small company. Consider reducing your exposure.")
        else:
            print(f"Your holding of {shares} shares in Microalgo (MLGO) is reasonable.")

    elif symbol == 'MSTR':
        print(f"Holding {shares} share(s) in Microstrategy (MSTR) is a concentrated bet on Bitcoin's success. Evaluate your risk tolerance.")

    elif symbol == 'RIOT':
        if shares > 50:
            print(f"You have a large holding of {shares} shares in Riot Platforms (RIOT). Consider trimming your position to reduce risk.")
        else:
            print(f"Your holding of {shares} shares in Riot Platforms (RIOT) seems reasonable.")

    else:
        print(f"No specific recommendation for {symbol}.")