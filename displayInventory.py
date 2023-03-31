stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    total_inventory = 0
    print('Inventory:')
    for item,amount in inventory.items():
        print(amount,item)
        total_inventory += amount
    print('Total number of items:',total_inventory)

if __name__ == "__main__":
    displayInventory(stuff)
