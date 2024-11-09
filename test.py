# import os

# # API keys (use your actual API keys)
# groq_api_key = os.environ.get("GROQ_API_KEY")
# google_api_key = os.environ.get("GOOGLE_API_KEY")

# if groq_api_key:
#     print(f"The value of MY_ENV_VAR is: {groq_api_key}")
# else:
#     print("MY_ENV_VAR is not set")

from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Access the environment variables
my_var = os.getenv("GROQ_API_KEY")
print(f"The value of MY_ENV_VAR is: {my_var}")

    