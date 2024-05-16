from sqlmodel import create_engine, SQLModel, Field
from pydantic import field_validator
from typing import ClassVar, List

#################
#################
#################
#################

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)

#################
#################
#################
#################

def create_tables():
    """Create the tables registered with SQLModel.metadata (i.e classes with table=True).
    More info: https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/#sqlmodel-metadata
    """
    SQLModel.metadata.create_all(engine)

#################
#################
#################
#################

class Staff(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    full_name: str
    phone_number: str
    agent_email: str
    agent_card_number: str
    active_contact_address: str
    passport_photo: str
    state_of_origin: str
    lga: str
    ward: str
    gender:str
    next_of_kin_name: str
    next_of_kin_phone_number: str
    next_of_kin_relationship: str
    next_of_kin_email_address: str
    guarantor_name: str
    guarantor_phone_number: str
    languages: str
    preferred_position: str
    preferred_location: str

    valid_genders: ClassVar[List[str]] = ["male", "female"]
    valid_positions: ClassVar[List[str]] = [
        'state managers',
        'state asst manager',
        'state admin sec',
        'state operations manager',
        'state media and public relations officer',
        'state legal asst',
        'state finance officer',
        'state tech officer',
        'state community relations officer',
        'state product dev officer',
        'state business development officer',
        'state personnel manager',
        'state desk officer( ngo desk office)',
        'dep desk officer',
        'gen secretary',
        'asst gen secretary',
        'financial secretary',
        'treasurer',
        'information officer ( public and traditional)',
        'asst information officer( social media)',
        'legal adviser',
        'women affairs officer',
        'youth affairs officer',
        'organising officer',
        'lg desk officer',
        'dep lg desk officer',
        'lg gen secretary',
        'lg asst gen secretary',
        'lg financial secretary',
        'lg treasurer',
        'lg information officer ( public and traditional)',
        'lg asst information officer( social media)',
        'lg legal adviser',
        'lg women affairs officer',
        'lg youth affairs officer',
        'lg organising officer',
        'lg business manager/coordinator',
        'lg asst business manager/coordinator ',
        'lg admin sec',
        'lg operations manager',
        'lg media and public relations officer',
        'lg legal asst',
        'lg finance officer',
        'lg tech officer',
        'lg community relations officer',
        'lg product dev officer',
        'lg business development officer',
        'lg personnel manager'
    ]
    valid_locations: ClassVar[List[str]] = [
        'abia', 'adamawa', 'akwa ibom', 'anambra', 'bauchi', 'bayelsa', 'benue', 'borno', 'cross river', 'delta', 'ebonyi', 'edo', 'ekiti', 'enugu', 'fct', 'gombe', 'imo', 'jigawa', 'kaduna', 'kano', 'katsina', 'kebbi', 'kogi', 'kwara', 'lagos', 'nasarawa', 'niger', 'ogun', 'ondo', 'osun', 'oyo', 'plateau', 'rivers', 'sokoto', 'taraba', 'yobe', 'zamfara'
    ]

    @field_validator('gender')
    def validate_gender(cls, value):
        if value.lower() not in cls.valid_genders:
            raise ValueError('Invalid gender')
        return value

    @field_validator('preferred_position')
    def validate_preferred_position(cls, value):
        if value.lower() not in cls.valid_positions:
            raise ValueError('Invalid preferred position')
        return value

    @field_validator('preferred_location')
    def validate_preferred_location(cls, value):
        if value.lower() not in cls.valid_locations:
            raise ValueError('Invalid preferred location')
        return value

if __name__ == '__main__':
    # creates the table if this file is run independently, as a script
    create_tables()
