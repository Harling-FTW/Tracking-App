# Tracking-App
This is a tracking app system

## SERIALIZERS:
  UserSerializer: Fields = ["id","first_name", "last_name", "username", "is_staff"]
  OrderSerializer: Fields = ['order_id', 'username', 'description', 'weight', 'order_date', 'dispatch_date', 'latest_location']
  
## API_URLS:
  ###Order list: r/api/Orders/
        Get Order: r/api/Orders/<pk:order_id>/get_order/
        Get User Order History: Get Order: r/api/Orders/<pk:user_id>/get_userhist/
  ###User list: r/api/Users/
        Get User: r/api/User/<pk:user_id>/get_user/
