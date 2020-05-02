all_items = {'arrows' : 12, 'gold coins' : 42, 'rope' : 1, 'torch': 6, 'dagger' : 1}


def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print('All items: ' + str(item_total))


displayInventory(all_items)