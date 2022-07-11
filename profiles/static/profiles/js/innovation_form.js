$(document).ready(function () {

    let innovation_submission_div = $('#innovation-submission-div');
    let contact_person_modal = $('#contact-person-modal');
    let contributors_modal = $('#contributors-modal');

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
        onFinished: function (event, currentIndex) {
            swal(
                "Form Submitted!",
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lorem erat eleifend ex semper, lobortis purus sed."
            );
        },
    });

    $('#contact-person-modal-btn').on('click', function (e) {
        e.preventDefault();
        contact_person_modal.iziModal('destroy');
        contact_person_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        }).iziModal('open');
    });

    $('#contributor-modal-btn').on('click', function (e) {
        e.preventDefault();
        contributors_modal.iziModal('destroy');
        contributors_modal.iziModal({
            history: false,
            width: screen.width * 0.5,
        }).iziModal('open');
    });
});

