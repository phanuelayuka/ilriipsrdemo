$(document).ready(function () {

    let innovation_submission_div = $('#innovation-submission-div');
    let contact_person_modal = $('#contact-person-modal');
    let contributors_modal = $('#contributors-modal');
    let images_modal = $('#innovation-image-modal');
    let reference_url_modal = $('#innovation-ref-material-modal');
    let contributors_form = $('#contributor-form');
    let images_form = $('#innovation-image-form');
    let reference_url_form = $('#innovation-ref-material-form');

    innovation_submission_div.steps({
        headerTag: "h6",
        bodyTag: "section",
        transitionEffect: "fade",
        enablePagination: false,
        titleTemplate: '<span class="step">#index#</span> #title#',
        startIndex: innovation_submission_div.data('current-step'),
        onStepChanging: function (event, currentIndex, newIndex) {
            return false;
        },
    });

    $('#contact-person-modal-btn').on('click', function (e) {
        e.preventDefault();
        contact_person_modal.iziModal('destroy');
        contact_person_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        });
        contact_person_modal.iziModal('open');
    });

    $('#contributor-modal-btn').on('click', function (e) {
        e.preventDefault();
        contributors_modal.iziModal('destroy');
        contributors_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        });
        contributors_modal.iziModal('open');
    });

    $('#innovation-image-modal-btn').on('click', function (e) {
        e.preventDefault();
        images_modal.iziModal('destroy');
        images_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        }).iziModal('open');
    });

    $('#innovation-ref-material-modal-btn').on('click', function (e) {
        e.preventDefault();
        reference_url_modal.iziModal('destroy');
        reference_url_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        }).iziModal('open');
    });

    contact_person_modal.on('submit', '#contact-person-form', function (e) {
        e.preventDefault();
        let contact_person_form = $(this);
        let submit_btn = contact_person_form.find('button[type=submit]');
        submit_btn.attr('disabled', 'disabled');
        $.ajax({
            url: contact_person_form.data('action'),
            data: contact_person_form.serialize(),
            method: "POST",
            success: function (data) {
                if(data.entry_html){
                    $('#contact-persons-table').find('tbody').append(data.entry_html);
                    contact_person_modal.iziModal('close');
                    contact_person_form.trigger('reset');
                    submit_btn.removeAttr('disabled');
                }
            },
            error: function (data) {

            }
        });
    });

    contributors_modal.on('submit', '#contributor-form', function (e) {
        e.preventDefault();
        let contributors_form = $(this);
        let submit_btn = contributors_form.find('button[type=submit]');
        submit_btn.attr('disabled', 'disabled');
        $.ajax({
            url: contributors_form.data('action'),
            data: contributors_form.serialize(),
            method: "POST",
            success: function (data) {
                if(data.entry_html){
                    $('#contributors-table').find('tbody').append(data.entry_html);
                    contributors_modal.iziModal('close');
                    contributors_form.trigger('reset');
                    submit_btn.removeAttr('disabled');
                }
            },
            error: function (data) {

            }
        });
    });
});

