import config
db = config.db

def load_judgement_by_votation(votation_id):
    """Returns an array"""
    ar = db.session.query(Judgement).filter(Judgement.votation_id == votation_id).order_by(Judgement.jud_value).all()
    return ar

ar = []
jud_array = load_judgement_by_votation(votation_id)
for j in range(len(jud_array)):
    n = db.session.query(Vote).filter(Vote.votation_id == votation_id, Vote.option_id == option_id, Vote.jud_value == j).count()
    ar.append( n )
print(ar)