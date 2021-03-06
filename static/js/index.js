
var get_output = function(job_desc, num_words, invoker) {
	var xmlhttp = new XMLHttpRequest();
//    var csrftoken = getCookie('csrftoken');
    var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    invoker.disabled = true;
    var most_freq_container = document.getElementById('most_freq_container');
    var least_freq_container = document.getElementById('least_freq_container');
    var status_elem = document.getElementById('status');
    most_freq_container.innerHTML = "";
    least_freq_container.innerHTML = "";
    status_elem.innerHTML = "<b><i>Processing...</i></b>";

	try {

		xmlhttp.onreadystatechange = function () {

			if (xmlhttp.readyState == 4) {
			    invoker.disabled = false;
                status_elem.innerHTML = "";

				if(xmlhttp.status == 200) {
				    var resp_json = JSON.parse(xmlhttp.responseText);
		            var img_most_freq = document.createElement('img');
		            img_most_freq.setAttribute('id', 'img_most_freq')
		            img_most_freq.setAttribute('src', resp_json.file1_name)

		            var img_least_freq = document.createElement('img');
		            img_least_freq.setAttribute('id', 'img_least_freq')
		            img_least_freq.setAttribute('src', resp_json.file2_name)

		            most_freq_container.appendChild(document.createElement('b').appendChild(document.createTextNode('Most frequent words')))
		            most_freq_container.appendChild(document.createElement('br'));
		            most_freq_container.appendChild(img_most_freq);
		            least_freq_container.appendChild(document.createElement('b').appendChild(document.createTextNode('Least frequent words')))
		            least_freq_container.appendChild(document.createElement('br'));
		            least_freq_container.appendChild(img_least_freq);
				}
				else if (xmlhttp.status == 500) {
					console.log(xmlhttp);
					var error_obj, error_msg;
					try {
                        error_obj = JSON.parse(xmlhttp.responseText);
                        if(error_obj.hasOwnProperty("error")) {
					        status_elem.innerHTML = error_obj.error;
                        }
                        else if(error_obj.hasOwnProperty("validation_error")) {
                            var err_element = document.getElementById(error_obj.field_name)
                            err_element.setCustomValidity(error_obj.validation_error);
                            err_element.reportValidity();
                        }
                        else {
					        status_elem.innerHTML = "Internal Server error. Check console logs";
					        console.log(error_obj)
                        }

                    } catch (e) {
                        error_msg = xmlhttp.statusText;
					    status_elem.innerHTML = error_msg;
                    }
				}
			}
		};

		xmlhttp.open("POST", "process", true);
		xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
		var formData = new FormData();
		formData.append("job_desc", job_desc.value);
		formData.append("num_words", num_words.value);
		xmlhttp.send(formData);

	}
	catch (e) {
		console.log("Error: " + xmlhttp.statusText + e.description);
	}
}