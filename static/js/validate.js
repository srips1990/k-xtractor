
var validateAndSubmitJobDescForm = function(formElement) {
    num_words.setCustomValidity('');
    job_desc.setCustomValidity('');
    if(num_words.value>100 || num_words<1) {
        num_words.setCustomValidity('Enter a valid integer between 1 and 100');
    }
    if(formElement.checkValidity()){
        get_output(job_desc,num_words,btn_submit);
    }
    else {
        formElement.reportValidity();
    }
}