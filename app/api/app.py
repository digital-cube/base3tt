import base


@base.route(PREFIX='/api/app', URI="/about")
class AboutAppHandler(base.Base):

    @base.api()
    async def get(self):
        print(1)

        import a_models as models

        d2 = models.App(test='TEST2')
        await d2.save()

        return {'service': 'app', 'id2': d2.id}
