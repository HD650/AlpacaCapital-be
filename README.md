# AlpacaCapital-be   
To deploy, install python3.5,mysql,django.   
Then disable firewall on the linux server and setup a endpoint for azure load blance.   
## get_company_list   
* describe: api to get companies brief   
* url: /get_company_list/   
* method: GET   
* param: int page (default 1)   
* response: json with company num and companies brief   
* react: render the companies brief   
## new_user   
* describe: api to create a new auth user   
* url: /new_user/   
* method: POST   
* param: string email, string password   
* response: "OK" if succeed, "FAIL" if failed   
* react: show succeed page or failed page   
## log_in   
* describe: api to log in a user   
* url: /log_in/   
* method: POST   
* param: string email, string password   
* response: "OK" with logined cookies, "FAIL" with nothing append   
* react: show log in page or failed page   
## log_out   
* describe: api to log out a user   
* url: /log_out/   
* method: GET   
* param: No, just append the logined cookies   
* response: "OK" for succeed, "FAIL" for error   
* react: show page with succeed loged out or failed to loged out   

## user_test   
* describe: api to authenticate a logined cookies   
* url: /user_test/   
* method: GET   
* param: No, just append the logined cookies given by log_in   
* response: "OK" for permisson, "FAIL" for deny   
* react: if get "OK" response, go to destination page, if "FAIL", deny the request   
