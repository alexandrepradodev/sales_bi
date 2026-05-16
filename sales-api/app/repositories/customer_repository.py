from datetime import datetime

def get_customers_data():
    return [

        {

            "customer_id": 1,

            "first_name": "Zeca",

            "last_name": "Silva",

            "email": "zeca@email.com",

            "created_at": datetime.now()

        },

        {

            "customer_id": 2,

            "first_name": "Ana",

            "last_name": "Souza",

            "email": "ana@email.com",

            "created_at": datetime.now()

        },

        {

            "customer_id": 3,

            "first_name": "Pedro",

            "last_name": "Costa",

            "email": "pedro@email.com",

            "created_at": datetime.now()

        }

    ]