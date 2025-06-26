# TODO: Complete the function below
def filter_fruits_starting_with_a(fruits):
    # Code here
    def filter_a(s):
        return s[0] == 'A' or s[0] == 'a'
    
    return list(filter(filter_a, fruits))

print(filter_fruits_starting_with_a(["aerwe", "erwfsd", "Adfsd", "dfgd"]))