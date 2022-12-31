def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        text_result ='YOU SHALL PASS'
        print(text_result)
    else:
        text_result ='YOU SHALL NOT PASS'
        print(text_result)
    return text_result    
leap_year(year)

assert leap_year(5) == 'YOU SHALL NOT PASS'
