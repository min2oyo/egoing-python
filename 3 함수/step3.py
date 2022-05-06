def get_vat(price, vat_rate=0.1):
    return price * vat_rate


print(get_vat(10000))
get_vat(10000, 0.2)

# email.send("ria@gmail.com", get_vat(10000, 0.3))
