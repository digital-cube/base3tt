import base


@base.route(PREFIX='/api/users', URI="/about")
class AboutUsersHandler(base.Base):

    @base.api()
    async def get(self):
        import models.users

        u = models.users.User(test='TEST2')
        await u.save()

        return {'service': 'users', 'id2': u.id}
