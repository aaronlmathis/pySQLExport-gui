"""
================================================================================
   Project: pySQLExport-gui
   Description: A PyQt6 GUI application for managing and exporting SQL query results.
   Author: Aaron
   Email: aaron.mathis@gmail.com
   License: GNU General Public License v3.0 (GPL-3.0)
   License URL: https://www.gnu.org/licenses/gpl-3.0.en.html
================================================================================

   This file is part of pySQLExport-gui.

   pySQLExport-gui is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   pySQLExport-gui is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with pySQLExport-gui. If not, see <https://www.gnu.org/licenses/>.

================================================================================
"""

def get_database(db_type, host, user, pw, database, port):
    if db_type == 'MySQL':
        from pySQLExport_gui.database_mysql import MySQLDatabase
        return MySQLDatabase(host, user, pw, database, port)
    elif db_type == 'PostgreSQL':
        from pySQLExport_gui.database_pgsql import PgSQLDatabase
        return PgSQLDatabase(host, user, pw, database, port)
