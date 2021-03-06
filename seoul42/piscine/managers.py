from django.db import models


class PiscineFtUserManager(models.Manager):
	def create(
			self,
			id: int = None,
			login: str = None,
			pool_year=None,
			pool_month=None,
			is_public=None,
			is_pass=None,
			piscine_level=None,
			peer_count=None,
	):
		piscine_ft_user = self.model(
			id=id,
			login=login,
			pool_year=pool_year,
			pool_month=pool_month,
			is_public=is_public,
			is_pass=is_pass,
			piscine_level=piscine_level,
			peer_count=peer_count,
		)
		piscine_ft_user.save(using=self._db)
		return piscine_ft_user