# tutorial/tables.py
import django_tables2 as tables
from api.models import Donor

class DonorTable(tables.Table):
    class Meta:
        model = Donor
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}