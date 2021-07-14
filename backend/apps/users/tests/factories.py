import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = 'user'
    email = 'eozz21@gmail.com'
    full_name = 'aiegoo'
