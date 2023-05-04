import datetime
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice

customer_Name = input('Enter Customer\'s Name : ')

doc = SimpleInvoice('invoice.pdf')

now = datetime.datetime.now()

doc.invoice_info = InvoiceInfo(1023, now, datetime.timedelta(days=3))
doc.service_provider_info = ServiceProviderInfo(
   name='Ousu\'s Hub',
    street='Anonymous lane, 680014.',
    city='Thrissur'
)

doc.client_info = ClientInfo(name = customer_Name)

while(True):
    item = input('Enter the name of the item : ')
    item_desc = input('Enter the description of item: ')
    price = int(input('Enter price of the item : '))
    unit = int(input('Number of units sold : '))
    doc.add_item(Item(item, item_desc, unit, price))
    r = input("Is there any more items? (y/n)")
    if r=="n":
        break

message = 'Thanks for shopping with us today!'

doc.set_item_tax_rate(6)
doc.set_bottom_tip("Thanks for shopping with us today!")
doc.finish()

print("pdf saved as invoice.pdf")
