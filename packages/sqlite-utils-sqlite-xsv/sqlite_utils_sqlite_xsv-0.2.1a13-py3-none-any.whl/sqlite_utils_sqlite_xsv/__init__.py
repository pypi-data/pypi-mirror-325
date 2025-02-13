
from sqlite_utils import hookimpl
import sqlite_xsv

__version__ = "0.2.1a13"
__version_info__ = tuple(__version__.split("."))

@hookimpl
def prepare_connection(conn):
  conn.enable_load_extension(True)
  sqlite_xsv.load(conn)
  conn.enable_load_extension(False)
