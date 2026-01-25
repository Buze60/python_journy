class UserSession:
    def __init__(self,user_id,auth_token):
        self.user_id = user_id
        self.auth_token = auth_token
        self.temp_counter = 0
        
session = UserSession(101,'abc123token')

attributes_to_clean = ['auth_token','temp_counter']

# loop through the list of the attributes to be cleaned
for attr in attributes_to_clean:
    if hasattr(session,attr):
        delattr(session,attr)
        print(f'Removed attribute: {attr}')


print('\n Final attributes remaining: ')

for attr in dir(session):
    if not attr.startswith('__') and not callable(getattr(session,attr)):
        print(f'{attr} : {getattr(session,attr)}')
        