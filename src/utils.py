from datetime import datetime
import data.data as data
from data.constants import EXPIRATION


def remove_expired_surveys():
    utcnow = datetime.utcnow()
    surveys_to_remove = []
    for index, survey in data.surveys:
        if survey.get(EXPIRATION) < utcnow:
            surveys_to_remove.append(survey)
    data.surveys = [survey for survey in data.surveys if survey not in surveys_to_remove]


remove_expired_surveys()
