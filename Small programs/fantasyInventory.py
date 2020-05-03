all_items = {'arrow' : 12, 'gold coin' : 42, 'rope' : 1, 'torch': 6, 'dagger' : 1}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('All items: ' + str(item_total))


displayInventory(all_items)


def addToInventory(inventory, addedItems):
    for k in addedItems:
        inventory.setdefault(k, 0)
        inventory[k] = inventory[k] + 1


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(all_items, dragonLoot)
displayInventory(all_items)

