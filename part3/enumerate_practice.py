#write a function which prints something. 

#call that function from a second function which enumerates over it. 

def print_green_juice(number, ingredients):
    print "Add to Vitamix #{} {}".format(number, ingredients)
    
def main():
    list_of_ingredients = ['kale', 'spinach', 'dandelion', 'coriandar']
    for i, list_of_ingredient in enumerate(list_of_ingredients):
        print_green_juice(i, list_of_ingredient)
        
if __name__=='__main__':
    main()