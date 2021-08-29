# Find reflection pivot algorithm - API

A basic Python Flask API that receives an array, process it and returns the reflection pivot (the index that separates the array in two parts which sum is the same).

A web interface was created to interact with the API directly from the browser:
- **GitHub repository:** https://github.com/cristianblar/kiwiflask-front
- **Vercel deployment:** https://kiwiflask-front-cristianblar.vercel.app/

## Tech Stack

- Python
- Flask
- Gunicorn
- Heroku

## Deployment

`https://kiwiflask-api.herokuapp.com/api/check-array`

## API Reference

#### Send array to receive results

```http
  POST /api/check-array
```

Request body:

```json
  {
      "array": [1, 2, 1]
  }
```
## Running Tests

To run tests, run the following command (locally, after cloning the project)

```bash
  python3 tests.py
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

  
