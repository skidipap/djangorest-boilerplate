# Django Boilerplate 

Minimal Django Boilerplate for Ready To Use

## Package Uses 

1. Django 4.0 
2. Django AllAuth
3. 

## Some COnfiguration 

1. Custom User With AbstractUser 
2. Social Account Adapter For Connecting Existing User and Social Account Email
3. Social Account Provider With Google

```python
# settings.py

# Django Allauth Social Account
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
```


4. Django All Auth with Some Configuration 

```python
# settings.py

LOGIN_REDIRECT_URL = ''
LOGOUT_REDIRECT_URL = ''

# Django All Auth Logout Without Render Template
ACCOUNT_LOGOUT_ON_GET = True 

# Django All Auth Email Login
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
```

## How to Use This Boilerplate

1. Make sure u Clone this repo
2. At first migrations make sures you included CustomUser
3. Done 
