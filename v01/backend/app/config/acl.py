

accesses = {
    # key structure:  <url_endpoint>|<method>: ['role1', 'role2']
    # client area
    'auth|post': ['customer', ],  # 'user' role is not used in db, fake this role with `customer` value
    'auth.forgot|post': ['customer', ],
    'auth.forgot.confirm|post': ['customer', ],
    'auth.reg.confirm|post': ['customer', ],
    'user|get': ['customer', ],
    'user|post': ['customer', ],
    'user.password|patch': ['customer', ],
    'user.forgottenpassword|post': ['customer'],

    # admin area
    'admin.auth|post': ['technical', 'exec', 'admin'],
    'admin.system.errors|get': ['technical', 'exec', 'admin'],
    'admin.system.errors.item|patch': ['technical', 'exec', 'admin'],
    'admin.transactions|get': ['technical', 'exec', 'admin'],
    'admin.users|get': ['technical', 'exec', 'admin'],
}