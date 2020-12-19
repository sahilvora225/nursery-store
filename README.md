# Online Nursery Store

This simple Django project helps us to establish an online nursery store's backend with a bunch of APIs. Following is the list of APIs along with their purpose.

- Signup (user and nursery)

    > 127.0.0.1:8000/user/signup/
    >
    > POST
    >
    > Parameters - email, password, name, user_type
    >
    > user_type - Seller = 'S', Buyer = 'B'

- Login (user and nursery)
  
    > 127.0.0.1:8000/user/login/
    >
    > POST
    >
    > Parameters - email, password

- Add a plant (nursery) (with image, price, name)

    > 127.0.0.1:8000/plant/
    >
    > POST
    >
    > Parameters - image, price, name

- List all plants (user)

    > 127.0.0.1:8000/plant/
    >
    > GET
    >
    > Parameters - NA

- View a plant (user)

    > 127.0.0.1:8000/plant/__id__/
    >
    > GET
    >
    > Parameters - NA

- Place order (user)
  
    > 127.0.0.1:8000/order/
    >
    > POST
    >
    > Parameters - quantity, price_each, plant
    >
    > For plant parameter we need to pass id

- View orders (nursery)

    > 127.0.0.1:8000/order/
    >
    > GET
    >
    > Parameters - NA