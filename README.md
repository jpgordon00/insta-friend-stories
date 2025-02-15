# Instagram Follower Manager

A Python script to automatically manage Instagram followers and add them to your close friends list. The script uses the instagrapi library to interact with Instagram's API safely and efficiently.

## Features

- Fetches all your Instagram followers (with optional limit)
- Adds followers to your close friends list
- Implements safe delays between requests to avoid rate limiting
- Supports session management to reduce login frequency
- Handles pagination for large follower lists
- Provides progress feedback during execution

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install the required dependencies:
```bash
pip install instagrapi
```

## Usage

You can run the script in two ways:

### 1. Using Environment Variables

Set your Instagram credentials as environment variables:
```bash
export IG_USERNAME="your_username"
export IG_PASSWORD="your_password"
```

Then run the script:
```bash
python main.py
```

### 2. Interactive Mode

Simply run the script and it will prompt for credentials:
```bash
python main.py
```

### Optional Parameters

- `--max`: Limit the number of followers to process
  ```bash
  python main.py --max 100
  ```

## Security Notes

- The script saves session information locally to reduce login frequency
- Credentials can be provided via environment variables for better security
- Implements random delays between requests to avoid rate limiting
- Never share your `session.json` file or credentials with others

## Error Handling

The script includes comprehensive error handling for:
- Network issues
- Rate limiting
- Invalid credentials
- API changes
- Session management

## Best Practices

1. Start with a small number of followers using the `--max` parameter to test
2. Monitor the script's output for any rate limiting warnings
3. Don't run the script too frequently to avoid Instagram restrictions
4. Keep your instagrapi library updated for the latest security patches

## Limitations

- Instagram may rate limit requests if used too frequently
- The script requires valid Instagram credentials
- Some users may have privacy settings that prevent adding them
- Instagram's API limitations may affect functionality

## Contributing

Feel free to submit issues and enhancement requests!
