import sqlalchemy
from sqlalchemy.orm import sessionmaker
from bd_tables import create_tables, BotUser, Candidate, Variants

query_info = [{'name': 'Александр', 'age_on': '30', 'age_to': '35', 'sex': 'female', 'city': 'SPb'}]
user_name = 55666889
candidates = [{'first_name':'Vfhbyf','last_name':'adfadsfa','vk_id':'3218534354','bdate':'311587','attach':['adfafadfasf','afdafadfa','adfadfadfasdfa'],'viewed':'False'}]



DSN = 'postgresql://postgres:310884@localhost:5432/vk_tinder_db'  # пароль нужен
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_botuser(query_info, user_name):
    for el in query_info:
        botuser = BotUser(user_vk_id=user_name,
                          name=el['name'],
                          age_on=el['age_on'],
                          age_to=el['age_to'],
                          pol=el['sex'],
                          city=el['city']
                          )
        session.add(botuser)
        session.commit()


def add_candidates(candidates, user_name):
    for el in candidates:
        candidate = Candidate(vk_id=el['vk_id'],
                              candidate_firstname=el['first_name'],
                              candidate_lastname=el['last_name'],
                              candidate_bdate=el['bdate'],
                              candidate_fots=el['attach'],
                              viewed='False'
                              )
        session.add(candidate)
        session.commit()

        bu = session.query(BotUser.id).filter(BotUser.user_vk_id == user_name).scalar()
        can = session.query(Candidate.id).filter(Candidate.vk_id ==el['vk_id']).scalar()

        variants = Variants(id_botuser=bu,
                            id_candidate= can,
                            loved='True'
                            )
        session.add(variants)
        session.commit()


add_botuser(query_info,user_name)
add_candidates(candidates,user_name)


session.close()
