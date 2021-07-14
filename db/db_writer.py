import psycopg2

from utilities import read_value_from_config


def write_data(url, response_time, status_code, regexp):
    """
    :param url: URL of checked web-site
    :param response_time: response time taken for get request
    :param status_code: status code of response
    :param regexp: is regexp pattern present on the page
    """
    db = read_value_from_config('db_connection')
    conn = psycopg2.connect(db)
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO results (url, response_time, status_code, regexp) VALUES ('%s', %.5f, %d, %r);" % (
            url, response_time, status_code, regexp))
        conn.commit()
    conn.close()
