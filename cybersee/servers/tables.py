from table import Table
from table.columns import Column

from cybersee.servers.models import ServerLog


class ServerLogTable(Table):
    message = Column(field='message')
    recorded = Column(field='recorded')

    class Meta:
        model = ServerLog
