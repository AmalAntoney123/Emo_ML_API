# Mood Prediction API

This API predicts a user's mood based on various input factors using a trained machine learning model.

## Features

- Predicts mood on a scale of 1 to 10
- Takes into account sleep quality, stress level, physical activity, and day of the week
- Uses a trained neural network model for predictions

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/mood-prediction-api.git
   cd mood-prediction-api
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. The API will be available at `http://localhost:5000`

3. To make a prediction, send a POST request to `/predict` with the following JSON payload:
   ```json
   {
     "sleep_quality": 7,
     "stress_level": 3,
     "physical_activity": 6,
     "day_of_week": 2
   }
   ```

   Example using curl:
   ```
   curl -X POST -H "Content-Type: application/json" -d '{"sleep_quality": 7, "stress_level": 3, "physical_activity": 6, "day_of_week": 2}' http://localhost:5000/predict
   ```

4. The API will respond with a JSON object containing the predicted mood:
   ```json
   {
     "predicted_mood": 7.5
   }
   ```

## Model Training

The model was trained using the `train_mood_model.py` script. It uses a dataset of mood data (`mood_data.csv`) to train a neural network regression model.

To retrain the model with new data:

1. Update the `mood_data.csv` file with new data
2. Run the training script:
   ```
   python train_mood_model.py
   ```

## Testing

To run the tests:
   ```
   pytest tests/
   ```


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.