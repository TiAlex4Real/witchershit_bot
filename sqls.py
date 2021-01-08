import sqlite3
import codecs

witchershit_db = "witchershit.db"


def init_db():
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        f = codecs.open("initdb.sql", "r", "utf_8_sig")
        cursor.executescript(f.read())
        f.close()
        conn.commit()


witchershit_update_sql = "INSERT OR REPLACE INTO witchershit_log VALUES(?, CURRENT_TIMESTAMP);"
witchershit_check_sql = "SELECT 1 from witchershit_log where " \
                        "chat_id = ? and last_enc > datetime('now', '-1 day');"


def witchershit_update(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(witchershit_update_sql, [chat_id])
        conn.commit()


def witchershit_check(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(witchershit_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


status_update_sql = "INSERT INTO status_log VALUES(?, ?, CURRENT_TIMESTAMP)"
status_get_phrase_sql = "SELECT phrase_id, text FROM status_phrases " \
                        "WHERE phrase_id NOT IN (SELECT phrase_id FROM status_log" \
                        "                        WHERE chat_id = ? ORDER BY encounter LIMIT 5) " \
                        "ORDER BY RANDOM() LIMIT 1;"
status_check_sql = "SELECT 1 FROM status_log WHERE encounter > datetime('now', '-1 hour' ) AND chat_id = ?"


def status_get_phrase_update(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(status_get_phrase_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            cursor.execute(status_update_sql, [chat_id, res[0]])
            conn.commit()
            return res[1]
    return False


def status_check(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(status_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


nintendo_update_sql = "INSERT INTO nintendo_log VALUES(?, ?, CURRENT_TIMESTAMP)"
nintendo_get_phrase_sql = "SELECT phrase_id, text FROM nintendo_phrases " \
                        "WHERE phrase_id NOT IN (SELECT phrase_id FROM nintendo_log" \
                        "                        WHERE chat_id = ? ORDER BY encounter LIMIT 3) " \
                        "ORDER BY RANDOM() LIMIT 1;"
nintendo_check_sql = "SELECT 1 FROM nintendo_log WHERE encounter > datetime('now', '-3 day' ) AND chat_id = ?"


def nintendo_get_phrase_update(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(nintendo_get_phrase_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            cursor.execute(nintendo_update_sql, [chat_id, res[0]])
            conn.commit()
            return res[1]
    return False


def nintendo_check(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(nintendo_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False


beautiful_update_sql = "INSERT OR REPLACE INTO beautiful_log VALUES(?, CURRENT_TIMESTAMP);"
beautiful_check_sql = "SELECT 1 from beautiful_log WHERE " \
                     "chat_id = ? and last_enc > datetime('now', '-1 week');"


def beautiful_update(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(beautiful_update_sql, [chat_id])
        conn.commit()


def beautiful_check_on_delay(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(beautiful_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False

        
miss_me_update_sql = "INSERT OR REPLACE INTO miss_me_log VALUES(?, CURRENT_TIMESTAMP);"
miss_me_check_sql = "SELECT 1 from miss_me_log WHERE " \
                     "chat_id = ? and last_enc > datetime('now', '-1 month');"


def miss_me_update(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(miss_me_update_sql, [chat_id])
        conn.commit()


def miss_me_check(chat_id):
    conn = sqlite3.connect(witchershit_db)
    with conn:
        cursor = conn.cursor()
        cursor.execute(miss_me_check_sql, [chat_id])
        res = cursor.fetchone()
        if res:
            return True
        return False
        