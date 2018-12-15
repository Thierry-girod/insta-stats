from flask import Blueprint, request, jsonify
from module.configuration import get_config
import requests

api_redirect_service = Blueprint('api_redirect', __name__)
conf = get_config()

@api_redirect_service.route('/api/retention-panel/', methods=['GET'])
def retention_panel():
    # Retrieve parameters
    quantity = request.args.get('qty', False)
    service_id = request.args.get('service_id', False)
    link = request.args.get('link', False)

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

    return jsonify(response.json())
