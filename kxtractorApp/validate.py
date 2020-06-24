
def validate_job_description(job_desc):
    resp = True
    if not(job_desc) or (len(job_desc) > 10000):
        resp = False
    return resp


def validate_num_words(words_count):
    resp = True
    if not words_count.isnumeric():
        resp = False
    elif not(1 <= int(words_count) <= 100):
        resp = False
    return resp
