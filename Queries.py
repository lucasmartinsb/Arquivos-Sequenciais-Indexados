def countFromCountry(indexCountry, country):
    count = 0
    for row in indexCountry:
        if(row[1][0:20].strip() == country):
            count+=1
    return count