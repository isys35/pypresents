for ol in c1.orders[0].line_items:
    ol.id, ol.item, ol.quantity

print('-------')

for ol in c1.orders[1].line_items:
    ol.id, ol.item, ol.quantity
