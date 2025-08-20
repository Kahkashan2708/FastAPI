from fastapi import FastAPI
from enum import Enum

app = FastAPI(title="Food & Coupons API", version="1.0.0")


# Cuisine Enum 
class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"
    chinese = "chinese"
    mexican = "mexican"
    japanese = "japanese"


# Food Items 
food_items = {
    "indian": ["Samosa", "Dosa", "Biryani", "Paneer Tikka"],
    "american": ["Hot Dog", "Apple Pie", "Burger", "Fried Chicken"],
    "italian": ["Ravioli", "Pizza", "Pasta", "Lasagna"],
    "chinese": ["Spring Roll", "Kung Pao Chicken", "Fried Rice", "Dumplings"],
    "mexican": ["Tacos", "Burrito", "Quesadilla", "Nachos"],
    "japanese": ["Sushi", "Ramen", "Tempura", "Miso Soup"]
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    return {
        "cuisine": cuisine,
        "items": food_items[cuisine]
    }


# Coupon Codes 
coupon_code = {
    1: "10%",
    2: "20%",
    3: "30%",
    4: "40%",
    5: "50%"
}


@app.get("/get_coupon/{code}")
async def get_coupon(code: int):
    discount = coupon_code.get(code)
    if discount:
        return {"coupon_code": code, "discount_amount": discount}
    return {"error": "Invalid coupon code"}


