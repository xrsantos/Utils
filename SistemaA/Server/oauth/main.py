import jwt

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from passlib.hash import bcrypt
from tortoise import fields 
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.models import Model 

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


JWT_SECRET = 'myjwtsecret'

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password_hash = fields.CharField(128)
    active = fields.BooleanField(default=True)

    def verify_password(self, password):
        return bcrypt.verify(password, self.password_hash)

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)
    if not user:
        return False 
    if not user.verify_password(password):
        return False
    return user 

@app.post('/token')
async def generate_token(form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        print ('form_data', form_data.username)  
        user = await authenticate_user(form_data.username, form_data.password)

        if not user:
            print ('Invalid username or password')
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT, 
                detail='Invalid username or password'
            )

        user_obj = await User_Pydantic.from_tortoise_orm(user)

        token = jwt.encode(user_obj.dict(), JWT_SECRET)

        return {'access_token' : token, 'token_type' : 'bearer'}
    except Exception as e:
        print ('Exception', e)
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT,
            detail=str(e)
        )

async def get_current_user(token: str = Depends(oauth2_scheme) ):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        user = await User.get(id=payload.get('id'))
    except:
        raise HTTPException(
            status_code=status.HTTP_204_NO_CONTENT, 
            detail='Invalid username or password'
        )

    return await User_Pydantic.from_tortoise_orm(user)


@app.post('/users', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):#, userAdm: User_Pydantic = Depends(get_current_user)):
    user_obj = User(username=user.username, password_hash=bcrypt.hash(user.password_hash))
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)

@app.get('/users/me', response_model=User_Pydantic)
async def get_user(user: User_Pydantic = Depends(get_current_user)):
    return user    

DATABASE_URL = "mysql://{}:{}@{}:{}/{}".format(
    "rick",
    "ri$enh@1979",
    "localhost",
     "3306",
    "dblogin"
)


#print( "Using pymysql:" )
#import pymysql
#myConnection = pymysql.connect( host="localhost" , user="rick", passwd="ri$enh@1979", db="dblogin" )
#doQuery( myConnection )
#myConnection.close()


register_tortoise(
    app, 
    db_url=DATABASE_URL,
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)