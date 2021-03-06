# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Upgrades MySQL database to InnoDB."""

from invenio.legacy.dbquery import run_sql


depends_on = [
    'collections_2015_07_14_innodb',
    'knowledge_2015_07_14_innodb',
    'oaiharvester_2015_07_14_innodb',
    'oauth2server_2015_07_14_innodb'
]


def info():
    """Return upgrade recipe information."""
    return "Upgrades MySQL database to InnoDB."


def do_upgrade():
    """Carry out the upgrade."""
    from flask import current_app
    if current_app.config.get('CFG_DATABASE_TYPE') == 'mysql':
        table_names = run_sql(
            "SELECT TABLE_NAME"
            " FROM INFORMATION_SCHEMA.TABLES"
            " WHERE ENGINE='MyISAM'"
            " AND table_schema=%s",
            (current_app.config.get('CFG_DATABASE_NAME'),)
        )
        for table_name in table_names:
            run_sql("ALTER TABLE `%s` ENGINE=InnoDB" % (table_name[0],))


def estimate():
    """Estimate running time of upgrade in seconds (optional)."""
    return 1


def pre_upgrade():
    """Pre-upgrade checks."""
    pass


def post_upgrade():
    """Post-upgrade checks."""
    pass
