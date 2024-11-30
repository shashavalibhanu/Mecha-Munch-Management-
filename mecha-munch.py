"""Functions to manage a users shopping cart items."""
def add_item(current_cart, items_to_add):
    for item in items_to_add:
        count = current_cart.setdefault(item, 0)
        current_cart[item] += 1
    return current_cart
   ## new_items = current_cart | items_to_add
    """Add items to shopping cart.
 
    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    pass
def read_notes(notes):
    
    note= dict.fromkeys(notes,1)
    return note
    
    
    """Create user cart from an iterable notes entry.
 
    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    pass
def update_recipes(ideas, recipe_updates):
    update_1 = ideas.update(recipe_updates)
    update_1 = ideas
    return update_1
    """Update the recipe ideas dictionary.
 
    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    pass
def sort_entries(cart):
  
    return dict(sorted(cart.items()))
    """Sort a users shopping cart in alphabetically order.
 
    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    pass
def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.
 
    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment_dict={}
    for item in cart.keys():
        isle_mapping[item].insert(0,cart[item])
        fulfillment_dict[item]=isle_mapping[item]
    new_dict={}
    new_dict |= reversed(sorted(fulfillment_dict.items()))
    return new_dict
        
    
        
    
   
    
    """Combine users order to aisle and refrigeration information.
 
    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    pass
def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        if store_inventory.get(item, 'err') != 'err':
            bought = fulfillment_cart[item][0]
            store_inventory[item][0] -= bought
            if store_inventory[item][0] == 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory
    ''' for key in fulfillment_cart.keys():
        store_inventory[key][0] -= fulfillment_cart[key][0]
        if store_inventory[key][0]<=0:
            store_inventory[key][0]="Out of Stock"
     return store_inventory'''
    
    """Update store inventory levels with user order.
 
    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    pass
