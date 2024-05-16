from sqlmodel import create_engine, SQLModel, Field

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)

def create_tables():
    """Create the tables registered with SQLModel.metadata (i.e classes with table=True).
    More info: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata
    """
    SQLModel.metadata.create_all(engine)