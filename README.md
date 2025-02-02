# Number Classification API

This is a Flask-based API that classifies a given number and returns its properties, such as whether it is a prime number, an Armstrong number, a perfect number, even or odd, and the sum of its digits. Additionally, if the number is an Armstrong number, the API provides a fun fact explaining why.

---

## Features

- **Number Classification**: The API classifies a number based on the following properties:
  - **Prime**: Whether the number is a prime number.
  - **Perfect**: Whether the number is a perfect number.
  - **Armstrong**: Whether the number is an Armstrong number.
  - **Even/Odd**: Whether the number is even or odd.
  - **Digit Sum**: The sum of the digits of the number.

- **Fun Fact for Armstrong Numbers**: If the number is an Armstrong number, the API provides a fun fact explaining why it is an Armstrong number (e.g., `371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371`). If the number is not an Armstrong number, the fun fact will be: `"This number does not have a fun fact"`.

- **Error Handling**: The API validates the input and returns appropriate error messages if:
  - The `number` parameter is missing.
  - The `number` parameter is not a valid integer.

---

## API Endpoint

### `GET /api/classify-number`

#### Request Parameters
- **number** (required): The number to classify. Must be a valid integer.

#### Example Request
```
GET /api/classify-number?number=371
```

#### Example Response
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit-sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

---

## Error Responses

### Invalid `number` Parameter
If the `number` parameter is not a valid integer, the API returns a `400 Bad Request` error.

#### Request
```
GET /api/classify-number?number=abc
```

#### Response
```json
{
  "number": "alphabet",
  "error": true
}
```

---

## How to Run the API

### Prerequisites
- Python 3.x
- Flask
- Flask-CORS

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/HNG-Stage1_task_backend.git
   cd HNG-Stage1_task_backend
   ```

2. Install the required dependencies:
   ```bash
   pip install Flask Flask-CORS
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. The API will be available at `https://hng-stage1-task-backend-qr5je98t7.vercel.app/api/classify-number`.

---

## Example Usage

### Using `curl`
```bash
curl "hng-stage1-task-backend.vercel.app/api/classify-number?number=371"
```

### Using Python (Requests Library)
```python
import requests

response = requests.get("https://hng-stage1-task-backend-qr5je98t7.vercel.app/api/classify-number", params={"number": 371})
print(response.json())
```

### Using a Browser
Open the following URL in your browser:
```
https://hng-stage1-task-backend-qr5je98t7.vercel.app//api/classify-number?number=371
```

---

## Response Fields

- **number**: The input number.
- **is_prime**: `true` if the number is prime, otherwise `false`.
- **is_perfect**: `true` if the number is perfect, otherwise `false`.
- **properties**: A list of properties, including `"armstrong"` (if applicable) and `"even"` or `"odd"`.
- **digit-sum**: The sum of the digits of the number.
- **fun_fact**: A fun fact explaining why the number is an Armstrong number (if applicable). If the number is not an Armstrong number, the fun fact will be: `"This number does not have a fun fact"`.

---

## Example Responses

### For `number=371` (Armstrong number):
```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit-sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### For `number=123` (Not an Armstrong number):
```json
{
  "number": 123,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["odd"],
  "digit-sum": 6,
  "fun_fact": "This number does not have a fun fact"
}
```

### For `number=153` (Armstrong number):
```json
{
  "number": 153,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit-sum": 9,
  "fun_fact": "153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153"
}
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author

[Rashid Abubakar Hussein](https://github.com/abdirashidabubakar50)

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Support

For any questions or issues, please open an issue on the [GitHub repository](https://github.com/abdirashidabubakar50/HNG-Stage1_task_backend).