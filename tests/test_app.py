import json
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    # Test data
    test_data = {
        'sleep_quality': 7,
        'stress_level': 3,
        'physical_activity': 60,
        'day_of_week': 2
    }

    # Send POST request to /predict endpoint
    response = client.post('/predict', 
                           data=json.dumps(test_data),
                           content_type='application/json')

    # Check if response is successful
    assert response.status_code == 200

    # Parse the response data
    data = json.loads(response.data)

    # Check if the response contains the predicted_mood key
    assert 'predicted_mood' in data

    # Check if the predicted_mood is a float
    assert isinstance(data['predicted_mood'], float)

    # Check if the predicted_mood is within a reasonable range (e.g., 1 to 10)
    assert 1 <= data['predicted_mood'] <= 10
