from lib import db


# spel beginnen in de databank
def DB_InsertGameinDB(antwoord):
    antwoord_string = ''.join(antwoord)
    sql = f"INSERT INTO mm SET mm_datumtijd=NOW(), mm_antwoord='{antwoord_string}'"
    gameid = db.DBInsert(sql)
    return gameid


# spel afbreken in de databank
def DB_CancelGameInDB(gameid, userinput):
    sql = f"UPDATE mm SET mm_afgebroken=NOW(), mm_input='{userinput}' where mm_id={gameid}"
    if db.DBUpdate(sql):
        pass
    else:
        print("Er liep iets fout bij het updaten van de database")


# spel voltooien in de databank
def DB_FinishGameInDB(gameid, userinput):
    sql = f"UPDATE mm SET mm_opgelost=NOW(), mm_input='{userinput}' where mm_id={gameid}"
    if db.DBUpdate(sql):
        pass
    else:
        print("Er liep iets fout bij het updaten van de database")
