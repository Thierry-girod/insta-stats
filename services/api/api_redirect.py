from flask import Blueprint, request
from module.configuration import get_config
import requests

api_redirect_service = Blueprint('api_redirect', __name__)
conf = get_config()

@api_redirect_service.route('/api/retention-panel/', methods=['GET'])
def retention_panel(api_key):
    # Retrieve parameters
    quantity = request.get('qty')
    service_id = request.get('service_id')
    link = request.get('link')

    # Call API
    url = "{scheme}://{host}/{path}".format(
        scheme=conf['RETENTION_API']['SCHEME'],
        host=conf['RETENTION_API']['HOST'],
        path=conf['RETENTION_API']['PATH']
    )
    response = requests.get(url,  params={
        'apiKey': conf['RETENTION_API']['API_KEY'],
        'qty': quantity,
        'service_id': service_id,
        'link': link
    })

    return jsonify(resp.json())
