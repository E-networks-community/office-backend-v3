from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, select
from database.schemas.schemas import AccountCreate
from database.config.config import engine, Staff
from uploads.cloudinary import upload_image_to_cloudinary
from pydantic import EmailStr, AnyUrl, constr

app = FastAPI()

# Define the origins that are allowed to access your API
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://enetworksjobs.com.ng"  # Assuming your frontend is running on this port
    # Add more origins as needed
]

# Add CORS middleware to your FastAPI app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Add methods that you want to allow
    allow_headers=["*"],  # Add headers that you want to allow
)

def get_session():
    with Session(engine) as session:
        yield session

@app.post("/create_account/")
async def create_account(
    full_name: str = Form(...),
    phone_number: str = Form(...),
    agent_email: str = Form(...),
    agent_card_number: str = Form(...),
    active_contact_address: str = Form(...),
    state_of_origin: str = Form(...),
    lga: str = Form(...),
    ward: str = Form(...),
    gender: str = Form(...),
    next_of_kin_name: str = Form(...),
    next_of_kin_phone_number: str = Form(...),
    next_of_kin_relationship: str = Form(...),
    next_of_kin_email_address: str = Form(...),
    guarantor_name: str = Form(...),
    guarantor_phone_number: str = Form(...),
    languages: str = Form(...),
    preferred_position: str = Form(...),
    preferred_location: str = Form(...),
    image: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    # Upload image to Cloudinary
    try:
        image_url = upload_image_to_cloudinary(image.file)

        staff = Staff(
            full_name=full_name,
            phone_number=phone_number,
            agent_email=agent_email,
            agent_card_number=agent_card_number,
            active_contact_address=active_contact_address,
            state_of_origin=state_of_origin,
            lga=lga,
            ward=ward,
            gender=gender,
            next_of_kin_name=next_of_kin_name,
            next_of_kin_phone_number=next_of_kin_phone_number,
            next_of_kin_relationship=next_of_kin_relationship,
            next_of_kin_email_address=next_of_kin_email_address,
            guarantor_name=guarantor_name,
            guarantor_phone_number=guarantor_phone_number,
            passport_photo=image_url,
            languages=languages,
            preferred_position=preferred_position,
            preferred_location=preferred_location
        )
        session.add(staff)
        session.commit()
        session.refresh(staff)
        return staff
    except Exception as e:
        print(f"An error occurred during account creation: {e}")  # Print the error to the terminal
        raise HTTPException(status_code=400, detail=str(e))  # Raise HTTPException with the error detail

@app.get("/accounts/")
async def read_accounts(session: Session = Depends(get_session)):
    accounts = session.exec(select(Staff)).all()
    return accounts
