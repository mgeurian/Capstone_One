#Educryption

##Description
Educryption is a place for users to add and follow a list of cryptocurrencies in which a user is interested.
This is a full-stack application written with Python, Javascript, jQuery, Bootstrap, Flask, Postgresql, and Bootstrap for styling.
This application utilizes the CoinMarketCap API.
This application was created as a Capstone Project for the Springboard Software Engineering Program.
A live version of this project can be found here: https://educryption.herokuapp.com/

The repository for the Educryption can be found at: https://github.com/mgeurian/Capstone_One

##Current Features
- An unregistered user can search for a specific cryptocurrency.
- An unregistered user can view information about a specific cryptocurrency.

- A Registered User (user) can register their information.
- A user can log-in and log-out of their account.
- A user can search for a specific cryptocurrency.
- A user can view information about a specific cryptocurrency.
- A user can add and remove cryptocurrencies.
- A user can delete their account.

##Additional Future Features:

- Users will be able to add currencies they own, along with amounts/values.
- CoinMarketCap API will be utilized to get exchange information to allow users to link their exchange accounts.
- Users will be able to view what other users are following.
- Users will be able to blog and write articles about what they think of specific cryptocurrencies.
- Users will be able to follow other users.

##Walkthrough

The navigation bar has 3 links.
On the navigation bar, registered users and non-registered users will see 'Educryption' to the left. 'Login' and 'Sign Up' to the right.

The title 'Educryption' will always bring you back to the home screen where a list of cryptocurrencies can be viewed.
Your username will take you directly to your list of 'favorited' cryptocurrencies.

To start, a user should sign-up or login for an account. A non-registered user will need to provide a first name, last name, email, username, and password to sign-up/register.

On the home page, a non-user can click a currency name to view information about that currency. A registered user will have a button to the right of the currency name to either add or remove the currency from their account.

###Registering OR Logging in
Upon login or registration completion, you will be taken to your profile page. 
On the profile page, there are 2 buttons. 
- The 'Delete' button will delete a user's account.
- The 'View All Currencies' button will take the user to the home page.
Below these buttons will be a user's list of 'favorited' currencies, if any exist.

License
MIT License

Copyright (c) [2022] [Matt C Geurian]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.