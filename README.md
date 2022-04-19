# RudolfKiss-website
One of the scetches of the website for cinematographer Rudolf Kiss.

This website is a fully functional with admin panel for managing content showed on the pages.



## Tech description
For file serving used S3 bucket on AWS.

For text information purposes used postgres database on Heroku as the cheapest one.

## Runinig the website
1. Clone the repo
2. Setup S3 Bucket on AWS
3. Add dynos Postgres and Ffmpeg dynos on Heroku
4. [Provide environment variables](#environment-variables)
5. Deploy code to heroku
6. Run 'python3 migrate.py create_all' on heroku cli

## Environment variables
To use this sckecth create '.env' file with variables or add this environment variables to your environment in terminal:

HEROKU_PROD_DB_URI=<YOUR_DB_URI>

AWS_ACCES_KEY=<YOUR_AWS_ACCES_KEY>

AWS_ACCES_SECRET=<YOUR_AWS_ACCES_SEKRET>

S3_BUCKET = <YOUR_S3_BUCKET_NAME>

S3_REGION = <YOUR_S3_BUCKET_REGION>
