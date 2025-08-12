from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str
    email: str
    
# prints output with "id"
#user_data = {"id": 11, "name": "John Doe", "email": "john.doe@example.com"}

# prints output with single quotes for id
#user_data = {'id': 11, "name": "John Doe", "email": "john.doe@example.com"}

# prints output with string id as pydentic will try to convert to int
user_data = {'id': "11", "name": "John Doe", "email": "john.doe@example.com"}

print(User(**user_data))


class Cart(BaseModel):
    id: int
    user_id: int
    items: list[str] = Field(description="List of item names in the cart",)
    
    
cartItems1 = {"ABCD", "PQRS", "XYZ"}
cartItems2 = {}

cart = Cart(id=1, user_id=1, items=list(cartItems2))
print("printing cart items: " + str(cart))

print("printing JSON representation of cart: " + str(cart.model_dump()))