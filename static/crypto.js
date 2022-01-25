const BASE_URL = `http://127.0.0.1:5000`;
const CMC_URL = `http:`;

async function getCurrencies(e) {
	e.preventDefault();

	const res = await axios.get(
		`https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY=8e821d14-0fcc-4565-ae47-acb55c2848dc`
	);
}

async function processForm(e) {
	e.preventDefault();

	// data collection for api

	let name = $('#name').val();

	const res = await axios.post(`http://127.0.0.1:5000/api/cryptodata`, { name });

	console.log(res.data.currencies[1].slug);
	console.log(res);

	data = res.data;

	let cryptoData = $(handleResponse(data));
	$('#currency-list').append(cryptoData);
}

function handleResponse(res) {
	// {% for error in field.errors %}
	// <span class="form-text text-danger"> {{ error }} </span>
	// {% endfor %}
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

// # **************************
// # **************************
// # **************************
// # **************************

// add a cupcake

$('#form-newCupcake').on('submit', async function(e) {
	e.preventDefault();

	let flavor = $('#input-flavor').val();
	let size = $('#input-size').val();
	let image = $('#input-image').val();
	let rating = $('#input-rating').val();

	const res = await axios.post(`${BASE_URL}/api/cupcakes`, { flavor, rating, size, image });

	console.log(res);
	let newCupcake = $(generateCupcake(res.data.cupcake));
	$('#cupcakes-list').append(newCupcake);
	$('#form-newCupcake').trigger('reset');
});

// delete cupcakes

$('#cupcakes-list').on('click', '.delete-cupcake', async function(e) {
	e.preventDefault();

	let $cupcake = $(e.target).closest('div');
	let cupcakeId = $cupcake.attr('data-cupcake-id');

	await axios.delete(`${BASE_URL}/api/cupcakes/${cupcakeId}`);
	$cupcake.remove();
});

// # **************************
// # **************************
// # **************************
// # **************************

// return `
// <div class="col-4" data-cupcake-id=${c.id}>
//     <button class="delete-cupcake">REMOVE</button>
//   <img class="img-thumbnail" src="${c.image}">
// </div>
// `
