const BASE_URL = `http://127.0.0.1:5000`;


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
	// {% for error in field.errors %}s
	// <span class="form-text text-danger"> {{ error }} </span>
	// {% endfor %}
	let currency_list;

	res.map(function (val, idx){
	  currency_list +=
	console.log('this is the response', res);

	return `
    <div>
      <p>will put something else here.</p>
    </div>
    `;

	// })

	return currency_list;
}

$('#crypto-form').on('submit', processForm);

// return `
// <div class="col-4" data-cupcake-id=${c.id}>
//     <button class="delete-cupcake">REMOVE</button>
//   <img class="img-thumbnail" src="${c.image}">
// </div>
// `
