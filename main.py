from fastapi import FastAPI
from routes import users,products,product_types,orders,incomes,expenses,customers,backet,login
app = FastAPI()

@app.get('/')
def home():
    return {"date":"Salom hammaga"}


app.include_router(
    router=login.login_router,
    tags=["Login bo'limi"],
    prefix='/login'
)
app.include_router(
    router=users.user_router,
    tags=["Users bo'limi"],
    prefix='/users'
)


app.include_router(
    router=products.user_router,
    tags=["Products bo'limi"],
    prefix='/products'
)


app.include_router(
    router=product_types.user_router,
    tags=["Types bo'limi"],
    prefix='/types'
)


app.include_router(
    router=orders.user_router,
    tags=["Orders bo'limi"],
    prefix='/orders'
)


app.include_router(
    router=incomes.user_router,
    tags=["Incomes bo'limi"],
    prefix='/incomes'
)


app.include_router(
    router=expenses.user_router,
    tags=["Expenses bo'limi"],
    prefix='/expenses'
)


app.include_router(
    router=customers.user_router,
    tags=["Customers bo'limi"],
    prefix='/customers'
)


app.include_router(
    router=backet.user_router,
    tags=["Backet bo'limi"],
    prefix='/backet'
)

