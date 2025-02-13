from fastapi import APIRouter
from app.ucase import BearerAuthentication
from app import logger
from app.repositories import prompt

auth = BearerAuthentication()
router = APIRouter()
repoPrompt = prompt.PromptRepositories()