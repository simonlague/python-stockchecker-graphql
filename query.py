import requests

query = """
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

variables = """
{
    "ids": [
        "12f6ef8d-1787-4dd6-bd95-6f113965bda0"
    ],
    "storeId": "ca",
    "language": "en",
    "displayCurrency": "CAD"
}
"""

def run_query():
    request = requests.post('https://ecomm.svc.ui.com/graphql', json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
