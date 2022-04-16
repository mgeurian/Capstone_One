const BASE_URL = `https://${location.host}`;

const username = "{{ session['username'] }}";

function toggleFavorite() {
	if (target.innerHTML === 'Remove') {
		removeCurrency();
	} else if (target.innerHTML === 'Add') {
		addCurrency();
	}
}

// add a currency

let addCurrency = async function(e) {
	console.log('add has been clicked');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');
	const res = await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);
	window.location.reload();
	console.log(res);
};

$('.add-currency').on('click', addCurrency);

// remove a currency

let removeCurrency = async function(e) {
	console.log('remove has been clicked');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');
	const res = await axios.delete(`${BASE_URL}/api/users/${username}/${currencyId}/delete`);
	window.location.reload();
	console.log(res);
};

$('.remove-currency').on('click', removeCurrency);
