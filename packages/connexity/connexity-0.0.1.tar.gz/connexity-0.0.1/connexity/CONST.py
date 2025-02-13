import os

from dotenv import load_dotenv

load_dotenv()

CONNEXITY_URL = os.environ.get('CONNEXITY_URL', default="https://connexity-gateway-owzhcfagkq-uc.a.run.app/process/sdk")
