const BASE_URL = `http://${location.host}`;

const username = "{{ session['username'] }}";

// # ******************************************************************************
// # ******************************************************************************
// # ********** need to remove event propagation from click events      ***********
// # ******************************************************************************
// # ******************************************************************************

// add a currency

let addCurrency = async function(e) {
	e.stopPropagation();
	console.log('is propagation stopped: ', e.isPropagationStopped());

	console.log('add has been clicked');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');
	const res = await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);
	console.log(res);
};

$('.add-currency').on('click', addCurrency);

// remove a currency

let removeCurrency = async function(e) {
	e.stopPropagation();
	console.log('is propagation stopped: ', e.isPropagationStopped());

	console.log('remove has been clicked');
	let $currency = $(e.target).closest('.card');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');

	const res = await axios.delete(`${BASE_URL}/api/users/${username}/${currencyId}/delete`);
	$currency.remove();
	console.log(res);
};

$('.remove-currency').on('click', removeCurrency);
