import uvicorn
from fastapi import FastAPI ,HTTPException , File, UploadFile
import pandas as pd
from models import add_an_analysis_column ,replacing_missing_values

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File()):
    df = pd.read_csv(file.file)
    big_df = add_an_analysis_column(df)
    clean_df = replacing_missing_values(big_df)
    print(clean_df.info())
    print(clean_df.to_string())




if __name__ ==  "__main__":
    uvicorn.run(app,host="localhost",port=8000)