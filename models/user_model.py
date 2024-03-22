# create python class that will be a SQL table; same as ddl.sql think: rules of the tables

from app import db

from werkzeug.security import generate_password_hash, check_password_hash # stores/hashes user pw but will never see raw pw

# follow UserSchema class or else there will be conflicts
class UserModel(db.Model): #sqlalchemy model class; note that sql swapcase 

    __tablename__ = 'users' # same name as UserModel

# create attribute for each schema item below
    
    id = db.Column(db.Integer, primary_key=True) #define what data type
    username = db.Column(db.String(50), nullable = False, unique = True) #string is varchar; setting constraints
    email = db.Column(db.String(50), nullable = False, unique = True)
    password_hash = db.Column(db.String, nullable = False) # we dont have access to the encryption key
    first_name = db.Column(db.String(75))
    last_name = db.Column(db.String(75))

# will also have methods (think: dml, commands)

    def save_user(self): 
        db.session.add(self)
        db.session.commit()

    def del_user(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self,user_dict):
        # loop through dict and set to the key
        for k, v in user_dict.items():
            if k != 'password':
            #setattr function sets key
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))