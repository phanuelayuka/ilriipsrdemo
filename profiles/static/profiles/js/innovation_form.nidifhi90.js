$(document).ready(function () {
    let innovation_submission_div = $('#innovation-submission-div');
    let contact_person_modal = $('#contact-person-modal');
    let contributors_modal = $('#contributors-modal');
    let images_modal = $('#innovation-image-modal');
    let reference_url_modal = $('#innovation-ref-material-modal');

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

    $('#id_title').textcounter({
        type: "word",
        max: 10,
        countDown: true
    });

    $('#id_description').textcounter({
        type: "word",
        max: 25,
        countDown: true
    });

    $('#id_in_cgiar_innovation_dashboard').on('change', function (e) {
        let in_cgiar_innovation_dashboard = $(this);
        let dashboard_id_title_div = $('div.innovation-dashboard-id-or-title-div');
        let dashboard_id_title_input = $('#id_innovation_dashboard_id_or_title');

        if(in_cgiar_innovation_dashboard.val() === 'yes'){
            dashboard_id_title_div.show();
            dashboard_id_title_input.attr('required', 'required');
        }else {
            dashboard_id_title_div.hide();
            dashboard_id_title_input.removeAttr('required');
        }
    }).trigger('change');

    $('#id_topology').on('change', function (e) {
        let in_cgiar_innovation_dashboard = $(this);
        let new_breed_div = $('div.new-improved-variety-breed-div');
        let new_breed_input = $('#id_new_improved_variety_breed');

        if(in_cgiar_innovation_dashboard.val() === 'technological'){
            new_breed_div.show();
            new_breed_input.attr('required', 'required');
        }else {
            new_breed_div.hide();
            new_breed_input.removeAttr('required');
        }
    }).trigger('change');

    $('#id_new_improved_variety_breed').on('change', function (e){
        let in_cgiar_innovation_dashboard = $(this);
        let new_breed_no_div = $('div.new-varieties-number-div');
        let new_breed_no_input = $('#id_improved_varieties_number');

        if(in_cgiar_innovation_dashboard.val() === 'yes'){
            new_breed_no_div.show();
            new_breed_no_input.attr('required', 'required');
        }else {
            new_breed_no_div.hide();
            new_breed_no_input.removeAttr('required');
        }
    }).trigger('change');

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
                submit_btn.removeAttr('disabled');
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
                submit_btn.removeAttr('disabled');
            }
        });
    });

    reference_url_modal.on('submit', '#ref-materials-form', function (e) {
        e.preventDefault();
        let reference_form = $(this);
        let submit_btn = reference_form.find('button[type=submit]');
        submit_btn.attr('disabled', 'disabled');
        $.ajax({
            url: reference_form.data('action'),
            data: reference_form.serialize(),
            method: "POST",
            success: function (data) {
                if(data.entry_html){
                    $('#ref-materials-table').find('tbody').append(data.entry_html);
                    reference_url_modal.iziModal('close');
                    reference_form.trigger('reset');
                    submit_btn.removeAttr('disabled');
                }
            },
            error: function (data) {
                submit_btn.removeAttr('disabled');
            }
        });
    });

    images_modal.on('submit', '#innovation-image-form', function (e) {
        e.preventDefault();
        let images_form = $(this);
        let form_data = new FormData(images_form[0]);
        let submit_btn = images_form.find('button[type=submit]');
        submit_btn.attr('disabled', 'disabled');
        $.ajax({
            url: images_form.data('action'),
            data: form_data,
            method: "POST",
            processData: false,
            contentType: false,

            success: function (data) {
                if(data.entry_html){
                    $('#innovation-images-table').find('tbody').append(data.entry_html);
                    images_modal.iziModal('close');
                    images_form.trigger('reset');
                    submit_btn.removeAttr('disabled');
                }
            },
            error: function (data) {
                submit_btn.removeAttr('disabled');
            }
        });
    });
});

