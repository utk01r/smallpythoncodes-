## scrap all emails from webpages

Scrap all email from website input via CLI

### Modules

- regex : For regex (to ensure it is an email)
- sys   : For system resources utilization
- requests : For HTTP requesting (mean intracting with url in browser)
- pandas : To convert raw scrapped data in data frame so that we can save in the csv format (Optional if you just printing the email list)
- google.colab : To save the .csv file 

### how to run: 
It takes two parameters:
- <Parameter1> : website URL
- <Parameter2> : file name (or location with file name) in .csv format 

```bash
python email_scraping_cli.py <website> <file_name.csv>
```

```bash
python email_scraping_cli.py https://in.yahoo.com/ yahoo_emails.csv 
```
