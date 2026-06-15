def tabla_cartera():

    '''Genera una tabla de activos predefinidos.'''

    #items = [nombre, ticker, valor_ref, vol_act, met_op, unidades, punt_conf]

    tabla_activos = [
    ["Apple Inc.", "AAPL", 213.50, 72000000000, "Swing Trading", 850000, 9],
    ["Microsoft Corporation", "MSFT", 415.20, 55000000000, "HODL", 430000, 9],
    ["NVIDIA Corporation", "NVDA", 1087.00, 98000000000, "Swing Trading", 210000, 8],
    ["Bitcoin", "BTC", 67400.00, 42000000000, "HODL", 15000, 7],
    ["Ethereum", "ETH", 3520.00, 18000000000, "Swing Trading", 95000, 7],
    ["SPDR S&P 500 ETF", "SPY", 528.75, 31000000000, "HODL", 600000, 10],
    ["Invesco QQQ Trust", "QQQ", 451.30, 22000000000, "Swing Trading", 380000, 9],
    ["Tesla Inc.", "TSLA", 177.60, 25000000000, "Day Trading", 500000, 6],
    ["Amazon.com Inc.", "AMZN", 188.40, 33000000000, "Swing Trading", 470000, 8],
    ["Alphabet Inc.", "GOOGL", 174.90, 27000000000, "HODL", 560000, 9],
    ["Meta Platforms Inc.", "META", 502.10, 29000000000, "Swing Trading", 310000, 8],
    ["Solana", "SOL", 175.30, 4200000000, "Day Trading", 120000, 6],
    ["Binance Coin", "BNB", 598.00, 2800000000, "HODL", 75000, 6],
    ["SPDR Gold Shares", "GLD", 228.50, 1900000000, "HODL", 420000, 9],
    ["iShares Silver Trust", "SLV", 27.40, 890000000, "Swing Trading", 900000, 7],
    ["Netflix Inc.", "NFLX", 648.00, 8500000000, "Swing Trading", 185000, 8],
    ["Berkshire Hathaway B", "BRK.B", 412.80, 5100000000, "HODL", 320000, 10],
    ["XRP", "XRP", 0.52, 2300000000, "Day Trading", 5000000, 5],
    ["Palantir Technologies", "PLTR", 24.80, 3700000000, "Scalping", 750000, 5],
    ["ARK Innovation ETF", "ARKK", 48.60, 1200000000, "Swing Trading", 430000, 5],
    ]
    return tabla_activos

def tabla_catalogo():
    '''
    Genera un catálogo amplio de activos disponibles.
    Columnas:
    [nombre, valor_ref, vol_act, met_op, punt_conf]
    '''

    tabla_catalogo = [
        # Activos originales (adaptados)
        ["Apple Inc.", 213.50, 72000000000, "Swing Trading", 9],
        ["Microsoft Corporation", 415.20, 55000000000, "HODL", 9],
        ["NVIDIA Corporation", 1087.00, 98000000000, "Swing Trading", 8],
        ["Bitcoin", 67400.00, 42000000000, "HODL", 7],
        ["Ethereum", 3520.00, 18000000000, "Swing Trading", 7],
        ["SPDR S&P 500 ETF", 528.75, 31000000000, "HODL", 10],
        ["Invesco QQQ Trust", 451.30, 22000000000, "Swing Trading", 9],
        ["Tesla Inc.", 177.60, 25000000000, "Day Trading", 6],
        ["Amazon.com Inc.", 188.40, 33000000000, "Swing Trading", 8],
        ["Alphabet Inc.", 174.90, 27000000000, "HODL", 9],
        ["Meta Platforms Inc.", 502.10, 29000000000, "Swing Trading", 8],
        ["Solana", 175.30, 4200000000, "Day Trading", 6],
        ["Binance Coin", 598.00, 2800000000, "HODL", 6],
        ["SPDR Gold Shares", 228.50, 1900000000, "HODL", 9],
        ["iShares Silver Trust", 27.40, 890000000, "Swing Trading", 7],
        ["Netflix Inc.", 648.00, 8500000000, "Swing Trading", 8],
        ["Berkshire Hathaway B", 412.80, 5100000000, "HODL", 10],
        ["XRP", 0.52, 2300000000, "Day Trading", 5],
        ["Palantir Technologies", 24.80, 3700000000, "Scalping", 5],
        ["ARK Innovation ETF", 48.60, 1200000000, "Swing Trading", 5],
        ["Advanced Micro Devices", 165.20, 21000000000, "Swing Trading", 8],
        ["Intel Corporation", 34.50, 15000000000, "HODL", 6],
        ["Salesforce Inc.", 255.80, 18000000000, "Swing Trading", 8],
        ["Adobe Inc.", 540.10, 12000000000, "HODL", 9],
        ["Oracle Corporation", 142.70, 11000000000, "Swing Trading", 7],
        ["Vanguard Total Stock Market ETF", 265.40, 14000000000, "HODL", 10],
        ["iShares MSCI Emerging Markets", 42.30, 9000000000, "Swing Trading", 7],
        ["Vanguard FTSE Europe ETF", 64.20, 3000000000, "HODL", 7],
        ["Cardano", 0.68, 1500000000, "Swing Trading", 6],
        ["Polkadot", 7.40, 1200000000, "Swing Trading", 6],
        ["Avalanche", 36.50, 1800000000, "Day Trading", 6],
        ["Chainlink", 18.90, 2100000000, "Swing Trading", 7],
        ["Litecoin", 92.10, 1300000000, "HODL", 6],
        ["Coca-Cola Company", 63.50, 8000000000, "HODL", 9],
        ["PepsiCo Inc.", 172.40, 7000000000, "HODL", 9],
        ["Nike Inc.", 98.30, 6000000000, "Swing Trading", 7],
        ["McDonald's Corporation", 282.60, 7500000000, "HODL", 9],
        ["Exxon Mobil Corporation", 118.20, 9500000000, "HODL", 8],
        ["Chevron Corporation", 160.50, 8700000000, "HODL", 8],
        ["NextEra Energy", 74.80, 5200000000, "Swing Trading", 8],
        ["JPMorgan Chase", 198.40, 11000000000, "HODL", 9],
        ["Goldman Sachs", 452.30, 7200000000, "Swing Trading", 8],
        ["Morgan Stanley", 102.10, 6800000000, "Swing Trading", 8],
        ["Johnson & Johnson", 158.20, 6500000000, "HODL", 9],
        ["Pfizer Inc.", 28.40, 5400000000, "Swing Trading", 6],
        ["Moderna Inc.", 132.50, 3200000000, "Day Trading", 6],
    ]

    return tabla_catalogo