function get_output(job_desc, num_words, output_element, invoker) {
	var xmlhttp = new XMLHttpRequest();
//    var csrftoken = getCookie('csrftoken');
    var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    invoker.disabled = true;
    output_element.innerHTML = "<b><i>Processing...</i></b>";

	try {

		xmlhttp.onreadystatechange = function () {

			if (xmlhttp.readyState == 4) {
			    invoker.disabled = false;
                output_element.innerHTML = "";

				if(xmlhttp.status == 200) {
				    var resp_json = JSON.parse(xmlhttp.responseText);
		            var img_most_freq = document.createElement('img');
		            img_most_freq.setAttribute('id', 'img_most_freq')
		            img_most_freq.setAttribute('src', resp_json.file1_name)
//		            img_most_freq.setAttribute('width', 400)
//		            img_most_freq.setAttribute('height', 300)

		            var img_least_freq = document.createElement('img');
		            img_least_freq.setAttribute('id', 'img_least_freq')
		            img_least_freq.setAttribute('src', resp_json.file2_name)
//		            img_least_freq.setAttribute('width', 400)
//		            img_least_freq.setAttribute('height', 300)

		            var image1_container = document.createElement('div');
		            image1_container.setAttribute('class', 'contact1-pic js-tilt')
		            image1_container.setAttribute('data-tilt', '')

		            var image2_container = document.createElement('div');
		            image2_container.setAttribute('class', 'contact1-pic js-tilt')
		            image2_container.setAttribute('data-tilt', '')

		            output_element.appendChild(document.createElement('br'))
		            output_element.appendChild(document.createElement('br'))
		            output_element.appendChild(document.createElement('b').appendChild(document.createTextNode('Most frequent words')))
		            output_element.appendChild(document.createElement('br'))
		            image1_container.appendChild(img_most_freq)
		            output_element.appendChild(image1_container)
		            output_element.appendChild(document.createElement('br'))
		            output_element.appendChild(document.createElement('br'))
		            output_element.appendChild(document.createElement('b').appendChild(document.createTextNode('Least frequent words')))
		            output_element.appendChild(document.createElement('br'))
		            image2_container.appendChild(img_least_freq)
		            output_element.appendChild(image2_container)
				}
				else if (xmlhttp.status == 500) {
					console.log(xmlhttp);
					output_element.innerHTML = xmlhttp.statusText;
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