import requests
from config import Config

class Query:

    __query = """
    query GetRecentProducts($ids: [UUID!]!, $storeId: StoreId!, $language: LowercaseTrimmedString!, $displayCurrency: Currency!) {
                storefrontProductsById(
                ids: $ids
                storeId: $storeId
                language: $language
                displayCurrency: $displayCurrency
                ) {
                ...ProductCardFragment
                __typename
                }
            }

            fragment ProductCardFragment on StorefrontProduct {
                id
                title
                shortDescription
                slug
                tags {
                id
                name
                __typename
                }
                thumbnail {
                ...ThumbnailAssetFragment
                __typename
                }
                variants {
                id
                isEarlyAccess
                isVisibleInStore
                sku
                status
                displayPrice {
                    amount
                    currency
                    __typename
                }
                __typename
                }
                __typename
            }

            fragment ThumbnailAssetFragment on Asset {
                id
                url
                height
                width
                mimeType
                filename
                __typename
            }
    """

    __variables = """
    {
        "ids": [
            "12f6ef8d-1787-4dd6-bd95-6f113965bda0"
        ],
        "storeId": "ca",
        "language": "en",
        "displayCurrency": "CAD"
    }
    """

    def __init__(self):
        self.__url = Config.get_instance().get_request_url()

    def run_query(self):
        request = requests.post(self.__url, json={'query': self.__query, 'variables': self.__variables})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, self.__query))
