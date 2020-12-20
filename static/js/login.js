$(function(){
    $('#submit_btn').click(function(e) {
        e.preventDefault();
        var bodyFormData = new FormData();
        bodyFormData.append('username', $('#login').val());
        bodyFormData.append('password', $('#password').val());
        axios({
            method: 'post',
            url: '/api/login/',
            data: bodyFormData
        })
        .then(function (response) {
            //handle success
            console.log('success', response);
        })
        .catch(function (response) {
            //handle error
            console.log('error', response);
        });
    });
});