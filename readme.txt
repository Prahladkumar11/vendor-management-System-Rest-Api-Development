step1:- pip install requirements.txt
Step2:-python manage.py runserver




Api detail :::----

api/vendors -- GET -- Retrieve all vendors

api/vendors/{vendor_id} -- GET -- Retrieve a specific vendor

api/vendors/{vendor_id} -- PUT -- Update a specific vendor

api/vendors/{vendor_id} -- DELETE -- Delete a specific vendor

api/vendors/{vendor_id}/purchaseOrders -- GET -- Retrieve all purchase orders for a specific vendor

api/purchaseOrders -- GET -- Retrieve all purchase orders

api/purchaseOrders/{purchaseOrder_id} -- GET -- Retrieve a specific purchase order

api/purchaseOrders/{purchaseOrder_id} -- PUT -- Update a specific purchase order

api/purchaseOrders/{purchaseOrder_id} -- DELETE -- Delete a specific purchase order

api/performances -- GET -- Retrieve all historical performances

api/performances/{performance_id} -- GET -- Retrieve a specific historical performance

api/performances/{performance_id} -- PUT -- Update a specific historical performance

api/performances/{performance_id} -- DELETE -- Delete a specific historical performance

api/vendors/{vendor_id}/performance -- GET -- Retrieve historical performance data for a specific vendor