import django.db.models as models
import lamindb.base.fields as fields
from lamindb.models import CASCADE, Space

# assumption is that the Space table is synced to the hub and shares the integer primary key with the corresponding
# table in the hub
# examples for syncing from within lamindb-setup: https://github.com/laminlabs/lamindb-setup/blob/9518bbd390f4f156fb3b8ec06c6518a2f8f8c0c0/lamindb_setup/_setup_user.py#L124C9-L124C37
# we need to the population of instance tables and central tables through the REST tables


class Account(models.Model):
    id = models.UUIDField(
        primary_key=True
    )  # this would be 1:1 matching the primary key on the hub
    lnid = fields.CharField(
        max_length=8
    )  # can be used to join on the lamindb.models.User table via lamindb.models.User.uid


class Team(models.Model):
    id = models.UUIDField(primary_key=True)
    name = fields.CharField(max_length=255)
    members = models.ManyToManyField(Account, related_name="teams")


class TeamUser(models.Model):
    team = fields.ForeignKey(Team, CASCADE, related_name="links_teamuser")
    user = fields.ForeignKey(Account, CASCADE, related_name="links_teamuser")


class SpaceTeam(models.Model):
    space = fields.ForeignKey(Space, CASCADE, related_name="links_teamuser")
    account = fields.ForeignKey(Account, CASCADE, related_name="links_teamuser")


class SpaceUser(models.Model):
    space = fields.ForeignKey(Space, CASCADE, related_name="links_teamuser")
    account = fields.ForeignKey(Account, CASCADE, related_name="links_teamuser")
