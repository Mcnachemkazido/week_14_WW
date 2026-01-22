import uvicorn
from fastapi import FastAPI ,HTTPException , File, UploadFile
import pandas as pd
from models import add_an_analysis_column ,replacing_missing_values
import db

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File()):
    try:
        df = pd.read_csv(file.file)
        big_df = add_an_analysis_column(df)
        clean_df = replacing_missing_values(big_df)
        dict_data = clean_df.to_dict('records')
        conn = db.get_connect()
        db.create_db(conn)
        db.create_tabel(conn)
        db.insert_into_db(conn,dict_data)
        return {"status": "success","inserted_records": len(dict_data)}
    except Exception as e:
        print(e)
        raise HTTPException(detail=e,status_code=400)








if __name__ ==  "__main__":
    uvicorn.run(app,host="localhost",port=8000)