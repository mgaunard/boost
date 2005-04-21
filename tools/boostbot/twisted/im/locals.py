# Twisted, the Framework of Your Internet
# Copyright (C) 2002-2003 Matthew W. Lefkowitz
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of version 2.1 of the GNU Lesser General Public
# License as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

class Enum:
    group = None

    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return '<%s: %s>' % (self.group, self.label)

    def __str__(self):
        return self.label


class StatusEnum(Enum):
    group = 'Status'

OFFLINE = Enum('Offline')
ONLINE = Enum('Online')
AWAY = Enum('Away')

class OfflineError(Exception):
    """The requested action can't happen while offline."""
