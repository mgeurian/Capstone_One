const BASE_URL = `http://${location.host}`;

const username = "{{ session['username'] }}";

async function processForm(e) {
	e.preventDefault();

	// data collection for api

	let slug = $('#name').val().toLowerCase();

	console.log(slug);

	// const API_KEY = '8e821d14-0fcc-4565-ae47-acb55c2848dc';
	// base_api = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?';
	// api_key = 'CMC_PRO_API_KEY=' + API_KEY;
	// individual_currency_id_url = base_api + api_key + '&slug=' + slug;

	// console.log(individual_currency_id_url);

	const searched_currency = await axios.get(`${BASE_URL}/currency/${slug}`);
	console.log(searched_currency);
}

$('#crypto-form').on('submit', processForm);

// # ******************************************************************************
// # ******************************************************************************
// # ********** need to remove event propagation from click events      ***********
// # ******************************************************************************
// # ******************************************************************************

// add a currency

// let addToUserCurrency = document.getElementById("add-currency");

// function addCurrency(e) {
// 	e.stopPropagation()
// 	let username = e.target.getAttribute('data-username');
// 	let currencyId = e.target.getAttribute('data-currency-id');

// 	const res = await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);
// 	console.log(res);
// }

$('.add-currency').on('click', async function(e) {
	e.stopPropagation();
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');

	await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);
});

// remove a currency

$('.remove-currency').on('click', async function(e) {
	e.stopPropagation();
	console.log('delete has been clicked');
	let $currency = $(e.target).closest('.card');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');

	const res = await axios.delete(`${BASE_URL}/api/users/${username}/${currencyId}/delete`);
	$currency.remove();

	console.log(res);

	// update current div by changing delete button ==> add button
});
