import requests

def test_local_url_accessibility():
    url = "http://localhost:8501"  # Replace with your actual local URL
    response = requests.get(url)
    assert response.status_code == 200

def test_local_url_content():
    url = "http://localhost:8501"  # Replace with your actual local URL
    response = requests.get(url)
    assert "Your Streamlit App Title" in response.text  # Replace with actual content to check