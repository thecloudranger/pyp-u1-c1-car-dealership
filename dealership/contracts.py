class Contract(object):
    def __init__(self, vehicle, customer):
      self.vehicle = vehicle
      self.customer = customer
      self.employee_discount = self.get_employee_discount()
#       self.vehicle_type = self.vehicle.__class__.__name__
    
    def get_vehicle_type(self):
      return self.vehicle.__class__.__name__
    
    def sale_price(self):
      return self.vehicle.sale_price()
    
    def get_employee_discount(self):
      if self.customer.is_employee():
        return 0.9
      else:
        return 1

class BuyContract(Contract):
    VEHICLE_MULTIPLIERS = {
        "Car": 1.07,
        "Motorcycle": 1.03,
        "Truck": 1.11
    }
    
    def __init__(self, vehicle, customer, monthly_payments):
        super().__init__(vehicle, customer)
        self.monthly_payments = monthly_payments
    
    def total_value(self):
      return (self.sale_price() + (self.VEHICLE_MULTIPLIERS[self.get_vehicle_type()]* self.monthly_payments * self.sale_price() /100)) * self.employee_discount
      
    def monthly_value(self):
      return self.total_value()/self.monthly_payments

class LeaseContract(Contract):
    VEHICLE_MULTIPLIERS = {
        "Car": 1.2,
        "Motorcycle": 1,
        "Truck": 1.7
    } 
    def __init__(self, vehicle, customer, length_in_months):
        super().__init__(vehicle, customer)
        self.length_in_months = length_in_months
        
    def total_value(self):
      return (self.sale_price() + (self.VEHICLE_MULTIPLIERS[self.get_vehicle_type()] * self.sale_price() /self.length_in_months))* self.employee_discount
    
    def monthly_value(self):
      return self.total_value()/self.length_in_months