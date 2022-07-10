$(document).ready(function () {

    let innovation_submission_div = $('#innovation-submission-div');
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
});

