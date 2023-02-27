o3 = Order(customer = c1)
orderline1 = OrderLine(item = i1, quantity = 5)
orderline2 = OrderLine(item = i2, quantity = 10)

o3.line_items.append(orderline1)
o3.line_items.append(orderline2)

session.add_all([o3,])
session.new
session.commit()
