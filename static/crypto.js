const BASE_URL = `http://${location.host}`;

const username = "{{ session['username'] }}";

// async function getCurrencies(e) {
// 	e.preventDefault();

// 	const res = await axios.get(
// 		`https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY=8e821d14-0fcc-4565-ae47-acb55c2848dc`
// 	);
// }

// async function getListedCurrencies(e) {
// 	e.preventDefault();

// 	const res = axios.get(
// 		`https://pro-api.coinmarketap.com/v1/cryptcurrency/map?CMC_PRO_API_KEY=8e821d14-0fcc-4565-ae47-acb55c2848dc`
// 	);
// }

async function processForm(e) {
	e.preventDefault();

	// data collection for api

	let name = $('#name').val();
	// take value .toLowerCase() and use the get request to retrieve
	const res = await axios.post(`http://127.0.0.1:5000/api/cryptodata`, { name });

	console.log(res.data.currencies[1].slug);
	console.log(res);

	data = res.data;

	let cryptoData = $(handleResponse(data));
	$('#currency-list').append(cryptoData);
}

function handleResponse(res) {
	let currency_list;

	res.map(function(val, idx) {
		currency_list += console.log('this is the response', res);

		return `
    <div>
      <p>will put something else here.</p>
    </div>
    `;
	});

	return currency_list;
}

$('#crypto-form').on('submit', processForm);

// add a currency

$('.add-currency').on('click', async function(e) {
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');

	const res = await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);

	console.log(res);
});

// remove a currency

$('.remove-currency').on('click', async function(e) {
	console.log('delete has been clicked');
	let $currency = $(e.target).closest('.card');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');

	const res = await axios.delete(`${BASE_URL}/api/users/${username}/${currencyId}/delete`);
	$currency.remove();

	console.log(res);

	// update current div by changing delete button ==> add button
});
