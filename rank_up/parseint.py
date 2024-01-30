def parse_int(string):
    all_words = string.split(" ")
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, 
               "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, 
               "twelve": 12, "thirteen": 13, "fourteen": 14, "fiveteen": 15, 
               "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19,
               "twenty": 20, "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60, 
               "seventy": 70, "eighty": 80, "ninety": 90}
    
    result = 0

    for word in all_words:
        n = 1

        if word == "hundred":
            m = 100
        elif word == "thousand":
            m = 1000

        for number in numbers:
            if word == number:
                n = number[word]
        
        

        #if word.endswith("ty"):
        #   


