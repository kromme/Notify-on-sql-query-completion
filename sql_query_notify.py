# -*- coding: cp1252 -*-
__author__ = "j.kromme"

import ctypes
import sys
import time
import winsound

from sqlalchemy import create_engine

# define query
QUERY = """
        SELECT
            A.SESSION_ID,
            A.START_TIME,
            A.COMMAND,
            B.TEXT
        FROM            SYS.DM_EXEC_REQUESTS A
        CROSS APPLY     SYS.DM_EXEC_SQL_TEXT(A.SQL_HANDLE) AS B
        WHERE           b.text not like \'%A.SESSION_ID%\'
    """


def get_sql_queries(connection_string: str):
    """Query the SQL database and get running queries.
    """
    # tables in database
    conn = create_engine(connection_string)
    session = conn.execute(QUERY)
    results = session.fetchall()
    return [t[0] for t in results]


def track(connection_string: str):
    """Start Tracking
    """

    print("Start tracking..")
    # get runnning queries
    sessions = get_sql_queries(connection_string)

    # loop until all queries are done
    while len(sessions) > 0:

        # get new sessions
        newSessions = [t[0] for t in get_sql_queries(connection_string)]

        # loop though the sessions
        for sessionId in sessions:

            # check whether the sessions is still running
            if sessionId not in newSessions:

                # if it's done pop up
                winsound.PlaySound("*", winsound.SND_ALIAS)
                ctypes.windll.user32.MessageBoxA(
                    0,
                    "A query is done. \n"
                    + str(len(newSessions))
                    + " are still running",
                    "Query done",
                    "MB_TOPMOST",
                )
                sessions.remove(sessionId)

        # rest for 10 seconds
        time.sleep(10)


if __name__ == "__main__":
    # get connection string from arguments
    connection_string = sys.argv[1]

    # track
    track(connection_string=connection_string)

