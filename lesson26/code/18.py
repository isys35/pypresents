class HomeWork(models.Model):
		...

    def get_absolute_url(self):
        return "/homework/%s/" % self.pk