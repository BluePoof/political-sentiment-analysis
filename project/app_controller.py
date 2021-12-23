"""Controller module"""
from project.schemas.post_schema import PostSchema
from project.schemas.page_schema import PageSchema
from project.schemas.comment_schema import CommentSchema

class AppController():
    """Basic controller for backend app"""
    def __init__(self):
        self.__post_schema = PostSchema()
        self.__page_schema = PageSchema()
        self.__comment_schema = CommentSchema()

    def get_pages(self):
        """Returns all resources in page table"""
        return self.__page_schema.get_all()

    def get_filters_fields(self):
        """Returns filter fields for data

        Returns:
            dict: Contains the name of filter as key, and filter data as a list
                Example:
                {
                    "page_name": [
                        "Irene Herrera",
                        "Virgilio Mendoza"
                    ],
                    "political_party": [
                        "Partido Revolucionario Institucional",
                        "Partido Verde Ecologista de México"
                    ],
                    "kind": [
                        "Presidencia Municipal",
                        "Gubernatura"
                    ],
                    "region": [
                        "Colima",
                        "Manzanillo"
                    ]
                }
        """

        filters = {
            "page_name": [],
            "political_party": [],
            "kind": [],
            "region": []
        }
        for field in filters:
            result = self.__page_schema.get_distinct(field)
            for data in result:
                filters[field].append(data[field])
        return filters
