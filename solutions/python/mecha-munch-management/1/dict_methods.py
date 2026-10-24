"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item in items_to_add:
        if item in current_cart.keys():
            quantity = current_cart.get(item)
            current_cart[item] = quantity + 1
        else:
            current_cart.setdefault(item, 1)
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    cart = {}
    for item in notes:
        cart.setdefault(item, 1)
    return cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict.
        recipe_updates (iterable): Updates for the ideas section.

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    ideas.update(recipe_updates)
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """
    sorted_cart = dict(sorted(cart.items()))
    return sorted_cart


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    fulfillment_cart = {}
    for item in cart:
        information = []
        if item in aisle_mapping.keys():
            quantity = cart.get(item)
            information.append(quantity)
            
            extra_info = aisle_mapping.get(item)
            for info in extra_info:
                information.append(info)
                    
            fulfillment_cart.setdefault(item, information)

    sorted_reverse = dict(sorted(fulfillment_cart.items(), reverse=True))
    return sorted_reverse


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for item in fulfillment_cart:
        if item in store_inventory.keys():
            store = store_inventory.get(item)
            fulfill = fulfillment_cart.get(item)
            new_quantity = int(store[0]) - int(fulfill[0])
            if new_quantity <= 0:
                new_quantity = "Out of Stock"
            store_inventory[item] = [new_quantity, store[1], store[2]]      
    return store_inventory
