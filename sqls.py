import sqlite3

witcher_db = "witchershit.db"

witchershit_update_sql = "INSERT OR REPLACE INTO witcher_log VALUES(?, CURRENT_TIMESTAMP);"
witchershit_check_sql = "SELECT 1 from witcher_log where " \
                        "chat_id = ? and last_enc > datetime('now', '-1 hour');"

alive_update_sql = "INSERT OR REPLACE INTO alive_log VALUES(?, CURRENT_TIMESTAMP, " \
                   "(COALESCE((select counter + 1 from alive_log where user_id = ? " \
                   "and last_enc > datetime('now', '-10 minute')), 1)));"
alive_check_overfill_sql = "SELECT 1 from alive_log where user_id = ? and counter > 2"
alive_check_pissed_off_sql = "SELECT 1 from alive_log where user_id = ? and counter > 3"
alive_check_hate_you_sql = "SELECT 1 from alive_log where user_id = ? and counter > 4"
alive_reset_sql = "UPDATE alive_log SET counter = 0 where user_id = ?;"

nintendo_update_sql = "INSERT OR REPLACE INTO nintendo_log VALUES(?, CURRENT_TIMESTAMP);"
nintendo_check_sql = "SELECT 1 from nintendo_log where " \
                     "chat_id = ? and last_enc > datetime('now', '-1 hour');"


def init_db(script_text):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.executescript(script_text)
        conn.commit()


def witchershit_update(chat_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(witchershit_update_sql, [chat_id])
        conn.commit()


def witchershit_check_on_delay(chat_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(witchershit_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


def alive_update(user_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(alive_update_sql, [user_id, user_id])
        conn.commit()


def alive_check_angry(user_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(alive_check_overfill_sql, [user_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


def alive_check_pissed_off(user_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(alive_check_pissed_off_sql, [user_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


def alive_check_hate_you(user_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(alive_check_hate_you_sql, [user_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


def alive_reset(user_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(alive_reset_sql, [user_id])
        conn.commit()


def nintendo_update(chat_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(nintendo_update_sql, [chat_id])
        conn.commit()


def nintendo_check_on_delay(chat_id):
    conn = sqlite3.connect(witcher_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(nintendo_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False
