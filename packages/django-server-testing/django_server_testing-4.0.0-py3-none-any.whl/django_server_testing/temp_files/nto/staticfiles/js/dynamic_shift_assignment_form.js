document.getElementById("id_task_production").oninput = 
	function(event) {
		var product_type_select = document.getElementById("id_producttype");
		var quantity_entry = document.getElementById("id_quantity");
		
		fetch("/task_production/serialize/" + event.target.selectedOptions[0].value)
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

document.getElementById("id_data_work").oninput = 
	function(event) {
		var work_area_select = document.getElementById("id_work_area");
		
		function clear() {
			work_area_select.replaceChildren();
			var option = document.createElement("option");
			option.value = '';
			option.text = "---------";
			work_area_select.appendChild(option);
			option.selected = true;
			option.defaultSelected = true;
		}
		clear();
		
		fetch("/shift_assignments/serialize/" + event.target.value)
			.then(response => response.json())
			.then(result => {
				Object.entries(result.data).forEach(
					(entry) => {
						const [name, values] = entry;
						
						var optgroup = document.createElement("optgroup");
						optgroup.label = name;
						
						for (let o of values) {
							let option = document.createElement("option");
							option.value = o.id;
							option.text = o.name;
							
							optgroup.appendChild(option);
						}
						
						work_area_select.appendChild(optgroup);
					}
				);
			})
			.catch(error => {
			})
			.finally();
	};
