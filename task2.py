def update_car_info(**kwargs):
    car = kwargs  
    car['is_available'] = True
    return car

car_data = update_car_info(brand="Porsche", price=75000)
print(car_data)