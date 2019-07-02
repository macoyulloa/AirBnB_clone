#!/usr/bin/python3
from models.base_model import BaseModel
"""
definition of the review
"""


class Review(BaseModel):
    'the review'
    place_id = ""
    user_id = ""
    text = ""
