import jsonpickle


def get_enc_polylines(response):
    try:
        return jsonpickle.decode(response.text) \
            .get('routes')[0].get('overview_polyline') \
            .get('points')
    except ValueError:
        return None



