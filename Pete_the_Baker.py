'''
Pete likes to bake some cakes. He has some recipes and ingredients. 
Unfortunately he is not good in maths. Can you help him to find out, 
how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the 
available ingredients (also an object) and returns the maximum number 
of cakes Pete can bake (integer). For simplicity there are no units 
for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 
200). Ingredients that are not present in the objects, can be 
considered as 0.

'''

def cakes(recipe, available):
    #start with defualt number of cakes
    num_cakes = False

    #loop through items in the recipe
    for key, value in recipe.items():
        #if the item is found in the receip cacluate the available 
        if key in available:
            #using int to round down 
            current_available = int(available[key]/value)
            #if the currently available is 0, break program (can't go any lower)
            if current_available == 0: 
                num_cakes = 0
                break
            #if the num_cake is at defult
            if num_cakes == False: num_cakes = current_available
            #see if the current avaible amount is less than previous num_cakes
            if current_available < num_cakes: num_cakes = current_available
            
            # print(key, current_available, num_cakes)
        
        #if the item isn't available then cakes = 0 and break loop
        else:
            num_cakes = 0
            print('no {} in available'.format(key))
            break

    
    print('\n', num_cakes)
    return num_cakes


# must return 2
cakes( 
    {'flour': 500, 'sugar': 200, 'eggs': 1} , 
    {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200} 
    )
# must return 0
cakes(
    {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, 
    {'sugar': 500, 'flour': 2000, 'milk': 2000}
    )

cakes(
    {'butter': 84, 'flour': 49, 'nuts': 99} ,

    {'butter': 1145, 'crumbles': 167, 'oil': 7162, 
    'eggs': 6914, 'nuts': 5886, 'apples': 8769, 
    'sugar': 8181, 'pears': 7958, 'flour': 4, 'chocolate': 9880}
    )
#should equal 0
