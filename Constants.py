from enum import Enum


class QueryType(Enum):
    GREETING = "Greeting"
    GENERAL_FAQ = "General FAQ"
    GENERAL_DATABASE = "General Database"
    SPECIFIC_DATABASE = "Specific Database"

class ResponseType(Enum):
    DEFAULT = "Please Provide a right Query"
    INTRO = "Hello! My name is Roboto. How can I help you ?"
    ASKID = "Please enter your Patient ID , After the symbol # </br>Ex: #9 <br> If you are not registered with TYPE #999"
    NOPATIENT = "Patient Not Found, Please Register yourself. Provide Name and Phone Number After $ in comma separated format<br>EX: $ABC,2345234545 <br>Make sure phone no. is [10-digit]"
    PATIENTFOUND = "Patient Id is registered with us.<br> Please Re Ask your query"
    WRONGINFO = "Wrong Data , Try Again later. Thanks !!"
