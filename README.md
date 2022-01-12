# Capstone1

Project Proposal



1. What goal will your website be designed to achieve? 

This website will be designed with an aesthetic look to share information about cryptocurrencies so as not to overwhelm newcomers to the cryptocurrency world with ideas and words often associated with this topic.



2. What kind of users will visit your site? In other words, what is the demographic of your users? 

This site will be designed for all people with a desire to learn more about cryptocurrency.



3. What data do you plan on using? You may have not picked your actual API yet, which is fine, just outline what kind of data you would like it to contain. 

The API chosen for this project is the ‘CoinMarketCap API’ (https://coinmarketcap.com/api/).
Metadata offered such as logos, descriptions, official website URLs, social links, and technical documentation will be included in the 



4. In brief, outline your approach to creating your project (knowing that you may not know everything in advance and that these details might change later). Answer questions like the ones below, but feel free to add more information: 

a. What does your database schema look like?

Username: 	username (PK), 
		password

Currency: 	id (PK), 
		name, 
		symbol, 
		category, 
		slug, 
		logo, 
		description, 
		tag, 
		platform: (
			id, 
			name, 
			symbol, 
			slug)
		 urls: 	(
			website, 
			technical documentation, 
			reddit,
			twitter)

User_Currency:	id (PK),
			username (FK),
			currency_id (FK)

Note:			id (PK),
			user_currency_id (FK),
			comments



b. What kinds of issues might you run into with your API? 

With the free version of the API, there are:

	a limited number of daily/monthly calls available
	a limited number of endpoints
	no historical data available
	no exchange information available

The tags available may not be included on all currencies. For example, Bitcoin runs the SHA256 hashing algorithm, whereas Groestlcoin uses the Groestl hashing algorithm. All currencies may not have a tag stating which hashing algorithms is used.



c. Is there any sensitive information you need to secure

Users will have an option to save cards  to their profile and view them later. But the ‘profile’ won’t contain any sensitive information aside from a password for authentication and authorization.



d. What functionality will your app include?

‘Cards’ will contain basic information on the currency that is contained on that card. 

Users will be able to click on a ‘card’ and be taken to another page to view more information on that currency. These currency pages will only contain information for that currency. But will include additional links to outside resources for further study.

Users will be able to create an account, be authenticated, and be authorized to view information specific to that user. Specific information will be cards that the user would like to track and/or study for later. There will also be a small section to add personal comments for each saved card.


e. What will the user flow look like?

Users will start at the homepage and can view currencies. Users have the option to login/register. Registering is the only way to access additional functionality. If the user decides to register, the user will be logged in and will be shown the user profile screen. (mostly empty at this time, stretch goals will include a short interactive “how-to” for using the site.)

Users will be able to ‘favorite’ currencies from the ‘home_page’ OR ‘main_currency_page’. When a currency is ‘favorited’, that currency is added to their list of favorites and can be viewed on the user’s profile_page. Uses will be able to delete favorites from their profile_page or the main_currency_page.

Users will be able to add notes to specific currencies from the profile_page by way of a notes form. When a note is added, that note is added to their list of notes and can be viewed on the user’s profile_page.

Users will be able to view/add/edit/delete notes on an additional ‘notes_page’.



f. What features make your site more than CRUD? Do you have any stretch goals?

The site will have sort and filter functions to view different currencies based on their functions and for what they were made. Eventually incorporating charts into the currency pages. As well as showing market caps and dominance through pie charts.

****************************************


FUTURE upgrades
Eventually, the following (with a paid API) would be nice to implement:

-  assets will have general information available and links to exchanges where they can purchase CCs.

-  ability to view exchange information

-  ability to view one's own CC  ownership information.
