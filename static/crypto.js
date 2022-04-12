const BASE_URL = `http://${location.host}`;

const username = "{{ session['username'] }}";

// # ******************************************************************************
// # ******************************************************************************
// # ********** need to remove event propagation from click events      ***********
// # ******************************************************************************
// # ******************************************************************************

function toggleFavorite() {
	if (target.innerHTML === 'Remove') {
		removeCurrency();
	} else if (target.innerHTML === 'Add') {
		addCurrency();
	}
}
// add a currency

let addCurrency = async function(e) {
	// e.stopPropagation();
	// console.log('is propagation stopped: ', e.isPropagationStopped());

	console.log('add has been clicked');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');
	const res = await axios.post(`${BASE_URL}/api/users/${username}/${currencyId}/add`);
	console.log(res);
	window.location.reload();
};

$('.add-currency').on('click', addCurrency);

// remove a currency

let removeCurrency = async function(e) {
	// e.stopPropagation();
	// console.log('is propagation stopped: ', e.isPropagationStopped());

	console.log('remove has been clicked');
	// let $currency = $(e.target).closest('.card');
	let username = e.target.getAttribute('data-username');
	let currencyId = e.target.getAttribute('data-currency-id');
	console.log(window.location.pathname);
	const res = await axios.delete(`${BASE_URL}/api/users/${username}/${currencyId}/delete`);
	// if (window.location.pathname === '/users/' + regex) {
	// $currency.remove();
	// }
	window.location.reload();
	console.log(res);
};

$('.remove-currency').on('click', removeCurrency);
