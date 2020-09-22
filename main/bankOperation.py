def addOperation(rubles, years):
    for i in range(years):
        rubles = rubles + (rubles/100*10)
    return (rubles)


def addAccount(rubles):
    for i in rubles:
        rubles = [rubles]
    return rubles
