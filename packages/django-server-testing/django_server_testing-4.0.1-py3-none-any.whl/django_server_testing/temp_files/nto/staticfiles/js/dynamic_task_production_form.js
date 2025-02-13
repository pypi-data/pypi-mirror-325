document.getElementById("id_order").oninput = 
	function(event) {
		var product_type_select = document.getElementById("id_producttype");
		var quantity_entry = document.getElementById("id_quantity");
		
		fetch("/orders/serialize/" + event.target.selectedOptions[0].value)
			.then(response => response.json())
			.then(result => {
				product_type_select.selectedIndex = 0;
				for (let i = 0; i < product_type_select.options.length; i++) {
					if (product_type_select.options[i].value == result.product_type) {
						product_type_select.selectedIndex = i;
						break;
					}
				}
				quantity_entry.value = result.quantity;
			})
			.catch(error => {
				product_type_select.selectedIndex = 0;
				quantity_entry.value = '';
			})
			.finally();
	};
	