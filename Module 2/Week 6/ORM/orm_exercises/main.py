from db import engine
from models import User, Address, Car 
from db import Base

def ensure_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    ensure_tables()
    print("✅ Tablas verificadas/creadas si faltaban.")
