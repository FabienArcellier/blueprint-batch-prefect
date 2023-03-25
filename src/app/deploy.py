"""
configure the flows to deploy from this module.
"""
import time

from app import main
from app.core import deploy

deploy_book = deploy.create_deploy_book()
deploy.register(deploy_book, main.my_favorite_function, interval=60)
deploy.register(deploy_book, main.my_favorite_function_2, cron="*/3 * * * *")

if __name__ == "__main__":
    time.sleep(5)
    """
    Inject a specific PREFECT_API_URL variable of the endpoint the deploy script will use.
    """
    deploy.deploy(deploy_book)
