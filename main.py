import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from bd_tables import create_tables, BotUser, Candidate, Variants

DSN = 'postgresql://postgres:310884@localhost:5432/vk_tinder_db'  # пароль нужен
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_botuser(query_info, user_name):
    for el in query_info:
        botuser = BotUser(user_id = user_name,
                              name = el['name'],
                              age_on = el['age_on'],
                              age_to = el['age_to'],
                              pol = el['sex'],
                              city = el['city']
                              )
        session.add(botuser)
        session.commit()




def add_candidates(candidates):
    for el in candidates:
        candidate = Candidate(vk_id = el['vk_id'],
                              candidate_firstname = el['first_name'],
                              candidate_lastname = el['last_name'],
                              candidate_bdate = el['bdate'],
                              id_botuser = el['id_botuser'],
                              candidate_fots = el['attach'],
                              viewed = 'False'
                              )
        session.add(candidate)
        session.commit()







session.close()
